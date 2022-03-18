str="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

byte_str=bytes.fromhex(str)
for j in range(300):
    if(byte_str[0]^j == 99): 
        for i in range(len(byte_str)):
            print(chr((byte_str[i])^j))
        break