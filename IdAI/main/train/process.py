# Importing Image class from PIL module
from PIL import Image
import os

dirs = ["trilobite", "ammonite"]
path = "D:/Eamon/Documents/GitHub/FossilIDImage/IdAI/main/train/dataset"

for directory in dirs:
    for file in os.listdir(path + "/fossils/" + directory): 
        # Opens a image in RGB mode
        im = Image.open(path + "/fossils/" + directory + "/" + file)
    
        im = im.resize((180, 180))
        
        im.save(path + "/fossils/" + directory + "/" + file)