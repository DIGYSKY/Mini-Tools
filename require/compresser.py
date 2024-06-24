import os
import tarfile

def compresser_tar_gz(entree, fichier_tar_gz):
    with tarfile.open(fichier_tar_gz, 'w:gz') as tar:
        if os.path.isfile(entree):
            tar.add(entree, arcname=os.path.basename(entree))
        elif os.path.isdir(entree):
            for racine, _, fichiers in os.walk(entree):
                for fichier in fichiers:
                    chemin_complet = os.path.join(racine, fichier)
                    chemin_rel = os.path.relpath(chemin_complet, os.path.dirname(entree))
                    tar.add(chemin_complet, arcname=chemin_rel)
        else:
            print(f"Erreur : {entree} n'est ni un fichier ni un dossier valide.")

def decompresser_tar_gz(fichier_tar_gz, sortie):
    with tarfile.open(fichier_tar_gz, 'r:gz') as tar:
        tar.extractall(path=sortie)
