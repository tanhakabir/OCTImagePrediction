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

RAND_WALK_X = 250
RAND_WALK_Y = 240
RAND_WALK_R = 10

def produceRandomWalkerSegmentation(filename):
	image = utils.readImageGrayscaled(filename)
	utils.saveImage(filename, 'original_gs', image)
	og = utils.readImageGrayscaled(filename)

	processed = processing.produceContrast3Tone(image)
	utils.saveImage(filename, 'contrast_3_tone_processed', processed)

	image_labels = np.zeros(processed.shape, dtype=np.uint8)
	indices_mid = draw.circle_perimeter(RAND_WALK_Y, RAND_WALK_X, RAND_WALK_R) #from here
	image_labels[indices_mid] = 1
	image_labels[90,:] = 2
	image_labels[300,:] = 2

	image_segmented = seg.random_walker(processed, image_labels)
	utils.saveImage(filename, 'rand_walk_band_' + str(RAND_WALK_X) + '_' + str(RAND_WALK_Y) + '_' + str(RAND_WALK_R), image_segmented);

	merged = og + image_segmented

	utils.saveImage(filename, 'merge_rand_walk_band_' + str(RAND_WALK_X) + '_' + str(RAND_WALK_Y) + '_' + str(RAND_WALK_R), merged);

	print('saved ' + filename + '_rand_walk_band_' + str(RAND_WALK_X) + '_' + str(RAND_WALK_Y) + '_' + str(RAND_WALK_R))


produceRandomWalkerSegmentation('sample')
produceRandomWalkerSegmentation('sample2')
produceRandomWalkerSegmentation('sample3')
produceRandomWalkerSegmentation('sample4')

