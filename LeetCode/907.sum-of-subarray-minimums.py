from collections import Counter
import bisect
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res, MOD = 0, 10 ** 9 + 7

        for i in range((l := len(arr))-1):
            
            res += (memo := min(arr[: i +2]))
            for finish in range(i +2, l):
                res += min(memo, arr[finish])
                print(arr[finish], memo)

            res %= MOD

        return res + sum(arr)
    

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res, stack = [0] * (l := len(arr := [0] + arr)), [0]

        for i in range(l):
            while arr[stack[-1]] > arr[i]: stack.pop()
                
            res[i] = res[(point := stack[-1])] + (i- point) * arr[i]
            stack.append(i)

        return sum(res) % (10**9 + 7)

        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.sumSubarrayMins([3, 1, 2, 4]))
# print(call)
print(t.hisobla(time, 1))


def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

