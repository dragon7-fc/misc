1100. Find K-Length Substrings With No Repeated Characters

Given a string `S`, return the number of substrings of length `K` with no repeated characters.

 

**Example 1:**
```
Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
```

**Example 2:**
```
Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.
```

**Note:**

* `1 <= S.length <= 10^4`
* All characters of S are lowercase English letters.
* `1 <= K <= 10^4`

# Submissions
---
**Solution 1: (Sliding Window, OrderedDict)**
```
Runtime: 88 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        N = len(S)
        i, j = 0, 0
        w = collections.OrderedDict()
        ans = 0
        while j < N:
            if S[j] in w:
                i = w[S[j]] + 1
                w.popitem(last=False)
                while S[j] in w:
                    w.popitem(last=False)
                w[S[j]] = j
            elif j-i+1 == K:
                w[S[j]] = j
                del w[S[i]]
                i += 1
                ans += 1
            else:
                w[S[j]] = j
            j += 1
        return ans
```

**Solution 2: (Sliding Window, Set)**
```
Runtime: 84 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        i = j = ans = 0
        inView = set()
        
        while i < len(S):
            if S[i] not in inView:
                inView.add(S[i])
                if i - j == K - 1:
                    ans += 1
                    inView.remove(S[j])
                    j += 1
                i += 1
            else:
                inView.remove(S[j])
                j += 1
                
        return ans
```