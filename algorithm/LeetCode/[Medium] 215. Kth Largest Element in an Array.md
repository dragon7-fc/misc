215. Kth Largest Element in an Array

Find the `k`th largest element in an unsorted array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

**Example 1:**
```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:**
```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note:**

* You may assume `k` is always valid, `1 ≤ k ≤ array's length`.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 44 ms
Memory Usage: N/A
```
```python
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]
```

**Solution 2: (Heap)**
```
Runtime: 48 ms
Memory Usage: N/A
```
```python
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
```

**Solution 3: (Divide and Conquer, Quick sort)**
```
Runtime: 2056 ms
Memory Usage: 115.1 MB
```
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[k-1]
        b = 0
        a = nums[-1]
        for i in range( len(nums)-1):
            if nums[i] < a:
                nums[i], nums[b] = nums[b], nums[i]
                b += 1
        nums[-1], nums[b] = nums[b], nums[-1]
        if len(nums)-b == k:
            return nums[b]
        elif k > len(nums)-b:
            return self.findKthLargest(nums[:b], k-len(nums)+b)
        else:
            return self.findKthLargest(nums[b+1:], k)
```