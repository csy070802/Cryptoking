from Crypto.Util.number import*
cb = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
print(cb)

def user_xor(org, num):
    result = ""
    for ch in org:
        result += chr((ch) ^ num)
    return result
    
for i in range(255+1):
    print(user_xor(cb, i))

    
