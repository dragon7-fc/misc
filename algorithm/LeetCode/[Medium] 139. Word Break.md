139. Word Break

Given a **non-empty** string `s` and a dictionary `wordDict` containing a list of **non-empty** words, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.

**Example 1:**
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3:**
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```
# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 40 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * N    
        for i in range(N):
            for w in wordDict:
                w_size = len(w)
                if w == s[i - w_size + 1:i + 1] and (dp[i - w_size] or i - w_size == -1):
                    dp[i] = True
        return dp[-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 32 ms
Memory Usage: 13.3 MB
```
```python
import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == N:
                return True
            rst = False
            for w in wordDict:
                w_size = len(w)
                if i + w_size <= N and s[i:i + w_size] == w:
                    rst = rst | dfs(i + w_size)
            return rst
        
        return dfs(0)
```

**Solution 3: (DP Top-Down)**
```
Runtime: 8 ms
Memory Usage: 9.3 MB
```
```c++
class Solution {
public:
    int dp[302];
    unordered_map<string, int> mp;
    bool solve(string s, int n, int idx){
        if(idx == n) return true;
        if(dp[idx] != -1) return dp[idx];
        string osf = "";
        for(int i = idx; i < s.length(); i++){
            osf += s[i];
            if(mp.count(osf) > 0){// check for the substring that is in map or not
                if(solve(s,n, i+1)) return dp[idx] = true;
            }
        }
        return dp[idx] = false;
    }
    
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        memset(dp, -1, sizeof(dp));
        for(auto word : wordDict){ // store word in map
            mp[word]++;
        }
        return solve(s,n,0);
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 13 ms
Memory: 13.2 MB
```
```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(n+1);
        dp[n] = true;
        unordered_set<string> st(wordDict.begin(), wordDict.end());
        for (int i = n-1; i >= 0; i --) {
            for (int k = 1; i+k <= n; k ++) {
                if (st.count(s.substr(i, k)) && dp[i+k]) {
                    dp[i] = true;
                    break;
                }
            }
        }        
        return dp[0];
    }
};
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 14 ms
Memory: 17.22 MB
```
```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(n+1);
        dp[0] = true;
        unordered_set<string> st(wordDict.begin(), wordDict.end());
        for (int j = 0; j < n; j ++) {
            for (int i = 0; i <= j; i ++) {
                if (st.count(s.substr(i, j-i+1))) {
                    dp[j+1] = dp[j+1] | dp[i];
                }
            }
        }
        return dp.back();
    }
};
```
