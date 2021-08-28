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
from tensorflow.keras.layers import LeakyReLU, Dense, PReLU
from tensorflow.keras.activations import elu

header = []
for i in range(10_351):
    header.append(str(i))
df = pd.read_csv("cleaned_doubled_maindatabase.csv", names=header)

actions = df.pop("10350")

img_train, img_test, action_train, action_test = train_test_split(np.array(df), np.array(actions), test_size=0.2)
img_train = img_train / 255.0
img_test = img_test / 255.0
action_train = action_train.astype(int)
action_test = action_test.astype(int)


def load_model():
    leaky_relu = LeakyReLU(alpha=0.01)
    para_relu = PReLU()
    model = keras.Sequential([
        keras.layers.Dense(1024, input_shape=(10350,), activation=leaky_relu),
        # keras.layers.Dense(264, input_shape=(10350,), activation=leaky_relu),
        #keras.layers.Dense(1024, activation=leaky_relu),
        # keras.layers.Dense(264, activation=leaky_relu),

        keras.layers.Dense(units=7)
    ])

    model.compile(optimizer=tf.keras.optimizers.SGD(),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])
    return model

model = load_model()
model.fit(img_train, action_train, epochs=10)
results = model.evaluate(img_test,  action_test, verbose=2)
print(results)

filename = os.getcwd()
model.save(os.getcwd())
print(f"Model saved to {filename}.")