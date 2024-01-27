#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: [], list2: []) -> []:
        # li = []
        # for i in range(max(len(list1),len(list2))):
        #     li.append(list1[i])
        #     li.append(list2[i])
        list1.extend(list2)
        return sorted(list1)
# @lc code=end

m = Solution()
print(m.mergeTwoLists([1,2,4],[1,3,4]))