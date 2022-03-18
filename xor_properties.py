a = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
ba = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
bc = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
facb = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
byte_a=bytes.fromhex(a)
byte_bc=bytes.fromhex(bc)
byte_facb=bytes.fromhex(facb)

for i in range(len(byte_a)):
    print (chr((byte_facb[i]^byte_bc[i])^byte_a[i]))