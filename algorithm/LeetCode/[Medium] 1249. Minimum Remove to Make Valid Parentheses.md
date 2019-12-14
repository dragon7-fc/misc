1249. Minimum Remove to Make Valid Parentheses

Given a string s of `'('` , `')'` and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

* It is the empty string, contains only lowercase characters, or
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
* It can be written as `(A)`, where `A` is a valid string.
 

**Example 1:**
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

**Example 2:**
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3:**
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

**Example 4:**
```
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s[i]` is one of  `'('` , `')'` and lowercase English letters.

# Submissions
---
**Solution 1:**
```
Runtime: 116 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return

        stack = []
        for i, token in enumerate(s):

            if token == ")" and stack and stack[-1][1] == "(":
                stack.pop()

            elif token in ('(',')'):
                stack.append((i,token))     # Trick is to append index and token both to stack. All unmatched/extra brackets will be 
                                            # left on stack which have to be removed from given string.
            else:
                continue

            #print token, stack

        s = list(s)
        while stack:
            index = stack.pop()[0]
            s.pop(index)                # Remove unmatched from string.
            #s[:] = s[:index] + s[index+1:]

        return ''.join(s)
        
```