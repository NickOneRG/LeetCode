from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        
        def mixer(r, c):
            total, count = 0, 0

            top, bottom = max(0, r - 1), min(rows, r + 2)
            left, right = max(0, c - 1), min(cols, c + 2)

            for row in range(top, bottom):
                for col in range(left, right):
                    total += img[row][col]
                    count += 1

            return total // count

        return [[mixer(r, c) for c in range(cols)] for r in range(rows)]
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
# print(call)
print(t.hisobla(time, 1))

# class Solution:
#     def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
#         # column = list(zip(*img))

#         # print(column[0][0])
#         def mixer(i, z):
            



#         for i in range(len(img)):
#             for z in range(len(img[i])):
#                 img[i][z] = mixer(i,z)