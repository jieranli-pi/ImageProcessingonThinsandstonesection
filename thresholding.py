# -*- coding: utf-8 -*-
"""
This code import the image

output the image threshold
"""
from PIL import Image
import numpy as np
import os


"""
Change directory to the photo to be opened
"""
input_directory='D:/Thesis_DATA/4/Test/test_data/'
output_directory_image='D:/Thesis_DATA/4/Test/output_thresholding/image/'
output_directory_array='D:/Thesis_DATA/4/Test/output_thresholding/array/'
os.chdir(output_directory_array)

mypath = os.listdir(input_directory)
list_len=len(mypath)
porosity_list=np.zeros(list_len)

for i in range(0,list_len):
    image = np.array(Image.open(input_directory+mypath[i]))
    a,b,c=np.shape(image)
    c=c-1
    image=image.reshape(int(np.size(image)/np.size(image, 2)),int(np.size(image, 2)))
    image = np.delete(image, -1, 1) #last column (row axis=0, column axis=1)
    #to plot the original
    #plt.imshow(image, cmap='gray')
    
    #filtering (oversimplified)
    grain_pixel=0
    matrix_pixel=0
    for ii in range(0,np.size(image,0)-1):
        if np.mean(image[ii])>=225: #200,215,220,222,225
            image[ii]=255
            matrix_pixel+=1
        else:
            image[ii]=0
            grain_pixel+=1
    image = image.reshape(a,b,c)
    np.save(mypath[i].replace(".png", ""), image) 
    image = Image.fromarray(image)        
    image.save(output_directory_image+mypath[i])
    porosity_list[i]=matrix_pixel/(grain_pixel+matrix_pixel)