from TestTime import TimeSet
from typing import List
t = TimeSet()
##
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
# @lc code=start
class NestedIterator:
    def __init__(self, nestedList: []):
        self.left, self.current = [], 0

        def flatten(nums):
            for i in nums:
                if i.isInteger():   self.left += [i]
                else:               flatten(i.getList())
        
        flatten(nestedList)
    
    def next(self) -> int:
        self.current += 1
        return self.left[self.current-1]
    
    def hasNext(self) -> bool:
         return self.current < len(self.left)
    


# @lc code=end

m = NestedIterator( [[1,1],2,[1,1]])
time = t.hisobla()
print(m.next())
# print(m.hasNext())
# print(call)  
print(t.hisobla(time,1))