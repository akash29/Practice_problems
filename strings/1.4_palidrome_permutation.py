def palidrome_permutation(string):
    str_lower = string.lower().replace(' ','')
    item_dict = {}
    for i in str_lower:
        if i not in item_dict.keys():
            item_dict[i]=1
        elif i in item_dict.keys():
            item_dict.pop(i)

    return len(item_dict)<=1

print(palidrome_permutation('Mdama mI daam')) #Madam Im Adam
