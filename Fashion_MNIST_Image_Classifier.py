# -*- coding: utf-8 -*-
"""Image Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZrYssaoI4VqR_wSsxgLNSXsnwLoJJF7W
"""

import numpy as np
import tensorflow as tf
import pandas as pd

import tensorflow_datasets as tfds

(fashion_train, fashion_test), info = tfds.load('fashion_mnist', split=['train[:60]', 'train'],with_info=True)

fashion_train

tfds.show_examples(fashion_train, info)

X_train = []
Y_train = []
   
for instance in fashion_train:
  X_train.append(instance['image'])
  Y_train.append(instance['label'])

X_train = np.array(X_train)
X_train.shape

Y_train = np.array(Y_train)
Y_train.shape

Y_train

# One Hot Encoding, 10 possibel values or classes
Y_train = tf.one_hot(Y_train, 10)

Y_train

# Building the Neural Network, Convolution Neural Network!

# Importing libraries
from tensorflow import keras
from keras import layers
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

cnn_model = keras.Sequential()

cnn_model.add(Conv2D(20, kernel_size=(2,2), strides=(1,1), activation='relu', input_shape=(28, 28, 1)))
cnn_model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))
cnn_model.add(Conv2D(15, kernel_size=(2,2), strides=(1,1), activation='relu', input_shape=(28, 28, 1)))
cnn_model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))
cnn_model.add(Conv2D(10, kernel_size=(2,2), strides=(1,1), activation='relu', input_shape=(28, 28, 1)))
cnn_model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))
cnn_model.add(Flatten())
cnn_model.add(Dense(10, activation='softmax'))

cnn_model.summary()

X_train = X_train/255

SGD = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.4)

cnn_model.compile(optimizer=SGD, loss='categorial_crossentropy', metrics=['accuracy'])

cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

cnn_model.fit(X_train, Y_train, epochs=35, batch_size=150, shuffle=True)

cnn_model.evaluate(X_train, Y_train)

predictions = cnn_model.predict(X_train)
predicted_classes = np.argmax(predictions, axis=1)

predictions

from google.colab import drive
drive.mount('/content/drive')

!pip install nbconvert
!jupyter nbconvert --to pdf Sample1.ipynb

!pip install nbconvert