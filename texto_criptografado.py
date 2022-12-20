from Crypto.Cipher import AES

from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

plaintext = b'secret data'

key = get_random_bytes(16)
print(key, '\n\n\n')
cipher = AES.new(key, AES.MODE_CBC)

# ==== Encriptando os dados ==== #
data_ciphered = cipher.encrypt(pad(plaintext, AES.block_size))


print(data_ciphered)


