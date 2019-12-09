1048. Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say `word1` is a predecessor of `word2` if and only if we can add exactly one letter anywhere in `word1` to make it equal to `word2`.  For example, `"abc"` is a predecessor of `"abac"`.

A word chain is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a predecessor of `word_2`, `word_2` is a predecessor of `word_3`, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

**Example 1:**

```
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
```

**Note:**

1. `1 <= words.length <= 1000`
1. `1 <= words[i].length <= 16`
1. `words[i]` only consists of English lowercase letters.

# Submissions
---
**Solution 1: (DP)**

**Algorithm:**

* we define a dictionary: word: longest length of its string chain
* sort the input array `words` by length
* starting from the shortest word, generating all possible predecessor (a shorter word with exactly one letter missing) from the current word
* if one of the predecessor already exsit in the dp array, which means we already calculated the longest string chain for its precessor. Now all we need to do is add the current word to the word chain by increament the length of the longest string chain by 1. We do this for all the predecessor of the current word. i.e. we update the longest string chain of each branch (each predecessor) for the current word by adding the current word. *The longest string chain for current word is the maximum of the longest string chains of all branches.
* We do this for each word.
* we can find the word with the longest string chain by calling dp[-1], no, just kidding, by finding the largest value in this dictionary, which is the longest string chain existing in the input.

```
Runtime: 156 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key = len):
            maxLen = 0
            for i in range(len(w)):
                predecessor = w[:i] + w[i+1:]
                maxLen = max(maxLen, dp.get(predecessor, 0) + 1)
            dp[w] = maxLen
        return max(dp.values())
```

* Time: $O(M * N)$ where $M$ is the length of the input array and $N$ is the avg length of each word.
* Space: $O(M)$