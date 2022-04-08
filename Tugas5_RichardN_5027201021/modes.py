import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]

r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]

print(bytearray.fromhex(plaintext).decode())