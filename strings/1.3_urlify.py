def urlify(string, len_str):
    new_arr = [i for i in string]
    for i in range(1, len_str):
        if new_arr[i-1] is ' ':
            new_arr[i - 1] = '%20'
    result_str = ''
    for k in new_arr:
        result_str += ''.join(k)

    return result_str

test_str = "Mr John Smith  "
print(urlify(test_str, 13))
