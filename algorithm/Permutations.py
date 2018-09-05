""" 
Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


""" Solution: 68 ms """
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def swap(i, j, nums):
            new_nums = list(nums)
            new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
            return new_nums