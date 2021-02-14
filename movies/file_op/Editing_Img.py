#1st from pillow library import img module
from PIL import Image,ImageEnhance
import os
#img1.save('puupy2.png')
#img1.save('puupy2.pdf')
#Here if just u want toshowurfile not to save then#img1.show()
#HOW TO RESIZE THE FILE
# max_size=(250,250)#Entry in tuple
# img1.thumbnail(max_size)
# img1.save('dog1small.jpg')
#when we want to sort many images through loop___________
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1=Image.open(item)
#         filename,extension=os.path.splitext(item)
#         img1.save(f'{filename}.png')
#--------------------------------
#Sharpness
img1=Image.open("puupy2.png")
enhancer=ImageEnhance.Sharpness(img1)
enhancer.enhance(5).save("dogeditted.jpg")









