from TestTime import TimeSet
from typing import List
t = TimeSet()

#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#

# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        common = (set(nums1) & set(nums2))
        return -1 if common == set() else min(common)
  
# @lc code=end

if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.getCommon([1,2,3],[2]))
    # print(call)  
    print(t.hisobla(time,1))