from Crypto.PublicKey import RSA

key = RSA.importKey(open('private_key.pem', 'rb').read())
print(key.n)
print(key.e)
print(key.d)