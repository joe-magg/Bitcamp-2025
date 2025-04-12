from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html', title="Home")

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """Renders the encrypt page and handles encryption."""
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        #  Add your encryption logic here.
        ciphertext = f"Encrypted: {plaintext}"  # Placeholder
        return render_template('encrypt.html', title="Encrypt", ciphertext=ciphertext, plaintext=plaintext)
    return render_template('encrypt.html', title="Encrypt", ciphertext=None, plaintext=None)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    """Renders the decrypt page and handles decryption."""
    if request.method == 'POST':
        ciphertext = request.form['ciphertext']
        # Add your decryption logic here
        plaintext = f"Decrypted: {ciphertext}"  # Placeholder
        return render_template('decrypt.html', title="Decrypt", plaintext=plaintext, ciphertext=ciphertext)
    return render_template('decrypt.html', title="Decrypt", plaintext=None, ciphertext=None)

if __name__ == '__main__':
    app.run(debug=True)
