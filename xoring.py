from Crypto.Util.number import*

fl = bytes.fromhex("54586b6458754f7b215c7c75424f21634f744275517d6d")

for i in range(256):
    if fl[0] ^ i == ord("D"):
        for ch in fl:
            print(chr(ch ^ i), end="")
            