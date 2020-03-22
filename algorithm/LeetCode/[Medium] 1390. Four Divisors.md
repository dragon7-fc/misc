1390. Four Divisors

Given an integer array `nums`, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return `0`.

 

**Example 1:**
```
Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
```

**Constraints:**

* `1 <= nums.length <= 10^4`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 356 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def four_divisors(num: int) -> int:
            first = 0
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    if first > 0: return 0
                    first = i
            if first == 0 or first == num // first: return 0
            return 1 + first + num // first + num
        
        return sum(four_divisors(num) for num in nums)
```