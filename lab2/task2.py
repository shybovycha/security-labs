from Crypto.Cipher import AES

key = '36f18357be4dbd77f050515c73fcf9f2'
cipher = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'

i = 0
res = ''

for start in range(32, len(cipher), 32):
    text = cipher[start:start + 32]
    iv = hex(int(cipher[:32], 16) + i)[2:][:-1]

    decoder = AES.new(key.decode('hex'), AES.MODE_CTR, counter=lambda: iv.decode('hex'))
    dt = decoder.decrypt(text.decode('hex'))

    res = res + dt

    i = i + 1

print(res)

# CTR mode lets you build a stream cipher from a block cipher.