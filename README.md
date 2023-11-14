Minecraft Auto Builder Script

To run:
    source minecraft/bin/activate
        loads up virtual environment

This script is intended to be run while also running minecraft.
AutoBuilder will control minecraft through the pyautogui library.

Before running th script the player must stand on a block, look down at their feet, and align themselves perpendicular to the block

Provided with a map of locations within the players inventory to the string names of block types in minecraft this script will
    Auto move the player character to given block positions
    select an block type
    place a block type

The script will know where to move and what to place through being provided a list or specific instructions that determine if and how the player will
    move to a given block
    place a specific block
    do a given action
    move the mouse to a new position to
        change direction
        target a block

This version of the script will not use image recognition, so the player will have to
    be placed in a specific starting position
    have surrounding terrain of the building area meet certain conditions
    be facing a certain direction in that terrain
    