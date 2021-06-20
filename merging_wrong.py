import numpy as np
import os
import time
import pandas as pd
# starting time
start = time.time()

"""
Change directory to the photo to be opened
"""
input_directory_image='D:/Thesis_DATA/4/Test/output_combine/train_data/images/'
#input_directory_array='D:/Thesis_DATA/4/Test/output_combine/train_data/Arrays/'
input_directory_array='D:/Thesis_DATA/4/Test/output_combine/train_data/generated_array/'
output_directory_image='D:/Thesis_DATA/4/Test/output_combine/Combined/'
output_directory_array='D:/Thesis_DATA/4/Test/output_combine/Combined/'

mypath_image = os.listdir(input_directory_image)
mypath_array = os.listdir(input_directory_array)

##sorting mypath_image
list1 = [None] * len(mypath_image)
list2 = [None] * len(mypath_image)
for i in range(0,len(mypath_image)):
    list1[i] = int(mypath_image[i].partition('x')[0])
    list2[i] = int(mypath_image[i].partition('x')[2].partition('x')[0])

z=list(zip(mypath_image,list1,list2))

df = pd.DataFrame(z, columns=['File_name', 'x_pixel', 'y_pixel'])
df=df.sort_values(["x_pixel", "y_pixel"], ascending = (True, True))
df = df.reset_index(drop=True)
mypath_image=df["File_name"].values.tolist()

##sorting mypath_array
for i in range(len(mypath_image)):
    mypath_array[i] = mypath_image[i].replace(".png", ".npy")

##Calculating the number of tile rows&columns
partitioned_list = mypath_image
for i in range(0,len(mypath_image)):
    partitioned_list[i] = mypath_image[i].partition('x')
first_column = [i for i in partitioned_list if '0' in i]
num_row=len(first_column)
num_col=int(len(mypath_image)/num_row)

##size of combined array, creating empty array for inserting tile
first_tile=np.load(input_directory_array+mypath_array[0])
a=np.size(first_tile, 0)
b=np.size(first_tile, 1)
c=np.size(first_tile, 2)
Combined_image=np.zeros((a*num_row,b*num_col,c),dtype=np.uint8)

##insertion
ct=0
for i in range(0,num_row):
    for j in range(0,num_col):
        Combined_image[i*a:(i+1)*a,j*b:(j+1)*b,:]=np.load(input_directory_array+mypath_array[ct]).astype(np.uint8)
        ct+=1

Combined_image=Combined_image.astype(np.uint8)

import matplotlib.pyplot as plt  
plt.imshow(Combined_image, cmap='gray')
# end time
end = time.time()
# total time taken
print(f"Runtime of the program is {end - start}")