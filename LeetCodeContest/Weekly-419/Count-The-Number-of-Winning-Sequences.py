from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n - k + 1):
            freq = {}
            for num in nums[i:i + k]:
                freq[num] = freq.get(num, 0) + 1

            freq_list = [(num, freq) for num, freq in freq.items()]

            freq_list.sort(key=lambda x: (-x[1], -x[0]))

            res.append(sum(num * freq for num, freq in freq_list[:x]))

        return res



m = Solution()
print(m.findXSum([1,1,2,2,3,4,2,3], 6, 2))  # nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
