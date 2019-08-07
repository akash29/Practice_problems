
def find_union(l1,l2):
    # [i for i in l1 if i not in l2]+[i for i in l2 if i not in l1]+find_intersection(l1,l2) -> O(n^2)
    return len(set(l1+l2))


def find_intersection(l1,l2):
    l2_set = set(l2)
    return len([i for i in l1 if i in l2_set])


def get_similarity(input_map):
    list_keys = list(input_map.keys())
    g_temp = {}
    for i in range(len(input_map)-1):
        for j in range(i+1,len(input_map)):
            inter_len = find_intersection(input_map[list_keys[i]],input_map[list_keys[j]])
            union_len = find_union(input_map[list_keys[i]], input_map[list_keys[j]])
            if (inter_len/float(union_len)) > 0:
                g_temp[(list_keys[i],list_keys[j])] = inter_len/float(union_len)

    print(g_temp)


similarity_input = {13: [14, 15, 100, 9, 3],
                    16: [32, 1, 9, 3, 5],
                    19: [15, 29, 2, 6, 8, 7],
                    24: [7, 10]
                    }

get_similarity(similarity_input)

