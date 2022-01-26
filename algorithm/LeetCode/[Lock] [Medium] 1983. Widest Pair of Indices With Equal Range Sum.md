1983. Widest Pair of Indices With Equal Range Sum

You are given two **0-indexed** binary arrays `nums1` and `nums2`. Find the **widest** pair of indices `(i, j)` such that `i <= j` and `nums1[i] + nums1[i+1] + ... + nums1[j] == nums2[i] + nums2[i+1] + ... + nums2[j]`.

The widest pair of indices is the pair with the **largest distance** between `i` and `j`. The **distance** between a pair of indices is defined as `j - i + 1`.

Return the **distance** of the **widest** pair of indices. If no pair of indices meets the conditions, return `0`.

 

**Example 1:**
```
Input: nums1 = [1,1,0,1], nums2 = [0,1,1,0]
Output: 3
Explanation:
If i = 1 and j = 3:
nums1[1] + nums1[2] + nums1[3] = 1 + 0 + 1 = 2.
nums2[1] + nums2[2] + nums2[3] = 1 + 1 + 0 = 2.
The distance between i and j is j - i + 1 = 3 - 1 + 1 = 3.
```

**Example 2:**
```
Input: nums1 = [0,1], nums2 = [1,1]
Output: 1
Explanation:
If i = 1 and j = 1:
nums1[1] = 1.
nums2[1] = 1.
The distance between i and j is j - i + 1 = 1 - 1 + 1 = 1.
```

**Example 3:**
```
Input: nums1 = [0], nums2 = [1]
Output: 0
Explanation:
There are no pairs of indices that meet the requirements.
```

**Constraints:**

* `n == nums1.length == nums2.length`
* `1 <= n <= 10^5`
* `nums1[i]` is either `0` or `1`.
* `nums2[i]` is either `0` or `1`.

# Submissions
---
**Solution 1: (Prefix Sum, Hash Table)**
```
Runtime: 2867 ms
Memory Usage: 34 MB
```
```python
class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        diff_prefix = {}
        diff_prefix[0] = -1
        n1_running_sum, n2_running_sum = 0, 0
        max_distance = 0
        for index,(n1,n2) in enumerate(zip(nums1,nums2)):
            n1_running_sum, n2_running_sum = n1_running_sum + n1, n2_running_sum + n2
            diff = n1_running_sum - n2_running_sum
            if diff in diff_prefix:
                max_distance = max(max_distance, index - diff_prefix[diff])
            else:
                diff_prefix[diff] = index
        
        return max_distance
```
