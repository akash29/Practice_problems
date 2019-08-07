x = 64
y = x & ~(x-1)
to_shift = y-1
print(bin(x))
print(bin(x|to_shift))