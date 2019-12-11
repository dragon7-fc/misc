833. Find And Replace in String

To some string `S`, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has `3` parameters: a starting index `i`, a source word `x` and a target word `y`.  The rule is that if `x` starts at position `i` in the original string S, then we will replace that occurrence of `x` with `y`.  If not, we do nothing.

For example, if we have `S = "abcd"` and we have some replacement operation `i = 2, x = "cd", y = "ffff"`, then because `"cd"` starts at position `2` in the original string `S`, we will replace it with `"ffff"`.

Using another example on `S = "abcd"`, if we have both the replacement operation `i = 0, x = "ab", y = "eee"`, as well as another replacement operation `i = 2, x = "ec", y = "ffff"`, this second operation does nothing because in the original string `S[2] = 'c'`, which doesn't match `x[0] = 'e'`.

All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, `S = "abc", indexes = [0, 1], sources = ["ab","bc"]` is not a valid test case.

**Example 1:**
```
Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"
Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
"cd" starts at index 2 in S, so it's replaced by "ffff".
```

**Example 2:**
```
Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation: "ab" starts at index 0 in S, so it's replaced by "eee". 
"ec" doesn't starts at index 2 in the original S, so we do nothing.
```

**Notes:**

1. `0 <= indexes.length = sources.length = targets.length <= 100`
1. `0 < indexes[i] < S.length <= 1000`
1. All characters in given inputs are lowercase letters.

# Solution
---
## Approach #1: Direct [Accepted]
**Intuition and Algorithm**

We showcase two different approaches. In both approaches, we build some answer string `ans`, that starts as `S`. Our main motivation in these approaches is to be able to identify and handle when a given replacement operation does nothing.

In Java, the idea is to build an array match that tells us `match[ix] = j whenever S[ix]` is the head of a successful replacement operation `j:` that is, whenever `S[ix:].startswith(sources[j])`.

After, we build the answer using this match array. For each index `ix` in `S`, we can use match to check whether `S[ix]` is being replaced or not. We repeatedly either write the next character `S[ix]`, or groups of characters `targets[match[ix]]`, depending on the value of `match[ix]`.

In Python, we sort our replacement jobs `(i, x, y)` in reverse order. If `S[i:].startswith(x)`, then we can replace that section `S[i:i+len(x)]` with the target `y`. We used a reverse order so that edits to `S` do not interfere with the rest of the queries.

```python
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            if all(i+k < len(S) and S[i+k] == x[k] for k in xrange(len(x))):
                S[i:i+len(x)] = list(y)

        return "".join(S)
```

**Complexity Analysis**

* Time Complexity: $O(NQ)$, where $N$ is the length of `S`, and we have $Q$ replacement operations. (Our complexity could be faster with a more accurate implementation, but it isn't necessary.)

* Space Complexity: $O(N)$, if we consider `targets[i].length <= 100` as a constant bound.

# Submissions
---
**Solution:**
```
Runtime: 36 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            if all(i+k < len(S) and S[i+k] == x[k] for k in range(len(x))):
                S[i:i+len(x)] = list(y)

        return "".join(S)
```