import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt

model = tf.keras.models.load_model('test_model.h5')

im_path = "D:/Eamon/Documents/GitHub/FossilIDImage/IdAI/main/train/test_images/2.jpg"

im = Image.open(im_path)
im = im.resize((180, 180))
im.save(im_path)

image = tf.keras.preprocessing.image.load_img(im_path, target_size=(180, 180))
import numpy as np

input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])  # Convert single image to a batch.

input_arr = input_arr.astype('float32') / 255.  # This is VERY important
predictions = model.predict(input_arr)
predicted_class = np.argmax(predictions[0], axis=-1)
print(predictions)
print(predicted_class)