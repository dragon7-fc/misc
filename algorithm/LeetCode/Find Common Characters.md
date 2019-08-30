Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
```
Input: ["bella","label","roller"]
Output: ["e","l","l"]
```

Example 2:
```
Input: ["cool","lock","cook"]
Output: ["c","o"]
```

Note:

1. 1 <= A.length <= 100
1. 1 <= A[i].length <= 100
1. A[i][j] is a lowercase letter

Solution: (52ms)
```python
class Solution:
    def commonChars(self, A: List[str]) -> L   ist[str]:
        d = {}
        for i in A:
        unique = list(set(i))
        for char in unique:
            if char in d.keys():
                d[char] += [i.count(char)]
            else:
                d[char] = [i.count(char)]
        ans = []
        for key in d.keys():
            if len(d[key]) == len(A):
                ans += [key]*min(d[key])
        return ans        
```

