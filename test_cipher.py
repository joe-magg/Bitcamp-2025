from cipher import PreHistoricCipher
import sys

cipher = PreHistoricCipher()
    
def test(input):
    print(input)
    encrypted = cipher.encrypt(input)
    print(encrypted)
    decrypted = cipher.decrypt(encrypted)
    print(decrypted)
    

if len(sys.argv) < 2:
    print("Please provide a message to encrypt/decrypt as a command line argument")
    sys.exit(1)

test(sys.argv[1])