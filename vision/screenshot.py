import mss
import os
import json
import time

screenshot_file_name = os.path.abspath("data/screenshots/screenshot.png")
current_directory = os.getcwd()
screenshot_path = os.path.join(current_directory, screenshot_file_name)

config_file_name = "config.json"
current_directory = os.getcwd()
file_path = os.path.join(current_directory, config_file_name)
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

monitor_number = data["monitor_number"]

def getScreenshot():
    with mss.mss() as sct:
        sct.shot(mon=monitor_number, output=screenshot_path)