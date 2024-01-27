

# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        
        if 4 > len(s) or len(s) > 12:
            return False
        if int(s[0:2]) > 256:
            

# @lc code=end


m = Solution()
print(m.restoreIpAddresses(input()))