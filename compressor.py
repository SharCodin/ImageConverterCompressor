import os
import sys
from tkinter import filedialog


import PIL
from PIL import Image


# Getting the directory of images.
imagesDir = filedialog.askdirectory()


def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


# if no directory selected, user cancel or quit the dialog box.
if not imagesDir:
    sys.exit("No directory selected.")

InitialSize = get_size(imagesDir)

# list all files in directory and apped to a list
listOfFiles = []
filetypes = ['.jpg', '.jpeg', '.png', '.gif']
print('Getting image files...')
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
print('Creating Directory...')
destinationFolder = os.path.join(imagesDir, "Compressed")
if not os.path.exists(destinationFolder):
    os.mkdir(destinationFolder)


# loop through images and convert or compress file.
print('Compressing images...')
totalFiles = 0
for imgFile in listOfFiles:
    imgFullPath = os.path.join(imagesDir, imgFile)
    im = Image.open(imgFullPath)
    imageWidth, imageHeight = im.size
    img = im.resize((imageWidth, imageHeight), PIL.Image.ANTIALIAS)
    destinationFileName = os.path.join(destinationFolder, imgFile)
    img.save(destinationFileName)
    totalFiles += 1

FinalSize = get_size(destinationFolder)

# completed
print('==============COMPLETED================')
print()
print('================STATS==================')
print(f'Total Files Processed: {totalFiles} files.')
print(f'File Size before compression: {InitialSize} bytes.')
print(f'File Size After compression: {FinalSize} bytes.')
print('=======================================')
input('Press ENTER to exit')
