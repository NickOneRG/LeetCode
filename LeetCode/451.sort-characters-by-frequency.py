from TestTime import TimeSet
from typing import List
from collections import defaultdict, Counter
t = TimeSet()
#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start


class Solution:  # First Approaches  ==> good running time
    def frequencySort(self, s: str) -> str:
        group = dict()

        for key, val in Counter(s).items():
            if val not in group:
                group[val] = [key]
            else:
                group[val].append(key)

        res = ""
        for key in sorted(group.keys(), reverse=True):
            for val in sorted(group[key]):
                res += val * key

        return res

        
class Solution:  # Second Approaches  ==> using sort in place, defaultdict and range 
    def frequencySort(self, s: str) -> str:
        memo, group = Counter(s), defaultdict(list)

        for key in memo.keys():
            group[memo[key]].append(key)

        memo = list(group.keys())
        memo.sort()

        res = ""
        for i in range(len(memo)-1, -1, -1):
            for val in sorted(group[memo[i]]):
                
                res += val * memo[i]

        return res
    

class Solution:  # Third Approaches  ==> one liner, + testing "most_common" built in methods
    def frequencySort(self, s: str) -> str:

        return "".join(key * val for key, val in Counter(s).most_common())



# @lc code=end


m = Solution()
time = t.hisobla()
print(m.frequencySort("cccaaa"))
# print(call)
print(t.hisobla(time, 1))