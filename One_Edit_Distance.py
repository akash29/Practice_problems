def find_one_edit(str1,str2):
    dict_str = {}
    if str1 == str2:
        return True
    elif abs(len(str1)-len(str2))==1:
        count_edits = 0
        for i,j in zip(str1,str2):
            if i not in dict_str:
                dict_str[i] = 1
            if j not in dict_str:
                count_edits+=1
                if count_edits >1:
                    return False

        if len(str1) < len(str2):
            shorter_str = str1
        else:
            shorter_str = str2
        if count_edits <1 and abs(len(dict_str)-len(shorter_str))<=1:
            return True
        else:
            return False
    else:
        return False




print (find_one_edit("geeks","geeks"))