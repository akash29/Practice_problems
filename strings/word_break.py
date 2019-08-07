def word_break(s, word_dict):
    table= [False for i in range(len(s)+1)]
    table[0] = True

    for i in range(len(s)):
        for j in range(i+1):
            if table[j] and s[j:i+1] in word_dict:
                print(s[j:i+1])
                table[i+1] = True
                break

    return table[len(s)]

word_break("catsanddogs",["cat","cats","sand","and","dog"])