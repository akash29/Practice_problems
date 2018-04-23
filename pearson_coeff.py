import numpy as np
import math

def compute_pearson(x,y):
    total_x = sum(x)
    total_y = sum(y)
    sq_x = np.square(x)
    sq_y = np.square(y)
    print(sq_x)
    print(sum(sq_x))
    N = len(x)
    xy = [x[i]*y[i] for i in range(len(x))]

    r_num = np.sum(xy)-(total_x*total_y)/N
    r_denom = math.sqrt((sum(sq_x) - (total_x**2/N))*(sum(sq_y)-(total_y**2/N)))
    return r_num/r_denom

x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]
print(compute_pearson(x,y))

