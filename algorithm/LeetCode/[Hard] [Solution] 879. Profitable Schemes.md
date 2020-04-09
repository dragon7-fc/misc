879. Profitable Schemes

There are G people in a gang, and a list of various crimes they could commit.

The i-th crime generates a `profit[i]` and requires `group[i]` gang members to participate.

If a gang member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least `P` profit, and the total number of gang members participating in that subset of crimes is at most G.

How many schemes can be chosen?  Since the answer may be very large, **return it modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: G = 5, P = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: 
To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
```

**Example 2:**
```
Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: 
To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
```

**Note:**

* `1 <= G <= 100`
* `0 <= P <= 100`
* `1 <= group[i] <= 100`
* `0 <= profit[i] <= 100`
* `1 <= group.length = profit.length <= 100`

# Solution
---
## Approach 1: Dynamic Programming
**Intuition**

We don't care about the profit of the scheme if it is $\geq P$, because it surely will be over the threshold of profitability required. Similarly, we don't care about the number of people required in the scheme if it is $> G$, since we know the scheme will be too big for the gang to execute.

As a result, the bounds are small enough to use dynamic programming. Let's keep track of `cur[p][g]`, the number of schemes with profitability $p$ and requiring $g$ gang members: except we'll say (without changing the answer) that all schemes that profit at least $P$ dollars will instead profit exactly $P$ dollars.

**Algorithm**

Keeping track of `cur[p][g]` as defined above, let's understand how it changes as we consider 1 extra crime that will profit `p0` and require `g0` gang members. We will put the updated counts into `cur2`.

For each possible scheme with profit `p1` and group size `g1`, that scheme plus the extra crime `(p0, g0)` being considered, has a profit of `p2 = min(p1 + p0, P)`, and uses a group size of `g2 = g1 + g0`.

```python
class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        MOD = 10**9 + 7
        cur = [[0] * (G + 1) for _ in xrange(P + 1)]
        cur[0][0] = 1

        for p0, g0 in zip(profit, group):
            # p0, g0 : the current crime profit and group size
            cur2 = [row[:] for row in cur]
            for p1 in xrange(P + 1):
                # p1 : the current profit
                # p2 : the new profit after committing this crime
                p2 = min(p1 + p0, P)
                for g1 in xrange(G - g0 + 1):
                    # g1 : the current group size
                    # g2 : the new group size after committing this crime
                    g2 = g1 + g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= MOD
            cur = cur2

        # Sum all schemes with profit P and group size 0 <= g <= G.
        return sum(cur[-1]) % MOD
```

**Complexity Analysis**

* Time Complexity:$ O(N * P * G)$, where $N$ is the number of crimes available to the gang.

* Space Complexity: $O(P * G)$.

# Submissions
---
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 1188 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        cur = [[0] * (G + 1) for _ in range(P + 1)]
        cur[0][0] = 1

        for p0, g0 in zip(profit, group):
            # p0, g0 : the current crime profit and group size
            cur2 = [row[:] for row in cur]
            for p1 in range(P + 1):
                # p1 : the current profit
                # p2 : the new profit after committing this crime
                p2 = min(p1 + p0, P)
                for g1 in range(G - g0 + 1):
                    # g1 : the current group size
                    # g2 : the new group size after committing this crime
                    g2 = g1 + g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= MOD
            cur = cur2

        # Sum all schemes with profit P and group size 0 <= g <= G.
        return sum(cur[-1]) % MOD
```