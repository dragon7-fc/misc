Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

Solution: (44 ms)
```python
class Solution:    
    # a method for finding the minimum index
    def findMinimumIndex(self, nums: List[int]):
        if len(nums) == 1:
            return 0

        l = 0
        r = len(nums) - 1

        if nums[0] < nums[r]:
            return 0

        while l <= r:
            mid = int((l+r)/2)

            if nums[mid+1] < nums[mid]:
                return mid+1
            elif nums[mid-1] > nums[mid]:
                return mid

            if nums[0] < nums[mid]:
                l = mid+1
            else:
                r = mid-1
                return -1

    # a method for binary search
    def binarySearch(self, nums: List[int], targe  t: int):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
                return -1
    
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1

        # find the index of the minimum
        minIndex = self.findMinimumIndex(nums)

        # using the minIndex, separate the nums into two lists
        leftNums = nums[0: minIndex]
        rightNums = nums[minIndex:]

        # after you split the nums, perform binary search of whichever half has the target

        # if found in left side, return index
        if self.binarySearch(leftNums, target) != -1:
            return self.binarySearch(leftNums, target)
        elif self.binarySearch(rightNums, target) != -1:i
            # if found in right side,   return minIndex + index
            return self.binarySearch(rightNums, target) + minIndex

        return -1
```
