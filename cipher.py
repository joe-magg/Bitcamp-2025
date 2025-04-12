class PreHistoricCipher:
    def __init__(self):
        self.key = 42
    
    def map_letter(self, letter):
        mapping = {
            'a': 'rock',
            'b': 'fire',
            'c': 'make',
            'd': 'stick',
            'e': 'boulder',
            'f': 'stone',
            'g': 'water',
            'h': 'hunt',
            'i': 'spear',
            'j': 'cave',
            'k': 'earth',
            'l': 'bow',
            'm': 'club',
            'n': 'flint',
            'o': 'bone',
            'p': 'fur',
            'q': 'hide',
            'r': 'hut',
            's': 'meat',
            't': 'river',
            'u': 'sky',
            'v': 'tree',
            'w': 'cloud',
            'x': 'tribe',
            'y': 'friend',
            'z': 'enemy',
            '!': 'fight',
            '?': 'strong',
            '.': 'chase',
            ',': 'me',   
            ' ': 'I',
            '"': 'go'
        }
        return mapping.get(letter, letter)

    def map_symbol(self, word):
        mapping = {
           'rock': r'[]',
           'fire': r'/\/\',
           'make': r'<>',
           'stick': r'|',
           'boulder': r'(O)',
           'stone': r'*',
           'water': r'~~^~~',
           'hunt': r'->o',
           'spear': r'====>',
           'cave': r'[__]',
           'earth': r'@@@',
           'bow': r'(--)',
           'club': r'=O',
           'flint': r'<>*',
           'bone': r'|-|',
           'fur': r'###',
           'hide': r'\|/',
           'hut': r'/\',
           'meat': r':o:',
           'river': r'~~~~~',
           'sky': r'* *',
           'tree': r'/|\',
           'cloud': r'(_)',
           'tribe': r'{o}',
           'friend': r':)',
           'enemy': r'>:(',
           'fight': r'><',
           'strong': r'||',
           'chase': r'>>',
           'me': r'&',
           'I': r'_',
           'go': r'"'
        }

    def encrypt(self, text):
        """
        Implement your custom encryption algorithm here.
        This is a simple example - replace with your team's custom cipher.
        """
        encrypted = ''
        return encrypted
    
    def decrypt(self, encrypted_text):
        """
        Implement your custom decryption algorithm here.
        This should reverse the encryption process.
        """
        decrypted = ''
        return decrypted 