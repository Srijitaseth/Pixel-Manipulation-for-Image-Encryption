from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from encryption_decryption import encrypt_image_math, decrypt_image_math, encrypt_image_swap, decrypt_image_swap
import os
import numpy as np
from PIL import Image

app = Flask(__name__, template_folder='../templates')


UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    print("Upload endpoint reached")  
    if 'file' not in request.files:
        return "No file part", 400  
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400  
    
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(f"File saved to: {file_path}")  
        

        method = request.form.get('method')
        key = int(request.form.get('key', 0))  
        operation = request.form.get('operation')
        
        if not method or not operation:
            return "Method or operation not specified", 400  #

       
        image_array = np.array(Image.open(file_path)).astype(np.uint8)
        print(f"Image array shape: {image_array.shape}") 

        
        try:
            if method == 'math':
                if operation == 'encrypt':
                    encrypted_array = encrypt_image_math(image_array, key)
                    result_image = Image.fromarray(encrypted_array)
                elif operation == 'decrypt':
                    decrypted_array = decrypt_image_math(image_array, key)
                    result_image = Image.fromarray(decrypted_array)
                else:
                    return "Invalid operation for math method", 400  
            elif method == 'swap':
                if operation == 'encrypt':
                    encrypted_array = encrypt_image_swap(image_array, key)
                    result_image = Image.fromarray(encrypted_array)
                elif operation == 'decrypt':
                    decrypted_array = decrypt_image_swap(image_array, key)  
                    result_image = Image.fromarray(decrypted_array)
                else:
                    return "Invalid operation for swap method", 400  
            else:
                return "Invalid method specified", 400  

            
            result_filename = f'{operation}_{method}_{key}_{filename}'
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)
            result_image.save(result_path, format='PNG')  
            print(f"Result image saved to: {result_path}")  

            
            return render_template('results.html', result_filename=result_filename, method=method, operation=operation, key=key)
        except Exception as e:
            print(f"Error occurred: {e}") 
            return "An error occurred", 500  

@app.route('/some_route')
def some_function():
    
    return redirect(url_for('index'))  

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve the uploaded file for download."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(f"Serving file from: {file_path}")  
    if not os.path.exists(file_path):
        return "File not found", 404  
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True, mimetype='image/png')

if __name__ == '__main__':
    
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
