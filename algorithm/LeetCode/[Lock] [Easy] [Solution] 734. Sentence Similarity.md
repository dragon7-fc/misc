734. Sentence Similarity

We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am",happy","with","leetcode"]`.

Given two sentences `sentence1` and `sentence2` each represented as a string array and given an array of string pairs `similarPairs` where `similarPairs[i] = [xi, yi]` indicates that the two words `xi` and `yi` are similar.

Return `true` if `sentence1` and `sentence2` are similar, or `false` if they are not similar.

Two sentences are similar if:

* They have **the same length** (i.e. the same number of words)
* `sentence1[i]` and `sentence2[i]` are similar.

Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words `a` and `b` are similar and the words `b` and `c` are similar, `a` and `c` are **not necessarily similar**.

 

**Example 1:**
```
Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
```

**Example 2:**
```
Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
Output: true
Explanation: A word is similar to itself.
```

**Example 3:**
```
Input: sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
Output: false
Explanation: As they don't have the same length, we return false.
```

**Constraints:**

* `1 <= sentence1.length, sentence2.length <= 1000`
* `1 <= sentence1[i].length, sentence2[i].length <= 20`
* `sentence1[i]` and `sentence2[i]` consist of lower-case and upper-case English letters.
* `0 <= similarPairs.length <= 1000`
* `similarPairs[i].length == 2`
* `1 <= xi.length, yi.length <= 20`
* `xi` and `yi` consist of lower-case and upper-case English letters.
* All the pairs `(xi, yi)` are **distinct**.

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 44 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        pairset = set(map(tuple, similarPairs))
        return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset
                   for w1, w2 in zip(sentence1, sentence2))
```

**Solution 2: (Hash Table, Set)**
```
Runtime: 9 ms
Memory: 12.5 MB
```
```c++
class Solution {
public:
    bool areSentencesSimilar(vector<string>& sentence1, vector<string>& sentence2, vector<vector<string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }
        unordered_map<string,unordered_set<string>> m;
        for (auto sp: similarPairs) {
            m[sp[0]].insert(sp[1]);
            m[sp[1]].insert(sp[0]);
        }
        for (int i = 0; i < sentence1.size(); i ++) {
            if (sentence1[i] != sentence2[i] && !m[sentence1[i]].count(sentence2[i])) {
                return false;
            }
        }
        return true;
    }
};
```
