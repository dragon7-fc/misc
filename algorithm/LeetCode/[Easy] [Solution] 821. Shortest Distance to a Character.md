821. Shortest Distance to a Character

Given a string `S` and a character `C`, return an array of integers representing the shortest distance from the character `C` in the string.

**Example 1:**
```
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
```

**Note:**

* `S` string length is in `[1, 10000]`.
* `C` is a single character, and guaranteed to be in string `S`.
* All letters in `S` and `C` are lowercase.

# Solution
---
## Approach #1: Min Array [Accepted]
**Intuition**

For each index `S[i]`, let's try to find the distance to the next character `C` going left, and going right. The answer is the minimum of these two values.

**Algorithm**

When going left to right, we'll remember the index `prev` of the last character `C` we've seen. Then the answer is `i - prev`.

When going right to left, we'll remember the index `prev` of the last character `C` we've seen. Then the answer is `prev - i`.

We take the minimum of these two answers to create our final answer.

```python
class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `S`. We scan through the string twice.

* Space Complexity: $O(N)$, the size of `ans`.

# Submissions
---
**Solution 1: (Min Array, Two Pass)**
```
Runtime: 40 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
```