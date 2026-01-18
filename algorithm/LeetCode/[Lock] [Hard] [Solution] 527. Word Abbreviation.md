527. Word Abbreviation

Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

1. Begin with the first character and then the number of characters abbreviated, which followed by the last character.
1. If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
1. If the abbreviation doesn't make the word shorter, then keep it as original.

**Example:**
```
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
```

**Note:**

* Both n and the length of each word will not exceed 400.
* The length of each word is greater than 1.
* The words consist of lowercase English letters only.
* The return answers should be in **the same order** as the original array.

# Solution
---
## Approach #1: Greedy [Accepted]
**Intuition**

Let's choose the shortest abbreviation for each word. Then, while we have duplicates, we'll increase the length of all duplicates.

**Algorithm**

For example, let's say we have `"aabaaa", "aacaaa", "aacdaa"`, then we start with `"a4a", "a4a", "a4a"`. Since these are duplicated, we lengthen them to `"aa3a", "aa3a", "aa3a"`. They are still duplicated, so we lengthen them to `"aab2a", "aac2a", "aac2a"`. The last two are still duplicated, so we lengthen them to `"aacaaa", "aacdaa"`.

Throughout this process, we were tracking an index `prefix[i]` which told us up to what index to take the prefix to. For example, `prefix[i] = 2` means to take a prefix of `word[0], word[1], word[2]`.

```python
class Solution(object):
    def wordsAbbreviation(self, words):
        def abbrev(word, i = 0):
            if (len(word) - i <= 3): return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        N = len(words)
        ans = map(abbrev, words)
        prefix = [0] * N

        for i in xrange(N):
            while True:
                dupes = set()
                for j in xrange(i+1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes: break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(C^2)$ where $C$ is the number of characters across all words in the given array.

* Space Complexity: $O(C)$.

## Approach #2: Group + Least Common Prefix [Accepted]
**Intuition and Algorithm**

Two words are only eligible to have the same abbreviation if they have the same first letter, last letter, and length. Let's group each word based on these properties, and then sort out the conflicts.

In each group `G`, if a word `W` has a longest common prefix `P` with any other word `X` in `G`, then our abbreviation must contain a prefix of more than `|P|` characters. The longest common prefixes must occur with words adjacent to `W` (in lexicographical order), so we can just sort `G` and look at the adjacent words.

```python
class Solution(object):
    def wordsAbbreviation(self, words):
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in words]

        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first, last), enum_words in groups.iteritems():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2 = enum_words[i-1][0]
                    lcp[i] = longest_common_prefix(word, word2)
                    lcp[i-1] = max(lcp[i-1], lcp[i])

            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= 1:
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(C \log C)$ where $C$ is the number of characters across all words in the given array. The complexity is dominated by the sorting step.

* Space Complexity: $O(C)$.

## Approach #3: Group + Trie [Accepted]
**Intuition and Algorithm**

As in Approach #1, let's group words based on length, first letter, and last letter, and discuss when words in a group do not share a longest common prefix.

Put the words of a group into a trie (prefix tree), and count at each node (representing some prefix `P`) the number of words with prefix `P`. If the count is 1, we know the prefix is unique.

```python
class Solution(object):
    def wordsAbbreviation(self, words):
        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        ans = [None] * len(words)
        Trie = lambda: collections.defaultdict(Trie)
        COUNT = False
        for group in groups.itervalues():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1: break
                    cur = cur[letter]
                if len(word) - i - 1 > 1:
                    ans[index] = word[:i] + str(len(word) - i - 1) + word[-1]
                else:
                    ans[index] = word
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(C)$ where $C$ is the number of characters across all words in the given array.

* Space Complexity: $O(C)$.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 208 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        def abbrev(word, i = 0):
            if (len(word) - i <= 3): return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        N = len(words)
        ans = list(map(abbrev, words))
        prefix = [0] * N

        for i in range(N):
            while True:
                dupes = set()
                for j in range(i+1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes: break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans
```

**Solution 2: (Group + Least Common Prefix)**
```
Runtime: 76 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in words]

        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first, last), enum_words in groups.items():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2 = enum_words[i-1][0]
                    lcp[i] = longest_common_prefix(word, word2)
                    lcp[i-1] = max(lcp[i-1], lcp[i])

            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= 1:
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last

        return ans
```

**Solution 1: (Group + Trie)**
```
Runtime: 516 ms
Memory Usage: 24.9 MB
```
```python
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        ans = [None] * len(words)
        Trie = lambda: collections.defaultdict(Trie)
        COUNT = False
        for group in groups.values():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1: break
                    cur = cur[letter]
                if len(word) - i - 1 > 1:
                    ans[index] = word[:i] + str(len(word) - i - 1) + word[-1]
                else:
                    ans[index] = word
        return ans
```

**Solution 2: (Trie, group)**

    words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
    l2e: like
    god: god
    i6l: i n t e r n a l, 
         i n t e r v a l
           ^       ^    
    me: me
    i6t: internet
    i7n: intension, intrusion
         inte 4  n  intr 4  n

query 1     2    3    4    5    6x
    root -> n -> t -> e -> r -> n -> a -> l
cnt   1     1    1    1    1    1    1
      2     2    2    2    2 -> v -> a -> l
                                1    1

```
Runtime: 170 ms, Beats 12.90%
Memory: 332.26 MB, Beats 6.45%
```
```c++
class Solution {
    struct TrieNode {
        TrieNode *child[26] = {nullptr};
        int cnt = 0;
    };
public:
    vector<string> wordsAbbreviation(vector<string>& words) {
        int n = words.size(), i;
        string s;
        unordered_map<string, vector<pair<string, int>>> mp;  // pattern, {word, index}
        vector<string> ans(n);
        for (i = 0; i < n; i ++) {
            if (words[i].length() > 3) {
                s = words[i][0] + to_string(words[i].length() - 2) + words[i].back();
                mp[s].push_back({words[i], i});
            } else {
                ans[i] = words[i];
            }
        }
        for (auto &[p, wv]: mp) {
            TrieNode *root = new TrieNode(), *node;
            for (auto &[w, wi]: wv) {
                node = root;
                for (i = 1; i < w.size(); i ++) {
                    node->cnt += 1;
                    if (!node->child[w[i] - 'a']) {
                        node->child[w[i] - 'a'] = new TrieNode();
                    }
                    node = node->child[w[i] - 'a'];
                }
            }
            for (auto &[w, wi]: wv) {
                node = root;
                for (i = 1; i < w.length(); i ++) {
                    if (node->cnt == 1) {
                        break;
                    }
                    node = node->child[w[i] - 'a'];
                }
                if (w.length() - i - 1 > 1) {
                    s = w.substr(0, i) + to_string(w.length() - i - 1) + p.back();
                    ans[wi] = s;
                } else {
                    ans[wi] = words[wi];
                }
            }
        }
        return ans;
    }
};
```
