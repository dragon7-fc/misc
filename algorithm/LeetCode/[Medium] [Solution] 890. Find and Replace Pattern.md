890. Find and Replace Pattern

You have a list of `words` and a `pattern`, and you want to know which words in `words` matches the `pattern`.

A word matches the pattern if there exists a permutation of letters `p` so that after replacing every letter `x` in the pattern with `p(x)`, we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

**Example 1:**
```
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
```

**Note:**

* `1 <= words.length <= 50`
* `1 <= pattern.length = words[i].length <= 20`

# Solution
---
## Approach 1: Two Maps
**Intuition and Algorithm**

If say, the first letter of the pattern is `"a"`, and the first letter of the word is `"x"`, then in the permutation, `"a"` must map to `"x"`.

We can write this bijection using two maps: a forward map $\text{m1}$ and a backwards map $\text{m2}$.

$\text{m1} : \text{"a"} \rightarrow \text{"x"}$ $\text{m2} : \text{"x"} \rightarrow \text{"a"}$

Then, if there is a contradiction later, we can catch it via one of the two maps. For example, if the (word, pattern) is `("aa", "xy")`, we will catch the mistake in $\text{m1}$ (namely, $\text{m1}(\text{"a"}) = \text{"x"} = \text{"y"}$). Similarly, with (word, pattern) = `("ab", "xx")`, we will catch the mistake in $\text{m2}$.

```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
```

**Complexity Analysis**

* Time Complexity: $O(N * K)$, where $N$ is the number of words, and $K$ is the length of each word.

* Space Complexity: $O(N * K)$, the space used by the answer.

## Approach 2: One Map
**Intuition and Algorithm**

As in Approach 1, we can have some forward map $\text{m1} : \mathbb{L} \rightarrow \mathbb{L}$, where $\mathbb{L}$ is the set of letters.

However, instead of keeping track of the reverse map $\text{m2}$, we could simply make sure that every value $\text{m1}(x)$ in the codomain is reached at most once. This would guarantee the desired permutation exists.

So our algorithm is this: after defining $\text{m1}(x)$ in the same way as Approach 1 (the forward map of the permutation), afterwards we make sure it reaches distinct values.

```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)
```

**Complexity Analysis**

* Time Complexity: $O(N * K)$, where $N$ is the number of words, and $K$ is the length of each word.

* Space Complexity: $O(N * K)$, the space used by the answer.

# Submissions
---
**Solution: (One Map)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)
```

**Solution 1: (Hash Table)**
```
Runtime: 3 ms
Memory Usage: 8.3 MB
```
```c++
class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        unordered_map<char, char> m;
        unordered_set<char> seen;
        vector<string> ans;
        for (auto word: words) {
            m.clear();
            seen.clear();
            for (int i = 0; i < pattern.size(); i ++) {
                if (!m.count(pattern[i]) && seen.count(word[i]) || 
                    m.count(pattern[i]) && m[pattern[i]] != word[i])
                    break;
                else if (!m.count(pattern[i])) {
                    m[pattern[i]] = word[i];
                    seen.insert(word[i]);
                }
                if (i == pattern.size()-1)
                    ans.push_back(word);
            }
        }
        return ans;
    }
};
```
