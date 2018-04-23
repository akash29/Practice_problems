class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)>0:
            end_pos = len(nums) - 1
            end_pos_2 = len(nums) - 2
            while end_pos_2 >= 0:
                end_val = nums[end_pos]
                end_val_2 = nums[end_pos_2]
                if end_val_2 < end_val:
                    min_index = max([i for i in range(end_pos,len(nums)) if nums[i] > end_val_2])
                    temp = nums[min_index]
                    nums[min_index] = end_val_2
                    nums[end_pos_2] = temp
                    start_index = end_pos
                    end_index = len(nums)-1
                    while end_index>=start_index:
                        temp = nums[start_index]
                        nums[start_index] = nums[end_index]
                        nums[end_index] = temp
                        start_index +=1
                        end_index-=1
                    print(nums)
                    break
                end_pos-=1
                end_pos_2-=1
            else:
                start_index = end_pos
                end_index = len(nums) - 1
                while end_index >= start_index:
                    temp = nums[start_index]
                    nums[start_index] = nums[end_index]
                    nums[end_index] = temp
                    start_index += 1
                    end_index -= 1
                print (nums)
        else:
            print (nums)

sol = Solution()
sol.nextPermutation([3,2,1])