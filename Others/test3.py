import numpy as np
np.random.seed(17)
rand_vals = np.random.rand()
print(rand_vals)











nums = [9,11,12,222,23,54,60]+[2,3,4]
map_temp = {6:5,2:1,3:4,5:8}

num_temp = [i//10 for i in nums]
print(num_temp)
map_sorted = sorted(map_temp.items(),key= lambda x:x[1],reverse=True)
temp_arr = []
for i in map_sorted:
    temp_arr+=[i[0]]*i[1]

print(temp_arr)

a = 'abc.sde.kqy'
a_temp = a.split('.')
print(a_temp[::-1])
