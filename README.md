# Mini-Tools

Mini-Tools est une collection d'outils utiles pour la gestion de divers aspects de votre système. Chaque outil est conçu pour résoudre des problèmes spécifiques de manière efficace et conviviale.

## Table des matières

- [Installation](#installation)
- [Outils disponibles](#outils-disponibles)
  - [Ports Manager](#ports-manager)
- [Contributions](#contributions)
- [Licence](#licence)

## Installation

Pour installer et utiliser les outils de ce dépôt, clonez le dépôt et ajoutez-le à votre PATH.

```bash
git clone https://github.com/DIGYSKY/Mini-Tools.git
cd Mini-Tools
chmod +x portsmanager  # Rendre le script exécutable
export PATH=$PATH:$(pwd)  # Ajouter le dossier courant au PATH
```

Ajoutez la ligne suivante à votre fichier `.bashrc` ou `.zshrc` pour rendre l'ajout au PATH permanent :

```bash
export PATH=$PATH:/chemin/vers/Mini-Tools
```

Rechargez votre terminal ou exécutez `source ~/.bashrc` ou `source ~/.zshrc` pour appliquer les modifications.

## Outils disponibles

### Ports Manager

`portsmanager` est un outil de gestion des ports permettant de lister et de gérer les processus écoutant sur des ports spécifiques ou sur tous les ports ouverts.

#### Utilisation

```bash
portsmanager <port> [<port> ...]
portsmanager <port> [<port> ...] [--kill|-k] [-y]
portsmanager [--all|-a]
portsmanager [--all|-a] [--kill|-k] [-y]
portsmanager [--kill-all|-ka]
portsmanager [--help|-h]
```

#### Options

- `<port>` : Spécifiez un ou plusieurs ports pour lesquels vous souhaitez lister les processus.
- `--kill, -k` : Optionnel. Tuer les processus écoutant sur les ports spécifiés après confirmation.
- `-y` : Optionnel. Utilisé avec `--kill` pour tuer les processus sans confirmation.
- `--all, -a` : Lister tous les ports ouverts.
- `--kill-all, -ka` : Tuer tous les processus écoutant sur tous les ports sans confirmation.
- `--help, -h` : Afficher ce message d'aide et quitter.

#### Exemples

- Lister les processus écoutant sur les ports 80 et 443 :
  ```bash
  portsmanager 80 443
  ```

- Lister et tuer les processus écoutant sur les ports 80 et 443 après confirmation :
  ```bash
  portsmanager 80 443 --kill
  ```

- Lister et tuer les processus écoutant sur les ports 80 et 443 sans confirmation :
  ```bash
  portsmanager 80 443 --kill -y
  ```

- Lister tous les ports ouverts :
  ```bash
  portsmanager --all
  ```

- Lister tous les ports ouverts et tuer les processus après confirmation :
  ```bash
  portsmanager --all --kill
  ```

- Tuer tous les processus écoutant sur tous les ports sans confirmation :
  ```bash
  portsmanager --kill-all
  ```

## Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations ou des nouveaux outils à ajouter, n'hésitez pas à ouvrir une issue ou une pull request.

## Licence

Ce projet est sous licence GNU GPLv3. Voir le fichier [LICENSE](LICENSE) pour plus de détails.