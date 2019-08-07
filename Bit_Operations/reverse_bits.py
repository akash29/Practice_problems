def reverse_bits(x):
    x = (x >> 32) | (x << 32)
    x = ((x & 0xffff0000ffff0000) >> 16) | ((x & 0x0000ffff0000ffff) << 16)
    x = ((x & 0xff00ff00ff00ff00) >> 8) | ((x & 0x00ff00ff00ff00ff) << 8)
    x = ((x & 0xf0f0f0f0f0f0f0f0) >> 4) | ((x & 0x0f0f0f0f0f0f0f0f) << 4)
    x = ((x & 0xcccccccccccccccc) >> 2) | ((x & 0x3333333333333333) << 2)
    x = ((x & 0xaaaaaaaaaaaaaaaa) >> 1) | ((x & 0x5555555555555555) << 1)
    return x

X = 1351510410656
print(bin(X))
rev_x = reverse_bits(X)
print(bin(rev_x))


