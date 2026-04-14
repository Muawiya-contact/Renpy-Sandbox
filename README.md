# MyGame - Ren'Py Visual Novel

## How to Run

1. **Install Ren'Py**: Download from [renpy.org](https://renpy.org/)
2. **Place engine files**: Extract Ren'Py into the `renpy/` folder
3. **Run the game**:
   ```bash
   python Setup.py
   ```
   Or directly with Ren'Py launcher

## Project Structure

- `game/` - Your game scripts and assets
  - `script.rpy` - Main story script
  - `options.rpy` - Game configuration
- `renpy/` - Ren'Py engine files
- `Setup.py` - Game launcher

## Creating Your Game

Edit `game/script.rpy` to write your story using Ren'Py script language.

Example:
```renpy
label start:
    "Character" "Hello!"
    menu:
        "Option 1":
            "You chose option 1"
        "Option 2":
            "You chose option 2"
```
