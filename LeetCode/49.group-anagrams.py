from TestTime import TimeSet
from typing import List
from collections import defaultdict
t = TimeSet()
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        memo = defaultdict(list)

        for s in strs:
            memo["".join(sorted(s))].append(s)

        return list(memo.values())
    
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(call)
print(t.hisobla(time, 1))
