import secrets
import pyperclip as pyperclip

# Get all available characters
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

password = ''
for i in range(15):
    # Generate a random character
    character = secrets.choice(characters)
    password += character

# Save password to clipboard
pyperclip.copy(password)
print(password)
