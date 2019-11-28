def majorityElement(nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 0
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2)
                    if nums.count(n) > len(nums) // 3]

test_arr = [1,1,1,3,3,2,2,2]
# test_arr = [3,2,3]
# test_arr = [2,2,1,1,1,2,2]
majorityElement(test_arr)