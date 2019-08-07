def computeTempArr(pat):
    temp_arr = [0] * len(pat)
    temp_arr[0] = 0
    j = 0
    i = 1
    while i < len(pat):
        if j == 0 and pat[i] != pat[j]:
            temp_arr[i] = 0
            i += 1
        elif j > 0 and pat[i] != pat[j]:
            j = temp_arr[j - 1]
        elif pat[i] == pat[j]:
            temp_arr[i] = j + 1
            i += 1
            j += 1
    return temp_arr


def find_pattern(str_val, pat, temp_arr):
    i = 0
    j = 0
    while i < len(str_val) and j < len(pat):
        if str_val[i] == pat[j]:
            i += 1
            j += 1
        elif j > 0 and str_val[i] != pat[j]:
            j = temp_arr[j - 1]
        elif j == 0 and str_val[i] != pat[j]:
            i += 1
        if j == len(pat):
            print("found at index: ", i-j)
            j = temp_arr[j-1]



pattern = "AAABAA"
text = "AABAACAADAABAABA"
temp_arr = computeTempArr(pattern)
print(temp_arr)
find_pattern(text,pattern,temp_arr)
