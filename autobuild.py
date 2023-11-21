import os
os.environ['DISPLAY'] = ':0'

import pyautogui
import keyboard
import actions
#from actions import *

keyboard.hook(actions.on_key_event)
keyboard.wait('esc')