3291. Minimum Number of Valid Strings to Form Target I

You are given an array of strings `words` and a string `target`.

A string `x` is called **valid** if `x` is a **prefix** of any string in `words`.

Return the **minimum** number of **valid** strings that can be concatenated to form `target`. If it is not possible to form target, return `-1`.

A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.

 

**Example 1:**
```
Input: words = ["abc","aaaaa","bcdef"], target = "aabcdabc"

Output: 3

Explanation:

The target string can be formed by concatenating:

Prefix of length 2 of words[1], i.e. "aa".
Prefix of length 3 of words[2], i.e. "bcd".
Prefix of length 3 of words[0], i.e. "abc".
```

**Example 2:**
```
Input: words = ["abababab","ab"], target = "ababaababa"

Output: 2

Explanation:

The target string can be formed by concatenating:

Prefix of length 5 of words[0], i.e. "ababa".
Prefix of length 5 of words[0], i.e. "ababa".
```

**Example 3:**
```
Input: words = ["abcdef"], target = "xyz"

Output: -1
```
 

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 5 * 10^3`
* The input is generated such that `sum(words[i].length) <= 10^5`.
* `words[i]` consists only of lowercase English letters.
* `1 <= target.length <= 5 * 10^3`
* `target` consists only of lowercase English letters.

# Submissions
---
**Solution 1: (Trie, DP Buttom-Up)**
```
Runtime: 1168 ms
Memory: 642.48 MB
```
```c++
class TrieNode {
public:
    TrieNode *child[26];
    bool flag = false;
};

class Trie {
public:
    TrieNode *root;
    Trie() {
        root = new TrieNode();
    }

    void insert(const string& word) {
        TrieNode *node = root;
        for (char c : word) {
            int ch = c - 'a';
            if (!node->child[ch]) {
                node->child[ch] = new TrieNode();
            }
            node = node->child[ch];
            node->flag = true;
        }
    }

   
    vector<int> search(const string& target, int start) {
        vector<int> valid_lengths;
        TrieNode *node = root;
        for (int i = start; i < target.length(); i++) {
            if (!node->child[target[i] - 'a']) break;
            node = node->child[target[i] - 'a'];
            if (node->flag) {
                valid_lengths.push_back(i - start + 1);
            }
        }
        return valid_lengths;
    }
};

class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        Trie trie;

        for (const string& word : words) {
            trie.insert(word);
        }

        int n = target.length();
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;  
        for (int i = 0; i < n; i++) {
            if (dp[i] == INT_MAX) continue;

            vector<int> lengths = trie.search(target, i);
            for (int len : lengths) {
                dp[i + len] = min(dp[i + len], dp[i] + 1);
            }
        }

        return dp[n] == INT_MAX ? -1 : dp[n];
    }
};
```
