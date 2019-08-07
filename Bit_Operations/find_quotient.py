def get_quotient(x,y):
    if x < y:
        return 0
    else:
        count = 0
        temp_y = y
        while x-y >= 0:
            temp_power = 0
            while x >= y:
                y <<= 1
                if y > x:
                    y >>= 1
                    break
                temp_power += 1

            x = x - y
            y = temp_y
            count += 1 << temp_power

        return count

X = 16
Y = 8
print(get_quotient(X,Y))