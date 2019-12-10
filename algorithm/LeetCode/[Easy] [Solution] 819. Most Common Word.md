819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

**Example:**
```
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
```

**Note:**

* `1 <= paragraph.length <= 1000`.
* `0 <= banned.length <= 100`.
* `1 <= banned[i].length <= 10`.
* The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
* paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
* There are no hyphens or hyphenated words.
* Words only consist of letters, never apostrophes or other punctuation symbols.

# Solution
---
## Approach #1: Counting [Accepted]
**Intuition**

This problem is about the implementation, as the question tells us how to solve the problem. We'll count each word separately, ignoring punctuation and converting each word to lowercase. The word with the highest frequency that isn't in the banned list is the answer.

**Algorithm**

We'll need some `count` of words (converted to lowercase) that we have seen in the paragraph. As we iterate through the paragraph, we will collect these words (with punctuation removed and converted to lowercase).

There are two ways we could try to collect these words: we could try to split the paragraph (delimited by spaces) and then clean up the fragment like `"Bob!"` to be `"bob"`. Or, we could add characters one by one to build the next word, stopping when we reach a character that isn't a letter.

For each word (lowercase, and free of punctuation), we'll update our count and update the answer if the count of that word is highest (and the word is not banned.)

```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(P + B)$, where $P$ is the size of paragraph and $B$ is the size of banned.

* Space Complexity: $O(P + B)$, to store the count and the banned set.

# Submissions
---
**Solution:**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans
```