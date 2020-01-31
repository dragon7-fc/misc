921. Minimum Add to Make Parentheses Valid

Given a string `S` of `'('` and `')'` parentheses, we add the minimum number of parentheses ( `'('` or `')'`, and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

* It is the empty string, or
* It can be written as `AB` (A concatenated with `B`), where `A` and `B` are valid strings, or
* It can be written as `(A)`, where `A` is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

**Example 1:**
```
Input: "())"
Output: 1
```

**Example 2:**
```
Input: "((("
Output: 3
```

**Example 3:**
```
Input: "()"
Output: 0
```

**Example 4:**
```
Input: "()))(("
Output: 4
```

**Note:**

* `S.length <= 1000`
* `S` only consists of `'('` and `')'` characters.

# Solution
---
## Approach 1: Balance
**Intuition and Algorithm**

Keep track of the balance of the string: the number of `'('`'s minus the number of `')'`'s. A string is valid if its balance is `0`, plus every prefix has non-negative balance.

The above idea is common with matching brackets problems, but could be difficult to find if you haven't seen it before.

Now, consider the balance of every prefix of `S`. If it is ever negative (say, `-1`), we must add a `'('` bracket. Also, if the balance of `S` is positive (say, `+B`), we must add B `')'` brackets at the end.

```python
class Solution(object):
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `S`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1  # invalid ')'
                bal += 1  # invalid '('
        return ans + bal
```