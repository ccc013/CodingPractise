# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:37:17 2015

@author: cai
"""

import os
from PIL import Image

image = Image.open('corn.jpg')
out = image.transpose(Image.FLIP_LEFT_RIGHT)

out.save("corn_left_to_right.jpg")

print 'done!'