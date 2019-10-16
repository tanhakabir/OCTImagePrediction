import skimage
import os
import numpy as np
import matplotlib.pyplot as plt
import utils

def produceContrast2Tone(grayImage):
	gray_r = grayImage.reshape(grayImage.shape[0]*grayImage.shape[1])
	for i in range(gray_r.shape[0]):
		if gray_r[i] > gray_r.mean():
			gray_r[i] = 1
		else:
			gray_r[i] = 0
	grayImage = gray_r.reshape(grayImage.shape[0],grayImage.shape[1])
	plt.imshow(grayImage, cmap='gray')

	return grayImage

def produceContrast3Tone(grayImage):
	gray_r = grayImage.reshape(grayImage.shape[0]*grayImage.shape[1])
	for i in range(gray_r.shape[0]):
		if gray_r[i] > gray_r.mean():
			gray_r[i] = 3
		elif gray_r[i] > 0.5:
			gray_r[i] = 2
		elif gray_r[i] > 0.25:
			gray_r[i] = 1
		else:
			gray_r[i] = 0
	grayImage = gray_r.reshape(grayImage.shape[0],grayImage.shape[1])
	plt.imshow(grayImage, cmap='gray')

	return grayImage