from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
            
        res, memo = [""] * numRows, {0: 1, numRows -1: -1}
        index, count = 0, 1

        for i in s:
            res[index] += i
            count = memo.get(index, count)
            index += count

        return "".join(res)

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.convert("123456789", 3))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1: return s

#         res = [""] * numRows
#         num = (numRows * 2) - 2
#         count, count_rev = 0, numRows-1

#         if numRows == 2:
#             for i, v in enumerate(s):
#                 if i % 2 == 0:
#                     res[0] += v
#                 else:
#                     res[1] += v
#             return "".join(res)
        
#         for i in s:
#             if count == num:    count, count_rev = 0, numRows-1
#             if count < numRows: index = count
#             else: 
#                 count_rev -= 1
#                 index = count_rev
#             res[index] += i
#             count += 1

#         return "".join(res)












# CREATE TABLE lesson_table(
#   id bigserial PRIMARY KEY NOT NULL,
#   sience_id BIGINT REFERENCES sience(id),
#   teacher_id BIGINT REFERENCES teacher(id),
#   week_id BIGINT REFERENCES week(id),
#   group_id BIGINT REFERENCES school_group(id))