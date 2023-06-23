from Crypto.Util.number import *
a=long_to_bytes("crypto{")
flag=bytes_to_long("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")^a
print(bytes.fromhex(flag).decode('utf-8'))