# Importing Image class from PIL module
from PIL import Image
import os

dirs = ["trilobite", "ammonite"]
training_path = "D:/Eamon/Documents/GitHub/FossilIDImage/IdAI/main/train/dataset/fossils/"
testing_path = "D:/Eamon/Documents/GitHub/FossilIDImage/IdAI/main/train/test_images/"

def process_images(dirs, im_path):
    for directory in dirs:
        for file in os.listdir(im_path + directory): 
            # Opens a image in RGB mode
            im = Image.open(im_path + directory + "/" + file)
            im = im.resize((180, 180))
            print(im.size)
            im.save(im_path + directory + "/" + file)

process_images(dirs, testing_path)