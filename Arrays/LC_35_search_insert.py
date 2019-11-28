def binSearch(nums, left, right, target):
    middle = left+((right-left)//2)
    if nums[middle] == target:
        return middle
    elif nums[middle] > target and left!=middle:
        return binSearch(nums, left, middle, target)
    elif nums[middle] < target  and right!=middle:
        return binSearch(nums, middle+1, right, target)
    elif left==right:
        if left < len(nums)-1 and left > 0:
            return middle
        elif left == len(nums)-1:
            return left+1
    else:
        return 0
    


test_nums= [1]
res = binSearch(test_nums, 0, len(test_nums)-1, 0)
print (res)