1065. Index Pairs of a String

Given a `text` string and `words` (a list of strings), return all index pairs `[i, j]` so that the substring `text[i]...text[j]` is in the list of `words`.

 

**Example 1:**
```
Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]
```

**Example 2:**
```
Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
```

**Note:**

* All strings contains only lowercase English letters.
* It's guaranteed that all strings in words are different.
* `1 <= text.length <= 100`
* `1 <= words.length <= 20`
* `1 <= words[i].length <= 50`
* Return the pairs `[i,j]` in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 40 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for i in range(len(text)):
            for word in words:
                if text[i:].startswith(word):
                    ans += [[i, i + len(word)-1]]
        
        return sorted(ans)
```

**Solution 2: (Hash Set)**
```
Runtime: 22 ms
Memory: 15.2 MB
```
```c++
class Solution {
public:
    vector<vector<int>> indexPairs(string text, vector<string>& words) {
        unordered_set<string> wordsSet(words.begin(), words.end());
        vector<vector<int>> ans;
        for (int i = 0; i < text.size(); i++) {
            for (int j = i; j < text.size(); j++) {
                if (wordsSet.count(text.substr(i, j - i + 1))) {
                    ans.push_back({i, j});
                }
            }
        }
        return ans;
    }
};
```

**Solution 3: (Trie)**
```
Runtime: 9 ms
Memory: 9.9 MB
```
```c++
struct TrieNode {
    bool flag;
    map<char, TrieNode*> next;
};
struct Trie {
    TrieNode* root;

    Trie() { root = new TrieNode(); }

    void insert(string word) {
        TrieNode* p = root;
        for (int i = 0; i < word.length(); ++i) {
            if ((p->next).count(word[i]) == 0) {
                (p->next).insert(make_pair(word[i], new TrieNode()));
            }
            p = (p->next)[word[i]];
        }
        p->flag = true;
    }
};

class Solution {
public:
    vector<vector<int>> indexPairs(string text, vector<string>& words) {
        Trie trie;
        for (const string& word : words) {
            trie.insert(word);
        }
        vector<vector<int>> result;
        for (int i = 0; i < text.size(); i++) {
            TrieNode* p = trie.root;
            for (int j = i; j < text.size(); j++) {
                if ((p->next).count(text[j]) == 0) {
                    break;
                }
                p = (p->next)[text[j]];
                if (p->flag) {
                    result.push_back({i, j});
                }
            }
        }
        return result;
    }
};
```
