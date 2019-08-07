def find_closest_int(x):
    lsb = x & 1
    temp = x
    count = 1
    while temp:
        if temp >> 1 & 1 == lsb:
            count += 1
            temp >>= 1
        else:
            break

    new_value = 1 << count | 1 << (count - 1)
    x ^= new_value
    return x

X = 6
print(find_closest_int(X))