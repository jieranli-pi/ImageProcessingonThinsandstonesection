import pandas as pd 
import numpy as np
from collections import Counter

data = pd.read_csv("D:/Thesis_DATA/Toshowreport/Overview/4_p/Results_crop.csv")
#data = pd.read_csv("D:/Thesis_DATA/1_report/Results_Pores.csv")

#Area in nm^2
Area = data[['Area']].to_numpy()[:,0]
Radius = np.sqrt(Area/np.pi)
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

#Area statistics
size_0_2=np.where(np.logical_and(Area>=0, Area<2**2*np.pi))
size_2_5=np.where(np.logical_and(Area>=2**2*np.pi, Area<5**2*np.pi))
size_5_15=np.where(np.logical_and(Area>=5**2*np.pi, Area<15**2*np.pi))
size_15=np.where(Area>=15**2*np.pi)

Round_0_2 = np.concatenate([Round_Shape[0], size_0_2[0]])
Round_2_5 = np.concatenate([Round_Shape[0], size_2_5[0]])
Round_5_15 = np.concatenate([Round_Shape[0], size_5_15[0]])
Round_15 = np.concatenate([Round_Shape[0], size_15[0]])
Intermediate_0_2= np.concatenate([Intermediate_Shape[0], size_0_2[0]])
Intermediate_2_5= np.concatenate([Intermediate_Shape[0], size_2_5[0]])
Intermediate_5_15= np.concatenate([Intermediate_Shape[0], size_5_15[0]])
Intermediate_15=np.concatenate([Intermediate_Shape[0], size_15[0]])
Enlongate_0_2=np.concatenate([Enlongate_shape[0], size_0_2[0]])
Enlongate_2_5=np.concatenate([Enlongate_shape[0], size_2_5[0]])
Enlongate_5_15=np.concatenate([Enlongate_shape[0], size_5_15[0]])
Enlongate_15=np.concatenate([Enlongate_shape[0], size_15[0]])

Round_0_2=[item for item, count in Counter(Round_0_2).items() if count > 1]
Round_2_5=[item for item, count in Counter(Round_2_5).items() if count > 1]
Round_5_15=[item for item, count in Counter(Round_5_15).items() if count > 1]
Round_15=[item for item, count in Counter(Round_15).items() if count > 1]
Intermediate_0_2=[item for item, count in Counter(Intermediate_0_2).items() if count > 1]
Intermediate_2_5=[item for item, count in Counter(Intermediate_2_5).items() if count > 1]
Intermediate_5_15=[item for item, count in Counter(Intermediate_5_15).items() if count > 1]
Intermediate_15=[item for item, count in Counter(Intermediate_15).items() if count > 1]
Enlongate_0_2=[item for item, count in Counter(Enlongate_0_2).items() if count > 1]
Enlongate_2_5=[item for item, count in Counter(Enlongate_2_5).items() if count > 1]
Enlongate_5_15=[item for item, count in Counter(Enlongate_5_15).items() if count > 1]
Enlongate_15=[item for item, count in Counter(Enlongate_15).items() if count > 1]

AreaRound_0_2 = np.sum(Area[Round_0_2])
AreaRound_2_5 = np.sum(Area[Round_2_5])
AreaRound_5_15 = np.sum(Area[Round_5_15])
AreaRound_15 = np.sum(Area[Round_15])
AreaIntermediate_0_2 = np.sum(Area[Intermediate_0_2])
AreaIntermediate_2_5 = np.sum(Area[Intermediate_2_5])
AreaIntermediate_5_15 = np.sum(Area[Intermediate_5_15])
AreaIntermediate_15 = np.sum(Area[Intermediate_15])
AreaEnlongate_0_2 = np.sum(Area[Enlongate_0_2])
AreaEnlongate_2_5 = np.sum(Area[Enlongate_2_5])
AreaEnlongate_5_15 = np.sum(Area[Enlongate_5_15])
AreaEnlongate_15 = np.sum(Area[Enlongate_15])

