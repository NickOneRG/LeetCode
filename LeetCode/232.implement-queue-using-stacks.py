from TestTime import TimeSet
from typing import List

t = TimeSet()

# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.one = []

    def push(self, x: int) -> None:
        self.one.append(x)

    def pop(self) -> int:
        return self.one.pop(0)

    def peek(self) -> int:
        return self.one[0]

    def empty(self) -> bool:
        return not self.one


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


