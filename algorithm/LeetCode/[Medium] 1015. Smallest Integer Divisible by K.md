1015. Smallest Integer Divisible by K

Given a positive integer `K`, you need find the **smallest** positive integer `N` such that `N` is divisible by `K`, and `N` only contains the digit **1**.

Return the length of `N`.  If there is no such `N`, return `-1`.

 

**Example 1:**
```
Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
```

**Example 2:**
```
Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
```

**Example 3:**
```
Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
```

**Note:**

* `1 <= K <= 10^5`

# Submissions
---
**Solution 1: (Checking Loop)**
```
Runtime: 48 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 0
        for length_N in range(1,K+1):
            remainder = (remainder*10+1) % K
            if remainder == 0:
                return length_N
        return -1
```

**Solution 2:**

Solution exists except for K % 2 == 0 or K%5 == 0
```
Example: K = 3
N = 1%3 = 1
N = 11%3 = 2
N = 21%3 = 0
return 3
```

```
Runtime: 36 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2 == 0 or K%5 == 0: return -1
        N, i = 0, 0
        while True:
            N = (N*10 + 1) % K
            i += 1
            if N == 0: return i
```

**Solution 3: (Math)**
```
Runtime: 7 ms
Memory Usage: 5.4 MB
```
```c


int smallestRepunitDivByK(int k){
    if (k%2 == 0 || k%5 == 0)
        return -1;
    int n = 0, i = 0;
    while (1) {
        n = (n*10 + 1) % k;
        i += 1;
        if (n == 0)
            return i;
    }
}
```

**Solution 4: (Math)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k%2 == 0 || k%5 == 0)
            return -1;
        int n = 0, i = 0;
        while (1) {
            n = (n*10 + 1) % k;
            i += 1;
            if (n == 0)
                return i;
        }
    }
};
```

**Solution 5: (Math, (a + b) % k = a % k + b % k, at most r kind remainder or it will loop)**

    ((a + r) * 10 + 1) % k
    = (a * 10) % k + (r * 10 + 1) % k
      ------------   ----------------
             0               0

```
Runtime: 0 ms, Beats 100.00%
Memory: 7.73 MB, Beats 81.50%
```
```c++
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        int a = 0, ans;
        for (ans = 1; ans <= k; ans ++) {
            a = (a * 10 + 1) % k;
            if (a == 0) {
                return ans;
            } 
        }
        return -1;
    }
};
```
