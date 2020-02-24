720. Longest Word in Dictionary

Given a list of strings `words` representing an English Dictionary, find the longest word in `words` that can be built one character at a time by other words in `words`. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

**Example 1:**
```
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
```

**Example 2:**
```
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
```

**Note:**

* All the strings in the input will only contain lowercase letters.
* The length of words will be in the range `[1, 1000]`.
* The length of words[i] will be in the range `[1, 30]`.

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition**

For each word, check if all prefixes `word[:k]` are present. We can use a Set structure to check this quickly.

**Algorithm**

Whenever our found word would be superior, we check if all it's prefixes are present, then replace our answer.

Alternatively, we could have sorted the words beforehand, so that we know the word we are considering would be the answer if all it's prefixes are present.

```python
class Solution(object):
    def longestWord(self, words):
    ans = ""
    wordset = set(words)
    for word in words:
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            if all(word[:k] in wordset for k in xrange(1, len(word))):
                ans = word

    return ans
```

Alternate Implementation

```python
class Solution(object):
    def longestWord(self, words):
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in xrange(1, len(word))):
                return word

        return ""
```

**Complexity Analysis**

* Time complexity : $O(\sum w_i^2)$, where $w_i$ is the length of `words[i]`. Checking whether all prefixes of `words[i]` are in the set is $(\sum w_i^2)$.

* ace complexity : $(\sum w_i^2)$ to create the substrings.

## roach #2: Trie + Depth-First Search [Accepted]
**tuition**

As prefixes of strings are involved, this is usually a natural fit for a trie (a prefix tree.)

**gorithm**

Put every word in a trie, then depth-first-search from the start of the trie, only searching nodes that ended a word. Every node found (except the root, which is a special case) then represents a word with all it's prefixes present. We take the best such word.

In Python, we showcase a method using `efaultdict` while in Java, we stick to a more general object-oriented approach.

```python
class Solution(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
```

**mplexity Analysis**

* me Complexity: $(\sum w_i)$, where $_i$ is the length of `ords[i]`. This is the complexity to build the trie and to search it.

If we used a BFS instead of a DFS, and ordered the children in an array, we could drop the need to check whether the candidate word at each node is better than the answer, by forcing that the last node visited will be the best answer.

* ace Complexity: $(\sum w_i)$, the space used by our trie.

# Submissions
---
**Solution: (Brute Force)**
```
Runtime: 68 ms
Memory Usage: 13.1 MB
```
```python
import functools
class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""
```

**Solution 2: (Trie + Depth-First Search)**
```
Runtime: 120 ms
Memory Usage: 13.4 MB
```
```python
import functools
class Solution:
    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie)[END] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
            
```