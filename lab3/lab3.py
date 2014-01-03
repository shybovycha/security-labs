from Crypto.Hash import SHA256

block_size = 1024

f = open('test.mp4', 'rb')
f.seek(0, 2)

last_block_pos = f.tell()

last_block_size = last_block_pos % block_size

blocks = range(0, last_block_pos, block_size)
blocks.reverse()

last_hash = ""

for b in blocks:
    f.seek(b, 0)

    block = f.read(block_size)

    hasher = SHA256.new()
    hasher.update(block)
    hasher.update(last_hash)

    last_hash = hasher.digest()

print last_hash.encode('hex')

# 03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8
# ==
# 03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8