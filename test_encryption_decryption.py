import unittest
import numpy as np
from src.encryption_decryption import encrypt_image_swap, decrypt_image_swap, encrypt_image_math, decrypt_image_math

class TestEncryptionDecryption(unittest.TestCase):
    
    def setUp(self):
        self.image_array = np.array([[[0, 0, 0], [255, 255, 255]],
                                    [[255, 255, 255], [0, 0, 0]]], dtype=np.uint8)
        self.key = 50
    
    def test_encrypt_decrypt_swap(self):
        encrypted_array = encrypt_image_swap(self.image_array)
        decrypted_array = decrypt_image_swap(encrypted_array)
        np.testing.assert_array_equal(self.image_array, decrypted_array)

    def test_encrypt_decrypt_math(self):
        encrypted_array = encrypt_image_math(self.image_array, self.key)
        decrypted_array = decrypt_image_math(encrypted_array, self.key)
        np.testing.assert_array_equal(self.image_array, decrypted_array)

if __name__ == "__main__":
    unittest.main()
