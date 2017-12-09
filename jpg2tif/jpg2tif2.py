#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import os
from PIL import Image
path='D:/data/www/ocr/img/'
files=os.listdir(path)
for filename in files:
    #print(filename)
    im=Image.open(path+filename)
    im.save(path+'tif/'+ filename.split('.')[0]+'.tif')