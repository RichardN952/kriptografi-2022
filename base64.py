import base64
str="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
by=bytes.fromhex(str)
res=base64.b64encode(by)
print(res)
