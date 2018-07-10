def k_charac(m,k,n):
    bin_num = bin(m)[2:]
    print(bin_num)
    replacement = {'0':'01','1':'10'}
    while n>0:
        end_str = ''
        for j in bin_num:
            end_str+=replacement[j]
        bin_num = end_str
        n-=1
    if len(bin_num)>k:
        return bin_num[k]


print(k_charac(5,5,3))
print(k_charac(11,6,4))