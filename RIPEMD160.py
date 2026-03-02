import hashlib

# creating the hash object
Hash = hashlib.new('ripemd160')
print(Hash)

# putting data to be hashed
Hash.update(b'Hello World!')
x = Hash.digest()
print(x)

# seeing the digest tin hexadecimal
size = Hash.block_size
print(size)

# getting the digest size
digest_size = Hash.digest_size
print(digest_size)

# notice that the digest size is smaller than the block size.
