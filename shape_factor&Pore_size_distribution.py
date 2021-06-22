import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv("D:/Thesis_DATA/4_report/Overview_Burg_result.csv")

#Area in nm^2
Area = data[['Area']].to_numpy()[:,0]
#Perimeter in nm
Perimeter = data[['Perim.']].to_numpy()[:,0]

#shape factor=A/p^2
Shape_factor=Area/Perimeter**2

#Shape index statistics
#Shape index >=0.04 Round
Round_Shape=np.where(Shape_factor>=0.04)
# 0.015 - 0.04 Intermediate
Intermediate_Shape=np.where(np.logical_and(Shape_factor>=0.015, Shape_factor<0.04))
#<0.015 Enlongate
Enlongate_shape=np.where(np.logical_and(Shape_factor>=0, Shape_factor<0.015))

print('number of Round=',np.size(Round_Shape))
print('number of Intermediate=',np.size(Intermediate_Shape))
print('number of Enlongate=',np.size(Enlongate_shape))

#Distribution of shape indexes
plt.figure(0)
plt.hist(Shape_factor, color = 'blue', edgecolor = 'black',
         bins = int(1000))
# Add labels
plt.title('The frequency of shape index')
plt.xlabel('Shape Index')
plt.ylabel('Frequency')

#Area statistics
#Large size >=156000000000nm^2
Large_size=np.where(Area>=156000000000)
#Medium size >=15600000000nm^2
Medium_size=np.where(np.logical_and(Area>=15600000000, Area<156000000000))
#small size
Small_size=np.where(np.logical_and(Area>=0, Area<15600000000))

print('number of Large=',np.size(Large_size))
print('number of Medium=',np.size(Medium_size))
print('number of Small=',np.size(Small_size))

plt.figure(1)
plt.hist(Area, color = 'blue', edgecolor = 'black',
         bins = int(1000))
# Add labels
plt.title('The frequency of particle area')
plt.xlabel('Particle Area')
plt.ylabel('Frequency')