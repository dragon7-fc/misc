394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like `3a` or `2[4]`.

**Examples:**
```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 20 ms
Memory Usage: 12.7 MB
```
```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(['', int(num)])
                num = ''
            elif ch.isalpha():
                stack[-1][0] += ch
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
        return stack[0][0]
```

**Solution 2: (DFS)**
```
Runtime: 20 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs():
            text = ""
            num = 0
            # the dfs recursion call absorbed "]", so that outer recursion can continue
            while self.idx < len(s) and s[self.idx] != "]":
                if s[self.idx].isdigit():
                    num = num * 10 + int(s[self.idx])
                    self.idx += 1
                elif s[self.idx].isalpha():
                    text += s[self.idx]
                    self.idx += 1
                else:
                    self.idx += 1  # s[self.idx] == "["
                    res = dfs()
                    text += num * res
                    num = 0
            self.idx += 1
            return text
        self.idx = 0
        return dfs()
```

**Solution 3: (Stack)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        keeper = []
        i = 0
        l = len(s)
        while i<l:
            if s[i] == ']':
                alpha = []
                while keeper and keeper[-1] != '[':
                    alpha.append(keeper.pop())
                keeper.pop()
                num = []
                while keeper and keeper[-1].isdigit():
                    num.append(keeper.pop())
                num = int(''.join(num[::-1]))
                alpha = alpha[::-1]
                keeper.append(''.join(alpha)*num)
            else:
                keeper.append(s[i])
            i += 1
        return ''.join(keeper)
```