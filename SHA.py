import hashlib

# the ones available in your system
print(hashlib.algorithms_available)

# the ones available in hashlib
print(hashlib.algorithms_guaranteed)

hashed_string = hashlib.sha224(b'Hello World')
encrypted_string = hashed_string.digest()
encrypted_hex_string = hashed_string.hexdigest()
print("The encrypted data is: " + str(encrypted_string))
print("The encrypted data is: " + str(encrypted_hex_string))




