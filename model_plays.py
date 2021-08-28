import csv
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
import pathlib
import os
import time
from sklearn.model_selection import train_test_split
import mss
from pynput.keyboard import Key, Controller
import cv2


mss_instance = mss.mss()
keyboard = Controller()
model = keras.models.load_model(os.getcwd())


def get_image_data(scale_percent=12):
    screenshot = mss_instance.grab({
        "left": 1206,
        "top": 100,
        "width": 385,
        "height": 625
    })
    img = np.array(screenshot)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    width = int(hsv_img.shape[1] * scale_percent / 100)
    height = int(hsv_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(hsv_img, dim, interpolation=cv2.INTER_AREA)
    #img_blur = cv2.GaussianBlur(resized, (3, 3), 0)
    flattened = resized.flatten()
    flattened = flattened / 255.0
    return flattened


def jump():
    keyboard.release("a")
    keyboard.release("s")
    keyboard.release("d")
    keyboard.release(Key.left)
    keyboard.release(Key.right)
    keyboard.press("w")
    time.sleep(0.01)


def slide():
    keyboard.release("w")
    keyboard.release("a")
    keyboard.release("d")
    keyboard.release(Key.left)
    keyboard.release(Key.right)
    keyboard.press("s")
    time.sleep(0.01)


def turn_right():
    keyboard.release("w")
    keyboard.release("a")
    keyboard.release("s")
    keyboard.release(Key.left)
    keyboard.release(Key.right)
    keyboard.press("d")
    time.sleep(0.01)


def turn_left():
    keyboard.release("w")
    keyboard.release("s")
    keyboard.release("d")
    keyboard.release(Key.left)
    keyboard.release(Key.right)
    keyboard.press("a")
    time.sleep(0.01)


def leftlane():
    keyboard.release("w")
    keyboard.release("a")
    keyboard.release("s")
    keyboard.release("d")
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    time.sleep(0.08)


def rightlane():
    keyboard.release("w")
    keyboard.release("a")
    keyboard.release("s")
    keyboard.release("d")
    keyboard.release(Key.left)
    keyboard.press(Key.right)
    time.sleep(0.08)


def do_nothing():
    keyboard.release("w")
    keyboard.release("a")
    keyboard.release("s")
    keyboard.release("d")
    keyboard.release(Key.left)
    keyboard.release(Key.right)


options = [do_nothing, jump, slide, turn_left, turn_right, leftlane, rightlane]


def take_action2(action, options=options):
    options[action]()
    print(action)

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()



while True:
    start = time.time()
    data = np.expand_dims(get_image_data(), 0)
    prediction = model.predict(data)
    # prediction = tf.nn.softmax(prediction[0])
    prediction[0][0] = prediction[0][0] - 2.2
    # prediction[0][1] = prediction[0][1] + 1.5
    # prediction[0][3] = prediction[0][3] - 1
    #prediction[0][4] = prediction[0][4] - 1
    take_action2(np.argmax(prediction))
    print(prediction)
    # print(time.time() - start)
