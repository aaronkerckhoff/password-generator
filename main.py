import secrets
import pyperclip as pyperclip

# Get all available characters
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%^&*()'


def generate_password():
    password = ''
    for i in range(15):
        # Generate a random character
        character = secrets.choice(lowercase_letters + uppercase_letters + numbers + special_characters)
        password += character
    return password


generated_password = ''


# Check if password includes at least one letter, one number, and one special character
# If not, generate a new password

def contains_lowercase_letter(password):
    return any(c in lowercase_letters for c in password)


def contains_uppercase_letter(password):
    return any(c in uppercase_letters for c in password)


def contains_number(password):
    return any(c in numbers for c in password)


def contains_special_character(password):
    return any(c in special_characters for c in password)


while not contains_lowercase_letter(generated_password) or not contains_uppercase_letter(generated_password) or not contains_number(generated_password) or not contains_special_character(generated_password):
    generated_password = generate_password()

pyperclip.copy(generated_password)
print(generated_password)
