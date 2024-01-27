#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        n = len(digits) - 1
        while n >= 0:
            if digits[n] == 9:
                digits[n] = 0
                n -= 1
            else:
                digits[n] += 1
                return digits
        return [1] + digits


# @lc code=end
# class Solution:
#     def plusOne(self, digits: [int]) -> [int]:
#         def rec(n):
#             if n < 0:
#                 digits.insert(0, 1)
#             else:
#                 j = digits[n] + 1
#                 if j == 10:
#                     digits[n] = 0
#                     rec(n-1)
#                 else:
#                     digits[n] = j
#         rec(len(digits)-1)
#         return digits
m = Solution()
print(m.plusOne([4,3,9,9]))