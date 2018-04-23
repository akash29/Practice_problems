class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) > 1:
            start_pos = 0
            end_pos = len(nums) - 1
            while end_pos >=start_pos:
                start_val = nums[start_pos]
                if start_val == val:
                    value = nums.pop(start_pos)
                    nums.append(value)
                    end_pos -= 1
                else:
                    start_pos += 1
            print (nums[:start_pos])
            return len(nums[:start_pos])
        elif len(nums) == 1:
            if nums[0] != val:
                return len(nums)
            else:
                nums.pop(0)
                return len(nums)
        else:
            return 0


sol = Solution()
print(sol.removeElement([3,2,2,3],3))