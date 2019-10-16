import skimage
import os

from skimage import io

import skimage.data as data
import skimage.segmentation as seg
from skimage import filters
from skimage import draw
from skimage import color
from skimage import exposure
from skimage.feature import canny

from skimage.color import rgb2gray
import numpy as np
import utils
import matplotlib.pyplot as plt
from scipy import ndimage

file_ext = '.tif'
output_file_ext = '.png'

def produceContrasted1(filename):
	image = plt.imread(filename + file_ext)
	image.shape

	gray = rgb2gray(image)
	gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
	for i in range(gray_r.shape[0]):
		if gray_r[i] > gray_r.mean():
			gray_r[i] = 1
		else:
			gray_r[i] = 0
	gray = gray_r.reshape(gray.shape[0],gray.shape[1])
	plt.imshow(gray, cmap='gray')

	io.imsave(filename + '_output1' + output_file_ext, gray)

	return gray


def produceContrasted2(filename):
	image = plt.imread(filename + file_ext)
	image.shape

	gray = rgb2gray(image)
	gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
	for i in range(gray_r.shape[0]):
		if gray_r[i] > gray_r.mean():
			gray_r[i] = 3
		elif gray_r[i] > 0.5:
			gray_r[i] = 2
		elif gray_r[i] > 0.25:
			gray_r[i] = 1
		else:
			gray_r[i] = 0
	gray = gray_r.reshape(gray.shape[0],gray.shape[1])

	io.imsave(filename + '_output2' + output_file_ext, gray)

	return gray

def circle_points(resolution, center, radius):
    """
    Generate points which define a circle on an image.Centre refers to the centre of the circle
    """   
    radians = np.linspace(0, 2*np.pi, resolution)
    c = center[1] + radius*np.cos(radians)#polar co-ordinates
    r = center[0] + radius*np.sin(radians)
    
    return np.array([c, r]).T


def produceRandomWalkerSegmentation(filename, x, y, radius, contrastFn):
	# Exclude last point because a closed path should not have duplicate points
	points = circle_points(200, [y, x], radius)[:-1]

	gray = contrastFn(filename)

	image_labels = np.zeros(gray.shape, dtype=np.uint8)
	indices = draw.circle_perimeter(y, x, 20)#from here
	image_labels[indices] = 1
	image_labels[points[:, 1].astype(np.int), points[:, 0].astype(np.int)] = 2

	image_segmented = seg.random_walker(gray, image_labels)

	io.imsave(filename + '_rand_walk_' + str(x) + '_' + str(y) + '_' + str(radius) + output_file_ext, image_segmented)


produceRandomWalkerSegmentation('sample', 240, 200, 250, produceContrasted2)
produceRandomWalkerSegmentation('sample2', 240, 200, 250, produceContrasted2)
produceRandomWalkerSegmentation('sample3', 240, 200, 250, produceContrasted2)

