#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
from typing import List
class Solution:
    def binary_search(self, low: int, high: int, target: int, mountainArr: 'MountainArray', reversed: bool) -> int:
        """
        Perform a binary search on the MountainArray.   

        Parameters:
            low (int): The lower bound of the search.
            high (int): The upper bound of the search.
            target (int): The target value to search for.
            mountainArr (MountainArray): The MountainArray to search.
            reversed (bool): Whether the MountainArray is reversed.  

        Returns:
            int: The index of the target in the MountainArray, or -1 if it is not found.
        """
        while low != high:
            mid = low + (high - low) // 2
            if reversed:
                if mountainArr.get(mid) > target:
                    low = mid + 1 
                else:
                    high = mid  
            else:
                if mountainArr.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid 
        return low  
     
    def find_peak_index(self, low, high, mountainArr):
        while low != high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1 
            else:
                high = mid 
        return low 
     
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        peak_index = self.find_peak_index(1, length - 2, mountain_arr)
        increasing_index = self.binary_search(0, peak_index, target, mountain_arr, False)
        if mountain_arr.get(increasing_index) == target:
            return increasing_index  
        decreasing_index = self.binary_search(peak_index + 1, length - 1, target, mountain_arr, True)
        if mountain_arr.get(decreasing_index) == target:
            return decreasing_index 

        return -1 
 
# @lc code=end

