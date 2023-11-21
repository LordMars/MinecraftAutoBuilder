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
    


Notes:
 In reduced debug mode I can use the chunks to determinie what block im on.
 By way of image recognition I can determine and calculate when Ive moved to a different block by seeing which of those numbers change and in what direction whn I move in a given direction.

 Reduced debug must be turned on then this way:
    Open the Minecraft menu.
    Go to "Options" > "Video Settings."
    Look for the "Reduced Debug Info" option.
    Set it to "On."

We will then use an image recognition library to actually check when those numbers change

Open debug text
Start script
screenshot
capture the block charachter is on from the chunk coords
delete screenshot
move charachter
take screenshot
determine if chunk changed in a way that matches intended movement.
    if not:
        move in a way to correct
        delete screenshot
        take another screenshot
        repeat
    if so:
        continue next step


As of 11/18/2023
This script uses tesseract and the pytesseract module in order o classify screenshots from the game to determine block positions
