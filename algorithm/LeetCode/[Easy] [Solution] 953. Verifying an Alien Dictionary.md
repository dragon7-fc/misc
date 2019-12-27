953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given words are sorted lexicographicaly in this alien language.

 

**Example 1:**
```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

**Example 2:**
```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```

**Example 3:**
```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
```

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 20`
* `order.length == 26`
* All characters in `words[i]` and `order` are English lowercase letters.

# Solution
---
## Approach 1: Check Adjacent Words
**Intuition**

The words are sorted lexicographically if and only if adjacent words are. This is because order is transitive: `a <= b` and `b <= c` implies `a <= c`.

**Algorithm**

Let's check whether all adjacent words `a` and `b` have `a <= b`.

To check whether `a <= b` for two adjacent words `a` and `b`, we can find their first difference. For example, `"applying"` and `"apples"` have a first difference of `y` vs `e`. After, we compare these characters to the index in order.

Care must be taken to deal with the blank character effectively. If for example, we are comparing `"app"` to `"apply"`, this is a first difference of `(null)` vs `"l"`.

```python
class Solution(object):
    def isAlienSorted(self, words, order):
        order_index = {c: i for i, c in enumerate(order)}

        for i in xrange(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in xrange(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{C})$, where $\mathcal{C}$ is the total content of words.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1:**
```
Runtime: 32 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key= lambda word: [order.index(c) for c in word])
```