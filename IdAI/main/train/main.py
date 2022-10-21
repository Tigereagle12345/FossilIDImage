# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow.keras import layers

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import os

import pandas as pd

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

print(tf.__version__)

fossils = pd.read_csv("FossilAITestDataSet.csv")
fossils.head()
fossil_features = fossils.copy()

inputs = {}

for name, column in fossil_features.items():
  dtype = column.dtype
  if dtype == object:
    dtype = tf.string
  else:
    dtype = tf.float32

  inputs[name] = tf.keras.Input(shape=(1,), name=name, dtype=dtype)

print(inputs)
numeric_inputs = {name:input for name,input in inputs.items()
                  if input.dtype==tf.float32}

x = layers.Concatenate()(list(numeric_inputs.values()))
norm = layers.Normalization()
norm.adapt(np.array(titanic[numeric_inputs.keys()]))
all_numeric_inputs = norm(x)

print("all_numeric_inputs")
