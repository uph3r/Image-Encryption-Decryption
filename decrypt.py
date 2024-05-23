from cryptography.fernet import Fernet

# Load the key from the file
with open('key.txt', 'rb') as f:
    key = f.read()

# Create a Fernet object with the key
fernet = Fernet(key)

# Read the encrypted image
with open('img.jpg', 'rb') as f:
    locked_photo = f.read()

# Decrypt the image
unlocked_photo = fernet.decrypt(locked_photo)

# Write the decrypted image
with open('img.jpg', 'wb') as unlocked_photo_file:
    unlocked_photo_file.write(unlocked_photo)

print("Image has been decrypted")