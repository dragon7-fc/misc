''' 
Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''


''' Solution1: 108 ms '''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums)
        tmp = 1
        ans[0] = tmp
        for i in range(len(nums)-1):
            tmp *= nums[i]
            ans[i+1] = tmp
        tmp = 1
        for i in range(len(nums)-1, 0, -1):
            tmp *= nums[i]
            ans[i-1] *= tmp
        return ans


''' Solution2: 104 ms '''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        p = 1
        for i in range(n):
            ans.append(p)
            p *= nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        return ans
        