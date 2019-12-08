522. Longest Uncommon Subsequence II

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A **subsequence** is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

**Example 1:**
```
Input: "aba", "cdc", "eae"
Output: 3
```

**Note:**

* All the given strings' lengths will not exceed 10.
* The length of the given list will be in the range of `[2, 50]`.

# Submissions
---
**Solution 1:**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Checks if string `a` is a subsequence of `b`
        def subseq(a, b):
            if len(a) >= len(b):
                return False
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)
        
        count = collections.Counter(strs)
        # Exlude all strings that occure in `strs` more than once
        exclude = [s for s, c in count.items() if c > 1]
        
        # Rest of the strings go to `check` array
        check = [s for s, c in count.items() if c == 1]
        # Sort by length from longest to shortest
        check.sort(key = lambda x: len(x), reverse = True)
        
        # If there are no items in exclude than longest strings is the answer
        if not exclude:
            return len(check[0])
        
        # Otherwise we need to check remaining strings one by one
        for s in check:
            # Check if string is subsequece of one of excluded
            for e in exclude:
                if subseq(s, e):
                    # If subsequence than mark current string as also exluded and go to next one
                    exclude.append(s)
                    break
                else:
                    # If not a subsequence than it's length is the answer
                    return len(s)
        
        return -1
```