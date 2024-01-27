from TestTime import TimeSet
t = TimeSet()
#
# @lc app=leetcode id=2038 lang=python3
#
# [2038] Remove Colored Pieces if Both Neighbors are the Same Color
colors = "AAABABB"

# @lc code=start
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        return sum([len(a) - 2 for a in colors.split('B') if len(a) > 2]) > sum([len(b) - 2 for b in colors.split('A') if len(b) > 2])

        

# @lc code=end

time = t.hisobla()

m = Solution()
print(m.winnerOfGame("AAAABBBBBBAAA"))

print(t.hisobla(time,1))


# class Solution:
#     def winnerOfGame(self, colors: str) -> bool:
#         len_color = len(colors)
#         if len_color < 3:
#             return False
#         elif len_color < 4 and colors[1] == "A":
#             return True
#         elif len_color < 4 and colors[1] == "B":
#             return False
#         colors = list(colors)
#         a = colors.count("A")
#         b = colors.count("B")
#         for i in range((len_color-1)):
#             jo = "".join(colors)
#             if "AAA" in jo:
#                 colors.remove("A")
#             else:
#                 return False
            
#             if "BBB" in jo:
#                 colors.remove("B")
#             else:
#                 return True