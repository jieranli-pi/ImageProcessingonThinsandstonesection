import cv2
import numpy as np
import os

"""
Change directory to the photo to be opened
"""
input_directory='D:/Thesis_DATA/4-ppol/Test/output_thresholding/image/'

mypath = os.listdir(input_directory)
list_len=len(mypath)
porosity_list=np.zeros(list_len)

for i in range(0,list_len):
    img = cv2.imread(input_directory+mypath[i], cv2.IMREAD_GRAYSCALE)
    n_white_pix = np.sum(img == 255)
    porosity_list[i]=n_white_pix/np.size(img)