from Crypto.Util.number import *

a = "label"

for i in range(len(a)):
    s = ord(a[i])
    b = s^13
    print(chr(b))