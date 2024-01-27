#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#[29,51,87,87,72,12]

# @lc code=start
class Solution:
    def candy(self, ratings):
        sana = 0
        d = 1
        for z in range(1, len(ratings)-1):
            
            if  ratings[z] < ratings[z +1] and ratings[z] < ratings[z -1] :
                sana += 1
                d = 1
            elif ratings[z] == ratings[z +1] and ratings[z] == ratings[z -1]:
                sana += 1
                d = 1

            elif ratings[z] <= ratings[z +1] and ratings[z] > ratings[z -1]:
                d += 1
                sana += d

            elif ratings[z] > ratings[z +1] and ratings[z] >= ratings[z -1]:
                sana += d

            elif  ratings[z] > ratings[z +1] or ratings[z] > ratings[z -1] :
                d -= 1
                sana += d
            else:
                
                sana += d
                

        if ratings[0] > ratings[1]:
            sana += 2
        else:
            sana += 1

        if ratings[len(ratings)-1] > ratings[len(ratings)-2]:
            sana += 2
        
        else:
            sana += 1

        return sana
# @lc code=end

r = list(map(int, input().split()))
m = Solution()
print(m.candy(r))

