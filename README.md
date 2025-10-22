# KeepAlive 🖱️

A Python application that moves the **real mouse cursor** randomly at specified intervals to prevent AFK (Away From Keyboard) timeouts. Simple installation with no build tools required!

## Features

- 🖱️ **Real Mouse Movement**: Actually moves your system mouse cursor (not just browser simulation)
- ⏱️ **Customizable Intervals**: Set delay between movements (1-3600 seconds)
- 🎨 **Beautiful Console Interface**: Colored output with ASCII art and real-time logging
- 📊 **Live Statistics**: Shows uptime, move count, and next movement countdown
- 📝 **Detailed Logging**: Timestamped logs with before/after coordinates
- 🛡️ **Safe Boundaries**: Keeps cursor away from screen edges (50px margin)
- 🚀 **Easy Installation**: Just Python + pip install (no build tools!)
- 💻 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🎯 **Smooth Movement**: Natural cursor transitions with configurable duration
- ⚡ **Lightweight**: Minimal resource usage

## Installation

### Option 1: Automatic Installation (Windows)
1. **Download/clone** this repository
2. **Double-click** `install.bat` to automatically install dependencies
3. **Run** using `run.bat [delay]`

### Option 2: Manual Installation
1. **Make sure Python 3.6+ is installed**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage (60-second default interval)
```bash
python keepalive.py
```

### Custom Delay
```bash
python keepalive.py 30        # Move every 30 seconds
python keepalive.py --delay 120  # Move every 2 minutes
```

### Windows Batch Files
```bash
run.bat           # Default 60 seconds
run.bat 30        # 30 second interval
run.bat 300       # 5 minute interval
```

## Dependencies

- **pyautogui**: Cross-platform mouse and keyboard automation
- **colorama**: Colored terminal output (Windows compatibility)
- **pyfiglet**: ASCII art text generation

## How It Works

1. **Screen Detection**: Automatically detects your screen resolution
2. **Random Positioning**: Generates random coordinates within safe boundaries
3. **Smooth Movement**: Moves mouse cursor with natural transition animation
4. **Real-time Logging**: Shows each movement with timestamps and coordinates
5. **Status Updates**: Displays uptime and statistics every 5 minutes
6. **Graceful Shutdown**: Handles Ctrl+C and system signals properly

## Console Output Example

```
 _  __              _    _ _           
| |/ /             | |  / \  | (_)          
| ' / ___  ___ _ __| | / _ \ | | |_   _____ 
|  < / _ \/ _ \ '_ \ |/ ___ \| | \ \ / / _ \
| . \  __/  __/ |_) / /   \ \ | |\ V /  __/
|_|\_\___|\___| .__/_/     \_\_|_| \_/ \___|
              |_|                          

🖱️  Mouse Anti-AFK Application (Python Edition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Started: 2025-10-21 12:32:15
⏱️  Interval: 30 seconds
🖥️  Screen Size: 1920x1080
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Starting mouse movement...
✅ [12:32:15] Mouse moved: (640, 360) → (1205, 543)
✅ [12:32:45] Mouse moved: (1205, 543) → (892, 234)
✅ [12:33:15] Mouse moved: (892, 234) → (1456, 789)
```

## System Requirements

- **Python**: Version 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Permissions**: May require elevated permissions on some systems for mouse control

## Troubleshooting

### Installation Issues
If you encounter issues installing dependencies:

**Windows:**
```bash
# Make sure Python and pip are in your PATH
python --version
pip --version

# Install dependencies
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
# Use python3 if python points to Python 2
python3 --version
pip3 install -r requirements.txt

# Run with python3
python3 keepalive.py
```

### Permission Issues
If you get permission errors:

**Windows:** Run Command Prompt as Administrator
**macOS/Linux:** You may need to run with sudo (not recommended for security)

### Common Issues
1. **Mouse doesn't move**: Check if pyautogui has proper permissions
2. **Import errors**: Make sure all dependencies are installed
3. **Screen detection fails**: Some virtual machines may have issues

### Tips for Best Results
- Run the script on your main display
- Ensure no other applications are controlling the mouse
- Use reasonable delay intervals (not too fast)
- Keep the terminal window open to see logs

## Advantages of Python Approach

- ✅ **Real Mouse Movement**: Actually moves your system cursor
- ✅ **No Build Tools**: Simple pip install (no C++ compilation)
- ✅ **Cross-Platform**: Works on Windows, macOS, and Linux
- ✅ **Lightweight**: Minimal resource usage
- ✅ **Reliable**: Direct system-level mouse control
- ✅ **Easy to Use**: Simple command-line interface

## License

MIT License - Feel free to modify and distribute as needed.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application.
