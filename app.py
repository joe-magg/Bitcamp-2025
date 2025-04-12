# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for
# Import secure_filename for safely handling filenames (optional but recommended)
from werkzeug.utils import secure_filename
import os # Needed for potential file saving/processing

# Initialize the Flask application
app = Flask(__name__)

# Optional: Configure an upload folder if you plan to save files
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html', title="Home")

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """
    Renders the encrypt page.
    Handles POST requests for encryption (currently placeholder).
    Requires 'plaintext' form data and 'image_file' file upload.
    """
    if request.method == 'POST':
        error = None
        ciphertext = None
        plaintext = request.form.get('plaintext') # Use .get for safety
        image_file = request.files.get('image_file') # Use .get for safety

        # --- Basic Validation ---
        if not plaintext:
            error = "Plaintext is required."
        elif not image_file or image_file.filename == '':
             error = "Image file is required."
        # Optional: Add more validation for file type, size etc.
        # elif not allowed_file(image_file.filename):
        #     error = "Invalid file type for image."

        if error is None:
            # --- Placeholder Encryption Logic ---
            # In a real app:
            # 1. Process the image_file (e.g., save it, read its bytes).
            #    filename = secure_filename(image_file.filename)
            #    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            #    image_file.save(image_path)
            # 2. Perform encryption using plaintext and the image data.
            # 3. Potentially embed ciphertext in a new image or return separately.
            print(f"Received plaintext: {plaintext}")
            print(f"Received image file: {secure_filename(image_file.filename)}")
            ciphertext = f"Encrypted '{plaintext}' using '{secure_filename(image_file.filename)}' (Placeholder)"
            # --- End Placeholder ---

        # Render the template with results or errors
        # Pass the original plaintext back to potentially repopulate the form
        return render_template('encrypt.html',
                               title="Encrypt Result",
                               ciphertext=ciphertext,
                               plaintext=plaintext,
                               error=error)

    # Handle GET request: Render the initial empty form
    return render_template('encrypt.html',
                           title="Encrypt",
                           ciphertext=None,
                           plaintext=None,
                           error=None)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    """
    Renders the decrypt page.
    Handles POST requests for decryption (currently placeholder).
    Expects 'encrypted_image_file' file upload instead of 'ciphertext'.
    """
    if request.method == 'POST':
        error = None
        plaintext = None
        # --- Check if the file part is in the request ---
        if 'encrypted_image_file' not in request.files:
            error = "No file part in the request."
            # Render the page again, showing the error
            return render_template('decrypt.html', title="Decrypt", error=error, plaintext=None)

        # --- Get the file object ---
        file = request.files['encrypted_image_file']

        # --- Check if a file was actually selected ---
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            error = 'No selected file.'
            # Render the page again, showing the error
            return render_template('decrypt.html', title="Decrypt", error=error, plaintext=None)

        # --- If file exists and has a name ---
        if file: # Optional: Add further file validation here (e.g., file type)
            filename = secure_filename(file.filename) # Sanitize filename
            print(f"Received file for decryption: {filename}")

            # --- Placeholder Decryption Logic ---
            # In a real app:
            # 1. Process the uploaded file (e.g., save it, read its bytes).
            #    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            #    file.save(image_path)
            # 2. Extract hidden data (ciphertext) from the image.
            # 3. Decrypt the extracted data.
            plaintext = f"Decrypted data from '{filename}' (Placeholder)"
            # --- End Placeholder ---

            # Render the template with the decryption result
            return render_template('decrypt.html', title="Decrypt Result", plaintext=plaintext, error=None)
        else:
             # This case might be redundant due to the filename check, but good practice
             error = "An unexpected error occurred with the file."
             return render_template('decrypt.html', title="Decrypt", error=error, plaintext=None)


    # --- Handle GET request ---
    # Render the initial empty form for decryption
    # Check if ciphertext was passed via URL (from encrypt page redirect) - this might be obsolete now
    ciphertext_from_url = request.args.get('ciphertext') # Example if needed
    return render_template('decrypt.html', title="Decrypt", plaintext=None, ciphertext=ciphertext_from_url, error=None)


# Example helper function for validating file extensions (if needed)
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True) # debug=True enables auto-reloading and detailed errors
