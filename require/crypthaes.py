import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def crypth_file(fichier_source, fichier_chiffre, cle):
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    with open(fichier_source, 'rb') as f:
        contenu = f.read()
    
    padder = padding.PKCS7(128).padder()
    contenu_padde = padder.update(contenu) + padder.finalize()
    
    contenu_chiffre = encryptor.update(contenu_padde) + encryptor.finalize()
    
    with open(fichier_chiffre, 'wb') as f:
        f.write(contenu_chiffre)
    
    with open(fichier_chiffre + '.iv', 'wb') as f:
        f.write(iv)

def decrypt_file(fichier_chiffre, fichier_dechiffre, cle):
    with open(fichier_chiffre + '.iv', 'rb') as f:
        iv = f.read()
    
    if not iv:
        print("Erreur : Aucun IV trouvé dans le fichier.")
        return
    
    with open(fichier_chiffre, 'rb') as f:
        contenu_chiffre = f.read()
    
    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    contenu_padde = decryptor.update(contenu_chiffre) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    contenu = unpadder.update(contenu_padde) + unpadder.finalize()
    
    with open(fichier_dechiffre, 'wb') as f:
        f.write(contenu)
