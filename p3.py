import random
import string

# Define the characters to use in the password
letters = string.ascii_letters  # Includes both uppercase and lowercase letters
numbers = string.digits         # Includes numbers 0-9
symbols = string.punctuation     # Includes special characters (!, @, #, etc.)

# Combine all characters
all_characters = letters + numbers + symbols

# Ask the user for the password length
password_length = int(input("Enter the length of the password: "))

# Generate a random password
password = ''.join(random.choice(all_characters) for _ in range(password_length))

# Display the generated password
print("Your secure password is:", password)
