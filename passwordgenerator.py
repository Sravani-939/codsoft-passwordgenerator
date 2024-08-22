import random
import string

def generate_password(length=12, include_symbols=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if include_symbols else ''

    # Combine character sets
    all_characters = letters + digits + symbols

    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Set password length and whether to include symbols
    length = int(input("Enter the desired password length: "))
    include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    # Generate and display the password
    password = generate_password(length, include_symbols)
    print("Generated password:", password)
