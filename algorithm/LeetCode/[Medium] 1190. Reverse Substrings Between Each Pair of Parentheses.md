1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string `s` that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

**Example 1:**
```
Input: s = "(abcd)"
Output: "dcba"
```

**Example 2:**
```
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
```

**Example 3:**
```
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
```

**Example 4:**
```
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
```

**Constraints:**

* `0 <= s.length <= 2000`
* `s` only contains lower case English characters and parentheses.
* It's guaranteed that all parentheses are balanced.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        content = ''
        for c in s:
            if c == '(':
                stack.append(content)
                content = ''
            elif c == ')':
                content = stack.pop() + content[::-1]
            else:
                content += c
                
        return content
```

**Solution 2: (Stack)**
```
Runtime: 0 ms
Memory: 8.14 MB
```
```c++
class Solution {
public:
    string reverseParentheses(string s) {
        stack<string> stk;
        string cur;
        stk.push("");
        for (auto c: s) {
            if (c == '(') {
                stk.push("");
            } else if (c == ')') {
                cur = stk.top();
                reverse(cur.begin(), cur.end());
                stk.pop();
                stk.top() += cur;
            } else {
                stk.top() += c;
            }
        }
        return stk.top();
    }
};
```
