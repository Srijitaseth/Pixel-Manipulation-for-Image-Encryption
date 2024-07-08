import unittest
from src.webapp import app

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Image Encryption/Decryption', response.data)
    
    def test_upload_image(self):
        with open('tests/test_image.png', 'rb') as f:
            response = self.app.post('/upload', data={
                'file': (f, 'test_image.png'),
                'method': 'math',
                'key': 50,
                'operation': 'encrypt'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'encrypted_image_math.png', response.data)

if __name__ == "__main__":
    unittest.main()
