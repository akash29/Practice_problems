def swap_bits(num,i,j):
    if num >> i & 0x1 != num >> j &0x1:
        num^=1<<j | 1<<i
    return num


print(swap_bits(73,1,6))