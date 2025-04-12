class PreHistoricCipher:
    def __init__(self):
        # You can customize this key and the cipher implementation
        self.key = 42
    
    def map_letter(self, letter):
        mapping = {
            'a': 'rock',
            'b': 'fire',
            'c': 'make',
            'd': 'stick',
            'e': 'boulder',
            'f': 'stone',
            'g': 'G',
            'h': 'H',
            'i': 'I',
            'j': 'J',
            'k': 'K',
            'l': 'L',
            'm': 'M',
            'n': 'N',
            'o': 'O',
            'p': 'P',
            'q': 'Q',
            'r': 'R',
            's': 'S',
            't': 'T',
            'u': 'U',
            'v': 'V',
            'w': 'W',
            'x': 'X',
            'y': 'Y',
            'z': 'Z',
        }
        return mapping.get(letter, letter)



    def encrypt(self, text):
        """
        Implement your custom encryption algorithm here.
        This is a simple example - replace with your team's custom cipher.
        """
        encrypted = ''
        for char in text:
            # Simple shift cipher as placeholder - replace with your implementation
            if char.isalpha():
                shifted = chr((ord(char.lower()) - ord('a') + self.key) % 26 + ord('a'))
                encrypted += shifted.upper() if char.isupper() else shifted
            else:
                encrypted += char
        return encrypted
    
    def decrypt(self, encrypted_text):
        """
        Implement your custom decryption algorithm here.
        This should reverse the encryption process.
        """
        decrypted = ''
        for char in encrypted_text:
            # Simple shift cipher reversal - replace with your implementation
            if char.isalpha():
                shifted = chr((ord(char.lower()) - ord('a') - self.key) % 26 + ord('a'))
                decrypted += shifted.upper() if char.isupper() else shifted
            else:
                decrypted += char
        return decrypted 