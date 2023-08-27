2834. Find the Minimum Possible Sum of a Beautiful Array

You are given positive integers `n` and `target`.

An array nums is **beautiful** if it meets the following conditions:

* `nums.length == n`.
* `nums` consists of pairwise **distinct positive** integers.
* There doesn't exist two **distinct** indices, `i``and `j`, in the range `[0, n - 1]`, such that `nums[i] + nums[j] == target`.

Return the **minimum** possible sum that a beautiful array could have.

 

**Example 1:**
```
Input: n = 2, target = 3
Output: 4
Explanation: We can see that nums = [1,3] is beautiful.
- The array nums has length n = 2.
- The array nums consists of pairwise distinct positive integers.
- There doesn't exist two distinct indices, i and j, with nums[i] + nums[j] == 3.
It can be proven that 4 is the minimum possible sum that a beautiful array could have.
```

**Example 2:**
```
Input: n = 3, target = 3
Output: 8
Explanation: We can see that nums = [1,3,4] is beautiful.
- The array nums has length n = 3.
- The array nums consists of pairwise distinct positive integers.
- There doesn't exist two distinct indices, i and j, with nums[i] + nums[j] == 3.
It can be proven that 8 is the minimum possible sum that a beautiful array could have.
```

**Example 3:**
```
Input: n = 1, target = 1
Output: 1
Explanation: We can see, that nums = [1] is beautiful.
```

**Constraints:**

* `1 <= n <= 10^5`
* `1 <= target <= 10^5`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 120 ms
Memory: 26.2 MB
```
```python
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        seen = set()
        i = 1
        while len(seen) < n:
            if target - i not in seen:
                seen.add(i)
            i += 1
        return sum(seen)
```

**Solution 2: (Math)**

k = target / 2 is the middle of taregt.
If n <= k,
we pick [1,2,3,...,n] as the beautiful array.
n + (n - 1) < k + k <= target,
so no problem,
the sum is n * (n + 1) / 2.

If n > k,
we pick [1,2,3,...,k] + [taregt, target + 1, .... , taregt + n - k - 1]
The sum of first part is k * (k + 1) / 2,
The sum of second part is (target + target + n - k - 1) * (n - k) / 2,

Time O(1), Space O(1)

```
Memory: 5.9 MB
Runtime: 0 ms
```
```c++
class Solution {
public:
    long long minimumPossibleSum(int n, int target) {
        long long k = target / 2;
        if (n <= k)
            return 1L * n * (n + 1) / 2;
        return k * (k + 1) / 2 + (target + target + n - k - 1) * (n - k) / 2;
    }
};
```
