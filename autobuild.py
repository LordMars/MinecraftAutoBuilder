import os
os.environ['DISPLAY'] = ':0'

import pyautogui
import keyboard
import time
import json
#in this file I will run the command
#give an argument to the script to choose which thing to build

file_path = 'config.json'
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

holdTime = data["default_key_hold_time"]
def forward(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('w')
        time.sleep(holdTime)
        pyautogui.keyUp('w')
        time.sleep(holdTime)
        print(f"F{i}")

def backward(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('s')
        time.sleep(holdTime)
        pyautogui.keyUp('s')
        time.sleep(holdTime)
        print(f"B{i}")

def left(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('a')
        time.sleep(holdTime)
        pyautogui.keyUp('a')
        time.sleep(holdTime)
        print(f"L{i}")

def right(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('d')
        time.sleep(holdTime)
        pyautogui.keyUp('d')
        time.sleep(holdTime)
        print(f"R{i}")

def moveTest():
    forward(4)
    time.sleep(holdTime)
    right(4)
    time.sleep(holdTime)
    backward(4)
    time.sleep(holdTime)
    left(4)
    time.sleep(holdTime)

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'page down':
            print("MOVE")
            for i in range(1000):
                if keyboard.is_pressed("esc"):
                    break
                print(i)
                moveTest()
            print("MOVE COMPLETE")

keyboard.hook(on_key_event)

keyboard.wait('esc')
