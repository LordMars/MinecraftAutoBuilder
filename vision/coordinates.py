import pytesseract
import os
import json
from PIL import Image, ImageEnhance
import time
import cv2
import numpy as np

config_file_name = "config.json"
current_directory = os.getcwd()
file_path = os.path.join(current_directory, config_file_name)
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

tessString = data["tesseract"]

crop_box = data["crop_box"]
crop_coords = (crop_box["left"], crop_box["top"], crop_box["right"], crop_box["bottom"])
custom_traineddata_path = ""

pytesseract.pytesseract.tesseract_cmd = tessString

def getCoords():
    process_image("data/screenshots/screenshot.png", "data/screenshots/processed_screenshot.png")
    image = Image.open("data/screenshots/processed_screenshot.png")#.convert("L")
    #crop_coords = (630, 550, 940, 760)

    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(10.0)

    image = image.crop(crop_coords)

    text = pytesseract.image_to_string(image, lang='mc')
    return text

def process_image(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
    hsv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)

    color_lower = np.array([100, 255, 220])
    color_upper = np.array([200, 255, 230])

    mask = cv2.inRange(hsv_image, color_lower, color_upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    image = cv2.cvtColor(np.array(result), cv2.COLOR_RGB2GRAY)

    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    cv2.imwrite(output_path, image)