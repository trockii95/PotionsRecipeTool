# Potion Recipes Config Editor for Ark Ascended

## Description

A graphical tool for creating and managing custom potion recipes configuration for **Ark: Survival Ascended**. This application helps generate the proper JSON structure required for the `TP_OverrideRecipesJson` setting in the game's INI configuration files.

## Features

- **Visual Recipe Management**: Create and edit custom potion recipes through an intuitive GUI interface
- **Item Database**: Pre-configured database of all available game items and potions
- **JSON Export**: Generate properly formatted JSON configuration in multiple formats:
  - Readable JSON (for manual editing)
  - URL-encoded JSON (for direct INI file use)
- **Cross-Platform**: Available as both Python source and Windows executable

## Usage

### For End Users (No Python Required)
- Download the `PotionConfigEditor.exe` from Releases
- Run the executable directly
- No additional software installation needed

### For Developers/Python Users
- Requires **Python 3.7+**
- Run the `PotionsConfigRecipesTool.py` script
- Install dependencies: `pip install tkinter` (usually included with Python)

## How It Works

1. **Select Potions**: Choose from pre-defined potion types or add custom ones
2. **Add Ingredients**: Build recipes by selecting items from the comprehensive database
3. **Set Quantities**: Define required amounts for each ingredient
4. **Export Configuration**: Copy the generated JSON to your game's INI file under the `TP_OverrideRecipesJson` setting

## Game Integration

The generated JSON configuration should be placed in your `gameusersetting.ini` file:

```ini
[TROCKII_Potions]
TP_OverrideRecipesJson=YOUR_GENERATED_JSON_HERE
