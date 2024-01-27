from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
class Solution: # my code 
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winn, lose = zip(*matches)
        lose_set = set(lose)

        no_lose = {win for win in winn if win not in lose_set}

        one_lose = [los for los, count in Counter(lose).items() if count == 1]

        return [sorted(no_lose), sorted(one_lose)]
    

class Solution:  # not my code from shubham_1307
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_loss = set()
        
        for winner, loser in matches:
            if (winner not in one_loss) and (winner not in more_loss):
                zero_loss.add(winner)

            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_loss.add(loser)
            elif loser in more_loss:
                continue
            else:
                one_loss.add(loser)          
            
        return [sorted(list(zero_loss)), sorted(list(one_loss))]
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
# print(call)
print(t.hisobla(time, 1))


class Solution: # working but hitt the time limit
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winn, lose = zip(*matches)

        no_lose = dict()
        for win in winn:
            if win not in lose: no_lose[win] = 0

        one_lose = [los for los, count in Counter(lose).items() if count == 1]

        return [sorted(list(no_lose.keys())), sorted(one_lose)]



