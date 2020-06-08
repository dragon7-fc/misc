859. Buddy Strings

Given two strings `A` and `B` of lowercase letters, return `true` if and only if we can swap two letters in `A` so that the result equals `B`.

 

**Example 1:**
```
Input: A = "ab", B = "ba"
Output: true
```

**Example 2:**
```
Input: A = "ab", B = "ab"
Output: false
```

**Example 3:**
```
Input: A = "aa", B = "aa"
Output: true
```

**Example 4:**
```
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
```

**Example 5:**
```
Input: A = "", B = "aa"
Output: false
```

**Note:**

1. `0 <= A.length <= 20000`
1. `0 <= B.length <= 20000`
1. `A` and `B` consist only of lowercase letters.

# Solution
---
## Approach 1: Enumerate Cases
**Intuition**

Let's say `i` is matched if `A[i] == B[i]`, otherwise `i` is unmatched. A buddy string has almost all matches, because a swap only affects two indices.

If swapping `A[i]` and `A[j]` would demonstrate that `A` and `B` are buddy strings, then `A[i] == B[j]` and `A[j] == B[i]`. That means among the four free variables `A[i], A[j], B[i], B[j]`, there are only two cases: either `A[i] == A[j]` or not.

**Algorithm**

Let's work through the cases.

In the case `A[i] == A[j] == B[i] == B[j]`, then the strings `A` and `B` are equal. So if `A == B`, we should check each index `i` for two matches with the same value.

In the case `A[i] == B[j], A[j] == B[i]`, `(A[i] != A[j])`, the rest of the indices match. So if `A` and `B` have only two unmatched indices (say `i` and `j`), we should check that the equalities `A[i] == B[j]` and `A[j] == B[i]` hold.

```python
class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in itertools.izip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A` and `B`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution: (Enumerate Cases)**
```
Runtime: 40 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
```