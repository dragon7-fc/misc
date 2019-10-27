467. Unique Substrings in Wraparound String

Consider the string `s` to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so `s` will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string `p`. Your job is to find out how many unique non-empty substrings of `p` are present in `s`. In particular, your input is the string `p` and you need to output the number of different non-empty substrings of `p` in the string s.

**Note:** `p` consists of only lowercase English letters and the size of `p` might be over 10000.

**Example 1:**
```
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
```

**Example 2:**
```
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
```

**Example 3:**
```
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
```

# Submissions
---
**Solution 1:**
```
Runtime: 104 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        L = len(p)
        if L == 0: return 0
        DP = [1] * L
        dic = collections.defaultdict(int)
        dic[p[0]] = 1
        for i in range(1, L):
            if ord(p[i]) - ord(p[i-1]) == 1 or (p[i] == 'a' and p[i-1] == 'z'):
                DP[i] = DP[i-1] + 1
            else:
                DP[i] = 1
            dic[p[i]] = max(dic[p[i]], DP[i])
        return sum(dic.values())
```