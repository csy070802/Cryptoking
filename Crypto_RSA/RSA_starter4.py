from Crypto.Util.number import *
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
n = p*q
phi = (p-1)*(q-1)
d = inverse(e,phi)
print(d)