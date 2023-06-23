from Crypto.Util.number import*

key1 = bytes_to_long(bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"))
key2 =key1^bytes_to_long(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"))
key3 =key2^bytes_to_long(bytes.fromhex( "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"))
flag = bytes_to_long(bytes.fromhex( "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))^key1^key2^key3

print(long_to_bytes(flag))