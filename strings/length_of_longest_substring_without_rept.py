class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        start, max_value = 0,0
        for i,j in enumerate(s):
            if j not in used.keys() and start<=i :
                used[j] = i
                max_value = max(max_value, i-start+1)
            else:
                start = used[j]+1
                used[j] = i

        return max_value



sol = Solution()
test_strs = ['abcabcbb','pwwkew','bbbbb', 'dvdf','bbtablud'] #'abcabcbb','pwwkew','bbbbb', 'dvdf
for i in test_strs:
    print(sol.lengthOfLongestSubstring(i))