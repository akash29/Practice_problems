from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_arr = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and sorted_arr[i] == sorted_arr[i-1]:
                continue
            target = sorted_arr[i]*-1
            start = i+1
            end = len(sorted_arr)-1
            while start < end:
                temp_result = sorted_arr[start]+sorted_arr[end]
                if temp_result == target:
                    result.append([sorted_arr[start],sorted_arr[end], sorted_arr[i]])
                    start+=1
                    while start < end and sorted_arr[start]==sorted_arr[start-1]:
                        start+=1
                elif temp_result < target:
                    start+=1
                elif temp_result > target:
                    end-=1
        print (result)
    
sol = Solution()
sol.threeSum([-1, 0, 1, 2, -1, -4])