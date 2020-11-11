from PIL import Image
import PIL
import os
from tkinter import filedialog
from timeit import default_timer as Timer
import datetime

startTimer = Timer()

base_im_width = 1600
base_im_height = 1000
ratio = 1.00

source_path = filedialog.askdirectory()
for dirpaths, dirnames, filenames in os.walk(source_path):
    print(dirpaths)
    for filename in filenames:
        if '.jpg' in filename.lower() or '.png' in filename.lower():
            im = Image.open(os.path.join(dirpaths, filename))
            im_width, im_height = im.size
            if im_width >= base_im_width and im_height >= im_height:
                if im_width <= im_height:
                    ratio = base_im_width / im_width
                else:
                    ratio = base_im_height / im_height
            else:
                ratio = 1.00
            new_im_width = int(ratio * im_width)
            new_im_height = int(ratio * im_height)
            resized_image = im.resize((new_im_width, new_im_height), PIL.Image.ANTIALIAS)
            resized_image.save(os.path.join(dirpaths, '_' + filename))
            im.close()
            os.remove(os.path.join(dirpaths, filename))

stopTimer = Timer()
print(str(datetime.timedelta(seconds=(round(stopTimer - startTimer, 2)))))
print('-' * 20)
