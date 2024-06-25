from tqdm import tqdm
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ProcessPoolExecutor, as_completed, Future

def pad_chunk(chunk):
    padder = padding.PKCS7(128).padder()
    return padder.update(chunk) + padder.finalize()

def encrypt_chunk(chunk, cle, iv):
    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(chunk) + encryptor.finalize()

def crypth_file(fichier_source, fichier_chiffre, cle):
    iv = os.urandom(16)
    with open(fichier_source, 'rb') as f:
        contenu = f.read()

    chunk_size = 1024 * 1024  # 1 Mo
    chunks = [contenu[i:i+chunk_size] for i in range(0, len(contenu), chunk_size)]

    print("\n")
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(pad_chunk, chunk): i for i, chunk in enumerate(chunks)}
        ordered_padded_chunks = [None] * len(chunks)
        for future in tqdm(as_completed(futures), total=len(chunks), desc="Padding"):
            index = futures[future]
            ordered_padded_chunks[index] = future.result()
        contenu_padde = b"".join(ordered_padded_chunks)

    chunk_size = 1048592
    padded_chunks = [contenu_padde[i:i+chunk_size] for i in range(0, len(contenu_padde), chunk_size)]

    print("\n")
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(encrypt_chunk, chunk, cle, iv): i for i, chunk in enumerate(padded_chunks)}
        ordered_encrypted_chunks = [None] * len(padded_chunks)
        for future in tqdm(as_completed(futures), total=len(padded_chunks), desc="Chiffrement"):
            index = futures[future]
            ordered_encrypted_chunks[index] = future.result()
        contenu_chiffre = b"".join(ordered_encrypted_chunks)

    print("\n")
    with open(fichier_chiffre, 'wb') as f:
        for i in tqdm(range(0, len(contenu_chiffre), chunk_size), desc="Écriture"):
            f.write(contenu_chiffre[i:i+chunk_size])

    with open(fichier_chiffre + '.iv', 'wb') as f:
        f.write(iv)

def decrypt_chunk(chunk, cle, iv):
    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(chunk) + decryptor.finalize()

def unpad_chunk(chunk):
    unpadder = padding.PKCS7(128).unpadder()
    try:
        return unpadder.update(chunk) + unpadder.finalize()
    except ValueError as e:
        print(f"\033[91mErreur de dépadding : {e}\033[0m")
        return b''

def ordered_results(futures):
    results = [None] * len(futures)
    for future, index in futures.items():
        results[index] = future.result()
    return results

def decrypt_file(fichier_chiffre, fichier_dechiffre, cle):
    with open(fichier_chiffre + '.iv', 'rb') as f:
        iv = f.read()
    
    if not iv or len(iv) != 16:
        print(f"\033[91mErreur : IV incorrect ou absent.\033[0m")
        return
    
    with open(fichier_chiffre, 'rb') as f:
        contenu_chiffre = f.read()

    if len(contenu_chiffre) % 16 != 0:
        print(f"\033[91mErreur : Les données chiffrées ont une taille incorrecte.\033[0m")
        return

    chunk_size = 1048592
    chunks = [contenu_chiffre[i:i+chunk_size] for i in range(0, len(contenu_chiffre), chunk_size)]

    print("\n")
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(decrypt_chunk, chunk, cle, iv): i for i, chunk in enumerate(chunks)}
        contenu_padde = b"".join(tqdm(ordered_results(futures), total=len(futures), desc="Déchiffrement"))

    padded_chunks = [contenu_padde[i:i+chunk_size] for i in range(0, len(contenu_padde), chunk_size)]

    print("\n")
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(unpad_chunk, chunk): i for i, chunk in enumerate(padded_chunks)}
        contenu = b"".join(tqdm(ordered_results(futures), total=len(futures), desc="Dépadding"))

    print("\n")
    with open(fichier_dechiffre, 'wb') as f:
        for i in tqdm(range(0, len(contenu), chunk_size), desc="Écriture"):
            f.write(contenu[i:i+chunk_size])
