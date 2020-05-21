869. Reordered Power of 2

Starting with a positive integer `N`, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return `true` if and only if we can do this in a way such that the resulting number is a power of `2`.

 

**Example 1:**
```
Input: 1
Output: true
```

**Example 2:**
```
Input: 10
Output: false
```

**Example 3:**
```
Input: 16
Output: true
```

**Example 4:**
```
Input: 24
Output: false
```

**Example 5:**
```
Input: 46
Output: true
```

**Note:**

* `1 <= N <= 10^9`

# Solution
---
## Approach 1: Permutations
**Intuition**

For each permutation of the digits of `N`, let's check if that permutation is a power of `2`.

**Algorithm**

This approach has two steps: how will we generate the permutations of the digits, and how will we check that the permutation represents a power of `2`?

To generate permutations of the digits, we place any digit into the first position (start = 0), then any of the remaining digits into the second position (start = 1), and so on. In Python, we can use the builtin function itertools.permutations.

To check whether a permutation represents a power of `2`, we check that there is no leading zero, and divide out all factors of `2`. If the result is `1` (that is, it contained no other factors besides `2`), then it was a power of `2`. In Python, we can use the check `bin(N).count('1') == 1`.

```python
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        Let's work through an example like N = 128.
        In the last line, 'for cand in itertools.permutations(str(N))' will
        iterate through the six possibilities cand = ('1', '2', '8'),
        cand = ('1', '8', '2'), cand = ('2', '1', '8'), and so on.

        The check cand[0] != '0' is a check that the candidate permutation
        does not have a leading zero.

        The check bin(int("".join(cand))).count('1') == 1 is a check that cand
        represents a power of 2: namely, that the number of ones in its binary
        representation is 1.
        """
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))
```

**Complexity Analysis**

* Time Complexity: $O((\log N)! * \log N)$. Note that $\log N$ is the number of digits in the binary representation of NN. For each of $(\log N)!$ permutations of the digits of $N$, we need to check that it is a power of `2` in $O(\log N)$ time.

* Space Complexity: $O(\log N)$, the space used by A (or cand in Python).

## Approach 2: Counting
**Intuition and Algorithm**

We can check whether two numbers have the same digits by comparing the count of their digits. For example, `338` and `833` have the same digits because they both have exactly two `3`'s and one `8`.

Since $N$ could only be a power of `2` with `9` digits or less (namely, $2^0, 2^1, \cdots, 2^9$), we can just check whether $N$ has the same digits as any of these possibilities.

```python
class Solution(object):
    def reorderedPowerOf2(self, N):
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in xrange(31))
```

**Complexity Analysis**

* Time Complexity: $O(\log^2 N)$. There are $\log N$ different candidate powers of `2`, and each comparison has $O(\log N)$ time complexity.

* Space Complexity: $O(\log N)$.

# Submissions
---
**Solution: (Counting)**
```
Runtime: 36 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))
```