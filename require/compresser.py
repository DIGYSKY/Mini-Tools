import os
import tarfile
from tqdm import tqdm

def compresser_tar_gz(entree, fichier_tar_gz):
    print("\n")
    if os.path.isfile(entree):
        with tarfile.open(fichier_tar_gz, 'w:gz') as tar:
            tar.add(entree, arcname=os.path.basename(entree))
    elif os.path.isdir(entree):
        fichiers = [os.path.join(racine, fichier) for racine, _, noms_fichiers in os.walk(entree) for fichier in noms_fichiers]
        with tarfile.open(fichier_tar_gz, 'w:gz') as tar:
            for fichier in tqdm(fichiers, desc="Compression des fichiers"):
                tar.add(fichier, arcname=os.path.relpath(fichier, entree))
    else:
        print(f"\033[91mErreur : {entree} n'est ni un fichier ni un dossier valide.\033[0m")

def decompresser_tar_gz(fichier_tar_gz, sortie):
    print("\n")
    try:
        with tarfile.open(fichier_tar_gz, 'r:gz') as tar:
            membres = tar.getmembers()
            for membre in tqdm(membres, desc="Décompression des fichiers"):
                tar.extract(membre, path=sortie)
    except tarfile.ReadError:
        print(f"\033[91mErreur : Le fichier n'est pas un fichier gzip valide.\033[0m")
