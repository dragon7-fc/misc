1300. Sum of Mutated Array Closest to Target

Given an integer array `arr` and a target value `target`, return the integer `value` such that when we change all the integers larger than `value` in the given array to be equal to `value`, the sum of the array gets as close as possible (in absolute difference) to `target`.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from `arr`.

 

**Example 1:**
```
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
```

**Example 2:**
```
Input: arr = [2,3,5], target = 10
Output: 5
```

**Example 3:**
```
Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
```

**Constraints:**

* `1 <= arr.length <= 10^4`
* `1 <= arr[i], target <= 10^5`

# Submissions
---
**Solution 1:**
```
Runtime: 112 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def getSum(val):
            total = 0
            for i in range(n):
                total += arr[i] if arr[i] <= val else val
            return total

        lo, hi, n = 0, max(arr), len(arr)
        diff = collections.defaultdict(set)
        while lo <= hi:
            mi = (lo+hi) // 2
            total = getSum(mi)
            # store the absolute differences
            diff[abs(total - target)].add(mi)
            if total < target:
                lo = mi + 1
            elif total > target:
                hi = mi - 1
            else:
                break

        # Find the lowest diff
        cand = diff[sorted(diff.keys())[0]]
        
        # Return the minimum value among candidates
        return sorted(cand)[0]
```