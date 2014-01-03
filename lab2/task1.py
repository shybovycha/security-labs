from Crypto.Cipher import AES

key = '140b41b22a29beb4061bda66b6747e14'
cipher = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

key = key.decode('hex')
cipher = cipher.decode('hex')

iv = cipher[:16]

decoder = AES.new(key, AES.MODE_CBC, iv)

res = decoder.decrypt(cipher[16:])

print(res)

# Basic CBC mode encryption needs padding.