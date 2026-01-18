3406. Find the Lexicographically Largest String From the Box II

You are given a string `word`, and an integer `numFriends`.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

* `word` is split into `numFriends` non-empty strings, such that no previous round has had the exact same split.
* All the split words are put into a box.

Find the **lexicographically largest** string from the box after all the rounds are finished.

A string `a` is lexicographically smaller than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.
If the first `min(a.length, b.length)` characters do not differ, then the shorter string is the lexicographically smaller one.

 

**Example 1:**
```
Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation:

All possible splits are:

"d" and "bca".
"db" and "ca".
"dbc" and "a".
```

**Example 2:**
```
Input: word = "gggg", numFriends = 4

Output: "g"

Explanation:

The only possible split is: "g", "g", "g", and "g".
```
 

**Constraints:**

* `1 <= word.length <= 2 * 10^5`
* `word` consists only of lowercase English letters.
* `1 <= numFriends <= word.length`

# Submissions
---
**Solution 1: (track the start index of max substring)**

Intuition
The max substring must always end with the last char. But in case there are too many numFriends, might cut a few ending chars from the max substring to satisfy numFriends.

Approach
First find max substring. Then shorten the max substring from the end to meed numFriends.

We scan from left to right, recording the start index of max substring.
If current char == max_substring[0], then compare next char with max_substring[1], 2nd next char with max_substring[2], ...
We use 'offset' to indicate which char after max_substring[0] we are comparing.

If current char < max_substring[0], or max_substring[offset] if we are continuing the equality compare from last char, then no need to update start index of max substring. If we are continue the equality compare from last char, need to clear 'offset'

If current char > max_substring[0], or max_substring[offset] if we are continuing the equaltiy compare from last char, then current char is better as the start index of max string. We update the start index and continue.

Complexity
Time complexity: O(n)
Space complexity: O(1)

```
Runtime: 135 ms, Beats 100.00%
Memory: 21.80 MB, Beats 36.36%
```
```python3
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        n = len(word)
        mx_i,offset = 0,0
        for i in range(1,n):
            v,mx_v = word[i],word[mx_i+offset]
            if v==mx_v:
                offset+=1
            elif v<mx_v:
                offset = 0
            elif v>mx_v:
                if word[i-offset]>=word[i]:
                    mx_i = i-offset
                else:
                    mx_i = i
                offset = 0
        extra = max(0,numFriends - mx_i - 1)
        if extra:
            return word[mx_i:-extra]
        return word[mx_i:]
```
