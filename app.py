# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for, flash
# Import other necessary modules
from werkzeug.utils import secure_filename
import os
from cipher import PreHistoricCipher
from stegano import lsb

# Initialize the Flask application
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return redirect(url_for('encrypt'))

"""
cipherzoic.tech/encrypt
responsible for running user input through our cipher and then hiding the encrypted text in an image
"""
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No image file uploaded')
            return redirect(request.url)
        
        file = request.files['image']
        text = request.form.get('text', '')
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if not file or not allowed_file(file.filename):
            flash('Invalid file type')
            return redirect(request.url)
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Apply custom cipher to text
        cipher = PreHistoricCipher()
        encrypted_text = cipher.encrypt(text)
        
        # Hide encrypted text in image
        secret = lsb.hide(filepath, encrypted_text)
        output_filename = 'encrypted_' + filename

        # Save the encrypted image
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        secret.save(output_path)
        
        return render_template('encrypt.html', 
                             result=True, 
                             original_image=filename,
                             encrypted_image=output_filename,
                             ciphertext = encrypted_text,)
    
    return render_template('encrypt.html', result=False)

"""
cipherzoic.tech/decrypt
responsible for extracting the hidden ciphertext from the image and then decrypting it to reveal secret message.
"""
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        if 'encrypted_image_file' not in request.files:
            return render_template('decrypt.html', error="No image file uploaded")
        
        file = request.files['encrypted_image_file']
        
        if file.filename == '':
            return render_template('decrypt.html', error="No file selected")
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            try:
                # Extract hidden text from image
                encrypted_text = lsb.reveal(filepath)
                
                # Decrypt the text
                cipher = PreHistoricCipher()
                decrypted_text = cipher.decrypt(encrypted_text)
                
                return render_template('decrypt.html', 
                                     result=True, 
                                     ciphertext=encrypted_text,
                                     plaintext=decrypted_text)
            except Exception as e:
                return render_template('decrypt.html', error=str(e))
    
    return render_template('decrypt.html', result=False)

# Run the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
