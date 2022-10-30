2457. Minimum Addition to Make Integer Beautiful

You are given two positive integers `n` and `target`.

An integer is considered **beautiful** if the sum of its digits is less than or equal to `target`.

Return the minimum **non-negative** integer `x` such that `n + x` is beautiful. The input will be generated such that it is always possible to make `n` beautiful.

 

**Example 1:**
```
Input: n = 16, target = 6
Output: 4
Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4.
```

**Example 2:**
```
Input: n = 467, target = 6
Output: 33
Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with adding non-negative integer less than 33.
```

**Example 3:**
```
Input: n = 1, target = 1
Output: 0
Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.
```

**Constraints:**

* `1 <= n <= 10^12`
* `1 <= target <= 150`
* The input will be generated such that it is always possible to make `n` beautiful.

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 54 ms
Memory: 13.9 MB
```
```python
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        n0 = n
        i = 0
        while sum(map(int, str(n))) > target:
            n = n // 10 + 1
            i += 1
        return n * (10 ** i) - n0
```

**Solution 2: (Math)**
```
Runtime: 0 ms
Memory: 5.8 MB
```
```c++
class Solution {
    int sum(long long n) {
        int res = 0;
        while (n) {
            res += n % 10;
            n /= 10;
        }
        return res;
    }
public:
    long long makeIntegerBeautiful(long long n, int target) {
        long long n0 = n, base = 1;
        while (sum(n) > target) {
            n = n / 10 + 1;
            base *= 10;
        }
        return n * base - n0;
    }
};
```
