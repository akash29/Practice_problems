class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_list = []
        self.binSearch(nums, 0, len(nums) - 1, target, val_list)
        
        sorted_list = sorted(val_list)
        new_list = [sorted_list[0], sorted_list[-1]]
        return new_list

    def binSearch(self, arr, low, high, target, val_list):
        if len(arr) > 0:
            middle = low + (high - low) // 2
            if low > high:
                return -1
            elif arr[middle] > target:
                middle -= 1
                return self.binSearch(arr, low, middle, target, val_list)
            elif arr[middle] < target:
                middle += 1
                return self.binSearch(arr, middle, high, target, val_list)
            elif arr[middle] == target:
                val_list.append(middle)
                self.binSearch(arr, middle+1, high, target, val_list)
                self.binSearch(arr, low, middle-1, target, val_list)
                return middle
            else:
                return -1

        else:
            return -1

sol = Solution()
val = sol.searchRange([5,5,7,7,8,8,8],8)
print (val)