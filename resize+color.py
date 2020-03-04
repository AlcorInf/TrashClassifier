from PIL import Image
import os

path = ('C:/Users/Kishan/Desktop/Python/pics/')
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((512,384), Image.ANTIALIAS)
	    imResize = im.convert('1')
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
resize()