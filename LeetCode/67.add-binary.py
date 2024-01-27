#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m_len = max(len(a), len(b))

        a = a.zfill(m_len)
        b = b.zfill(m_len)

        res = ''
        carry = 0

        for i in range(m_len-1, -1, -1):
            b_sum = carry
            b_sum += 1 if a[i] == '1' else 0
            b_sum += 1 if b[i] == '1' else 0

            carry = 1 if b_sum >= 2 else 0
            res = ('1' if b_sum % 2 == 1 else '0') + res

        if carry != 0 : 
            res = '1' + res

        return res.zfill(m_len)
# @lc code=end


m = Solution()
print(m.addBinary("11","1"))
