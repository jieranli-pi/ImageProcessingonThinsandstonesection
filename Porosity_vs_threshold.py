from PIL import Image
import numpy as np
import os
from matplotlib import pyplot as plt

input_directory='D:/Thesis_DATA/Toshowreport/'
mypath = os.listdir(input_directory)
list_len=len(mypath)

image = np.array(Image.open(input_directory+mypath[0]))
a,b,c=np.shape(image)
image=image.reshape(int(np.size(image)/np.size(image, 2)),int(np.size(image, 2)))

# matplotlib histogram
plt.figure(0)
plt.hist(image[:,0], color = 'blue', edgecolor = 'black',
         bins = int(255))
# Add labels
plt.title('Greyscale distribution')
plt.xlabel('Shade of grey')
plt.ylabel('Amount of pixels')

#Porosity vs threshold
Distribution=np.histogram(image, bins=255)
Distribution=np.hstack([np.zeros(1),Distribution[0]])
porosity_list=1-np.cumsum(Distribution/np.size(image))
index=np.arange(256)
plt.figure(1)
plt.plot(index,porosity_list)
# Add labels
plt.title('Porosity versus threshold')
plt.xlabel('Threshold')
plt.ylabel('Pororsity')