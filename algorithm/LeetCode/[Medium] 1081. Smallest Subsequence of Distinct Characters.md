1081. Smallest Subsequence of Distinct Characters

Return the lexicographically smallest subsequence of `text` that contains all the distinct characters of `text` exactly once.

 

**Example 1:**
```
Input: "cdadabcc"
Output: "adbc"
```

**Example 2:**
```
Input: "abcd"
Output: "abcd"
```

**Example 3:**
```
Input: "ecbacba"
Output: "eacb"
```

**Example 4:**
```
Input: "leetcode"
Output: "letcod"
```

**Note:**

1. `1 <= text.length <= 1000`
1. `text` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Stack, Hash Table)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last_place = {}
        # record all the last-chance places for each distinct character
        for i in range(len(text)):
            last_place[text[i]] = i
        
        soln_stack = []
        dist_set = set()
        # iterate through and use a stack and set to keep track of the solution
        for i in range(len(text)):
            #while:
            #1. the stack is not empty
            #2. the current character is lexographically before the last one in the stack
            #3. the last character in the stack isn't the last of its kind in the string
            #4. the current character isn't already in the stack (as kept track by the set)
            while soln_stack and text[i] < soln_stack[-1] and i < last_place[soln_stack[-1]] and text[i] not in dist_set:
                #remove the last character from the stack and set
                dist_set.remove(soln_stack[-1])
                soln_stack.pop()
            if text[i] not in dist_set:
                #add character to stack and set if not already there
                soln_stack.append(text[i])
                dist_set.add(text[i])
        
        return ''.join(soln_stack)
```