from collections import defaultdict

synonyms = [('Jon', 'John'), ('John', 'Johnny'), ('Chris', 'Kris'), ('Chris', 'Christian')]
             # ('Muhamed', 'Mohhamad'),('Mohmed', 'muhhamad'), ('Muhamed', 'Mohmed')]
names = [('John', 15), ('Jon', 12), ('Chris',13), ('Kris',4), ('Christian', 19)]


def construct_baby_names():
    baby_name = defaultdict(list)
    for i,j in synonyms:
        baby_name[i].append(j)
    return baby_name


def construct_baby_freq():
    baby_freq_dict = {}
    for i,j in names:
        baby_freq_dict[i]=j
    return baby_freq_dict


def dfs(baby_name_gr,visited):
    dfs_result = []
    for i in baby_name_gr.keys():
        if not visited[i]:
            dfs_result.append(dfs_util(i,visited,baby_name_gr))

    return dfs_result


def dfs_util(node,visited,baby_name_gr):
    dfs_stack = [node]
    result=[]
    while dfs_stack:
        elem = dfs_stack.pop()
        result.append(elem)
        if not visited[elem]:
            visited[elem] = True
        if elem in baby_name_gr.keys():
            for j in baby_name_gr[elem]:
                dfs_stack.append(j)
    return result


def get_init_visited(baby_names):
    visited = {}
    for i,j in baby_names.items():
        if i not in visited:
            visited[i] = False
        for k in j:
            if k not in visited:
                visited[k] = False

    return visited


def compute_freq(union_list):
    for i in union_list:
        sum_freq = 0
        for j in i:
            if j in baby_freq.keys():
                sum_freq += baby_freq[j]
        print(i[0]+" ({0})".format(sum_freq))


baby_name_dict = construct_baby_names()
baby_freq = construct_baby_freq()
visited_dict = get_init_visited(baby_name_dict)
dfs_list = dfs(baby_name_dict,visited_dict)
compute_freq(dfs_list)


