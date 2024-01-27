#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: [int]) -> bool:
        n = len(nums)
        m_l = nums[:]
        for i in range(1, n):
            m_l[i] = min(m_l[i - 1], nums[i])
        st = []
        for j in range(n - 1, -1, -1):
            if nums[j] > m_l[j]:
                while st and st[-1] <= m_l[j]:
                    st.pop()
                if st and st[-1] < nums[j]:
                    return True
                st.append(nums[j])
        return False

# @lc code=end

# class Solution:  # Usul - 1
#     def find132pattern(self, nums: [int]) -> bool:
#         n = len(nums)
#         for i in range(n-2):
#             for j in range(i+1, n-1):
#                 for k in range(j+1, n):
#                     if nums[k] < nums[j] and nums[k] > nums[i] and nums[j] > nums[i]:
#                         return True
#         return False

# class Solution:   #  Usul - 2
#     def find132pattern(self, nums: [int]) -> bool:
#         b = [] 
#         mn = float('inf')
#         for i in nums:
#             mn = min(i, mn)
#             b.append(mn)
    
#         st = []
#         for i in range(len(nums)-1, 0, -1):
#             while st and st[-1] <= b[i-1]:
#                 st.pop()
#             if st and st[-1] > b[i-1] and nums[i] > st[-1]:
#                 return True
#             else:
#                 st.append(nums[i])
#         return False

m = Solution()
print(m.find132pattern([1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0]))

