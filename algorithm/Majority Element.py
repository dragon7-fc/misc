""" 
Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


""" Solution1: 60 ms """
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        threshold = n // 2
        dict = collections.defaultdict(list)
        for i in range(n):
            dict[nums[i]].append(nums[i])
        for key in dict.keys():
            if len(dict[key]) > threshold:
                return key


""" Solution2: 48 ms """
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]