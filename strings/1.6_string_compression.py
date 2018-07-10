def string_compression(org_str):
    count=1
    new_str = ''
    for i in range(1,len(org_str)+1):
        if i < len(org_str):
            if org_str[i]==org_str[i-1]:
                count+=1
            elif org_str[i]!=org_str[i-1]:
                act_str = org_str[i-1]
                act_str+=''.join(str(count))
                new_str+=''.join(act_str)
                count=1
        else:
            act_str = org_str[i - 1]
            act_str += ''.join(str(count))
            new_str += ''.join(act_str)

    return new_str if new_str < org_str else org_str

print(string_compression('aabcccccaaa'))


