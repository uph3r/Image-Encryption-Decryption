from cryptography.fernet import Fernet

# To Generate a key and save it into a file
key = Fernet.generate_key()

with open('key.txt', 'wb') as f:
    f.write(key)

# Load the key from the file
with open('key.txt', 'rb') as f:
    key = f.read()

# Create a Fernet object with the key
fernet = Fernet(key)

# Read the image to be encrypted
with open('img.jpg', 'rb') as f:
    photo = f.read()

# Encrypt the image
locked_photo = fernet.encrypt(photo)

# Write the encrypted image to a new file
with open('img.jpg', 'wb') as locked_photo_file:
    locked_photo_file.write(locked_photo)

print("Image has been encrypted")
