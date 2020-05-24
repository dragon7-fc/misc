906. Super Palindromes

Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers `L` and `R` (represented as strings), return the number of superpalindromes in the inclusive range `[L, R]`.

 

**Example 1:**
```
Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
```

**Note:**

* `1 <= len(L) <= 18`
* `1 <= len(R) <= 18`
* `L` and `R` are strings representing integers in the range `[1, 10^18)`.
* `int(L) <= int(R)`

# Solution
---
## Approach 1: Mathematical
**Intuition**

Say $P = R^2$ is a superpalindrome.

Because $R$ is a palindrome, the first half of the digits in $R$ determine $R$ up to two possibilities. We can iterate through these digits: let $k$ be the first half of the digits in $R$. For example, if $k = 1234$, then $R = 1234321$ or $R = 12344321$. Each possibility has either an odd or an even number of digits in $R$.

Notice because $P < 10^{18}$, $R < (10^{18})^{\frac{1}{2}} = 10^9$, and $R = k | k'$ (concatenation), where $k'$ is $k$ reversed (and also possibly truncated by one digit); so that $k < 10^5 = \small\text{MAGIC}$, our magic constant.

**Algorithm**

For each $1 \leq k < \small\text{MAGIC}$, let's create the associated palindrome $R$, and check whether $R^2$ is a palindrome.

We should handle the odd and even possibilities separately, as we would like to break early so as not to do extra work.

To check whether an integer is a palindrome, we could check whether it is equal to its reverse. To create the reverse of an integer, we can do it digit by digit.

```python
class Solution(object):
    def superpalindromesInRange(self, L, R):
        L, R = int(L), int(R)
        MAGIC = 100000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)

        ans = 0

        # count odd length
        for k in xrange(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[-2::-1]  # t = '1234321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        # count even length
        for k in xrange(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[::-1]  # t = '12344321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(W^{\frac{1}{4}} * \log W)$, where $W = 10^{18}$ is our upper limit for $R$. The $\log W$ term comes from checking whether each candidate is the root of a palindrome.

* Space Complexity: $O(\log W)$, the space used to create the candidate palindrome.

# Submissions
---
**Solution: (Mathematical)**
```
Runtime: 2732 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        L, R = int(L), int(R)
        MAGIC = 100000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)

        ans = 0

        # count odd length
        for k in range(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[-2::-1]  # t = '1234321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        # count even length
        for k in range(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[::-1]  # t = '12344321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        return ans
```