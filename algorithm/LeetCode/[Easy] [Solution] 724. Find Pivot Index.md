724. Find Pivot Index

Given an array of integers `nums`, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

**Example 1:**
```
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
``` 

**Example 2:**
```
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
```

**Note:**

* The length of nums will be in the range [0, 10000]`.
* Each element `nums[i]` will be an integer in the range `[-1000, 1000]`.

# Solution
---
## Approach #1: Prefix Sum [Accepted]
**Intuition and Algorithm**

We need to quickly compute the sum of values to the left and the right of every index.

Let's say we knew `S` as the sum of the numbers, and we are at index `i`. If we knew the sum of numbers `leftsum` that are to the left of index `i`, then the other sum to the right of the index would just be `S - nums[i] - leftsum`.

As such, we only need to know about `leftsum` to check whether an index is a pivot index in constant time. Let's do that: as we iterate through candidate indexes `i`, we will maintain the correct value of `leftsum`.

```python
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `nums`.

* Space Complexity: $O(1)$, the space used by `leftsum` and `S`.

# Submissions
---
**Solution**
```
Runtime: 176 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
```