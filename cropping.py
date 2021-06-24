# -*- coding: utf-8 -*-
"""
cropping the image to omit the empty part
"""

from PIL import Image
import numpy as np
#im = Image.open(r"D:\Thesis_DATA\4\Huge_Burg_Paint_resized_through_Paint_3D.png")
im = Image.open(r"D:\Thesis_DATA\1\Huge_Bent_Paint_resized_through_Paint_3D.png")

width, height = im.size
 
# Setting the points for cropped image
left = width/12
top = height / 12
right = 11* width/12
bottom = 11 * height / 12
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Shows and saves the image in image viewer
im1.show()
im1.save('Huge_Bent_cropped.jpg')

im1_array=np.array(im1)
porosity=1-(im1_array[np.where(im1_array == 0)].size)/(im1_array.size)