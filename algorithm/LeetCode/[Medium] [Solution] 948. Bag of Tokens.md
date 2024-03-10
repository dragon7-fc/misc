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

**Solution 1: (Greedy, Sort, Two Pointers)**
```
Runtime: 12 ms
Memory Usage: 10.6 MB
```
```c++
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int left = 0, right = tokens.size()-1;
        int ans = 0, score = 0;
        bool flag;
        sort(tokens.begin(), tokens.end());
        while (left <= right) {
            flag = false;
            while (left <= right && tokens[left] <= power) {
                power -= tokens[left];
                score += 1;
                left += 1;
                flag = true;
            }
            if (!flag)
                break;
            ans = max(ans, score);
            if (left <= right && score) {
                power += tokens[right];
                score -= 1;
                right -= 1;
            }
        }
        return ans;
    }
};
```‵

**Solution 2: (Greedy, Sort, Two Pointers)**
```
Runtime: 4 ms
Memory: 13.04 MB
```
```c++
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        int n = tokens.size();
        int score = 0;
        int max_score = 0;
        int left = 0;
        int right = n - 1;
        
        while (left <= right) {
            if (power >= tokens[left]) {
                power -= tokens[left];
                score += 1;
                left += 1;
                max_score = max(max_score, score);
            } else if (score > 0) {
                power += tokens[right];
                score -= 1;
                right -= 1;
            } else {
                break;
            }
        }
        
        return max_score;
    }
};
```
