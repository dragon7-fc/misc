829. Consecutive Numbers Sum

Given a positive integer `N`, how many ways can we write it as a sum of consecutive positive integers?

**Example 1:**
```
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
```

**Example 2:**
```
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
```

**Example 3:**
```
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
```

**Note:** `1 <= N <= 10 ^ 9`.

# Solution
---
## Approach #1: Brute Force [Time Limit Exceeded]
**Intuition and Algorithm**

For each starting number, we scan forward until we meet or exceed the target `N`. If we meet it, then it represents one way to write `N` as a sum of consecutive numbers.

For example, if `N = 6`, and we scan forward from `1`, we'll get `1 + 2 + 3 = 6` which contributes to the answer. If we scan forward from `2`, we'll get `2 + 3 + 4` (the first time that the sum is `>= N`) which is too big.

```python
class Solution(object):
    def consecutiveNumbersSum(self, N):
        ans = 0
        for start in xrange(1, N+1):
            target = N
            while target > 0:
                target -= start
                start += 1
            if target == 0: ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$.

* Space Complexity: $O(1)$.

## Approach #2: Mathematical (Naive) [Time Limit Exceeded]
**Intuition and Algorithm**

We can model the situation by the equation $N = (x+1) + (x+2) + \cdots + (x+k)$. Here, $x \geq 0, k \geq 1$. Using the identity $1 + 2 + \cdots + k = \frac{k(k+1)}{2}$, we can simplify this equation to $2*N = k(2*x + k + 1)$.

From here, clearly $1 \leq k \leq 2*N$. We can try every such $k$. We need $x = \frac{\frac{2*N}{k} - k - 1}{2}$ to be a non-negative integer for a solution to exist for the $k$ we are trying.

```python
class Solution(object):
    def consecutiveNumbersSum(self, N):
        # 2N = k(2x + k + 1)
        ans = 0
        for k in xrange(1, 2*N + 1):
            if 2*N % k == 0:
                y = 2 * N / k - k - 1
                if y % 2 == 0 and y >= 0:
                    ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$.

* Space Complexity: $O(1)$.

## Approach #3: Mathematical (Fast) [Accepted]
**Intuition and Algorithm**

As in Approach #2, $2*N = k(2*x + k + 1)$ with $x \geq 0, k \geq 1$. Call $k$ the first factor, and $2*x + k + 1$ the second factor. We are looking for ways to solve this equation without trying all $2*N$ possibilities.

Now notice that the parity of $k$ and $(2*x + k + 1)$ are different. That is, if $k$ is even then the other quantity is odd, and vice versa. Also, $2*x + k + 1 \geq k + 1 > k$, so the second factor must be bigger.

Now write $2N = 2^\alpha * M$ where $M$ is odd. If we factor $M = a * b$, then two candidate solutions are $k = a, 2x+k+1 = b * 2^\alpha$, or $k = a * 2^\alpha, 2x+k+1 = b$. However, only one of these solutions will have the second factor larger than the first. (Because $\alpha \geq 1$, we are guaranteed that one factor is strictly larger.)

Thus, the answer is the number of ways to factor the odd part of $N$.

```python
class Solution(object):
    def consecutiveNumbersSum(self, N):
        while N & 1 == 0:
            N >>= 1

        ans = 1    
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(\sqrt(N))$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Mathematical)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        while N & 1 == 0:
            N >>= 1

        ans = 1    
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans
```
