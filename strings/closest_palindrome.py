def isPalindrome(item):
    for i in range(len(item)//2):
        if item[i] != item[len(item)-1-i]:
            return False

def minDiff(num1,num2):
    return abs(num1-num2)

def closest_palindrome(item):
    # case1: middle digit 0
    mid_index = len(item)//2
    min_1 = float('inf')
    min_2 = float('inf')
    min_3 = float('inf')
    new_num_1,new_num_2,new_num_3 = 0,0,0
    if len(item)>1:
        if item[mid_index] =='0':
            left_half = int(item[:mid_index+1])
            left_half-=1
            left_half = str(left_half)
            new_num_1 = left_half+left_half[mid_index-1::-1]
            min_1 = minDiff(int(item),int(new_num_1))

        #case2: middle digit 9
        elif item[mid_index]=='9':
            left_half = int(item[:mid_index+1])
            left_half += 1
            left_half = str(left_half)
            new_num_2 = left_half + left_half[mid_index - 1::-1]
            min_2 = minDiff(int(item),int(new_num_2))

        #case3: all other numbers
        else:
            left_half = item[:mid_index+1]
            new_num_3 = left_half + left_half[mid_index - 1::-1]
            min_3 = minDiff(int(item),int(new_num_3))

        if min_1 < min_2 and min_1 < min_3:
            return new_num_1
        elif min_2 < min_1 and min_2 < min_3:
            return new_num_2
        else:
            return new_num_3
    else:
        return item


print(closest_palindrome("10987"))
print(closest_palindrome("111"))
print(closest_palindrome("3000001"))
print(closest_palindrome("4"))



