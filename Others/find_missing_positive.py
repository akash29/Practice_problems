class Solution:
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(A))
        nums = [i for i in nums if i >= 0]
        if len(nums) > 0:
            sorted_list = sorted(nums)
            start_index = 0
            next_index = start_index + 1
            while next_index < len(sorted_list):
                if sorted_list[next_index] - sorted_list[start_index] == 1:
                    next_index += 1
                    start_index += 1
                elif sorted_list[0]!=0 and sorted_list[0] > 1:
                    return 1
                else:

                    print(sorted_list[start_index] + 1)
                    return sorted_list[start_index] + 1

            else:
                if sorted_list[0] != 0 and sorted_list[0] > 1:
                    return 1
                else:
                    return sorted_list[start_index]+1
        else:
            return 1

sol = Solution()
print(sol.firstMissingPositive([-1,-3]))