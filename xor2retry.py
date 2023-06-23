from Crypto.Util.number import *
fl = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):
    if fl[0] ^ i == ord('c'):
        # for char in fl:
        #     print(char ^ i, end=" ")
        # print()
        for char in fl:
            print(chr(char ^ i), end=" ")
        print()
