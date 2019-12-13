1156. Swap For Longest Repeated Character Substring

Given a string `text`, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

 

**Example 1:**
```
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
```

**Example 2:**
```
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
```

**Example 3:**
```
Input: text = "aaabbaaa"
Output: 4
```

**Example 4:**
```
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
```

**Example 5:**
```
Input: text = "abcdef"
Output: 1
```

**Constraints:**

* `1 <= text.length <= 20000`
* text consist of lowercase English characters only.

# Submissions
---
**Solution 1:**

**Intuition**
There are only 2 cases that we need to take care of:

* extend the group by 1
* merge 2 adjacent groups together, which are separated by only 1 character

**Explanation**
For `S = "AAABBCB"`
`[[c, len(list(g))] for c, g in groupby(S)] --> [[A,3],[B,2],[C,1],[B,1]]`
collections.Counter(S) --> {A:3, B:3, C:1}
With these two data, calculate the best solution for the two cases above.


**Complexity**
* Time $O(N)$
* Space $O(N)$

```
Runtime: 68 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(text)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res
            
```