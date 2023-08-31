def xor_decrypt(ciphertext, key):
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted_char = chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
        decrypted += decrypted_char
    return decrypted

ciphertexts = [
    "142b342b2662212d2e2d30316226232c2127622b2c62362a276231293b",
    "0723252730622a2723303631622e27233262352b362a62282d3b",
    "1023262b232c366231372c312736316e62236220302723362a3623292b2c2562312b252a36",
    "1b2723302c2b2c2562242d30622f2d2f272c363162362a2336622c2734273062232c2c2d3b",
    "07232527306231362732316235276236232927",
    "0362282d37302c273b622c2d3662362d2d62212d2f322e273a",
    "112b2f322e2762362331293162352762372c26273036232927",
    "1b2723302c2b2c2562242d30623137212127313162362a23366531622723313b"
]

keys = [
    "XOR_KEY_1",
    "XOR_KEY_2",
    "XOR_KEY_3",
    "XOR_KEY_4",
    "XOR_KEY_5",
    "XOR_KEY_6",
    "XOR_KEY_7",
    "XOR_KEY_8"
]

for i in range(len(ciphertexts)):
    decrypted_text = xor_decrypt(ciphertexts[i], keys[i])
    print(decrypted_text)