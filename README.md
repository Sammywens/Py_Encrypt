Py_Encrypt is a Python-based encryption and decryption tool for securely handling sensitive data, like login details, passwords, or other confidential information. This program uses symmetric encryption to encrypt and decrypt text files, ensuring safe storage and transmission of sensitive data.

Features
Text encryption and decryption using secure cryptography libraries.
Simple user interface for entering text, encrypting, and decrypting.

Requirements
To run this project, you'll need:

Python 3.6 or higher
cryptography library
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Sammywens/Py_Encrypt.git
cd Py_Encrypt
Install the required packages (if you haven't installed them already):

bash
Copy code
pip install cryptography

Usage
Run the script:

bash
Copy code
python3 app.py
Encryption/Decryption:

The program will prompt for text to encrypt or decrypt.
Follow on-screen instructions to encrypt data (it will save an encrypted file) or decrypt an existing encrypted file.
Code Explanation
Main Components
Imports:

from cryptography.fernet import Fernet: Imports Fernet from the cryptography library, which provides secure symmetric encryption.
Generate Key Function:

A unique key is generated for encryption. This key is essential for both encrypting and decrypting data, so it must be securely stored.
python
Copy code
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
Load Key Function:

Retrieves the key needed to encrypt or decrypt data.
python
Copy code
def load_key():
    return open("secret.key", "rb").read()
Encrypt Message Function:

Accepts plaintext and uses the loaded key to encrypt it.
Saves the encrypted message in a separate file.
python
Copy code
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    with open("encrypted_message.txt", "wb") as file:
        file.write(encrypted_message)
Decrypt Message Function:

Reads the encrypted message and uses the key to decrypt it.
python
Copy code
def decrypt_message():
    key = load_key()
    f = Fernet(key)
    with open("encrypted_message.txt", "rb") as file:
        encrypted_message = file.read()
    decrypted_message = f.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message.decode())
User Interface:

Prompts the user to input a message and choose to either encrypt or decrypt it.
