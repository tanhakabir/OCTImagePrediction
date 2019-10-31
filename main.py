import skimage
import os
import utils
import processing
import time

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
import matplotlib.pyplot as plt
from scipy import ndimage

def produceContrasted1(filename):
	gray = utils.readImageGrayscaled(filename)
	processed = processing.produceContrast2Tone(gray)
	utils.saveImage(filename + '_output1', processed)
	return processed


def produceContrasted2(filename):
	gray = utils.readImageGrayscaled(filename)
	processed = processing.produceContrast3Tone(gray)
	utils.saveImage(filename + '_output2', processed)
	return processed

def produceRandomWalkerSegmentation(filename, x, y, contrastFn):
	gray = contrastFn(filename)

	image_labels = np.zeros(gray.shape, dtype=np.uint8)
	indices = draw.circle_perimeter(y, x, 5)#from here
	image_labels[indices] = 1
	image_labels[90,:] = 2
	image_labels[300,:] = 2

	image_segmented = seg.random_walker(gray, image_labels)

	utils.saveImage(filename + '_rand_walk_band_' + str(x) + '_' + str(y), image_segmented)




image = utils.readImageGrayscaled('sample')
produceRandomWalkerSegmentation('sample', 250, 250, produceContrasted2)

image = utils.readImageGrayscaled('sample2')
produceRandomWalkerSegmentation('sample2', 250, 250, produceContrasted2)

image = utils.readImageGrayscaled('sample3')
produceRandomWalkerSegmentation('sample3', 250, 250, produceContrasted2)

image = utils.readImageGrayscaled('sample4')
produceRandomWalkerSegmentation('sample4', 250, 250, produceContrasted2)

