479. Largest Palindrome Product

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

 

**Example:**
```
Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
```

**Note:**

* The range of n is `[1,8]`.

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 2548 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        high = 10**n
        low = 10**(n-1)
        for i in range(high-1, low-1, -1):
            w = int(str(i) + str(i)[::-1])
            for j in range(high-1, int(w**0.5)+1, -1):
                if w%j == 0:
                    z = w//j
                    if z < high and z >= low:
                        return w%1337
```

**Solution 2: (Math)**
```
Runtime: 288 ms
Memory Usage: 6.7 MB
```
```c++
class Solution {
public:
    int largestPalindrome(int n) {
        if (n == 1)return 9;
        long long max = pow(10, n) - 1;
        for (int v = max - 1; v > (max / 10); v--) {
            string s = to_string(v), s0 = s;
            reverse(s.begin(), s.end());
            long long u = atoll((s0 + s).c_str());
            for (long long x = max; x*x >= u; x--)if (u%x == 0)return(int)(u%1337);
        }
        return 0;
    }
};
```