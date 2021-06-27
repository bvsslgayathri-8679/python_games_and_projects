import PIL 

from PIL import Image

w=300
h=200

img=Image.open('Capture.png')
img1=img.resize((w,h),PIL.Image.ANTIALIAS)
img1.save('resize.png')