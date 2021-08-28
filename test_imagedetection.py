import cv2
import numpy as np
# import tensorflow as tf
import os
import mss
from pynput.keyboard import Key, Controller
import keyboard
import csv
import time
import pickle


mss_instance = mss.mss()
keyboard_instance = Controller()


def get_image_data(scale_percent=20):
    screenshot = mss_instance.grab({
        "left": 1206,
        "top": 100,
        "width": 385,
        "height": 625
    })
    img = np.array(screenshot)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    width = int(img_gray.shape[1] * scale_percent / 100)
    height = int(img_gray.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)
    img_blur = cv2.GaussianBlur(resized, (3, 3), 0)
    flattened = img_blur.flatten()
    return img, img_blur, width, height, flattened


while True:

    image, blur, width, height, flattened = get_image_data()

    cv2.imshow("daf", image)
    cv2.imshow("da", blur)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        cv2.destroyAllWidndows()
        break