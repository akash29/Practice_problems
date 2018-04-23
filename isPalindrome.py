import numpy as np

def test():
    arr_0 = np.arange(1, 25).reshape((2, 3, 4))
    arr_1 = arr_0.reshape(4, 6)
    arr_2 = arr_0.reshape(6, 4).transpose()

    print (arr_0)
    print(arr_1)
    print (arr_2)

test()

def isPalindrome(str):
    str = str.lower()
    left = 0
    right = len(str)-1
    while left < right :
        if str[left]==str[right]:
            left+=1
            right-=1
        else:
            return False
    return True

print (isPalindrome("Deleveled"))