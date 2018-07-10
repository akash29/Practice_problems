def isUnique(str1):
    sorted_str = sorted(str1)

    i = sorted_str[0]
    for j in range(1,len(sorted_str)):
        if i==sorted_str[j]:
            return False
        else:
            i=sorted_str[j]
    return True

print(isUnique("qwerty"))
