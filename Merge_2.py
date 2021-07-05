from PIL import Image
import os
Image.MAX_IMAGE_PIXELS = None
#Read the two images
image1 = Image.open('D:/Thesis_DATA/3/out/Part1.png')
image2 = Image.open('D:/Thesis_DATA/3/out/Part2.png')
#resize, first image
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(image1_size[0]+image2_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))

os.chdir('D:/Thesis_DATA/3/out/')
new_image.save("Huge_Obern_right.png")