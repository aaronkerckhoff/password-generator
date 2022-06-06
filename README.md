# Secure password generator
This project generates secure 15-character passwords using cryptographic randomness. After generation, the password is being checked for the following criteria:
* At least one uppercase letter
* At least one lowercase letter
* At least one number
* At least one special character

The generated password meeting all the above criteria is then being copied to the clipboard.

## Libraries
[requirements.txt](requirements.txt)

## Usage
You can bind `main.py` to some keybind to always generate a new secure password.