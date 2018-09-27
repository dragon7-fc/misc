""" 
Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

"""


""" Solution: 1300 ms """
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (sum(nums) / 2.)  in possible_sums 


""" Solution2: 60 ms """
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        # Need to run with copy because .remove mutates the array.
        return any(self.dfs(num, nums.copy(), total_sum//2, 0) for num in nums)
        
    
    def dfs(self, num, nums, target, current_sum):
        current_sum += num
        if current_sum == target:
            return True
        elif current_sum > target:
            return False
        else:
            nums.remove(num)
            return any(self.dfs(num, nums, target, current_sum) for num in nums)