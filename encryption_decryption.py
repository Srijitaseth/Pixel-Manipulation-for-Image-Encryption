from PIL import Image
import numpy as np

def encrypt_image_math(image_array, key):
    """Encrypts an image using a simple mathematical transformation."""
    
    key = int(key) % 256  
    encrypted_array = image_array.copy()
    encrypted_array[..., :3] = (encrypted_array[..., :3].astype(np.int16) + key) % 256
    return encrypted_array.astype(np.uint8)

def decrypt_image_math(image_array, key):
    """Decrypts an image using a simple mathematical transformation."""
    
    key = int(key) % 256  
    decrypted_array = image_array.copy()
    decrypted_array[..., :3] = (decrypted_array[..., :3].astype(np.int16) - key) % 256
    return decrypted_array.astype(np.uint8)

def encrypt_image_swap(image_array, key):
    """Encrypts an image using a pixel value swap transformation."""
    encrypted_array = image_array.copy()
    encrypted_array[..., 0], encrypted_array[..., 1] = encrypted_array[..., 1], encrypted_array[..., 0]
    return encrypted_array

def decrypt_image_swap(image_array, key):
    """Decrypts an image by reversing the pixel value swap."""
    decrypted_array = image_array.copy()
    decrypted_array[..., 0], decrypted_array[..., 1] = decrypted_array[..., 1], decrypted_array[..., 0]
    return decrypted_array
