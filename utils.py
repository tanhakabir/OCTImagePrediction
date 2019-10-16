import os
import matplotlib.pyplot as plt
import skimage
from skimage.color import rgb2gray
from skimage import io
import numpy as np

file_ext = '.tif'
output_file_ext = '.png'

def readImageGrayscaled(filename):
        image = plt.imread(filename + file_ext)
        image.shape
        gray = rgb2gray(image)
        return gray

def saveImage(filename, image):
        io.imsave(filename + output_file_ext, image)


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