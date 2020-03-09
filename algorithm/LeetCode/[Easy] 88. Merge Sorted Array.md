88. Merge Sorted Array

Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array.

**Note:**

* The number of elements initialized in `nums1` and `nums2` are `m` and `n` respectively.
* You may assume that nums1 has enough space (size that is greater or equal to `m + n`) to hold additional elements from `nums2`.

**Example:**
```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 24 ms
Memory Usage: N/A
```
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1.sort()
```

**Solution 2: (Two Pointers)**
```
Runtime: 56 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i = j = 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i < m: 
            res.append(nums1[i])
            i+=1
        while j < n: 
            res.append(nums2[j])
            j+=1
        
        for i in range(len(res)):
            nums1[i] = res[i]
```