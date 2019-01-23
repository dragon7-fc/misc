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
        ans = set()
        n = len(nums)
        ans.add(tuple(nums))
        for i in range(n):
            for j in range(n):
                if j != i:
                    tmp_list = nums
                    tmp = tmp_list[i]
                    tmp_list[i] = tmp_list[j]
                    tmp_list[j] = tmp
                    ans.add(tuple(tmp_list))
        return [l for l in ans]