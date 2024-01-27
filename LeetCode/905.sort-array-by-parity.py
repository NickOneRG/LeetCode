#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: [int]) -> [int]:
              
        return ([nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]) + ([nums[i] for i in range(len(nums)) if nums[i] % 2 != 0])
            
# @lc code=end
        # even, odd = [], []
         
        # for i in range(len(nums)):
        #     even.append(nums[i]) if nums[i] % 2 == 0 else odd.append(nums[i]) 
        # even.extend(odd)
        # return even
        # 
m = Solution()
print(m.sortArrayByParity([3,1,2,4]))