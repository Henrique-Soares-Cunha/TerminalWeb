# TerminalWeb
Web Automation CLI

A lightweight Python CLI tool for Linux that allows you to open your favorite bookmarked websites directly from the terminal by name and automatically closes the terminal window upon launch.
🛠️ Prerequisites

    OS: Linux (Arch Linux, Ubuntu, Debian, Fedora, etc.) or macOS

    Python: Python 3.x installed (python3 --version)

    Shell: Bash or Zsh

🚀 Installation

Open your terminal and follow these steps to clone and set up the project:
1. Clone the Repository
Bash

git clone https://github.com/Henrique-Soares-Cunha/TerminalWeb.git
cd TerminalWeb

2. Make the Installer Executable
Bash

chmod +x install.sh

3. Run the Installer
Bash

./install.sh

4. Reload Your Shell Configuration

Apply the changes to your current terminal session:
Bash

source ~/.bashrc
# Or if you use Zsh:
# source ~/.zshrc

📖 Usage

Once installed, you can launch any saved website using the web command followed by the site's shortcut name:
Bash

web notion

Available Default Shortcuts in /sites.json

⚙️ Adding or Editing Shortcuts

All bookmarks are managed inside a simple JSON configuration file.

To add new websites or edit existing URLs, open the configuration file in your terminal:
Bash

nano ~/.local/share/web-automation/sites.json

Add your custom shortcuts following this format:
JSON

{
  "name-you-chose":"URL",
}

Save and exit (Ctrl + O, Enter, Ctrl + X). The changes will take effect immediately.
📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
