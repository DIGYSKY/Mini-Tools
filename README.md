# Mini-Tools 1.2.1

Mini-Tools is a collection of useful tools for managing various aspects of your system. Each tool is designed to solve specific problems efficiently and user-friendly.

## Table of Contents

- [Installation](#installation)
- [Mini-Tools command](#mini-tools-command)
- [Available Tools](#available-tools)
  - [Ports Manager](#ports-manager)
    - [Usage](#usage)
    - [Options](#options)
    - [Examples](#examples)
    - [Prerequisites](#prerequisites)
  - [Env Manager](#env-manager)
    - [Usage](#usage)
    - [Options](#options)
    - [Examples](#examples)
    - [Prerequisites](#prerequisites)
- [Contributions](#contributions)
- [License](#license)
- [Authors](#authors)

## Installation

To install and use the tools in this repository, clone the repository and add it to your PATH.

```bash
git clone https://github.com/DIGYSKY/Mini-Tools.git && cd Mini-Tools && chmod +x install_MiniTools && ./install_MiniTools
```

Reload your terminal or run `source ~/.bashrc` or `source ~/.zshrc` to apply the changes.

### Note

The `install_MiniTools` script is a bash script that checks that the necessary tools are installed and available in the PATH. If a tool requires a specific tool, it gives the tools the necessary permissions to be executable. In other words, it installs the necessary prerequisites.

## Mini-Tools command

`minitools` is the main command to manage the available tools in the Mini-Tools project. Here is a guide to using this command.

### Usage

- `-v, --version`: Display the version of Mini-Tools
- `-l, --list-tools`: List available tools and unavailable tools
- `-up, --update`: Update Mini-Tools from the repository
- `-h, --help`: Display this help

## Available Tools

### Ports Manager

`portsmanager` is a port management tool that allows you to list and manage processes listening on specific ports or on all open ports.

#### Usage

```bash
portsmanager <port> [<port> ...]
portsmanager <port> [<port> ...] [--kill|-k] [-y]
portsmanager [--all|-a]
portsmanager [--all|-a] [--kill|-k] [-y]
portsmanager [--kill-all|-ka]
portsmanager [--help|-h]
```

#### Options

- `<port>`: Specify one or more ports for which you want to list the processes.
- `--kill, -k`: Optional. Kill the processes listening on the specified ports after confirmation.
- `-y`: Optional. Used with `--kill` to kill the processes without confirmation.
- `--all, -a`: List all open ports.
- `--kill-all, -ka`: Kill all processes listening on all ports without confirmation.
- `-a -k -y` is the same as `-ka`.
- `--help, -h`: Display this help message and exit.

#### Examples

- List processes listening on ports 80 and 443:
  ```bash
  portsmanager 80 443
  ```

- List and kill processes listening on ports 80 and 443 after confirmation:
  ```bash
  portsmanager 80 443 --kill
  ```

- List and kill processes listening on ports 80 and 443 without confirmation:
  ```bash
  portsmanager 80 443 --kill -y
  ```

- List all open ports:
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

- List all open ports and kill processes after confirmation:
  ```bash
  portsmanager --all --kill
  ```

- Kill all processes listening on all ports without confirmation:
  ```bash
  portsmanager --kill-all
  ```

## Prerequisites

Before using `portsmanager`, ensure that your system meets the following prerequisites:

1. **Operating System**: `portsmanager` is designed to work on Unix-based operating systems, such as Linux and macOS.
2. **Sudo Permissions**: Some commands require elevated permissions to list and kill processes. Ensure your user has sudo permissions.
3. **Installed Tools**: The following tools must be installed and available in your PATH:
   - `lsof`: Used to list processes listening on ports.
   - `ps`: Used to get the name of applications from their PID.
   
   You can check the installation of these tools with the following commands:
   ```bash
   which lsof
   which ps
   ```
   If these commands do not return any path, you need to install the necessary tools.

4. **Executable Permissions**: Ensure the `portsmanager` script is executable. You can set the executable permissions with the command:
   ```bash
   chmod +x portsmanager
   ```

### Env Manager

`envmanager` is a tool for managing environment variables, allowing you to show, add, delete, list, and find environment variables.

#### Usage

```bash
envmanager [options]
```

#### Options

- `-s, --show VARIABLE`: Show the value of an environment variable.
- `-a, --add VARIABLE=VALUE`: Add a new environment variable.
- `-d, --delete VARIABLE`: Delete an environment variable.
- `-l, --list`: List all environment variables.
- `-f, --find VARIABLE`: Find an environment variable by name.
- `-h, --help`: Display this help message and exit.

#### Examples

- Show the value of an environment variable:
  ```bash
  envmanager -s VARIABLE
  ```

- Add a new environment variable:
  ```bash
  envmanager -a VARIABLE=VALUE
  ```

- Delete an environment variable with confirmation:
  ```bash
  envmanager -d VARIABLE
  ```

- List all environment variables:
  ```bash
  envmanager -l
  ```

- Find an environment variable by name:
  ```bash
  envmanager -f VARIABLE
  ```

#### Prerequisites

Before using `envmanager`, ensure that your system meets the following prerequisites:

1. **Operating System**: `envmanager` is designed to work on Unix-based operating systems, such as Linux and macOS.
2. **Shell**: You need to use a compatible shell such as `bash`, `zsh`, or any other POSIX-compliant shell.
3. **Executable Permissions**: Ensure the `envmanager` script is executable. You can set the executable permissions with the following command:
   ```bash
   chmod +x envmanager
   ```

## Contributions

Contributions are welcome! If you have ideas for improvements or new tools to add, feel free to open an issue or a pull request.

To add a tool to Mini-Tools, add it to the `mini_tools_list.txt` file.

If a tool requires a specific tool, add it to the `install_list.txt` file.

Add your username in the "Authors" section of the README.md with your contribution.

## Authors

- [DIGYSKY "Lilyan CHAUVEAU"](https://github.com/DIGYSKY) (Project Initiator)
  - Created the structure of Mini-Tools
  - Created the `install_MiniTools` script
  - Created the `mini_tools_list.txt` file
  - Created the `install_list.txt` file
  - Created the `README.md` file
  - Added the `LICENSE` file
  - Created the Ports Manager tool `portsmanager`
  - Created the Env Manager tool `envmanager`
  - Created main command `minitools`

## License

This project is licensed under the GNU GPLv3 license. See the [LICENSE](LICENSE) file for details.

