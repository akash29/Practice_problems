def isSubstring(str1,str2):
    if len(str1)==len(str2):
        str1_sorted = sorted(str1)
        str2_sorted = sorted(str2)

        return str1_sorted == str2_sorted
    else:
        return False

str1 = 'hunter'#"waterbottle"
str2 = 'terhum'#"erbottlewat"
print(isSubstring(str1, str2))


def isSubstring_2(str1,str2):
    return len(str1)==len(str2) and str1 in (str1+str2)

str1 = "waterbottle"
str2 = "erbottlewat"
print(isSubstring_2(str1,str2))


