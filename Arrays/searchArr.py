def findpivot(nums, left, right):
    if left <=right and len(nums)>1:
        mid = left+(right-left)//2
        if mid < len(nums)-1 and mid>0 and nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        if mid == len(nums) -1 and nums[mid] < nums[mid-1]:
            return mid
        if mid == 0 and nums[mid] > nums[mid+1]:
            return mid
        else:
            if nums[left] > nums[mid]:
                return findpivot(nums, left, mid)
            else:
                return findpivot(nums, mid+1,right)
    return -1
    
def binSearch(nums, left, right, target):
    if len(nums)>1:
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        elif left!=right and nums[mid] > target:
            return binSearch(nums, left, mid, target)
        elif left!=right and nums[mid] < target:
            return binSearch(nums, mid+1, right, target)
        else:
            return -1
    else:
        return 0 if nums[0] == target else -1

# test_arr = [5,6,1,2,3,4]
# test_arr = [2,3,4,5,6,1]
# test_arr = [6,5,4,3,2,1]
# test_arr=[1,3,5]
test_arr=[1,2]

val = binSearch(test_arr, 0, len(test_arr)-1, 2)

# val = findpivot(test_arr,0, len(test_arr)-1)
print (val)