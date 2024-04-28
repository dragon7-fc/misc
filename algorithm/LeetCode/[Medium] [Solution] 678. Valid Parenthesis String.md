678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
1. Any right parenthesis ')' must have a corresponding left parenthesis '('.
1. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
1. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
1. An empty string is also valid.

**Example 1:**
```
Input: "()"
Output: True
```

**Example 2:**
```
Input: "(*)"
Output: True
```

**Example 3:**
```
Input: "(*))"
Output: True
```

**Note:**

* The string size will be in the range `[1, 100]`.

## Approach #1: Brute Force [Time Limit Exceeded]
**Intuition and Algorithm**

For each asterisk, let's try both possibilities.

```python
class Solution(object):
    def checkValidString(self, s):
        if not s: return True
        A = list(s)
        self.ans = False

        def solve(i):
            if i == len(A):
                self.ans |= valid()
            elif A[i] == '*':
                for c in '() ':
                    A[i] = c
                    solve(i+1)
                    if self.ans: return
                A[i] = '*'
            else:
                solve(i+1)

        def valid():
            bal = 0
            for x in A:
                if x == '(': bal += 1
                if x == ')': bal -= 1
                if bal < 0: break
            return bal == 0

        solve(0)
        return self.ans
```

**Complexity Analysis**

* Time Complexity: $O(N * 3^{N})$, where $N$ is the length of the string. For each asterisk we try 3 different values. Thus, we could be checking the validity of up to $3^N$ strings. Then, each check of validity is $O(N)$.

* Space Complexity: $O(N)$, the space used by our character array.

## Approach #2: Dynamic Programming [Accepted]
**Intuition and Algorithm**

Let `dp[i][j]` be true if and only if the interval `s[i], s[i+1], ..., s[j]` can be made valid. Then `dp[i][j]` is true only if:

* `s[i]` is '*', and the interval `s[i+1], s[i+2], ..., s[j]` can be made valid;

* or, `s[i]` can be made to be `'('`, and there is some `k` in `[i+1, j]` such that `s[k]` can be made to be `')'`, plus the two intervals cut by `s[k]` (`s[i+1: k]` and `s[k+1: j+1]`) can be made valid;

```python
class Solution(object):
    def checkValidString(self, s):
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]
        for i in xrange(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        for size in xrange(2, n):
            for i in xrange(n - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in xrange(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$, where $N$ is the length of the string. There are $O(N^2)$ states corresponding to entries of `dp`, and we do an average of $O(N)$ work on each state.

* Space Complexity: $O(N^2)$, the space used to store intermediate results in `dp`.

## Approach #3: Greedy [Accepted]
**Intuition**

When checking whether the string is valid, we only cared about the `"balance"`: the number of extra, open left brackets as we parsed through the string. For example, when checking whether `'(()())'` is valid, we had a balance of `1, 2, 1, 2, 1, 0` as we parse through the string: `'('` has `1` left bracket, `'(('` has `2`, `'(()'` has `1`, and so on. This means that after parsing the first `i` symbols, (which may include asterisks,) we only need to keep track of what the `balance` could be.

For example, if we have string `'(***)'`, then as we parse each symbol, the set of possible values for the balance is `[1]` for `'('`; `[0, 1, 2]` for `'(*'`; `[0, 1, 2, 3]` for `'(**'`; `[0, 1, 2, 3, 4]` for `'(***'`, and `[0, 1, 2, 3]` for `'(***)'`.

Furthermore, we can prove these states always form a contiguous interval. Thus, we only need to know the left and right bounds of this interval. That is, we would keep those intermediate states described above as `[lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4], [0, 3]`.

**Algorithm**

Let `lo`, `hi` respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.

If we encounter a left bracket (`c == '('`), then `lo++`, otherwise we could write a right bracket, so `lo--`. If we encounter what can be a left bracket (`c != ')'`), then `hi++`, otherwise we must write a right bracket, so `hi--`. If `hi < 0`, then the current prefix can't be made valid no matter what our choices are. Also, we can never have less than 0 open left brackets. At the end, we should check that we can have exactly `0` open left brackets.

```python
class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of the string. We iterate through the string once.

* Space Complexity: $O(1)$, the space used by our `lo` and `hi` pointers. However, creating a new character array will take $O(N)$ space.

# Submissions
---
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 268 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        for size in range(2, n):
            for i in range(n - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in range(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 96 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        
        @functools.lru_cache(None)
        def dp(i, j):  # state: (index1, index2)
            if i == j:
                if s[i]  == '*':
                    return True
                else:
                    return False
            elif j == i+1:
                if s[i] in LEFTY and s[j] in RIGHTY:
                    return True
                else:
                    return False
            if s[i] == '*' and dp(i+1, j):
                return True
            elif s[i] in LEFTY:
                for k in range(i+1, j+1):
                    if (s[k] in RIGHTY and 
                            (k == i+1 or dp(i+1, k-1)) and
                            (k == j or dp(k+1, j))):
                        return True
                return False
            return False
                
        return dp(0, n-1)
```

**Solution 3: (Greedy)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
```

**Solution 4: (Two Stack)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i, x in enumerate(s):
            if x == '(':
                stack.append(i)
            elif x == '*':
                star.append(i)
            else:
                if not stack and not star:
                    return False
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
        
        while stack and star:
            if stack.pop() > star.pop():
                return False
        
        if not stack:
            return True
        else:
            return False
```

**Solution 5: (DP Top-Down)**
```
Runtime: 32 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        
        @functools.lru_cache(None)
        def dp(i, n):  # state: (index, count)
            if i == N:
                return True if n == 0 else False
            if n < 0:
                return False
            if s[i] == '(':
                return dp(i+1, n+1)
            elif s[i] == ')':
                return dp(i+1, n-1);
            else:
                return dp(i+1, n+1) or dp(i+1, n-1) or dp(i+1, n)
        
        return dp(0, 0)
```

**Solution 6: (Two Pointers)**
```
Runtime: 3 ms
Memory: 7.33 MB
```
```c++
class Solution {
public:
    bool checkValidString(string s) {
        int openCount = 0;
        int closeCount = 0;
        int length = s.length() - 1;
        
        // Traverse the string from both ends simultaneously
        for (int i = 0; i <= length; i++) {
            // Count open parentheses or asterisks
            if (s[i] == '(' || s[i] == '*') {
                openCount++;
            } else {
                openCount--;
            }
            
            // Count close parentheses or asterisks
            if (s[length - i] == ')' || s[length - i] == '*') {
                closeCount++;
            } else {
                closeCount--;
            }
            
            // If at any point open count or close count goes negative, the string is invalid
            if (openCount < 0 || closeCount < 0) {
                return false;
            }
        }
        
        // If open count and close count are both non-negative, the string is valid
        return true;
    }
};
```
