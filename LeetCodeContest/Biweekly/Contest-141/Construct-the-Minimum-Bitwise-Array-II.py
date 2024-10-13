from typing import List




class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            num = nums[i]
            miniAns = float('inf')
            check = False

            for bit in range(31):
                if (num >> bit) & 1 == 1:
                    memo = num & ~(1 << bit)
                    if memo < 0:
                        continue
                    if (memo | (memo +1)) == num:
                        if memo < miniAns:
                            miniAns = memo
                            check = True
            
            ans[i] = miniAns if check else -1

        return ans
    


m = Solution()
print(m.minBitwiseArray([2, 3,5,7]))