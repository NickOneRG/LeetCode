from TestTime import TimeSet
from typing import List
from collections import Counter
t = TimeSet()
#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#

# @lc code=start
class Solution: # my code 
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        res = [[] for _ in range(l)]
        
        l, ind = len(nums)//3, 0

        for i in range(l):
            res[i] = nums[ind: ind+3]
            
            if res[i][2] - res[i][0] > k: 
                return []

            ind += 3

        return res


class Solution:  # sombody from leetcode , good use of slicing
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()     

        if max(i-j for i, j in zip(nums[2::3],nums[::3])) > k: return []
            
        return zip(nums[::3],nums[1::3],nums[2::3])

        '''
        :: is used for slicing sequences such as lists or strings. 
        The syntax for slicing is [start:stop:step]. 
        If start is not provided, it defaults to the beginning of the sequence. 
        If stop is not provided, it defaults to the end of the sequence. 
        If step is not provided, it defaults to 1.

        nums[::3] means “take every third element from nums, starting from the first element”. 
        Similarly, nums[1::3] means “take every third element from nums, 
        starting from the second element”, 
        and nums[2::3] means “take every third element from nums, 
        starting from the third element”.

        So, if nums is [0, 1, 2, 3, 4, 5, 6, 7, 8], then nums[::3] would be [0, 3, 6], 
        nums[1::3] would be [1, 4, 7], and nums[2::3] would be [2, 5, 8].
        '''

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.divideArray([15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2], 2))
# print(call)
print(t.hisobla(time, 1))