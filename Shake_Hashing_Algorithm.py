# shake is one of the hashing algorithm,
# the digest in the shake algorithm can be of variable length,

import hashlib

print(hashlib.algorithms_available)

# this is the hash object
Hash = hashlib.shake_256(b'Hello World!')
print(Hash)

x = Hash.digest(12)
print(x)

# hex digest of 10 size
y = Hash.hexdigest(10)
print(y)

# increasing the size of the digest
y = Hash.hexdigest(10)
print(y)

# shake_128 can be also used instead of the shake_256



