#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
class Solution:
    def minOperations(self, nums: [int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        maxi = -1
        left = 0
        current = 0

        for right in range(n):
            current += nums[right]
            while current > total - x and left < n:
                current -= nums[left]
                left += 1
            if current == total - x:
                maxi = max(maxi, right - left + 1)

        return n - maxi if maxi != -1 else -1


# @lc code=end

# class Solution:
#     def minOperations(self, nums: [int], x: int) -> int:
#             li = []
#             il = []
#             res = []
#             if sum(nums) < x:
#                  return -1
#             for i in range(1, len(nums) + 1):
#                 subarray = nums[0:i]
#                 li.append(subarray)
#                 subarrays = nums[::-1][0:i]
#                 il.append(subarrays)
            

#             for z in range(len(li)):
#                 if sum(li[z]) == x:
#                     res.append(len(li[z]))
#                 if sum(il[z]) == x:
#                     res.append(len(il[z]))
#                 for i in list(il):
#                     if sum(i)+sum(li[z]) == x:
#                         res.append(len(i)+len(li[z]))

            

                 
#             return min(res) if res != []  else -1
m = Solution()
l = [5,2,3,1,1]
print(m.minOperations( l, 5))