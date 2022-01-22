1794. Count Pairs of Equal Substrings With Minimum Difference

You are given two strings `firstString` and `secondString` that are **0-indexed** and consist only of lowercase English letters. Count the number of index quadruples (i,j,a,b) that satisfy the following conditions:

* `0 <= i <= j < firstString.length`
* `0 <= a <= b < secondString.length`
* The substring of `firstString` that starts at the `i`th character and ends at the `j`th character (inclusive) is equal to the substring of `secondString` that starts at the `a`th character and ends at the `b`th character (inclusive).
* `j - a` is the **minimum** possible value among all quadruples that satisfy the previous conditions.

Return the **number** of such quadruples.

**Example 1:**
```
Input: firstString = "abcd", secondString = "bccda"
Output: 1
Explanation: The quadruple (0,0,4,4) is the only one that satisfies all the conditions and minimizes j - a.
```

**Example 2:**
```
Input: firstString = "ab", secondString = "cd"
Output: 0
Explanation: There are no quadruples satisfying all the conditions.
```

**Constraints:**

* `1 <= firstString.length, secondString.length <= 2 * 10^5`
* Both strings consist only of lowercase English letters.

# Submissions
---
**SOlution 1: (Hash Table)**
```
Runtime: 230 ms
Memory Usage: 16.2 MB
```
```python
class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        #define a map to hold the leftmost indices of each char
        indices = {}
        
        #iterate the firstString to get the leftmost indices of each char
        for i,c in enumerate(firstString):
            if c not in indices:
                indices[c]=i

        #define two variables to hold the result and dist==INF        
        result,dist = 0, float("inf")
        
        # now iterate the secondString :
        # 1. for each char check if present in firstString
        for a in range(len(secondString)):
            c = secondString[a]
            #2. if char present in both, get the dist of indices
            if c in indices:
                # new smallest distance found, update the distance & result
                if indices[c]-a<dist:
                    dist=indices[c]-a
                    result=1
                # else another instance of smallest distance found, increase result by 1
                elif indices[c]-a==dist:
                    result+=1
        return result
```
