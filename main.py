import secrets
import pyperclip as pyperclip

# Get all available characters
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'


def generate_password():
    password = ''
    for i in range(15):
        # Generate a random character
        character = secrets.choice(characters)
        password += character
    return password


# Copy password to clipboard
generated_password = generate_password()
pyperclip.copy(generated_password)
print(generated_password)
