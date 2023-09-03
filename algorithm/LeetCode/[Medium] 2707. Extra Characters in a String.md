2707. Extra Characters in a String

You are given a **0-indexed** string `s` and a dictionary of words `dictionary`. You have to break `s` into one or more **non-overlapping** substrings such that each substring is present in `dictionary`. There may be some extra characters in `s` which are not present in any of the substrings.

Return the **minimum** number of extra characters left over if you break up `s` optimally.

 

**Example 1:**
```
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.
```

**Example 2:**
```
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
```

**Constraints:**

* `1 <= s.length <= 50`
* `1 <= dictionary.length <= 50`
* `1 <= dictionary[i].length <= 50`
* `dictionary[i]` and `s` consists of only lowercase English letters
* `dictionary` contains distinct words

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 360 ms
Memory: 16.9 MB
```
```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        
        @functools.lru_cache(None)
        def dp(i):
            if i == N:
                return 0
            rst = float('inf')
            for w in dictionary:
                if i+len(w) <= N and s[i:i+len(w)] == w:
                    rst = min(rst, dp(i+len(w)))
            rst = min(rst, dp(i+1)+1)
            return rst 
            
        return dp(0)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 64 ms
Memory: 55.1 MB
```
```c++
class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int dp[51] = {};
        for (int i = s.size() - 1; i >= 0; --i) {
            dp[i] = 1 + dp[i + 1];
            for (const auto &w: dictionary)
                if (s.compare(i, w.size(), w) == 0)
                    dp[i] = min(dp[i], dp[i + w.size()]);
        }
        return dp[0];
    }
};
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 51 ms
Memory: 54.8 MB
```
```c++
class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.size(), k;
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i < n; i ++) {
            dp[i+1] = min(dp[i+1], dp[i] + 1);
            for (int j = 0; j < dictionary.size(); j ++) {
                for (k = 0; i+k <= n-1 && k < dictionary[j].size(); k ++) {
                    if (s[i+k] != dictionary[j][k]) {
                        break;
                    }
                }
                if (k == dictionary[j].size()) {
                    dp[i+k] = min(dp[i+k], dp[i]);
                }
            }
        }
        return dp[n];
    }
};
```
