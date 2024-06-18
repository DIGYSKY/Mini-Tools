# Mini-Tools

Mini-Tools est une collection d'outils utiles pour la gestion de divers aspects de votre système. Chaque outil est conçu pour résoudre des problèmes spécifiques de manière efficace et conviviale.

## Table des matières

- [Installation](#installation)
- [Outils disponibles](#outils-disponibles)
  - [Ports Manager](#ports-manager)
    - [Utilisation](#utilisation)
    - [Options](#options)
    - [Exemples](#exemples)
    - [Prérequis](#prérequis)
- [Contributions](#contributions)
- [Licence](#licence)
- [Auteurs](#auteurs)

## Installation

Pour installer et utiliser les outils de ce dépôt, clonez le dépôt et ajoutez-le à votre PATH.

```bash
git clone https://github.com/votre-utilisateur/Mini-Tools.git && cd Mini-Tools && chmod +x install_MiniTools && ./install_MiniTools
```

Rechargez votre terminal ou exécutez `source ~/.bashrc` ou `source ~/.zshrc` pour appliquer les modifications.

### Note

Le script `install_MiniTools` est un script bash qui vérifie que les outils nécessaires sont installés et disponibles dans le PATH. Si un outil nécessite un outil spécifique, donne aux outils les permissions nécéssaires pour être exécutable. En d'autres termes, il installe les prérequis nécessaires.

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
  Port: 22
  PID     User        Application         Protocol        Name
  1111    root        sshd                TCP             sshd

  Port: 80
  PID     User        Application         Protocol        Name
  1234    root        nginx               TCP             nginx

  Port: 443
  PID     User        Application         Protocol        Name
  5678    root        nginx               TCP             nginx
  ```

- Lister tous les ports ouverts et tuer les processus après confirmation :
  ```bash
  portsmanager --all --kill
  ```

- Tuer tous les processus écoutant sur tous les ports sans confirmation :
  ```bash
  portsmanager --kill-all
  ```

## Prérequis

Avant d'utiliser `portsmanager`, assurez-vous que votre système dispose des prérequis suivants :

1. **Système d'exploitation** : `portsmanager` est conçu pour fonctionner sur les systèmes d'exploitation basés sur Unix, comme Linux et macOS.
2. **Permissions sudo** : Certaines commandes nécessitent des permissions élevées pour lister et tuer les processus. Assurez-vous que votre utilisateur dispose des permissions sudo.
3. **Outils installés** : Les outils suivants doivent être installés et disponibles dans votre PATH :
   - `lsof` : Utilisé pour lister les processus écoutant sur les ports.
   - `ps` : Utilisé pour obtenir le nom des applications à partir de leurs PID.
   
   Vous pouvez vérifier l'installation de ces outils avec les commandes suivantes :
   ```bash
   which lsof
   which ps
   ```
   Si ces commandes ne renvoient aucun chemin, vous devez installer les outils nécessaires.

4. **Permissions d'exécution** : Assurez-vous que le script `portsmanager` est exécutable. Vous pouvez définir les permissions d'exécution avec la commande :
   ```bash
   chmod +x portsmanager
   ```

## Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations ou des nouveaux outils à ajouter, n'hésitez pas à ouvrir une issue ou une pull request.

Pour ajouter un Tools à Mini-Tools, il faut l'ajouter dans le fichier mini_tools_list.txt

Si un outil nécessite un outil spécifique, il faut l'ajouter dans le fichier install_list.txt

Ajouter votre pseudo dans la section "Auteurs" du README.md

## Auteurs

- [DIGYSKY "lilyan CHAUVEAU"](https://github.com/DIGYSKY) (Initiateur du projet)

## Licence

Ce projet est sous licence GNU GPLv3. Voir le fichier [LICENSE](LICENSE) pour plus de détails.