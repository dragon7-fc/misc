29. Divide Two Integers

Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing `dividend` by `divisor`.

The integer division should truncate toward zero.

**Example 1:**
```
Input: dividend = 10, divisor = 3
Output: 3
```

**Example 2:**
```
Input: dividend = 7, divisor = -3
Output: -2
```

**Note:**

* Both dividend and divisor will be 32-bit signed integers.
* The divisor will never be `0`.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: `[−2^31,  2^31 − 1]`. For the purpose of this problem, assume that your function returns `2^31 − 1` when the division result overflows.

# Submissions
---

**How it works**

For example, we `divide(5000, 14)`:

1. After the first inner loop: `the_sum = 3584` which is `14` multiplied `256` times.
1. We can't multiply any more — because after `256` is coming `256 + 256 = 512` and `14 * 512 = 7168` which is larger than our `dividend`, so we exit the inner loop,
1. Reducing `dividend`: `dividend = 5000 - 3584 = 1416`
1. And moving to another cycle of outer loop
1. After the second inner loop: `the_sum = 896` which is `14` multiplied `64` times.
1. Third: `the_sum = 448` which is `14` multiplied `32` times.
1. And so on
1. Finally we have: `quotient = 256 + 64 + 32 + 4 + 1 = 357`

**Solution 1: (Math, With bitwise operators)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2**31 -1, max(-quotient if is_negative else quotient, -2**31))
```

**Solution 2: (Math, Without bitwise operators)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                current_quotient += current_quotient
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2**31 - 1, max(-quotient if is_negative else quotient, -2**31))
```

**Solution 3: (Math, With bitwise operators)**
```
Runtime: 0 ms
Memory Usage: 5.4 MB
```
```c

#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) > (b) ? (a) : (b))
int divide(int dividend, int divisor){
    bool is_negative = (dividend < 0) != (divisor < 0);
    long ldivisor = divisor;
    ldivisor = ldivisor < 0 ? -ldivisor : ldivisor;
    long ldividend = dividend;
    ldividend = ldividend < 0 ? -ldividend : ldividend;

    long quotient = 0, current_quotient;
    long the_sum = ldivisor;

    while (the_sum <= ldividend) {
        current_quotient = 1;
        while ((the_sum << 1) <= ldividend) {
            the_sum <<= 1;
            current_quotient <<= 1;
        }
        ldividend -= the_sum;
        the_sum = ldivisor;
        quotient += current_quotient;
    }

    return min(pow(2,31) - 1, max(is_negative ? -quotient : quotient, -pow(2,31)));
}
```

**Solution 3: (Math, Bit Manipulation)**

    10 / 3 = 3.333
             ^

    3  2 1 0
   24 12 6 3

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.70 MB, Beats 37.69%
```
```c++
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        long long r = labs(dividend), d = labs(divisor), a, c, ans = 0;
        while (r >= d) {
            a = d;
            c = 1;
            while ((a<<1) <= r) {
                a <<= 1;
                c <<= 1;
            }
            r -= a;
            ans += c;
        }
        ans = ans * (((dividend > 0)^(divisor > 0)) ? -1 : 1);
        if (ans < INT_MIN) {
            ans = INT_MIN;
        }
        if (ans > INT_MAX) {
            ans = INT_MAX;
        }
        return ans;
    }
};
```
