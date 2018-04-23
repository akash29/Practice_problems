class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, j in enumerate(nums):
            if j > target:
                print(j)
                continue
            for k,l in enumerate(nums):
                if l > target:
                    continue
                elif i !=k and j+l == target:
                    print(i,k)


sol = Solution()
sol.twoSum([-3,4,3,90],0)