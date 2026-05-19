import numpy as np
import os

os.environ["KERAS_BACKEND"] = "tensorflow"

# Note that Keras should only be imported after the backend
# has been configured. The backend cannot be changed once the
# package is imported.
import keras
from keras import layers
import tensorflow as tf


# # Check if TensorFlow can access the GPU
# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# # Check Keras version
# print(f"Keras version: {keras.__version__}")

# # Create a tiny model to test the "flow"
# model = keras.Sequential([
#     layers.Input(shape=(1,)), 
#     layers.Dense(1)
# ])

# model.compile(optimizer='adam', loss='mse')
# print("Model compiled successfully!")

# ML HELLO WORLD EQUIVALENT: TRAIN A MODEL TO CLASSIFY HANDWRITTEN DIGITS
# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print("y_train shape:", y_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# Model parameters
num_classes = 10
input_shape = (28, 28, 1)

model = keras.Sequential(
    [
        keras.layers.Input(shape=input_shape),
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        keras.layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
        keras.layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(num_classes, activation="softmax"),
    ]
)
model.summary()
