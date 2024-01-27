#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: [str]) -> int:
        i = 0
        count = 1
        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j - 1]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                count = 1
        return i


# @lc code=end

m = Solution()
print(m.compress(["a","a","b","b","c","c"]))