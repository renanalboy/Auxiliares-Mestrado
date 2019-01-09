# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:49:50 2018

@author: Renan Alboy
"""

import os
import PIL
from PIL import Image

basewidth = 256
hsize = 256
#caminho_entrada = "C:/Users/Win7/Desktop/Imagens_dataset/"
arq = 'resize2.py'

for name in os.listdir('.'):
	if name != arq:
		img = Image.open(name)
		img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
		img.save(name)