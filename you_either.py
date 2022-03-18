str="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
byte_str=bytes.fromhex(str)

format = b"crypto{"
key = [o1 ^ o2
       for (o1, o2) in zip(byte_str,format)] + [ord("y")]
for i in range(len(byte_str)):
    print(chr(byte_str[i] ^ key[i % len(key)]))