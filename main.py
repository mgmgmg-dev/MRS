import cv2 as cv
import numpy as np
import os

# Makes sure that input and output folders exist
try: os.mkdir("input")
except: pass
try: os.mkdir("output")
except: pass

input("Place the images to convert in the \"input\" folder, then press enter.")
columns = int(input("Number of columns: "))
rows = int(input("Number of rows: "))

for file in os.listdir("input"):
    img = cv.imread("input/" + file)
    if img is None:
        print("Something went wrong trying to read \"%s\"" % file)
        continue

    # Assigns utility variables
    height, width, colours = img.shape
    vertical = int(height/rows)
    horizontal = int(width/columns)
    newImage = np.array([[[0] * colours] * width] * height)

    # Fills spaces to the right
    activeWidth = horizontal * columns
    if activeWidth != width:
        newImage[:, activeWidth:] = img[:, activeWidth:]
    
    # Fills spaces at the bottom
    activeHeight = vertical * rows
    if activeHeight != height:
        newImage[activeHeight:, :] = img[activeHeight:, :]

    # Reverses magapoke's shuffle
    for i in range(rows):
        for j in range(columns):
            newImage[i*vertical:(i+1)*vertical, j*horizontal:(j+1)*horizontal] = \
                img[j*vertical:(j+1)*vertical, i*horizontal:(i+1)*horizontal]

    # Writes the processed image to disk
    cv.imwrite("output/output-" + file, newImage)
    print("Processed image \"%s\"" % file)