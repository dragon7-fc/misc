809. Expressive Words

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string `S`, a query word is stretchy if it can be made to be equal to `S` by any number of applications of the following extension operation: choose a group consisting of characters `c`, and add some number of characters `c` to the group so that the size of the group is `3` or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

**Example:**
```
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
```

**Notes:**

* `0 <= len(S) <= 100`.
* `0 <= len(words) <= 100`.
* `0 <= len(words[i]) <= 100`.
* `S` and all words in words consist only of lowercase letters

# Solution
---
## Approach #1: Run Length Encoding [Accepted]
**Intuition**

For some word, write the head character of every group, and the count of that group. For example, for "abbcccddddaaaaa", we'll write the "key" of "abcda", and the "count" `[1,2,3,4,5]`.

Let's see if a word is stretchy. Evidently, it needs to have the same key as `S`.

Now, let's say we have individual counts `c1 = S.count[i]` and `c2 = word.count[i]`.

* If `c1 < c2`, then we can't make the ith group of word equal to the ith word of `S` by adding characters.

* If `c1 >= 3`, then we can add letters to the ith group of word to match the ith group of `S`, as the latter is extended.

* Else, if `c1 < 3`, then we must have `c2 == c1` for the ith groups of word and `S` to match.

```python
class Solution(object):
    def expressiveWords(self, S, words):
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(QK)$, where $Q$ is the length of words (at least `1`), and $K$ is the maximum length of a word.

* Space Complexity: $O(K)$.

# Submissions
---
**Solution: (Run Length Encoding)**
```
Runtime: 48 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans
```