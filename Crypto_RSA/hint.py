from secret import get_flag, get_private_key
from Crypto.Util.number import bytes_to_long, getPrime


p, q = getPrime(1024), getPrimse(1024)
e = 0x10001
n, d= get_private_key(q, p, e)
flag = {???????}

print(f"p = {p}")
print(f"q = {q}")
print(f"e = {e}")
print(f"ct = {pow(flag, e, n)}")

# what is the flag?
