758. Bold Words in String

Given a set of keywords `words` and a string `S`, make all appearances of all keywords in `S` bold. Any letters between `<b>` and `</b>` tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that `words = ["ab", "bc"]` and `S = "aabcd"`, we should return `"a<b>abc</b>d"`. Note that returning `"a<b>a<b>b</b>c</b>d"` would use more tags, so it is incorrect.

**Constraints:**

* `words` has length in range `[0, 50]`.
* `words[i]` has length in range `[1, 10]`.
* `S` has length in range `[0, 500]`.
* All characters in `words[i]` and `S` are lowercase letters.

**Note:** This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-string/

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition**

Let's try to learn which letters end up bold, since the resulting answer will just be the canonical one - we put bold tags around each group of bold letters.

To do this, we'll check for all occurrences of each word and mark the corresponding letters bold.

**Algorithm**

Let's work on first setting `mask[i] = true` if and only if the `i`-th letter is bold. For each starting position `i` in `S`, for each word, if `S[i]` starts with word, we'll set the appropriate letters bold.

Now armed with the correct mask, let's try to output the answer. A letter in position `i` is the first bold letter of the group if `mask[i] && (i == 0 || !mask[i-1]`), and is the last bold letter if `mask[i] && (i == N-1 || !mask[i+1]`). Alternatively, we could use `itertools.groupby` in Python.

Once we know which letters are the first and last bold letters of a group, we know where to put the `"<b>"` and `"</b>"` tags.

```python
class Solution(object):
    def boldWords(self, words, S):
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

**Solution 1: (Brute Force)**
```
Runtime: 112 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i+len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans)
```