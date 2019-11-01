import os
import matplotlib.pyplot as plt
import skimage
from skimage.color import rgb2gray
from skimage import io
import numpy as np

file_ext = '.tif'
output_file_ext = '.png'

def readImageGrayscaled(filename):
        path = os.path.join('raw_images', filename + file_ext)
        image = plt.imread(path)
        gray = rgb2gray(image)
        return gray

def saveImageSegment(sampleName, filename, image):
        dir_seg = os.path.join('segmented')
        if not os.path.exists(dir_seg):
                os.mkdir(dir_seg)

        dir_sample = os.path.join('segmented', sampleName)
        if not os.path.exists(dir_sample):
                os.mkdir(dir_sample)

        path = os.path.join('segmented', sampleName, filename + output_file_ext);
        io.imsave(path, image)

def saveImageSegmentResult(sampleName, strategyName, image):
        dir_seg_re = os.path.join('segmentation_results')
        if not os.path.exists(dir_seg_re):
                os.mkdir(dir_seg_re)

        dir_strat = os.path.join('segmentation_results', strategyName)
        if not os.path.exists(dir_strat):
                os.mkdir(dir_strat)

        path = os.path.join('segmentation_results', strategyName, sampleName + output_file_ext);
        io.imsave(path, image)


def savefig(fname, verbose=True):
    path = os.path.join('..', 'figs', fname)
    plt.savefig(path)
    if verbose:
        print("Figure saved as '{}'".format(path))


def circle_points(resolution, center, radius):
    """
    Generate points which define a circle on an image.Centre refers to the centre of the circle
    """   
    radians = np.linspace(0, 2*np.pi, resolution)
    c = center[1] + radius*np.cos(radians)#polar co-ordinates
    r = center[0] + radius*np.sin(radians)
    
    return np.array([c, r]).T