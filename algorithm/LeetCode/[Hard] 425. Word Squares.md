425. Word Squares

Given an array of unique strings `words`, return all the word squares you can build from `words`. The same word from words can be used multiple times. You can return the answer in any order.

A sequence of strings forms a valid word square if the `k`th row and column read the same string, where `0 <= k < max(numRows, numColumns)`.

* For example, the word sequence `["ball","area","lead","lady"]` forms a word square because each word reads the same both horizontally and vertically.
 

**Example 1:**
```
Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
```

**Example 2:**
```
Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
```

**Constraints:**

* `1 <= words.length <= 1000`
* `1 <= words[i].length <= 4`
* All `words[i]` have the same length.
* `words[i]` consists of only lowercase English letters.
* All `words[i]` are unique.

# Submissions
---
**Solution 1: (Backtracking with Trie, O(N * 26^L * L))**

        0      1      2      3      4
    ["area","lead","wall","lady","ball"]
         ^    ^             ^       ^
         ^    ^      ^      ^

    "ball",
       ^
    "area",
       ^
    "lead",
     ^^
    "lady"
    
    "wall",
    "area",
    "lead",
    "lady"


       'a'        'r'         'e'        'a'
root   ->    0    ->     0    ->    0    ->    0
       'b'        'a'         'l'        'l'   
       ->    4    ->     4    ->    4    ->    4
       'l'        'a'         'd'        'y'   
       ->    1    ->     3    ->    3    ->    3
             3    'e'         'a'        'd'   
                  ->     1    ->    1    ->    1
       'w'        'a'         'l'        'l'   
       ->    2    ->     2    ->    2    ->    2 


     v            v            v
    ball   ->   ball   ->   ball   ->   ball
          area  area  lead  area  lady  area
          ^           ^^    lead  ^^^   lead
                                        ladyx
```
Runtime: 68 ms, Beats 81.63%
Memory: 67.63 MB, Beats 66.33%
```
```c++
class Solution {
    struct TrieNode {
        TrieNode *child[26] = {nullptr};
        vector<int> dpi;
    };
    vector<string> dp;
    TrieNode *root;
    int k;
    void build(string &s, int i) {
        TrieNode *node = root;
        for (auto &c: s) {
            if (!node->child[c-'a']) {
                node->child[c-'a'] = new TrieNode();
            }
            node = node->child[c-'a'];
            node->dpi.push_back(i);
        }
    }
    vector<int> query(string &s) {
        TrieNode *node = root;
        for (auto &c: s) {
            if (node->child[c-'a']) {
                node = node->child[c-'a'];
            } else {
                return {};
            }
        }
        return node->dpi;
    }
    void bt(int i, vector<string> &path, vector<vector<string>> &ans) {
        if (i == k) {
            ans.push_back(path);
            return;
        }
        string prefix;
        for (auto &s: path) {
            prefix += s[i];
        }
        for (auto &&j: query(prefix)) {
            path.push_back(dp[j]);
            bt(i + 1, path, ans);
            path.pop_back();
        }
    }
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        root = new TrieNode();
        dp = words;
        k = words[0].size();
        int i;
        for (i = 0; i < words.size(); i ++) {
            build(words[i], i);
        }
        vector<string> path;
        vector<vector<string>> ans;
        for (i = 0; i < words.size(); i ++) {
            path.push_back(words[i]);
            bt(1, path, ans);
            path.pop_back();
        }
        return ans;
    }
};
```
