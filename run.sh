#!/bin/bash

# KeepAlive Runner Script for Ubuntu/Linux
# Usage: ./run.sh [delay_in_seconds]

# Check if we're in a graphical environment
if [ -z "$DISPLAY" ]; then
    echo "❌ Error: No display detected!"
    echo "   Make sure you're running this in a graphical environment."
    echo "   If using SSH, try: ssh -X username@hostname"
    exit 1
fi

# Check if Python3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python3 is not installed!"
    echo "   Run './install.sh' first to install dependencies."
    exit 1
fi

# Check if keepalive.py exists
if [ ! -f "keepalive.py" ]; then
    echo "❌ Error: keepalive.py not found!"
    echo "   Make sure you're running this script from the KeepAlive directory."
    exit 1
fi

# Run the Python script with or without delay parameter
if [ -z "$1" ]; then
    echo "🚀 Starting KeepAlive with default 60-second interval..."
    python3 keepalive.py
else
    echo "🚀 Starting KeepAlive with $1-second interval..."
    python3 keepalive.py "$1"
fi
