2098. Subsequence of Size K With the Largest Even Sum

You are given an integer array `nums` and an integer `k`. Find the **largest even sum** of any subsequence of nums that has a length of `k`.

Return this sum, or `-1` if such a sum does not exist.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

**Example 1:**
```
Input: nums = [4,1,5,3,1], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,5,3]. It has a sum of 4 + 5 + 3 = 12.
```

**Example 2:**
```
Input: nums = [4,6,2], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,6,2]. It has a sum of 4 + 6 + 2 = 12.
```

**Example 3:**
```
Input: nums = [1,3,5], k = 1
Output: -1
Explanation:
No subsequence of nums with length 1 has an even sum.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^5`
* `1 <= k <= nums.length`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 624 ms
Memory Usage: 28.4 MB
```
```python
# Approach 1: 
# Time: O(nlogn)
# Space:O(n)

# Algorithm:
# First, get the sum of top k largest numbers res.
# If res is even, just return it.
# Otherwise, res is odd and we just need to change one number, that is, replace an odd number by an even number or vise versa. More specifically:
# replace the smallest even number from res by the largest odd number from the rest of the array, or
# replace the smallest odd number from res by the largest even number from the rest of the array.

class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        topkSum = sum(nums[:k])

        if topkSum % 2 == 0: 
            return topkSum

        minOdd = minEven = float('inf')

        for i in range(k):
            if nums[i] % 2 == 1:
                minOdd = min(minOdd, nums[i])
            else:
                minEven = min(minEven, nums[i])

        ret = -1
        for i in range(k,n):
            if nums[i] % 2 == 1 and minEven != float('inf'):
                ret = max(ret, topkSum + nums[i] - minEven)
            if nums[i] % 2 == 0 and minOdd != float('inf'):
                ret = max(ret, topkSum + nums[i] - minOdd)

        return ret
```
