d = 256
p = 199


def multi_search(s_list, m):
    hash_dict = {}
    search_hash = 0
    for i in s_list:
        hash_val = 0
        for j in i:
            hash_val = (d*hash_val+ord(j)) % p
        hash_dict[hash_val] = i
    for k in m:
        search_hash = (d*search_hash+ord(k)) % p
    if search_hash in hash_dict.keys():
        return True
    else:
        return False


str_list = ['abc', 'bca', 'aak', 'caa', 'lol']
search_str = 'lol'
print(multi_search(str_list,search_str))
