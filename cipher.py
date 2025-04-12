class PreHistoricCipher:
    def __init__(self):
        self.mapping = {
            'A': '---->', # arrow
            'B': '8======8', # bone
            'C': '()====-', # club
            'D': '_,,,---\'\'\'\'\'---,,,_', # _,,,---'''''---,,,_ - cloud
            'E': '(((O)))', # earth
            'F': '!x/ \\x!', # fight !x/ \x!
            'G': 'GRRR', # grrr
            'H': '...> /)> o', # hunt
            'I': 'o/', # me
            'J': 'o/   \\o', # o/   \o -  us
            'K': '//^^^^^^^^\\\\', # //^^^^^^^^\\ - cave
            'L': '(^_^)', # like
            'M': '[===]', # meat
            'N': 'NAH', # nah
            'O': 'OOGA', # ooga
            'P': '\\_________________/', # \_________________/ - pit
            'Q': 'QUAHHH', # quahhh
            'R': 'RAHHH', # rahhh
            'S': '.o0o.', # stone
            'T': '*^|*/\\|---', # *^|*/\|--- - tree (look sideways)
            'U': 'UUGHH', # uughh
            'V': '----|-=-=-=-=->', # spear
            'W': '~~~^~~~^~~~^~~~^~~~', # water
            'X': '>:x o!', # kill
            'Y': 'YAHOO!!!', # yahoo
            'Z': '(_ _)...zZz', # sleep
            '!': 'AARGH!', # aargh!
            '?': 'HUH?', # huh?
            '.': 'GRAH!', # grah!
            ',': ',', # ,
            '1': 'ONE', # one
            '2': 'TWO', # two
            '3': 'THREE', # three
            '4': 'FOUR', # four
            '5': 'FIVE', # five
            '6': 'CANT', # cant
            '7': 'COUNT', # count
            '8': 'THAT', # that
            '9': 'HIGH', # high
            '0': 'NO', # no
            ' ': 'AND'
        }
    def map_symbol(self, symbol):
        return self.mapping[symbol]

    def encrypt(self, text):
        """
        Implement your custom encryption algorithm here.
        This is a simple example - replace with your team's custom cipher.
        """
        encrypted = ''
        # Check for invalid characters
        allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,?! ')
        if not all(c.upper() in allowed_chars for c in text):
            return "ERROR: CAVEMAN ONLY LIKE VALID CHARACTER. ONLY A-Za-z, 0-9, comma, space, ?, AND !."
            
        # Convert to uppercase and encrypt each character
        text = text.upper()
        encrypted_chars = [self.map_symbol(c) for c in text]
        encrypted = '    '.join(encrypted_chars)
        return encrypted
    
    def decrypt(self, encrypted_text):
        """
        Implement your custom decryption algorithm here.
        This should reverse the encryption process.
        """
        decrypted = ''
        # Create reverse mapping from encrypted symbols to letters
        reverse_mapping = {v: k for k, v in self.mapping.items()}
        
        # Split by double spaces to get encrypted symbols
        encrypted_symbols = encrypted_text.split('    ')
        
        # Convert each symbol back to original letter using reverse mapping
        decrypted_chars = []
        for symbol in encrypted_symbols:
            if symbol in reverse_mapping:
                decrypted_chars.append(reverse_mapping[symbol])
            else:
                return "ERROR: CAVEMAN NO UNDERSTAND THIS SYMBOL:" + symbol
                
        # Join characters back together
        decrypted = ''.join(decrypted_chars)
        return decrypted