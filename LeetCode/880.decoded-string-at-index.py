#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
  def decodeAtIndex(self, S: str, K: int) -> str:
    size = 0
    for c in S:
      if c.isdigit():
        size *= int(c)
      else:
        size += 1

    for i in range(len(S) - 1, -1, -1):
      char = S[i]
      if char.isdigit():
        size /= int(char)
        K %= size
      else:
        if K % size == 0 or K == size:
          return char
        size -= 1



# @lc code=end

m = Solution()
print(m.decodeAtIndex("ixm5xmgo78", 711))