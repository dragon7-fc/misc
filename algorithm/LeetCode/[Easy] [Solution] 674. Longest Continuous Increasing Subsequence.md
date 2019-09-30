674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest `continuous` increasing subsequence (subarray).

**Example 1:**
```
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
```

**Example 2:**
```
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
```
**Note:** Length of the array will not exceed 10,000.

# Solution
---
## Approach #1: Sliding Window [Accepted]
**Intuition and Algorithm**

Every (continuous) increasing subsequence is disjoint, and the boundary of each such subsequence occurs whenever `nums[i-1] >= nums[i]`. When it does, it marks the start of a new increasing subsequence at `nums[i]`, and we store such `i` in the variable `anchor`.

For example, if `nums = [7, 8, 9, 1, 2, 3]`, then `anchor` starts at 0 `(nums[anchor] = 7)` and gets set again to anchor = 3 `(nums[anchor] = 1)`. Regardless of the value of anchor, we record a candidate answer of `i - anchor + 1`, the length of the subarray `nums[anchor], nums[anchor+1], ..., nums[i]`; and our answer gets updated appropriately.

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of nums. We perform one loop through nums.

* Space Complexity: $O(1)$, the space used by anchor and ans.

# Submissions
---
**Solution:**
```
Runtime: 92 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
```
