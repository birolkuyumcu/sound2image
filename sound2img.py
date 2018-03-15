# -*- coding: utf-8 -*-
"""
Birol Kuyumcu 

random selected parts of sound 2 image utilty

"""
import numpy as np
import librosa
import cv2
import random
from gen_image import gen_rgb

filename = u"sesim.wav"

samples,sample_rate = librosa.load(filename)

width = 4096

for i in range(5):
	ix = random.randint(0,samples.shape[0]-width-1)
	print( ix,samples[ix:ix+width])
	img = gen_rgb(samples[ix:ix+width])
	cv2.imshow('Sample',img)
	cv2.imwrite('Sample_%d.png'%ix,img)
	key = cv2.waitKey(0) 
	if key == 27:
		break
cv2.destroyAllWindows()   