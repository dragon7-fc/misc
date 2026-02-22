762. Prime Number of Set Bits in Binary Representation

Given two integers `L` and `R`, find the count of numbers in the range `[L, R]` (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, `21` written in binary is `10101` which has `3` set bits. Also, `1` is not a prime.)

**Example 1:**
```
Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
```

**Example 2:**
```
Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
```

**Note:**

* `L`, `R` will be integers L <= R in the range `[1, 10^6]`.
* `R - L` will be at most `10000`.

# Solution
---
## Approach #1: Direct [Accepted]
**Intuition and Approach**

For each number from `L` to `R`, let's find out how many set bits it has. If that number is `2, 3, 5, 7, 11, 13, 17, or 19`, then we add one to our count. We only need primes up to `19` because $R \leq 10^6 < 2^{20}$.

```python
class Solution(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in xrange(L, R+1))
```

**Complexity Analysis**

* Time Complexity: $O(D)$, where $D = R-L$ is the number of integers considered. In a bit complexity model, this would be $O(D\log D)$ as we have to count the bits in $O(\log D)$ time.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Direct, Bit Manipulation)**
```
Runtime: 180 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in range(L, R+1))
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.02 MB, Beats 35.12%
````
```c++
class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        int a, b, c, ans = 0;
        int prime[] = {2, 3, 5, 7, 11, 13, 17, 19};
        c = 0;
        for (auto &p: prime) {
            c |= (1 << p);
        }
        for (a = left; a <= right; a ++) {
            b = __builtin_popcount(a);
            if (c & (1 << b)) {
                ans += 1;
            }
        }
        return ans;
    }
};
````
