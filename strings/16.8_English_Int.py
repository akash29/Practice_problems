from collections import deque

num_units_maps = {4:"billion ",3:"million ",2:"thousand ",1:" ", 0: " "}

num_to_english_single = {0:"",1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
                      6:"six",7:"seven",8:"eight",9:"nine"}

num_to_english_tys={2:"twen",3:"thirt",5:"fif"}

num_to_english_two = {10:"ten",11:"eleven",12:"twelve",13:"thirteen"}


def get_num(num):
    str_num = str(num)
    num_list = deque()
    while str_num:
        new_num = str_num[-3:]
        num_list.appendleft(int(new_num))
        str_num = str_num[:-3]
    return num_list


def construct_str(num_list):
    out_result = ""
    while num_list:
        len_str = len(num_list)
        elem = num_list.popleft()
        out_result += construct_str_util(elem,len_str,out_result)

    return out_result.strip(" ")


def construct_str_util(s,l,new_str):
    len_str = len(str(s))
    if len_str == 3:
        char1 = int(str(s)[0])
        out_str = num_to_english_single[char1]+" hundred"
        temp_num = int(str(s)[1:])
        return construct_str_util(temp_num,l,out_str)
    elif len_str == 2:
        if s not in num_to_english_two.keys():
            char1 = int(str(s)[0])
            if char1 not in num_to_english_tys.keys():
                new_str += " "+num_to_english_single[char1]+"ty"
                temp_num = int(str(s)[1:])
                return construct_str_util(temp_num, l, new_str)
            else:
                new_str += " "+num_to_english_tys[char1]+"ty"
                temp_num = int(str(s)[1:])
                return construct_str_util(temp_num, l, new_str)

        else:
            new_str += " "+num_to_english_two[s]
            return construct_str_util(0,l,new_str)

    else:
        return new_str+" "+num_to_english_single[s]+" "+num_units_maps[l]


test_num = 10
val = get_num(test_num)
print(construct_str(val))