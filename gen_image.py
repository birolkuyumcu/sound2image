# -*- coding: utf-8 -*-
"""
Birol Kuyumcu 

poicare plot like sound 2 image utilty

"""
import numpy as np
import cv2

def gen_lines(samples):
    L = samples.shape[0]
    vmin = np.float32(samples.min())
    vmax = np.float32(samples.max())
    mat = np.zeros((512,512))
    if vmin != vmax :
        dt = 511.0*(1.0*samples - vmin)/(vmax-vmin)
        pts = [(int(dt[i]),int(dt[i+1])) for i in range(L-1) ]
        for i in range(len(pts)-1):
            cv2.line(mat,pts[i],pts[i+1],255,1)
    else:
        print("Error",vmax,vmin,samples.sum())

    return mat 

def gen_rgb(samples):
    rgb = np.zeros((512,512,3))
    sub = int(samples.shape[0]/2.0)
    sub2 = int(sub/2.0)
    ch = []
    ch.append(samples[:sub])
    ch.append(samples[sub2:sub2+sub])
    ch.append(samples[sub:])
    for i in range(3):
        rgb[:,:,i] = gen_lines(ch[i])
    return rgb 
