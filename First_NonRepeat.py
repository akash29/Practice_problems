def find_non_repeat(s):
    dict_str = {}
    for i,j in enumerate(s):
        if j not in dict_str:
            dict_str[j+str(i)] = 1
        else:
            dict_str[j+str(i)]+=1

    for i,j in dict_str.items():
        if j > 1:
            return i

    #return max(dict_str, key=dict_str.get)

print(find_non_repeat("finding"))