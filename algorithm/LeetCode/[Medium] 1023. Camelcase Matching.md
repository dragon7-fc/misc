1023. Camelcase Matching

A query word matches a given `pattern` if we can insert **lowercase** letters to the `pattern` word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of `queries`, and a `pattern`, return an answer list of booleans, where `answer[i]` is true if and only if `queries[i]` matches the pattern.

 

**Example 1:**
```
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
```

**Example 2:**
```
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: 
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
```

**Example 3:**
```
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: 
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
```

**Note:**

1. `1 <= queries.length <= 100`
1. `1 <= queries[i].length <= 100`
1. `1 <= pattern.length <= 100`
1. All strings consists only of lower and upper case English letters.

# Submissions
---
**Solution 1: (Pointer, String)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        N = len(pattern)
        
        def is_camelcase(query):
            p_i = 0
            for c in query:
                if p_i < N:
                    if c == pattern[p_i]:
                        p_i += 1
                    elif c.isupper():
                        return False
                elif p_i == N:
                    if c.isupper():
                        return False
            if p_i < N:
                return False
            return True
                
        return map(is_camelcase, queries)
```