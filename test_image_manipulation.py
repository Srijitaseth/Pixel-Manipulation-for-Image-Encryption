import unittest
from PIL import Image
from image_manipulation import load_image, save_image, image_to_array, array_to_image
import numpy as np

class TestImageManipulation(unittest.TestCase):
    
    def test_image_to_array(self):
        image_path = 'samples/sample_image.png'  
        image = load_image(image_path)
        image_array = image_to_array(image)
        self.assertIsInstance(image_array, np.ndarray)
    
    def test_array_to_image(self):
        array = np.zeros((10, 10, 3), dtype=np.uint8)
        image = array_to_image(array)
        self.assertIsInstance(image, Image.Image)

if __name__ == "__main__":
    unittest.main()
