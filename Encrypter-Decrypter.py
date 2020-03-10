# Lets create file encryption program .
import random
import os
from cryptography.fernet import Fernet

# Random byte string
key = Fernet.generate_key()
# Used to encryption and decryption
token = Fernet(key)
# Random key file name
keyFile = str(random.randint(100, 1001)) + 'key.txt'
# Give full path of the text file and you don't have to write the file name.
desktop = os.path.abspath('File path')
 
def encrypt():
    userFile = str(input('\n File must be in Desktop!\n Enter File name and extension: '))
    try:
        with open(os.path.join(desktop, userFile), 'rb+') as plainFile:
            # File data
            plainText = plainFile.read()
            cipherText = token.encrypt(plainText)
            # Return to the beginning of the file
            plainFile.seek(0)
            # Empty the file
            plainFile.truncate()
            plainFile.write(cipherText)
            print(f'\n File data: {plainText}')
            print('\n File is encrypted!')
            print('\n We are creating the key file in your Desktop')
            with open(os.path.join(desktop, keyFile), 'wb') as keyfile:
                keyfile.write(key)
    except Exception as e:
        print(f'Error! {e}')
 
def decrypt():

    userFile = str(input('\n File must be in Desktop! Enter file name and extension: '))
    userKey = str(input('\n Enter Key to decrypt the file: '))
    try:
        tokenDec = Fernet(userKey)
        with open(os.path.join(desktop, userFile), 'rb+') as f:
            cipherText = f.read()
            plainText = tokenDec.decrypt(cipherText)
            f.seek(0)
            f.truncate()
            f.write(plainText)
            print('\n File is decrypted!')
    except Exception as e:
        print(f'\n Error! {e}')
 
if __name__ == '__main__':

    userChoice = str(input('\n 1. Encrypt\n 2. Decrypt\n\n What do you want to perform? > '))
    if userChoice == '1':
        encrypt()
    elif userChoice == '2':
        decrypt()
    else:
        print('Invalid Input!')
