class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        temp_list = []
        start = 0
        sorted_cand = sorted(candidates)
        self.backtrack(sorted_cand, [], start, target, temp_list)
        print(temp_list)


    def backtrack(self, cand, temp_arr, index,target, initial):
        if target < 0:
            return
        elif target == 0:
            initial.append(temp_arr)
            return
        else:
            for i in range(index,len(cand)):
                if i > index and cand[i] == cand[i-1]:
                    continue
                self.backtrack(cand, temp_arr+[cand[i]], i, target - cand[i], initial)


sol = Solution()
sol.combinationSum([2,3,6,7],7)

