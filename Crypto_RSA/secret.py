from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

def get_flag():
    return b"hsoc{w0w_y0u_f0und_th3_fl4g}"

def get_private_key(q, p, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    return n, d