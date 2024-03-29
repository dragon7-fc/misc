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

**Solution 3: (DP Top-Down)**
```
Runtime: 0 ms
Memory: 8.2 MB
```
```c++
class Solution {
    vector<string> dfs(int i, vector<vector<string>> &dp, unordered_set<string> &st, string &s) {
        if (i == s.size()) {
            return {""};
        }
        if (!dp[i].empty()) {
            return dp[i];
        }
        vector<string> rst;
        string pre;
        for (int k = 1; k <= s.size()-i; k++) {
            pre = s.substr(i, k);
            if (st.count(pre)) {
                for (auto suffix : dfs(i+k, dp, st, s)) {
                    if (suffix != "") {
                        rst.push_back(pre + " " + suffix);
                    } else {
                        rst.push_back(pre);
                    }
                }
            }
        }
        dp[i] = rst;
        for (int j = 0; j < rst.size(); j ++) {
            cout << dp[i][j] << endl;
        }
        return rst;
    }
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        unordered_set<string> st(wordDict.begin(), wordDict.end());
        vector<vector<string>> dp(n);
        return dfs(0, dp, st, s);
    }
};
```
