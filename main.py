from PIL import Image
# import required module
#pip install pillow

import os
# assign directory
directory = '..\..\Create Dataset\Google-Image-Downloader-Python\download'
 
count = 1 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        image = Image.open(f)
        rgb_im = image.convert('RGB')
        #yoloicin 640-640
        new_image = rgb_im.resize((640, 640))
        new_image.save(f'DataFormatted/{count}.jpg')
        count += 1 

