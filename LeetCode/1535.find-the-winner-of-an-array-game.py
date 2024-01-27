from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1535 lang=python3
#
# [1535] Find the Winner of an Array Game
#

# @lc code=start   
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        res, win = arr[0], 0
        for i in range(1, len(arr)):
            if res < arr[i]: res, win = arr[i], 0
            win += 1
            if win == k: return res        
        return res

            
# @lc code=end

if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.getWinner([3,2,1], 0))
    # print(call)  
    print(t.hisobla(time,1))
    
# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:
#         if len(arr) < k: return max(arr)
#         memo = dict()
#         for _ in range(2):
#             for _ in arr:
#                 arr0, arr1 = arr[0], arr[1]

#                 if arr0 < arr1:
#                     memo[arr1] = (memo[arr1] + 1) if arr1 in memo else 1
#                     arr.append(arr.pop(0))

#                 else:
#                     memo[arr0] = (memo[arr0] + 1) if arr0 in memo else 1
#                     arr.append(arr.pop(1))
        
#         for key, value in memo.items():
#             if value == k :
#                 return key
#         return max(memo, key=memo.get)
# 
# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:
#         if len(arr) <= k: return max(arr)
#         cou, res = 0, arr[0]
        
#         for x in arr[1:]:
#             if x > res: res, cou = x, 1
#             else:       cou += 1
                
#             if cou == k: break
#         return res