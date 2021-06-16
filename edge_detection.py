import numpy as np
import matplotlib.pyplot as plt
import cv2

#clearing data
plt.clf()

"""
Change directory to the photo to be opened
"""
image = cv2.imread('C:/Users/Realli/Desktop/Thesis/Python_image_processing/0x0x520x384.jpg')

# convert to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show the grayscale image
plt.figure(0)
plt.imshow(grayscale, cmap="gray")
plt.show()

# perform the canny edge detector to detect image edges
edges = cv2.Canny(grayscale, threshold1=30, threshold2=100)

plt.figure(1)
plt.imshow(edges, cmap="gray")
plt.show()
