import concurrent.futures as cf
import datetime
import os
from timeit import default_timer as Timer
from tkinter import filedialog

import PIL
from PIL import Image


def resizerCore(image):

    base_im_width = 1600
    base_im_height = 1000
    ratio = 1.00

    im = Image.open(image)
    dirpaths, filename = os.path.split(image)
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

if __name__ == "__main__":
    startTimer = Timer()

    list_of_images = []
    source_path = filedialog.askdirectory()
    for dirpaths, _, filenames in os.walk(source_path):
        print(dirpaths)
        for filename in filenames:
            if '.jpg' in filename.lower() or '.png' in filename.lower():
                list_of_images.append(os.path.join(dirpaths, filename))
            else:
                continue

    with cf.ProcessPoolExecutor() as executor:
        executor.map(resizerCore, list_of_images)


    stopTimer = Timer()
    print(str(datetime.timedelta(seconds=(round(stopTimer - startTimer, 2)))))
    print('-' * 20)
