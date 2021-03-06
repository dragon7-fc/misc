948. Bag of Tokens

You have an initial power `P`, an initial score of 0 points, and a bag of `tokens`.

Each token can be used at most once, has a value `token[i]`, and has potentially two ways to use it.

* If we have at least `token[i]` power, we may play the token face up, losing `token[i]` power, and gaining `1` point.
* If we have at least `1` point, we may play the token face down, gaining `token[i]` power, and losing `1` point.

Return the largest number of points we can have after playing any number of `tokens`.

 

**Example 1:**
```
Input: tokens = [100], P = 50
Output: 0
```

**Example 2:**
```
Input: tokens = [100,200], P = 150
Output: 1
```

**Example 3:**
```
Input: tokens = [100,200,300,400], P = 200
Output: 2
``` 

**Note:**

* `tokens.length <= 1000`
* `0 <= tokens[i] < 10000`
* `0 <= P < 10000`

# Solution
---
## Approach 1: Greedy
**Intuition**

If we play a token face up, we might as well play the one with the smallest value. Similarly, if we play a token face down, we might as well play the one with the largest value.

**Algorithm**

We don't need to play anything until absolutely necessary. Let's play tokens face up until we can't, then play a token face down and continue.

We must be careful, as it is easy for our implementation to be incorrect if we do not handle corner cases correctly. We should always play tokens face up until exhaustion, then play one token face down and continue.

Our loop must be constructed with the right termination condition: we can either play a token face up or face down.

Our final answer could be any of the intermediate answers we got after playing tokens face up (but before playing them face down.)

```python
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `tokens`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 68 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans
```