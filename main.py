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

from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk

from PIL import Image

RAND_WALK_X = 250
RAND_WALK_Y = 240
RAND_WALK_R = 10

def produceRandomWalkerSegmentation(filename):
	image = utils.readImageGrayscaled(filename)
	utils.saveImageSegment(filename, 'original_gs', image)
	og = utils.readImageGrayscaled(filename)

	processed = processing.produceContrast3Tone(image)
	utils.saveImageSegment(filename, 'contrast_3_tone_processed', processed)

	image_labels = np.zeros(processed.shape, dtype=np.uint8)
	indices_mid = draw.circle_perimeter(RAND_WALK_Y, RAND_WALK_X, RAND_WALK_R) #from here
	image_labels[indices_mid] = 1
	image_labels[90,:] = 2
	image_labels[300,:] = 2

	image_segmented = seg.random_walker(processed, image_labels)
	utils.saveImageSegment(filename, 'rand_walk_band_' + str(RAND_WALK_X) + '_' + str(RAND_WALK_Y) + '_' + str(RAND_WALK_R), image_segmented)

	merged = og + image_segmented

	utils.saveImageSegment(filename, 'merge_rand_walk_band_' + str(RAND_WALK_X) + '_' + str(RAND_WALK_Y) + '_' + str(RAND_WALK_R), merged)
	utils.saveImageSegmentResult(filename, 'rand_walk_band_' + str(RAND_WALK_X) + '_' + str(RAND_WALK_Y) + '_' + str(RAND_WALK_R), merged)

	print('saved ' + filename + '_rand_walk_band_' + str(RAND_WALK_X) + '_' + str(RAND_WALK_Y) + '_' + str(RAND_WALK_R))

def produceRandomWalkerSegmentationNoContrast(filename):
	image = utils.readImageGrayscaled(filename)
	utils.saveImageSegment(filename, 'original_gs', image)

	markers = np.zeros(image.shape, dtype=np.uint8)
	markers[image < 0.25] = 2
	markers[image > 0.5] = 1

	image_segmented = seg.random_walker(image, markers)
	utils.saveImageSegment(filename, 'rand_walk_unsupervised', image_segmented)

	merged = image + image_segmented

	utils.saveImageSegment(filename, 'merge_rand_walk_unsupervised', merged)
	utils.saveImageSegmentResult(filename, 'rand_walk_unsupervised', merged)


def produceMorphologicalFiltering(filename):
	image = utils.readImageGrayscaled(filename)
	utils.saveImageSegment(filename, 'original_gs', image)

	selem = disk(6)
	eroded = erosion(image, selem)

	eroded_dilated = dilation(eroded, selem)

	edges = canny(eroded_dilated)

	closed = closing(edges, selem)

	# utils.saveImageSegment(filename, 'morph_filtered', closed)

	merged = image + closed

	utils.saveImageSegment(filename, 'merge_morph_filtered', merged)
	utils.saveImageSegmentResult(filename, 'morph_filtered', merged)

path = os.path.join('raw_images')
files = os.listdir(path)

print(files)

for filename in files:
	if os.path.splitext(filename)[1] != '.tif':
		continue
	produceMorphologicalFiltering(os.path.splitext(filename)[0])


