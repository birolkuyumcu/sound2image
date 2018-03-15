# -*- coding: utf-8 -*-
"""
Birol Kuyumcu 

playing sound with generated poicare plot like images

"""
import numpy as np
import librosa
import cv2
import pyaudio
import wave
from gen_image import gen_rgb


filename = u"Çetin_Akdeniz _Şeyh_Şamil.wav"

p = pyaudio.PyAudio()
wf = wave.open(filename, 'rb')
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
				

samples,sample_rate = librosa.load(filename)

duration = samples.shape[0] / sample_rate
fps = 25
width = samples.shape[0] / (fps*duration)

for ix,i in enumerate(range(0,samples.shape[0],width)):
	img = gen_rgb(samples[i:i+width])
	data = wf.readframes(2*width)
	cv2.imshow('sound2Image',img)
	stream.write(data)
	key = cv2.waitKey(1) 
	if key == 27:
		break
cv2.destroyAllWindows()   
stream.stop_stream()
stream.close()
p.terminate()