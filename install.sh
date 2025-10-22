#!/bin/bash

echo
echo "========================================"
echo "   KeepAlive - Installation Script"
echo "========================================"
echo

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Installing Python3..."
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
else
    echo "✅ Python3 is already installed"
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Installing pip3..."
    sudo apt install -y python3-pip
else
    echo "✅ pip3 is already installed"
fi

# Install system dependencies for pyautogui (required for GUI automation on Linux)
echo
echo "Installing system dependencies for GUI automation..."
sudo apt update
sudo apt install -y python3-tk python3-dev scrot python3-xlib

# Install Python dependencies
echo
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo
    echo "✅ Installation completed successfully!"
    echo
    echo "To run KeepAlive:"
    echo "  ./run.sh [delay_in_seconds]"
    echo
    echo "Examples:"
    echo "  ./run.sh          (60 second default)"
    echo "  ./run.sh 30       (30 second interval)"
    echo "  ./run.sh 120      (2 minute interval)"
    echo
    echo "Note: Make sure you're running this in a graphical environment (not SSH without X11 forwarding)"
    echo
else
    echo
    echo "❌ Installation failed!"
    echo "Please check the error messages above and try again."
    echo
    exit 1
fi

# Make run script executable
chmod +x run.sh

echo "🔧 Made run.sh executable"
echo
echo "Ready to use! Run './run.sh' to start KeepAlive."
