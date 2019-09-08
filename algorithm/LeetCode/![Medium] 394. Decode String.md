394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

**Examples:**
```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

Solution 1: 24 ms
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

Solution 2: 20 ms
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
```python