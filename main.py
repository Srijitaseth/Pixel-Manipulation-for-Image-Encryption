from encryption_decryption import encrypt_image_math, decrypt_image_math, encrypt_image_swap, decrypt_image_swap
from image_manipulation import load_image, save_image, image_to_array, array_to_image

def main():
    
    image_path = 'samples/sample_image.png'  
    image = load_image(image_path)

   
    image_array = image_to_array(image)

    
    key = 50
    encrypted_array = encrypt_image_math(image_array, key)

    
    encrypted_image = array_to_image(encrypted_array)
    save_image(encrypted_image, 'encrypted_image_math.png')

    
    decrypted_array = decrypt_image_math(encrypted_array, key)
    decrypted_image = array_to_image(decrypted_array)
    save_image(decrypted_image, 'decrypted_image_math.png')


    encrypted_array_swap = encrypt_image_swap(image_array)
    encrypted_image_swap = array_to_image(encrypted_array_swap)
    save_image(encrypted_image_swap, 'encrypted_image_swap.png')

    decrypted_array_swap = decrypt_image_swap(encrypted_array_swap)
    decrypted_image_swap = array_to_image(decrypted_array_swap)
    save_image(decrypted_image_swap, 'decrypted_image_swap.png')

if __name__ == "__main__":
    main()
