from Crypto.Util.number import *
fl = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):
    for char in fl:
        print(chr(char ^ i), end="")
        print(type(char))
    
        # 증가하는 i값과 변수 fl이 들어있는 char을 xor
        # if (char[0] == 'c'):
        #     print()
        