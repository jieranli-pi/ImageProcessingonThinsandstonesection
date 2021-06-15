import pandas as pd
import os
import time
# starting time
start = time.time()
"""
Change directory to the photo to be opened
"""
input_directory_image='D:/Thesis_DATA/4/Test/output_combine/train_data/images/'
input_directory_array='D:/Thesis_DATA/4/Test/output_combine/train_data/Arrays/'
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