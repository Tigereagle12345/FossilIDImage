from PIL import Image, ImageFilter
import pandas as pd

def find_object(file):
    image = Image.open(file)
    image = image.convert("L")
    image = image.filter(ImageFilter.FIND_EDGES)
    image.save("Edge-" + file)
    measure_object("Edge-" + file)

def find_edges(file):
    edges = []
    im = Image.open(file)
    xsize, ysize = im.size
    pixels = list(im.getdata())
    print(pixels)
    
    return edges

def measure_object(file):
    edges = find_edges(file)

find_object("fossilpic3.png")
