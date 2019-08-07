# test if x is power of 2
x = pow(2,9)-7
y = 2
print(x)
print(y)
out = True if (x & (y-1))==0 else False
print(out)