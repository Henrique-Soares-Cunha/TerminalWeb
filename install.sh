# Safe destination directory inside the user's home folder
TARGET_DIR="$HOME/.local/share/web-automation"

echo "Installing Web Automation..."

# 1. Create the destination directory
mkdir -p "$TARGET_DIR"

# 2. Copy project files to the installation path
cp webAutomationScript.py sites.json "$TARGET_DIR/"

# 3. Identify which shell configuration file the user is using
if [ -n "$ZSH_VERSION" ] || [ -f "$HOME/.zshrc" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
else
    SHELL_CONFIG="$HOME/.bashrc"
fi

# 4. Inject the web() function only if it does not already exist in the file
if ! grep -q "web()" "$SHELL_CONFIG"; then
    echo "" >> "$SHELL_CONFIG"
    echo "# Web Automation CLI" >> "$SHELL_CONFIG"
    echo 'web() { python3 '$TARGET_DIR'/webAutomationScript.py "$@"; exit; }' >> "$SHELL_CONFIG"

    echo "Installation completed successfully!"
    echo "Run 'source $SHELL_CONFIG' or restart your terminal to use the 'web' command."
    cd ..
    rm -rf TerminalWeb
else
    echo "The 'web()' command is already configured in your $SHELL_CONFIG."
fi