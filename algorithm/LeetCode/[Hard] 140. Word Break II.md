140. Word Break II

Given a **non-empty** string s and a dictionary wordDict containing a list of **non-empty** words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

**Note:**

* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.

**Example 1:**
```
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```

**Example 2:**
```
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
```

**Example 3:**
```
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
```

# Submissions
---
**Solution 1: (DP Top-Down Memorization)**
```
Runtime: 40 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        set_wordDict = set(wordDict)
        memo = {}
        
        def dfs(seq):
            if not seq:
                return []
            if seq in memo:
                return memo[seq]
            rst = []
            if seq in set_wordDict:
                rst.append(seq)
            for i in range(1, len(seq)):
                prefix = seq[:i]
                if prefix in set_wordDict:
                    sufix_list = dfs(seq[i:])
                    if sufix_list:
                        for sufix in sufix_list:
                            rst.append(prefix+' ' + sufix)
            memo[seq] = rst
            return rst
        
        ans = dfs(s)
        return ans
```

**Solution 2: (DP Top-Down)**
```
Runtime: 40 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        set_wordDict = set(wordDict)
        
        @functools.lru_cache(None)
        def dfs(seq):
            if not seq:
                return []
            rst = []
            if seq in set_wordDict:
                rst.append(seq)
            for i in range(1, len(seq)):
                prefix = seq[:i]
                if prefix in set_wordDict:
                    for sufix in dfs(seq[i:]):
                        rst.append(prefix+' ' + sufix)
            return rst
        
        ans = dfs(s)
        return ans
```

**Solution 3: (Backtracking)**
```
Runtime: 4 ms
Memory: 9.31 MB
```
```c++
class Solution {
    void bt(int i, string pre, string &cur, vector<string> &ans, string &s, unordered_set<string> &st) {
        if (i == s.size()) {
            if (pre == "") {
                ans.push_back(cur);
            }
            return;
        }
        pre += s[i];
        bt(i+1, pre, cur, ans, s, st);
        if (st.count(pre)) {
            if (cur.size()) {
                cur += " ";
            }
            cur += pre;
            bt(i+1, "", cur, ans, s, st);
            for (int j = 0; j < pre.size(); j ++) {
                cur.pop_back();
            }
            if (cur.size() && cur.back() == ' ') {
                cur.pop_back();
            }
        }
    }
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> ans;
        string cur, pre;
        unordered_set<string> st(wordDict.begin(), wordDict.end());
        bt(0, pre, cur, ans, s, st);
        return ans;
    }
};
```

**Solution 4: (DP Top-Down)**
```
Runtime: 4 ms
Memory: 9.63 MB
```
```c++
class Solution {
    vector<string> dfs(int i, string &cur, vector<vector<string>> &dp, string &s, unordered_set<string> &st) {
        if (i == s.size()) {
            return {""};
        }
        if (dp[i].size() != 0) {
            return dp[i];
        }
        vector<string> rst;
        for (int j = i; j < s.size(); j ++) {
            cur += s[j];
            if (st.count(cur)) {
                string pre = "";
                for (auto ncur: dfs(j+1, pre, dp, s, st)) {
                    if (ncur.size()) {
                        rst.push_back(cur + " " + ncur);
                    } else {
                        rst.push_back(cur);
                    }
                }
            }
        }
        dp[i] = rst;
        return dp[i];
    }
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        string cur;
        unordered_set<string> st(wordDict.begin(), wordDict.end());
        vector<vector<string>> dp(s.size());
        return dfs(0, cur, dp, s, st);
    }
};
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory: 8.61 MB
```
```c++
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        string cur;
        unordered_set<string> st(wordDict.begin(), wordDict.end());
        vector<vector<string>> dp(n+1);
        dp[n] = {""};
        for (int i = n-1; i >= 0; i --) {
            cur = "";
            for (int j = i; j < n; j ++) {
                cur += s[j];
                if (st.count(cur)) {
                    for (auto ncur: dp[j+1]) {
                        if (ncur != "") {
                            dp[i].push_back(cur + " " + ncur);
                        } else {
                            dp[i].push_back(cur);
                        }
                    }
                }
            }
        }
        return dp[0];
    }
};
```

**Solution 6: (DP Bottom-Up, Trie)**
```
Runtime: 0 ms
Memory: 8.81 MB
```
```c++
class TrieNode {
public:
    bool isEnd;
    TrieNode *c[26];

    TrieNode() {
        isEnd = false;
        for (int i = 0; i < 26; i++) {
            c[i] = nullptr;
        }
    }
};

class Trie {
public:
    TrieNode *root;

    Trie() {
        root = new TrieNode(); 
    }

    void insert(string word) {
        TrieNode *node = root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->c[index]) {
                node->c[index] = new TrieNode();
            }
            node = node->c[index];
        }
        node->isEnd = true;
    }
};

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        string cur;
        vector<vector<string>> dp(n+1);
        Trie trie;
        TrieNode *node;
        for (string word : wordDict) {
            trie.insert(word);
        }
        dp[n] = {""};
        
        for (int i = n-1; i >= 0; i --) {
            cur = "";
            node = trie.root;
            for (int j = i; j < n; j ++) {
                if (!node->c[s[j]-'a']) {
                    break;
                }
                cur += s[j];
                node = node->c[s[j]-'a'];
                if (node->isEnd) {
                    for (auto ncur: dp[j+1]) {
                        if (ncur != "") {
                            dp[i].push_back(cur + " " + ncur);
                        } else {
                            dp[i].push_back(cur);
                        }
                    }
                }
            }
        }
        return dp[0];
    }
};
```
