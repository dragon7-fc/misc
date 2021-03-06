1003. Check If Word Is Valid After Substitutions

We are given that the string `"abc"` is valid.

From any valid string `V`, we may split `V` into two pieces `X` and `Y` such that `X + Y` (`X `concatenated with `Y`) is equal to `V`.  (`X` or `Y` may be empty.)  Then, `X + "abc" + Y` is also valid.

If for example `S = "abc"`, then examples of valid strings are: `"abc"`, `"aabcbc"`, `"abcabc"`, `"abcabcababcc"`.  Examples of invalid strings are: `"abccba"`, `"ab"`, `"cababc"`, `"bac"`.

Return `true` if and only if the given string `S` is valid.

 

**Example 1:**
```
Input: "aabcbc"
Output: true
Explanation: 
We start with the valid string "abc".
Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".
```

**Example 2:**
```
Input: "abcabcababcc"
Output: true
Explanation: 
"abcabcabc" is valid after consecutive insertings of "abc".
Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".
```

**Example 3:**
```
Input: "abccba"
Output: false
```

**Example 4:**
```
Input: "cababc"
Output: false
```

**Note:**

1. `1 <= S.length <= 20000`
1. `S[i]` is `'a'`, `'b'`, or `'c'`

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 128 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        
        for char in S:
            stack.append(char)
            
            if len(stack) >= 3 and stack[-3] + stack[-2] + stack[-1] == 'abc':
                for i in range(3):
                    stack.pop()
            
        return not stack
```

**Solution 2: (DFS)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def isValid(self, S: str) -> bool:
        def chop(s):
            if len(s) == 0:
                result = True
            elif s.find('abc') == -1:
                result = False
            else:
                loc = s.find('abc')
                result = chop(s.strip().replace('abc', ''))
                
            return result
        
        return chop(S)
```