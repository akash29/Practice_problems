class Solution:
    def bin_search(self, arr, low, high, target):
        if len(arr)>1:
            middle = low+(high-low)// 2
            if low > high:
                return -1
            elif arr[middle] > target:
                middle -= 1
                high = middle
                return self.bin_search(arr, low, high, target)
            elif arr[middle] < target:
                middle += 1
                low = middle
                return self.bin_search(arr, low, high, target)
            elif arr[middle] == target:
                return middle
        elif arr[0] == target:
            return 0
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) > 0:
            end_pos = len(nums) - 1
            end_pos_2 = len(nums) - 2
            while end_pos_2 >= 0:
                if nums[end_pos_2] > nums[end_pos]:
                    arr1 = nums[:end_pos_2 + 1]
                    arr2 = nums[end_pos:]
                    out_1 = self.bin_search(arr1, 0, len(arr1)-1, target)
                    if out_1 >-1:
                        return out_1
                    out_2 = self.bin_search(arr2, 0, len(arr2)-1, target)
                    if out_2 >-1:
                        return end_pos+out_2
                    return -1
                end_pos -= 1
                end_pos_2 -= 1
            else:
                return self.bin_search(nums,0,len(nums)-1, target)
        else:
            return -1

sol = Solution()
print (sol.search([4,5,6,7,1,2,3],4))