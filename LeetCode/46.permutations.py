#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        
        res = []
        if len(nums) == 0:
            return res
        elif len(nums) == 1:
            return [nums]
        else:
            for i in range(len(nums)):
                n = nums.pop(i)
                perms = self.permute(nums)
                for perm in perms:
                    res.append([n] + perm)
                nums.insert(i, n)
        return res



# @lc code=end

m = Solution()
print(m.permute(list(map(int, input().split()))))

from itertools import combinations

lst = [0, 3, 4,7]
result = list(combinations(lst, 2))

print(result)
