616. Add Bold Tag in String

Given a string s and a list of strings dict, you need to add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

**Example 1:**
```
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
```

**Example 2:**
```
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
```

**Constraints:**

* The given dict won't contain duplicates, and its length won't exceed `100`.
* All the strings in input have length in range `[1, 1000]`.

**Note:** This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition**

Let's try to learn which letters end up bold, since the resulting answer will just be the canonical one - we put bold tags around each group of bold letters.

To do this, we'll check for all occurrences of each word and mark the corresponding letters bold.

**Algorithm**

Let's work on first setting `mask[i] = true` if and only if the `i`-th letter is bold. For each starting position `i` in `S`, for each word, if `S[i]` starts with word, we'll set the appropriate letters bold.

Now armed with the correct mask, let's try to output the answer. A letter in position `i` is the first bold letter of the group if `mask[i] && (i == 0 || !mask[i-1])`, and is the last bold letter if `mask[i] && (i == N-1 || !mask[i+1])`. Alternatively, we could use `itertools.groupby` in Python.

Once we know which letters are the first and last bold letters of a group, we know where to put the `"<b>"` and `"</b>"` tags.

```python
class Solution(object):
    def boldWords(self, S, words):
        N = len(S)
        mask = [False] * N
        for i in xrange(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in xrange(i, min(i+len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans)
```

**Complexity Analysis**

* Time Complexity: $O(N\sum w_i)$, where $N$ is the length of `S` and $w_i$ is the sum of `W`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 180 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        N = len(s)
        mask = [False] * N
        for i in range(N):
            prefix = s[i:]
            for word in dict:
                if prefix.startswith(word):
                    for j in range(i, min(i+len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(s, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans)
```

**Solution 2: (String)**
```
Runtime: 168 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        test = [False for i in range(len(s))]

        for word in dict:
            w_s = len(word)
            for i in range(len(s)-w_s+1):
                if s[i:i+w_s] == word:
                    test[i:i+w_s] = [True for i in range(w_s)]
        
        res = []
        for i in range(len(test)):
            if test[i]:
                if i == 0 or not test[i-1]:
                    res.append("<b>")

                res.append(s[i])
                
                if i == len(test)-1 or not test[i+1]:
                    res.append("</b>")
            else:
                res.append(s[i])

        return "".join(res)
```
