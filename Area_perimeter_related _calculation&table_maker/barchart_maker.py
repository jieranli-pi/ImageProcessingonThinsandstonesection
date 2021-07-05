import matplotlib.pyplot as plt
 
#Burgpreppach
name_list = ['0-2','2-5','5-15','>15']

Abs_ful_ppol=[0.009006280598209,
0.001729999890251,
0.019696756412418,
0.091566963099122
]

Abs_crop_ppol=[0.007220498684936,
0.016134365427335,
0.023213616879917,
0.084839674853308
]

Fitzner=[0.0574,
0.0109,
0.0682,
0.0339,
]


Abs_full_xpol=[
0.000678473498124,
0.001507920196747,
0.002858083239984,
0.525955523065145
]

Abs_crop_xpol=[0.000755171810096,
0.001679047277313,
0.003388995847817,
0.473176785064775
]


x =list(range(len(name_list)))
total_width, n = 0.8, 2
width = total_width / 2

plt.figure(0)
plt.bar(name_list, Abs_ful_ppol, width=width, label='Full_ppol',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Abs_crop_ppol, width=width, label='Crop_ppol',tick_label = name_list,fc = 'r')
plt.legend()
plt.title('Relative pore size distribution ppol')
plt.xlabel('Pore size (micrometer)')
plt.ylabel('Porosity')

plt.figure(1)
plt.bar(x, Abs_full_xpol, width=width, label='Full_xpol',tick_label = name_list,fc = 'g')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Abs_crop_xpol, width=width, label='Crop_xpol',tick_label = name_list,fc = 'b')
plt.legend()
plt.title('Relative pore size distribution xpol')
plt.xlabel('Pore size (micrometer)')
plt.ylabel('Porosity')

x =list(range(len(name_list)))
#comparefitzner
total_width, n = 0.8, 3
width = total_width / 2
plt.figure(2)
plt.bar(x, Abs_crop_ppol, width=width, label='crop_ppol',tick_label = name_list,fc = 'g')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Fitzner, width=width, label='Porosimetry method',tick_label = name_list,fc = 'r')
plt.legend()
plt.title('Absolute pore size distribution of cropped ppol and Porosimetry')
plt.xlabel('Pore size (micrometer)')
plt.ylabel('Porosity')



#Bentheimer
Abs_crop_xpol=[0.005051418213599,
0.011848058433195,
0.025479663083816,
0.075620860269391,
]

plt.figure(2)
plt.bar(name_list, Abs_crop_xpol, width=width, label='Full_xpol',fc = 'r')
plt.legend()
plt.title('Relative pore size distribution xpol')
plt.xlabel('Pore size (micrometer)')
plt.ylabel('Porosity')

#Obbernkirchen
Abs_crop_xpol=[0.001703029031413,
0.108384994332516,
0.065510998724057,
0.044400977912014
]


Fitzner=[0.0479,
0.0667,
0.0667,
0.005
]

plt.figure(3)
plt.bar(name_list, Abs_crop_xpol, width=width, label='Full_xpol',fc = 'r')
plt.legend()
plt.title('Relative pore size distribution xpol')
plt.xlabel('Pore size (micrometer)')
plt.ylabel('Porosity')

x =list(range(len(name_list)))
#comparefitzner
total_width, n = 0.8, 3
width = total_width / 2
plt.figure(2)
plt.bar(x, Abs_crop_xpol, width=width, label='Obern_crop_xpol',tick_label = name_list,fc = 'g')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Fitzner, width=width, label='Porosimetry method',tick_label = name_list,fc = 'r')
plt.legend()
plt.title('Absolute pore size distribution of Obern cropped xpol and Porosimetry')
plt.xlabel('Pore size (micrometer)')
plt.ylabel('Porosity')


Abs_crop_Burg=[0.007220498684936,
0.016134365427335,
0.023213616879917,
0.084839674853308
]
Abs_crop_Bent=[0.005051418213599,
0.011848058433195,
0.025479663083816,
0.075620860269391,
]
Abs_crop_Obern=[0.001703029031413,
0.108384994332516,
0.065510998724057,
0.044400977912014
]
x =list(range(len(name_list)))
#comparefitzner
total_width, n = 0.8, 3
width = total_width / 3
plt.figure(2)
plt.bar(name_list, Abs_crop_Burg, width=width, label='Burgpreppach_ppol',fc = 'r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Abs_crop_Bent, width=width, label='Bent_xpol',tick_label = name_list,fc = 'g')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Abs_crop_Obern, width=width, label='Obern_xpol',tick_label = name_list,fc = 'b')
plt.legend()
plt.title('Absolute pore size distribution of Burgpreppach, Bentiheim and Obernkircken')
plt.xlabel('Pore size (micrometer)')
plt.ylabel('Porosity')
