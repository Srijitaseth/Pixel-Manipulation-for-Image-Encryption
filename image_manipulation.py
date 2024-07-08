from PIL import Image
import numpy as np

def load_image(image_path):
    """
    Load an image from a file path.
    """
    return Image.open(image_path)

def save_image(image, save_path):
    """
    Save an image to a file path.
    """
    image.save(save_path)

def image_to_array(image):
    """
    Convert a PIL image to a numpy array.
    """
    return np.array(image)

def array_to_image(array):
    """
    Convert a numpy array to a PIL image.
    """
    return Image.fromarray(array)
