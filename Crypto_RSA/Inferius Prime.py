from Crypto.Util.number import long_to_bytes
# import Crypto.Util.number
p = 752708788837165590355094155871
q = 986369682585281993933185289261
n = q*p
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
phi = (p-1)*(q-1)
D = pow(e,-1,phi)
flag = long_to_bytes(pow(ct,D,n))
print(flag)