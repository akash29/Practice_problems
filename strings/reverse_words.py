def reverse_words_util(arr):
    n = len(arr)
    i = 0
    j = 0

    while j < n:
        while j < n and arr[j] != ' ':
            j += 1
        arr = reverse_words(arr, i, j - 1)
        j += 1
        i = j

    return arr


def reverse_words(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


test_arr = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
rev_arr = reverse_words(test_arr, 0, len(test_arr) - 1)
print(rev_arr)
print(reverse_words_util(rev_arr))
