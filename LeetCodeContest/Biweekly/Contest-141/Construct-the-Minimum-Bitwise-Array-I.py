from typing import List



class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            for x in range(nums[i] + 1):
                if (x | (x + 1)) == nums[i]:
                    ans[i] = x
                    break

        return ans


m = Solution()
print(m.minBitwiseArray([2, 3,5,7]))