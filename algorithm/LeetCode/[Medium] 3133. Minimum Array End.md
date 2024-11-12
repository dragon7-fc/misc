3133. Minimum Array End

You are given two integers `n` and `x`. You have to construct an array of positive integers nums of size `n` where for every `0 <= i < n - 1`, `nums[i + 1]` is greater than `nums[i]`, and the result of the bitwise `AND` operation between all elements of `nums` is `x`.

Return the **minimum** possible value of `nums[n - 1]`.

 

**Example 1:**
```
Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.
```

**Example 2:**
```
Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.
```
 

**Constraints:**

* `1 <= n, x <= 10^8`

# Submissions
---
**SOlution 1: (Bit Manipulation)**

Each time increment a, then OR with x,
So we get the next bigger valid element.

We do this n - 1 times,
and return the result.

Time O(n)
Space O(1)

```
Runtime: 1739 ms
Memory: 7.66 MB
```
```c++
class Solution {
public:
    long long minEnd(int n, int x) {
        long long a = x;
        while (--n)
            a = (a + 1) | x;
        return a;
    }
};
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms
Memory: 8.49 MB
```
```c++
class Solution {
public:
    long long minEnd(int n, int x) {
        int i = 0, j = 0;
        long long ans = x;
        while ((1<<j) <= (n-1)) {
            if ((ans & (1LL<<i)) == 0) {
                ans |= (1LL<<i)*(((n-1)&(1<<j)) != 0);
                j += 1;
            }
            i += 1;
        }
        return ans;
    }
};
```

**SOlution 3: (Bit Manipulation)**
```
```c++
class Solution {
public:
    long long minEnd(int n, int x) {
        n--;
        long long a = x, b;
        for (b = 1; n > 0; b <<= 1) {
            if ((b & x) == 0) {
                a |= (n & 1) * b;
                n >>= 1;
            }
        }
        return a;
    }
};
```

