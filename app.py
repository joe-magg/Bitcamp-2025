# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for, flash
# Import secure_filename for safely handling filenames (optional but recommended)
from werkzeug.utils import secure_filename
import os # Needed for potential file saving/processing
from cipher import PreHistoricCipher
from stegano import lsb
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-here')

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return redirect(url_for('encrypt'))

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
                             encrypted_image=output_filename)
    
    return render_template('encrypt.html', result=False)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No image file uploaded')
            return redirect(request.url)
        
        file = request.files['image']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
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
                                     decrypted_text=decrypted_text,
                                     image=filename)
            except Exception as e:
                flash('Error decrypting image: ' + str(e))
                return redirect(request.url)
    
    return render_template('decrypt.html', result=False)

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True) # debug=True enables auto-reloading and detailed errors
