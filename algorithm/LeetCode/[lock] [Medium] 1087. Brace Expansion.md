1087. Brace Expansion

You are given a string `s` representing a list of words. Each letter in the word has one or more options.

* If there is one option, the letter is represented as is.
* If there is more than one option, then curly braces delimit the options. For example, `"{a,b,c}"` represents options `["a", "b", "c"]`.

For example, if `s = "a{b,c}"`, the first character is always `'a'`, but the second character can be `'b'` or `'c'`. The original list is `["ab", "ac"]`.

Return all words that can be formed in this manner, **sorted** in lexicographical order.

 

**Example 1:**
```
Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
```

**Example 2:**
```
Input: s = "abcd"
Output: ["abcd"]
```

**Constraints:**

* `1 <= s.length <= 50`
* `s` consists of curly brackets `'{}'`, commas `','`, and lowercase English letters.
* `s` is guaranteed to be a valid input.
* There are no nested curly brackets.
* All characters inside a pair of consecutive opening and ending curly brackets are different.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 63 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def expand(self, s: str) -> List[str]:
        arr = []
        idx = 0
        while idx < len(s):
            sub = []
            if s[idx] == '{':
                while s[idx] != '}':
                    if s[idx].isalpha():
                        sub.append(s[idx])
                    idx += 1
            else:
                sub.append(s[idx])
            
            idx += 1 
            arr.append(sub)
        res = []
        
        def backtrack(idx, res, cur_lst):
            if idx == len(arr):
                res.append(''.join(cur_lst))
                return 

            sub_list = arr[idx]
            for symbol in sub_list:
                backtrack(idx + 1, res, cur_lst + [symbol])
        
        backtrack(0, res, [])
        
        return sorted(res)
```
