input_doc= "jesslookedliketimherbrother"
dict_of_words=["looked","like","her","kite","time","brother"]


def naive_impl():
    new_input_doc = ""
    input_len = len(input_doc)
    i = 1
    k=0
    while i <= input_len:
        for j in range(k,i):
            str = input_doc[j:i]
            if str in dict_of_words:
                temp_word = input_doc[k:j]
                if len(temp_word)>0:
                    new_word = temp_word+" "+str+" "
                else:
                    new_word = str+" "
                new_input_doc += "".join(new_word)
                k = i
                break
        i += 1
    print(new_input_doc)

naive_impl()
