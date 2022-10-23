import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('test_model.h5', compile = True)

def predict(im_path):

    model = tf.keras.models.load_model('test_model.h5', compile = True)

    classes = ["Ammonite", "Trilobite"]

    im = Image.open(im_path)
    im = im.resize((180, 180))
    im.save(im_path)

    img_width, img_height = 180, 180
    img = tf.keras.preprocessing.image.load_img(im_path, target_size = (img_width, img_height))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)

    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)
    predicted_class = classes[predicted_class[0]]

    #print(prediction)
    #print(predicted_class)

    return predicted_class

predict("D:/Eamon/Documents/GitHub/FossilIDImage/IdAI/main/train/test_images/ammonite/2.jpg")