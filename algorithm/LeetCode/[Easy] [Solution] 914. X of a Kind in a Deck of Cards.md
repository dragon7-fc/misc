914. X of a Kind in a Deck of Cards

In a deck of cards, each card has an integer written on it.

Return `true` if and only if you can choose `X >= 2` such that it is possible to split the entire deck into 1 or more groups of cards, where:

* Each group has exactly `X` cards.
* All the cards in each group have the same integer.
 
**Example 1:**
```
Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
```

**Example 2:**
```
Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
```

**Example 3:**
```
Input: [1]
Output: false
Explanation: No possible partition.
```

**Example 4:**
```
Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
```

**Example 5:**
```
Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
```

**Note:**

* `1 <= deck.length <= 10000`
* `0 <= deck[i] < 10000`

# Solution
---
## Approach 1: Brute Force
**Intuition**

We can try every possible `X`.

**Algorithm**

Since we divide the deck of `N` cards into say, `K` piles of `X` cards each, we must have `N % X == 0`.

Then, say the deck has `C_i` copies of cards with number `i`. Each group with number `i` has `X` copies, so we must have `C_i % X == 0`. These are necessary and sufficient conditions.

```python
class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in xrange(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False
```

**Complexity Analysis**

* Time Complexity: $O(N^2 \log \log N)$, where $N$ is the number of cards. It is outside the scope of this article to prove that the number of divisors of $N$ is bounded by O(N \log \log N)O(NloglogN).

* Space Complexity: $O(N)$.

## Approach 2: Greatest Common Divisor
**Intuition and Algorithm**

Again, say there are $C_i$ cards of number `i`. These must be broken down into piles of `X` cards each, ie. $C_i$ % X == 0 for all `i`.

Thus, `X` must divide the greatest common divisor of $C_i$. If this greatest common divisor `g` is greater than 1, then `X = g` will satisfy. Otherwise, it won't.

```python
class Solution(object):
    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
```

**Complexity Analysis**

* Time Complexity: $O(N \log^2 N)$, where $N$ is the number of votes. If there are $C_i$ cards with number $i$, then each gcd operation is naively $O(\log^2 C_i)$. Better bounds exist, but are outside the scope of this article to develop.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution**
```
Runtime: 156 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from functools import reduce
        vals = collections.Counter(deck).values()
        return reduce(math.gcd, vals) >= 2
```