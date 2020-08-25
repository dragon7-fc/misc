1067. Digit Count in Range

Given an integer `d` between `0` and `9`, and two positive integers `low` and `high` as lower and upper bounds, respectively. Return the number of times that d occurs as a digit in all integers between `low` and `high`, including the bounds `low` and `high`.
 

**Example 1:**
```
Input: d = 1, low = 1, high = 13
Output: 6
Explanation: 
The digit d=1 occurs 6 times in 1,10,11,12,13. Note that the digit d=1 occurs twice in the number 11.
```

**Example 2:**
```
Input: d = 3, low = 100, high = 250
Output: 35
Explanation: 
The digit d=3 occurs 35 times in 103,113,123,130,131,...,238,239,243.
```

**Note:**

* `0 <= d <= 9`
* `1 <= low <= high <= 2×10^8`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        
        def countDigitD(n, d):
            # Q0233, count num of digit d appearance on all positive integer x, 1 <= x <= n.
            count, m = 0, 1
            while n > m - 1:
                q, r = n // (10 * m), n % (10 * m)
                if d == 0:
                    count += (q * m) if r >= m else ((q - 1) * m + r + 1)
                else:
                    count += q * m + min(max(0, r - m * d + 1), m)
                m *= 10
            return count
        
        return countDigitD(high, d) - countDigitD(low - 1, d)
```

**Solution 2: (Math)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int digitsCount(int d, int low, int high) {
        return count(d, high) - count(d, low - 1);
    }
    int count(int digit, int n) {
        int cnt = 0;
        if(digit != 0)
        {
            for(int num = 1; num <= n; num *= 10)
            {
                int divisor = num * 10;
                cnt += (n / divisor) * num;
                cnt += min(max(n % divisor - digit * num + 1, 0), num);
            }
        }
        else
        {
            for(int num = 1; num <= n; num *= 10)
            {
                int divisor = num * 10;
                cnt += (n / divisor) * num;
                if(n / divisor > 0)
                {
                    cnt -= num;
                    cnt += min(n % divisor + 1, num);
                }
            }
        }
        return cnt;
    }
};
```