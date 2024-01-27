from TestTime import TimeSet
from typing import List
t = TimeSet()




class Solution:
    def minCommon(self,n: int, data: List[int]) -> List[int]:
        res, count = [], 1

        for i in range(n):
            memo = []
            for z in range(n - i):
                memo.append(data[z:z + count])

            memo_set = [set(lst) for lst in memo]
            common   = list(set.intersection(*memo_set))

            if   common == []:     res.append(-1)
            elif len(common) == 1: res.append(common[0])
            else:                  res.append(min(common))

            count     += 1

            # print(*memo)

        return res
    

if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.minCommon(5, [4,3,3,4,2]))
    # print(call)  
    print(t.hisobla(time,1))


class Solution:
    def minCommon(self, n: int, data: List[int]) -> List[int]:
        res, count = [], 1

        for i in range(n):
            count, memo = i + 1, []
             
            for z in range(0, len(data) - count + 1):
                memo.append(data[z:z + count])

            memo_set = [set(lst) for lst in memo]
            common = list(set.intersection(*memo_set))

            if   common == []:     res.append(-1) 
            elif len(common) == 1: res.append(common[0])
            else:                  res.append(min(common))
                

        return res
    

if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.minCommon(5, [4,3,3,4,2]))
    # print(call)  
    print(t.hisobla(time,1))


import collections
class Solution:
    def minCommon(self,n: int, arr: List[int]) -> List[int]:

        idx=collections.defaultdict(list)

        for i,j in enumerate(arr):
            idx[j]+=[i]

        res=[float('inf')]*n

        for num in idx:
            x=[-1]+idx[num]+[n]
            y=max(j-i for i,j in zip(x[:-1],x[1:]))
            res[y-1]=min(res[y-1],num)

        for i in range(1,n):
           res[i]=min(res[i],res[i-1])     

        return res
    
if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.minCommon(5, [4,3,3,4,2]))
    # print(call)  
    print(t.hisobla(time,1))



from collections import defaultdict

class Solution:
    def minCommon(self, n: int, data: List[int]) -> List[int]:
        idx = defaultdict(list)
        for i, num in enumerate(data):
            idx[num].append(i)
        
        res = [float('inf')] * n
        for num in idx:
            indices = [-1] + idx[num] + [n]
            max_gap = max(j - i for i, j in zip(indices, indices[1:]))
            if max_gap <= n:
                res[max_gap - 1] = min(res[max_gap - 1], num)
        
        for i in range(1, n):
            res[i] = min(res[i], res[i - 1])
        
        return [-1 if num == float('inf') else num for num in res]
    
    
if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.minCommon(5, [4,3,3,4,2]))
    # print(call)  
    print(t.hisobla(time,1))


class Solution:    # with memoization
    def minCommon(self, n: int, data: List[int]) -> List[int]:
        memo, res = {}, [float('inf')] * n

        for i, v in enumerate(data):
            if v not in memo: memo[v] = []
            memo[v].append(i)
        
        for num in memo:
            indices = [-1] + memo[num] + [n]
            max_gap = max(j - i    for i, j in zip(indices, indices[1:]))
            if max_gap <= n: res[max_gap - 1] = min(res[max_gap - 1], num)
                
        for i in range(1, n): res[i] = min(res[i], res[i - 1])
        
        return [-1 if num == float('inf') else num for num in res]


if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.minCommon(5, [4,3,3,4,2]))
    # print(call)  
    print(t.hisobla(time,1))