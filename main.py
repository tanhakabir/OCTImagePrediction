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

def produceRandomWalkerSegmentation(filename, x, y, r):
	image = utils.readImageGrayscaled(filename)
	utils.saveImage(filename, 'original_gs', image)

	processed = processing.produceContrast3Tone(image)
	utils.saveImage(filename, 'contrast_3_tone_processed', processed)

	image_labels = np.zeros(processed.shape, dtype=np.uint8)
	indices_mid = draw.circle_perimeter(y, x, r)#from here
	image_labels[indices_mid] = 1
	image_labels[90,:] = 2
	image_labels[300,:] = 2

	image_segmented = seg.random_walker(processed, image_labels)
	utils.saveImage(filename, 'rand_walk_band_' + str(x) + '_' + str(y) + '_' + str(r), image_segmented);

	print('saved ' + filename + '_rand_walk_band_' + str(x) + '_' + str(y) + '_' + str(r))


image = utils.readImageGrayscaled('sample')
produceRandomWalkerSegmentation('sample', 250, 230, 20)

image = utils.readImageGrayscaled('sample2')
produceRandomWalkerSegmentation('sample2', 250, 230, 20)

image = utils.readImageGrayscaled('sample3')
produceRandomWalkerSegmentation('sample3', 250, 230, 20)

image = utils.readImageGrayscaled('sample4')
produceRandomWalkerSegmentation('sample4', 250, 220, 20)

