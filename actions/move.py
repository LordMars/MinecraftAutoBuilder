import keyboard
import time
import json
import os
import pyautogui

file_name = "config.json"
current_directory = os.getcwd()
file_path = os.path.join(current_directory, file_name)
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

holdTime = data["default_key_hold_time"]
endDelay = data["default_key_release_delay"]

def forward(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('w')
        time.sleep(holdTime)
        pyautogui.keyUp('w')
        time.sleep(endDelay)
        print(f"F{i}")

def backward(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('s')
        time.sleep(holdTime)
        pyautogui.keyUp('s')
        time.sleep(endDelay)
        print(f"B{i}")

def left(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('a')
        time.sleep(holdTime)
        pyautogui.keyUp('a')
        time.sleep(endDelay)
        print(f"L{i}")

def right(times=1):
    for i in range(times):
        if keyboard.is_pressed("esc"):
            break
        pyautogui.keyDown('d')
        time.sleep(holdTime)
        pyautogui.keyUp('d')
        time.sleep(endDelay)
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