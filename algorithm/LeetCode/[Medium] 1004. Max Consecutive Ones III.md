1004. Max Consecutive Ones III

Given an array `A` of `0`s and `1`s, we may change up to `K` values from `0` to `1`.

Return the length of the longest (contiguous) subarray that contains only `1`s. 

 

**Example 1:**
```
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

**Example 2:**
```
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

**Note:**

* `1 <= A.length <= 20000`
* `0 <= K <= A.length`
* `A[i]` is `0` or `1`

# Submissions
---
**Solution 1: (Greedy, Two Pointers)**
```
Runtime: 760 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeroes = 0
        left, right = 0, 0
        ans = 0
        while right < len(A):
            if A[right] == 0:
                zeroes += 1
            while zeroes > K:
                if A[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans
```