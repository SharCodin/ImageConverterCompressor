import os
import sys
from tkinter import filedialog

import PIL
from PIL import Image

# Getting the directory of images.
imagesDir = filedialog.askdirectory()

# if no directory selected, user cancel or quit the dialog box.
if not imagesDir:
    sys.exit("No directory selected.")

# list all files in directory and apped to a list
listOfFiles = []
filetypes = ['.jpg', '.jpeg', '.png', '.gif']
for name in os.listdir(imagesDir):
    filePath = os.path.join(imagesDir, name)
    if os.path.isfile(filePath):
        for file in filetypes:
            if file in name:
                listOfFiles.append(name)

# check if image files exist
if not listOfFiles:
    sys.exit("No images found in directory")


# Path to save images
destinationFolder = os.path.join(imagesDir, "Compressed")
if not os.path.exists(destinationFolder):
    os.mkdir(destinationFolder)

# loop through images and convert or compress file.
for imgFile in listOfFiles:
    imgFullPath = os.path.join(imagesDir, imgFile)
    im = Image.open(imgFullPath)
    imageWidth, imageHeight = im.size
    img = im.resize((imageWidth, imageHeight), PIL.Image.ANTIALIAS)
    destinationFileName = os.path.join(destinationFolder, imgFile)
    img.save(destinationFileName)

# completed
print('=======================================')
print('==============COMPLETED================')
print('=======================================')
