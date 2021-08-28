import csv
import pickle
import numpy as np
import pandas as pd
import pathlib
import os
import time
from sklearn.model_selection import train_test_split
import mss
from pynput.keyboard import Key, Controller
import cv2
import collections
import keyboard

mss_instance = mss.mss()
screenshot_queue = collections.deque([[1, 2], [3, 4]])


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
    #print(len(flattened))
    return resized, flattened


def detect_action():
    if keyboard.is_pressed('w'):
        action = 1
        time.sleep(0.12)
    elif keyboard.is_pressed("s"):
        action = 2
        time.sleep(0.09)
    elif keyboard.is_pressed("a"):
        action = 3
        time.sleep(0.03)
    elif keyboard.is_pressed("d"):
        action = 4
        time.sleep(0.03)
    elif keyboard.is_pressed("left"):
        action = 5
        time.sleep(0.09)
    elif keyboard.is_pressed("right"):
        action = 6
        time.sleep(0.09)
    else:
        action = 0
    return action


if __name__ == "__main__":
    time.sleep(2)
    print("Gathering data...")

    with open("database1.csv", "w", newline="") as log_csv:
        writer = csv.writer(log_csv, dialect="excel")
        while True:
            start = time.time()
            hsv, flattened = get_image_data()
            action = detect_action()
            screenshot_queue.appendleft(flattened)
            screenshot_queue.pop()
            training_data = np.append(screenshot_queue[1], action)
            writer.writerow(training_data)
            if action == 0:
                print("NO ACTION")
            elif action == 1:
                print("JUMP")
            elif action == 2:
                print("SLIDE")
            elif action == 3:
                print("LEFT TURN")
            elif action == 4:
                print("RIGHT TURN")
            elif action == 5:
                print("LEFT LANE")
            elif action == 6:
                print("RIGHT LANE")
            elapsed = time.time() - start
            while elapsed < 0.035:
                elapsed = time.time() - start
            # print(elapsed)
            cv2.imshow("dsad", hsv)
            if cv2.waitKey(5) & 0xFF == ord("q"):
                cv2.destroyAllWidndows()
                break


