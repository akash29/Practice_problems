def count_bit(x:int)->int:
    num_bits = 0
    while x:
        num_bits+=x&1
        x<<=2
        temp = pow(12,2)
    return num_bits

print(count_bit(12))