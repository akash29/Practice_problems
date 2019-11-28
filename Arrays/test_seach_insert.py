from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, 0, len(nums)-1, target)
        
    
    def binSearch(self, nums, left, right, target)->int:
        middle = left+((right-left)//2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target and left!=right:
            return self.binSearch(nums, left, middle, target)
        elif nums[middle] < target and left !=right:
            return self.binSearch(nums, middle+1, right, target)
        elif left == right:
            if left < len(nums):
                if left == len(nums)-1 and nums[left] < target:
                    return left+1
                else:
                    return middle
            else:
                return 0

s = Solution().searchInsert([1],0)
print (s)