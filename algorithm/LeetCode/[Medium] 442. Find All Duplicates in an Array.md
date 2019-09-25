442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it without extra space and in O(n) runtime?

**Example:**
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```

# Submissions
---
**Solution**
```
Runtime: 440 ms
Memory Usage: 21.6 MB
```
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                ans.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return ans
```
