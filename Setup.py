#!/usr/bin/env python
"""
MyGame Launcher - Start your Ren'Py game

NOTE: The Ren'Py SDK you downloaded needs the FULL version with 
compiled libraries. See SETUP.txt for detailed instructions.
"""

import os
import sys

def main():
    game_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("\n" + "="*70)
    print("[MyGame] Ren'Py Game Launcher")
    print("="*70 + "\n")
    
    print("SETUP NEEDED: Your Ren'Py SDK is incomplete.\n")
    
    print("What to do:")
    print("1. Download Ren'Py from: https://www.renpy.org/latest.html")
    print("   - Windows: Get the installer or full SDK .zip")
    print("   - Don't use the .7z.exe installer stub\n")
    
    print("2. Extract the FULL Ren'Py to: MyGame\\renpy\\")
    print("   You should have files like:")
    print("   - MyGame\\renpy\\renpy\\     (engine)")
    print("   - MyGame\\renpy\\launcher\\  (tools)")
    print("   - MyGame\\renpy\\lib\\       (libraries)\n")
    
    print("3. Then run: python Setup.py\n")
    
    print("ALTERNATIVELY:")
    print("- Use the Ren'Py Launcher directly")
    print("- Click Browse, select MyGame folder, click Launch\n")
    
    print("See SETUP.txt in this folder for more help.\n")
    
    print("="*70 + "\n")
    
    # Try to open SETUP.txt if it exists
    setup_file = os.path.join(game_dir, "SETUP.txt")
    if os.path.exists(setup_file):
        print("Opening SETUP.txt for more details...\n")
        try:
            if sys.platform == "win32":
                os.startfile(setup_file, "open")
            else:
                os.system(f"cat '{setup_file}'")
        except:
            pass
    
    return 1

if __name__ == "__main__":
    sys.exit(main())
