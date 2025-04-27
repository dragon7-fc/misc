3481. Apply Substitutions

You are given a `replacements` mapping and a text string that may contain **placeholders** formatted as `%var%`, where each var corresponds to a key in the replacements mapping. Each replacement value may itself contain one or more such **placeholders**. Each **placeholder** is replaced by the value associated with its corresponding replacement key.

Return the fully substituted text string which does not contain any **placeholders**.

 

**Example 1:**
```
Input: replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"

Output: "abc_def"

Explanation:

The mapping associates "A" with "abc" and "B" with "def".
Replace %A% with "abc" and %B% with "def" in the text.
The final text becomes "abc_def".
```

**Example 2:**
```
Input: replacements = [["A","bce"],["B","ace"],["C","abc%B%"]], text = "%A%_%B%_%C%"

Output: "bce_ace_abcace"

Explanation:

The mapping associates "A" with "bce", "B" with "ace", and "C" with "abc%B%".
Replace %A% with "bce" and %B% with "ace" in the text.
Then, for %C%, substitute %B% in "abc%B%" with "ace" to obtain "abcace".
The final text becomes "bce_ace_abcace".
```

**Constraints:**

* `1 <= replacements.length <= 10`
* Each element of replacements is a two-element list `[key, value]`, where:
* `key` is a single uppercase English letter.
* `value` is a non-empty string of at most 8 characters that may contain zero or more placeholders formatted as `%<key>%`.
* All replacement keys are unique.
* The `text` string is formed by concatenating all key placeholders (formatted as `%<key>%`) randomly from the replacements mapping, separated by underscores.
* `text.length == 4 * replacements.length - 1`
* Every `placeholder` in the `text` or in any replacement value corresponds to a key in the `replacements` mapping.
* There are no cyclic dependencies between replacement keys.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 20 ms, Beats 35.21%
Memory: 44.92 MB, Beats 18.72%
```
```c++
class Solution {
    string dfs(string s, int i, unordered_map<string, string> &dp) {
        if (i == s.size()) {
            return "";
        }
        for (int j = i; j < (int)s.size() - 2; j ++) {
            if (s[j] == '%' && s[j+2] == '%' && dp.count(s.substr(j, 3))) {
                return s.substr(i, j-i) + dfs(dp[s.substr(j, 3)] + s.substr(j+3), 0, dp);
            }
        }
        return s.substr(i, s.size()-i);
    }
public:
    string applySubstitutions(vector<vector<string>>& replacements, string text) {
        int m = replacements.size(), i;
        string ss;
        unordered_map<string,string> dp;
        for (i = 0; i < m; i ++) {
            dp["%" + replacements[i][0] + "%"] = replacements[i][1];
        }
        for (auto &[_, s]: dp) {
            s = dfs(s, 0, dp);
        }
        string ans = text;
        for (i = 0; i < (int)ans.size() - 2; i ++) {
            if (ans[i] == '%' && ans[i+2] == '%') {
                ss = ans.substr(i, 3);
                if (dp.count(ss)) {
                    ans = ans.substr(0, i) + dfs(dp[ss] + ans.substr(i+3), 0, dp);
                }
            }
        }
        return ans;
    }
};
```

**Solution 2: (DFS)**
```
Runtime: 7 ms, Beats 89.14%
Memory: 44.19 MB, Beats 21.47%
```
```c++
class Solution {
    unordered_map<string, string>Map;
    string dfs(string s){
        int i = s.find('%');
        if(i == string::npos)
            return s;
        int j = s.find('%', i+1);
        if(j == string::npos)
            return s;
        string key = s.substr(i+1, j-i-1);
        string replace = Map[key];
        return s.substr(0, i) + dfs(replace) + dfs(s.substr(j+1));
    }
public:
    string applySubstitutions(vector<vector<string>>& replacements, string text) {
        for(auto data : replacements){
            Map[data[0]] = data[1];
        }
        return dfs(text);
    }
};
```
