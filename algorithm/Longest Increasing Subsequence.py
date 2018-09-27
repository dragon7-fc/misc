""" 
Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""


""" Solution: 708 ms """
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            dp[i] = max([dp[x] for x in range(i) if nums[x] < nums[i]]+[0]) + 1
        return max(dp)


""" Solution2: 60 ms """
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def insert_num_into_sorted_sequence(sequence, target, i, j):  
            while i <= j:
                m = i + (j - i) // 2
                if sequence[m] < target:
                    i = m + 1
                elif sequence[m] > target:
                    j = m - 1
                else:
                    return sequence
            sequence[i] = target
            return sequence

        if not nums: return 0
        if len(nums) == 1: return 1
        sequence = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sequence[-1]:
                sequence.append(nums[i])
            else:
                insert_num_into_sorted_sequence(sequence, nums[i], 0, len(sequence))
        return len(sequence)