class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num)!=1:
            memo = 0
            for i in num:
                memo += int(i)
            num = str(memo)

        return int(num)
