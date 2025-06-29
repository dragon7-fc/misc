966. Vowel Spellchecker

Given a `wordlist`, we want to implement a spellchecker that converts a query word into a correct word.

For a given `query` word, the spell checker handles two categories of spelling mistakes:

* Capitalization: If the query matches a word in the wordlist (**case-insensitive**), then the query word is returned with the same case as the case in the wordlist.
    * Example: `wordlist = ["yellow"], query = "YellOw": correct = "yellow"`
    * Example: `wordlist = ["Yellow"], query = "yellow": correct = "Yellow"`
    * Example: `wordlist = ["yellow"], query = "yellow": correct = "yellow"`
* Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
    * Example: `wordlist = ["YellOw"], query = "yollow": correct = "YellOw"`
    * Example: `wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)`
    * Example: `wordlist = ["YellOw"], query = "yllw": correct = "" (no match)`

In addition, the spell checker operates under the following precedence rules:

* When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
* When the query matches a word up to capitlization, you should return the first such match in the wordlist.
* When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
* If the query has no matches in the wordlist, you should return the empty string.

Given some `queries`, return a list of words `answer`, where `answer[i]` is the correct word for `query = queries[i]`.

 

**Example 1:**
```
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```

**Note:**

* `1 <= wordlist.length <= 5000`
* `1 <= queries.length <= 5000`
* `1 <= wordlist[i].length <= 7`
* `1 <= queries[i].length <= 7`
* All strings in `wordlist` and `queries` consist only of english letters.

# Solution
---
## Approach 1: HashMap
**Intuition and Algorithm**

We analyze the 3 cases that the algorithm needs to consider: when the query is an exact match, when the query is a match up to capitalization, and when the query is a match up to vowel errors.

In all 3 cases, we can use a hash table to query the answer.

* For the first case (exact match), we hold a set of words to efficiently test whether our query is in the set.
* For the second case (capitalization), we hold a hash table that converts the word from its lowercase version to the original word (with correct capitalization).
* For the third case (vowel replacement), we hold a hash table that converts the word from its lowercase version with the vowels masked out, to the original word.

The rest of the algorithm is careful planning and reading the problem carefully.

```python
class Solution(object):
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{C})$, where $\mathcal{C}$ is the total content of wordlist and queries.

* Space Complexity: $O(\mathcal{C})$.

# Submissions
---
**Solution: (HashMap)**
```
Runtime: 192 ms
Memory Usage: 17 MB
```
```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)
```

**Solution i: (Hash Table)**
```
Runtime: 41 ms, Beats 59.41%
Memory: 42.98 MB, Beats 27.65%
```
```c++
class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        int i;
        string wl, wlv, ql, qlv, VOWEL = "aeiou";
        unordered_map<string,string> m, ml, mlv;
        vector<string> ans;
        for (auto w: wordlist) {
            m[w] = w;
            wl = "";
            for (auto c: w) {
                wl += tolower(c);
            }
            if (!ml.count(wl)) {
                ml[wl] = w;
            }
            wlv = wl;
            for (i = 0; i < wlv.length(); i++) {
                if (VOWEL.find(wlv[i]) != string::npos) {
                    wlv[i] = '*';
                }
            }
            if (!mlv.count(wlv)) {
                mlv[wlv] = w;
            }
        }
        for (auto q: queries) {
            if (m.count(q)) {
                ans.push_back(m[q]);
                continue;
            }
            ql = "";
            for (auto c: q) {
                ql += tolower(c);
            }
            if (ml.count(ql)) {
                ans.push_back(ml[ql]);
                continue;
            }
            qlv = ql;
            for (i = 0; i < qlv.length(); i ++) {
                if (VOWEL.find(qlv[i]) != string::npos) {
                    qlv[i] = '*';
                }
            }
            if (mlv.count(qlv)) {
                ans.push_back(mlv[qlv]);
            } else {
                ans.push_back("");
            }
        }
        return ans;
    }
};
```
