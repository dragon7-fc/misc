""" 
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


""" Solution1: 80 ms """
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        nxt = -1
        while i+1 < n:
            if nums[i] == 0 and nums[i+1] != 0:
                nxt += 1
                nums[nxt] = nums[i+1]
                nums[i+1] = 0
            elif nums[i] != 0:
                nxt += 1
            i += 1



""" Solution2: 48 ms """
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        nxt = 0
        while i < n:
            if nums[i] != 0:
                tmp = nums[nxt]
                nums[nxt] = nums[i]
                nums[i] = tmp
                nxt += 1
            i += 1