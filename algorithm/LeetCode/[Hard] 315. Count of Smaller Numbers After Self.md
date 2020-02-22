315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

**Example:**
```
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 1228 ms
Memory Usage: 15.8 MB
```
```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        ans = [None] * len(nums)
        for i in range(len(nums)):
            j = arr.index(nums[i])
            ans[i] = j
            arr.pop(j)
        return ans

        # find nums[i]'s index in the arr in each loop.
        # think of this index as a rank, so there are j elements smaller than nums[i]
        # nums[i] is no longer useful for nums[i+1],nums[i+2].... Since we only need to consider the elements to the right
        # so pop out nums[i] from the arr, and start the next loop		
```

**Solution 2: (Binary Search)**
```
Runtime: 108 ms
Memory Usage: 15.9 MB
```
```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        sortedNums = [nums[-1]]
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums) -2, -1, -1):
            index = bisect.bisect_left(sortedNums, nums[i])
            ans[i] = index
            sortedNums.insert(index, nums[i])
        return ans
```