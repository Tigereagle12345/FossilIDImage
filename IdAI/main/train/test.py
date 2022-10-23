import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('test_model.h5', compile = True)

im_path_1 = "D:/Eamon/Documents/GitHub/FossilIDImage/IdAI/main/train/test_images/ammonite/1.jpg"
im_path_2 = "D:/Eamon/Documents/GitHub/FossilIDImage/IdAI/main/train/test_images/trilobite/2.jpg"

def predict(im_path):
    im = Image.open(im_path)
    im = im.resize((180, 180))
    im.save(im_path)

    img_width, img_height = 180, 180
    img = tf.keras.preprocessing.image.load_img(im_path, target_size = (img_width, img_height))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)

    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)
    print(prediction)
    print(predicted_class)

predict(im_path_1)