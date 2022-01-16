439. Ternary Expression Parser

Given a string **expression** representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it.

You can always assume that the given expression is valid and only contains digits, `'?'`, `':'`, `'T'`, and `'F'` where `'T'` is `true` and `'F'` is `false`. All the numbers in the expression are **one-digit** numbers (i.e., in the range `[0, 9]`).

The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, `'T'` or `'F'`.

 

**Example 1:**
```
Input: expression = "T?2:3"
Output: "2"
Explanation: If true, then result is 2; otherwise result is 3.
```

**Example 2:**
```
Input: expression = "F?1:T?4:5"
Output: "4"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"
```

**Example 3:**
```
Input: expression = "T?T?F:5:3"
Output: "F"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"
```

**Constraints:**

* `5 <= expression.length <= 10^4`
* `expression` consists of digits, `'T'`, `'F'`, `'?'`, and `':'`.
* It is **guaranteed** that `expression` is a valid ternary expression and that each number is a **one-digit number**.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 67 ms
Memory Usage: 17 MB
```
```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        n = len(expression)
        
        def helper(i):
            nonlocal n
            if (i+1 >= n) or (i+1 < n and expression[i+1] == ':'):
                return expression[i], i+2
            exp = expression[i]
            l, i = helper(i+2)
            r, i = helper(i)
            if exp == 'T':
                return l, i
            return r, i
        
        ans, _ = helper(0)
        return ans
```

**Solution 2: (Stack)**
```
Runtime: 70 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        stackmark=[]
        stacknumalpha=[]
        for i in expression[::-1]:
            if i.isalpha() and len(stackmark)>1 and stackmark[-1]=="?":
                first=stacknumalpha.pop()
                second=stacknumalpha.pop()
                stackmark.pop()
                stackmark.pop()
                if i == "T":
                    stacknumalpha.append(first)
                elif i == "F":
                    stacknumalpha.append(second)
            elif i.isalpha() or i.isdigit():
                stacknumalpha.append(i)
            elif i in ":?":
                stackmark.append(i)
        return stacknumalpha[0]
```
