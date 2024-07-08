from PIL import Image
import numpy as np

def generate_test_image():
    # Create a simple 2x2 image with black and white pixels
    image_array = np.array([[[0, 0, 0], [255, 255, 255]],
                            [[255, 255, 255], [0, 0, 0]]], dtype=np.uint8)

    # Create an Image object from the array
    image = Image.fromarray(image_array)

    # Save the image to the tests directory
    test_image_path = 'tests/test_image.png'
    image.save(test_image_path)
    print(f"Test image generated and saved to '{test_image_path}'")

# Generate the test image
generate_test_image()
