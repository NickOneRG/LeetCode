

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # res, memo = len(s), ord(s[0])

        # for char in s:
        #     dif = memo - (check := ord(char))
        #     dif = dif if dif > 0 else dif * -1

        #     if dif <= k: memo = check
        #     else:        res -= 1
                
        # return res 
    

        memo = [0] * 128
        
        for char in s:
            check = ord(char)
            memo[check] = max(memo[check - k: check + k + 1]) + 1

        return max(memo)


m = Solution()
print(m.longestIdealString("acfgbd", 2))
