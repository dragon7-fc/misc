""" 
Binary Search

iven a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

"""


""" Solution1: 68 ms """
return nums.index(target) if target in nums else -1


""" Solution2: 60 ms """
class Solution:
    __index = 0
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        return -1


""" Solution3: 60 ms """
class Solution:
    __index = 0
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


''' Solution4: 48 ms '''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        high = len(nums)
        low = 0
        guess = int((high+low)/2)
        while low!=high:
            if nums[guess]>target:
                high = guess
            elif nums[guess] < target:
                low = guess
            else:
                return guess
            guess = int((high + low)/2)
        return guess