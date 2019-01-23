""" 
Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


""" Solution: 44 ms """
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(nums==[]):
            return [[]]
        allSubsets=[]
        for subset in self.subsets(nums[1:]):
            allSubsets+=[subset]
            allSubsets+=[[nums[0]]+subset]
        return allSubsets