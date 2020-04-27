1218. Longest Arithmetic Subsequence of Given Difference

Given an integer array `arr` and an integer `difference`, return the length of the longest subsequence in `arr` which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals `difference`.

**Example 1:**
```
Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
```

**Example 2:**
```
Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
```

**Example 3:**
```
Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `-10^4 <= arr[i], difference <= 10^4`

# Submissions
---
**Solution 1: (DP Bottom-Up, Hash Table)**
```
Runtime: 736 ms
Memory Usage: 27.1 MB
```
```python
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = {}  # {end with num arithematic subsequence: count}
        res = float('-inf')
        for num in arr:
            count = 1
            if num - difference in dic:
                count += dic[num - difference]

            if num in dic:
                dic[num] = max(dic[num], count)
            else:
                dic[num] = count

            res = max(res, dic[num])
    
        return res
```