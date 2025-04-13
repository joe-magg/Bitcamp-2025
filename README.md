# Cipherzoic

A Flask web application that combines a custom cipher with steganography to embed secret messages in images. 

Built for Bitcamp 2025.

## Features

- Custom cipher implementation for message encryption
- Steganography using LSB (Least Significant Bit) technique
- Upload and process PNG/JPG images
- User-friendly web interface

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Custom Cipher

The Prehistoric Cipher uses a unique mapping system that converts modern text into "caveman-style" symbols and expressions. Here's how characters are mapped:

### Letter Mappings
- A → `---->` (arrow)
- B → `>=--=<` (bone) 
- C → `()====-` (club)
- D → `_,,,---'''''---,,,_` (cloud)
- E → `(((O)))` (earth)
- F → `!><!` (fight)
- G → `GRRR` (growl)
and so on...

The cipher converts all text to uppercase before encryption and joins the mapped symbols with 4 spaces between each symbol. For decryption, it splits the text by 4 spaces and maps each symbol back to its original character.

