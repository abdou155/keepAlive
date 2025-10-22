#!/usr/bin/env python3
"""
KeepAlive - Anti-AFK Mouse Movement Tool
A Python script that moves the mouse cursor randomly to prevent AFK timeouts.
"""

import pyautogui
import time
import random
import sys
import argparse
import signal
import os
from datetime import datetime
from colorama import Fore, Back, Style, init
import pyfiglet

# Initialize colorama for Windows compatibility
init(autoreset=True)

class KeepAlive:
    def __init__(self, delay=60):
        self.delay = delay
        self.is_running = False
        self.start_time = None
        self.move_count = 0
        
        # Disable pyautogui failsafe (moving mouse to corner won't stop the program)
        pyautogui.FAILSAFE = False
        
        # Get screen size
        self.screen_width, self.screen_height = pyautogui.size()
        self.margin = 50  # Keep cursor away from edges
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def display_header(self):
        """Display the application header with ASCII art and info"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # ASCII Art Header
        ascii_art = pyfiglet.figlet_format("KeepAlive", font="small")
        print(Fore.CYAN + ascii_art)
        
        # Header info
        print(Fore.YELLOW + "🖱️  Mouse Anti-AFK Application (Python Edition)")
        print(Fore.LIGHTBLACK_EX + "━" * 60)
        print(Fore.LIGHTBLACK_EX + f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(Fore.LIGHTBLACK_EX + f"⏱️  Interval: {self.delay} seconds")
        print(Fore.LIGHTBLACK_EX + f"🖥️  Screen Size: {self.screen_width}x{self.screen_height}")
        print(Fore.LIGHTBLACK_EX + "━" * 60)
        print()

    def get_random_position(self):
        """Generate a random position within screen bounds with margin"""
        x = random.randint(self.margin, self.screen_width - self.margin)
        y = random.randint(self.margin, self.screen_height - self.margin)
        return x, y

    def move_mouse_randomly(self):
        """Move mouse to a random position"""
        try:
            # Get current position
            current_x, current_y = pyautogui.position()
            
            # Get new random position
            new_x, new_y = self.get_random_position()
            
            # Move mouse smoothly
            pyautogui.moveTo(new_x, new_y, duration=0.5)
            
            # Increment move counter
            self.move_count += 1
            
            # Log the movement
            timestamp = datetime.now().strftime('%H:%M:%S')
            print(
                Fore.GREEN + "✅" + 
                Fore.WHITE + f" [{timestamp}] " + 
                Fore.BLUE + "Mouse moved: " + 
                Fore.LIGHTBLACK_EX + f"({current_x}, {current_y})" + 
                Fore.WHITE + " → " + 
                Fore.LIGHTBLACK_EX + f"({new_x}, {new_y})"
            )
            
            return True
            
        except Exception as e:
            timestamp = datetime.now().strftime('%H:%M:%S')
            print(
                Fore.RED + "❌" + 
                Fore.WHITE + f" [{timestamp}] " + 
                Fore.RED + "Error moving mouse: " + 
                Fore.LIGHTBLACK_EX + str(e)
            )
            return False

    def display_status(self):
        """Display current status information"""
        if self.start_time:
            uptime = time.time() - self.start_time
            hours = int(uptime // 3600)
            minutes = int((uptime % 3600) // 60)
            seconds = int(uptime % 60)
            
            print()
            print(Fore.LIGHTBLACK_EX + "━" * 60)
            print(Fore.YELLOW + "📊 Status Information:")
            print(Fore.LIGHTBLACK_EX + f"   Uptime: {hours:02d}h {minutes:02d}m {seconds:02d}s")
            print(Fore.LIGHTBLACK_EX + f"   Total Moves: {self.move_count}")
            print(Fore.LIGHTBLACK_EX + f"   Next move in: {self.delay} seconds")
            print(Fore.LIGHTBLACK_EX + f"   Press Ctrl+C to stop")
            print(Fore.LIGHTBLACK_EX + "━" * 60)
            print()

    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        self.stop()

    def stop(self):
        """Stop the application gracefully"""
        self.is_running = False
        print()
        print(Fore.YELLOW + "🛑 Shutting down KeepAlive...")
        print(Fore.LIGHTBLACK_EX + "   Mouse movement stopped.")
        
        if self.start_time:
            total_time = time.time() - self.start_time
            print(Fore.LIGHTBLACK_EX + f"   Total runtime: {int(total_time)} seconds")
            print(Fore.LIGHTBLACK_EX + f"   Total moves: {self.move_count}")
        
        print(Fore.GREEN + "✅ Application closed successfully.")
        sys.exit(0)

    def run(self):
        """Main application loop"""
        self.display_header()
        
        # Validate screen access
        try:
            pyautogui.position()
        except Exception as e:
            print(Fore.RED + "❌ Error: Unable to access mouse control.")
            print(Fore.LIGHTBLACK_EX + "   Make sure you have the necessary permissions.")
            print(Fore.LIGHTBLACK_EX + f"   Error details: {e}")
            sys.exit(1)
        
        self.is_running = True
        self.start_time = time.time()
        
        print(Fore.BLUE + "🚀 Starting mouse movement...")
        
        # Perform initial mouse movement
        self.move_mouse_randomly()
        
        print(Fore.GREEN + "✅ KeepAlive is now running...")
        print(Fore.LIGHTBLACK_EX + "   Press Ctrl+C to stop the application")
        print()
        
        # Status display counter
        status_counter = 0
        
        try:
            while self.is_running:
                # Wait for the specified delay
                for i in range(self.delay):
                    if not self.is_running:
                        break
                    time.sleep(1)
                
                if not self.is_running:
                    break
                
                # Move mouse
                self.move_mouse_randomly()
                
                # Display status every 5 minutes (300 seconds)
                status_counter += self.delay
                if status_counter >= 300:
                    self.display_status()
                    status_counter = 0
                    
        except KeyboardInterrupt:
            self.stop()

def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(
        description="KeepAlive - Anti-AFK Mouse Movement Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python keepalive.py           # Use default 60 second interval
  python keepalive.py 30        # Move mouse every 30 seconds
  python keepalive.py --delay 120  # Move mouse every 2 minutes
        """
    )
    
    parser.add_argument(
        'delay', 
        nargs='?', 
        type=int, 
        default=60,
        help='Delay between mouse movements in seconds (default: 60)'
    )
    
    parser.add_argument(
        '--delay', '-d',
        type=int,
        help='Alternative way to specify delay'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='KeepAlive 2.0.0 (Python Edition)'
    )
    
    args = parser.parse_args()
    
    # Use --delay if specified, otherwise use positional argument
    delay = args.delay if args.delay else args.delay
    
    # Validate delay
    if delay < 1:
        print(Fore.RED + "❌ Error: Delay must be at least 1 second")
        sys.exit(1)
    elif delay > 3600:
        print(Fore.YELLOW + "⚠️  Warning: Delay is very long (>1 hour)")
    
    # Create and run the application
    app = KeepAlive(delay)
    app.run()

if __name__ == "__main__":
    main()
