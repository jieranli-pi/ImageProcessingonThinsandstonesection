import pandas as pd
import os

"""
Change directory to the photo to be opened
"""
input_directory='D:/Thesis_DATA/Fitzner/'
mypath = os.listdir(input_directory)

FitznerFData = pd.read_csv (input_directory+mypath[1])

Overall_porosity=pd.read_csv (input_directory+mypath[2])

Distribution=pd.read_csv (input_directory+mypath[0])

CumDistribution=Distribution.cumsum()

Overall_porosity.plot.bar()

Distribution.plot.bar()

CumDistribution.plot()