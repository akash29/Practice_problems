from collections import defaultdict


def load_words():
    valid_words_dict = defaultdict(list)
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
        for i in valid_words:
            valid_words_dict[len(i)].append(i.upper())
    return valid_words_dict


def get_equal_length_words(words_dict,n):
    return words_dict[n]


def compute_edit_distance(str1,str2):
    if str1 == str2:
        return 0
    else:
        word_distance = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                if i==0:
                    word_distance[i][j]=j
                elif j==0:
                    word_distance[i][j]=i
                else:
                    if str1[i-1]==str2[j-1]:
                        word_distance[i][j] = word_distance[i-1][j-1]
                    else:
                        word_distance[i][j]=1+word_distance[i-1][j-1]

        return word_distance[len(str1)][len(str2)]


def get_distance(in_str,out_str,word_list_1,init_distance):
    print(in_str)
    for j,k in enumerate(word_list_1):
        new_in_dist = compute_edit_distance(k,in_str)
        new_out_dist = compute_edit_distance(k,out_str)
        if new_in_dist == 1 and new_out_dist<init_distance:
            word_list_1.pop(j)
            init_distance = new_out_dist
            in_str = k
            return get_distance(in_str,out_str,word_list_1,init_distance)


if __name__ == '__main__':
    english_words = load_words()
    input_str = 'DAMP'
    output_str = 'CAKE'
    word_list = (get_equal_length_words(english_words,len(input_str)))
    init_dist = compute_edit_distance(input_str,output_str)
    get_distance(input_str,output_str,word_list,init_dist)


