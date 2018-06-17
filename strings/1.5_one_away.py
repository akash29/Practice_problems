def one_away(str1,str2):
    if abs(len(str1)-len(str2)) <=1:
        ptr_1=0
        ptr_2=0
        num_edits = 0
        while ptr_1<len(str1) and ptr_2<len(str2):
            if str1[ptr_1]==str2[ptr_2] and num_edits<2:
                ptr_1+=1
                ptr_2+=1
            elif str1[ptr_1]!=str2[ptr_2] and num_edits<2:
                if len(str1) > len(str2):
                    ptr_1+=1
                elif len(str2) > len(str1):
                    ptr_2+=1
                else:
                    ptr_1+=1
                    ptr_2+=1
                num_edits+=1
            else:
                return False
        if abs(ptr_1-ptr_2)>1:
            return False

        return True
    else:
        return False


print(one_away('pale','bale'))
print(one_away('pale','bake'))
print(one_away('pales','pale'))
print(one_away('pale','ple'))