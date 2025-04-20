3253. Construct String with Minimum Cost (Easy)

You are given a string target, an array of strings words, and an integer array costs, both arrays of the same length.

Imagine an empty string s.

You can perform the following operation any number of times (including zero):

Choose an index i in the range [0, words.length - 1].
Append words[i] to s.
The cost of operation is costs[i].
Return the minimum cost to make s equal to target. If it's not possible, return -1.

 

**Example 1:**
```
Input: target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]

Output: 7

Explanation:

The minimum cost can be achieved by performing the following operations:

Select index 1 and append "abc" to s at a cost of 1, resulting in s = "abc".
Select index 2 and append "d" to s at a cost of 1, resulting in s = "abcd".
Select index 4 and append "ef" to s at a cost of 5, resulting in s = "abcdef".
```

**Example 2:**
```
Input: target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]

Output: -1

Explanation:

It is impossible to make s equal to target, so we return -1.
```
 

**Constraints:**

* `1 <= target.length <= 2000`
* `1 <= words.length == costs.length <= 50`
* `1 <= words[i].length <= target.length`
* `target` and `words[i]` consist only of lowercase English letters.
* `1 <= costs[i] <= 105`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 612 ms, Beats 5.00%
Memory: 453.40 MB, Beats 25.00%
```
```c++
class Solution {
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        int m = target.length(), n = words.size(), i, j, k;
        vector<long long> dp(m+1, INT_MAX);
        dp[0] = 0;
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                k = words[j].length();
                if (k <= i+1 && target.substr(i - k + 1, k) == words[j]) {
                    dp[i + 1] = min(dp[i + 1], dp[i - k + 1] + costs[j]);
                }
            }
        }
        if (dp[m] == INT_MAX) {
            return -1;
        }
        return dp[m];
    }
};
```

**Solution 2: (Trie, DP Top-Down)**
```
Runtime: 256 ms, Beats 30.00%
Memory: 568.17 MB, Beats 25.00%
```
```c++
class Solution {
    struct TrieNode {
        TrieNode *child[26] = {nullptr};
        int c = 0;
    };
    TrieNode *root;
    void build(string s, int cost) {
        TrieNode *node = root;
        for (auto c: s) {
            if (!node->child[c-'a']) {
                node->child[c-'a'] = new TrieNode();
            }
            node = node->child[c-'a'];
        }
        if (node->c) {
            node->c = min(node->c, cost);
        } else {
            node->c = cost;
        }
    }
    int dfs(string target, int i, vector<int> &dp, vector<int> &costs) {
        if (i == target.length()) {
            return 0;
        }
        if (dp[i] != -1) {
            return dp[i];
        }
        TrieNode *node = root;
        long long rst = INT_MAX;
        for (int j = i; j < target.length(); j ++) {
            if (node->child[target[j]-'a']) {
                node = node->child[target[j]-'a'];
                if (node->c) {
                    rst = min(rst, ((long long)node->c + dfs(target, j+1, dp, costs)));
                }
            } else {
                break;
            }
        }
        dp[i] = rst;
        return rst;
    }
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        int m = target.length(), n = words.size(), i;
        root = new TrieNode();
        for (i = 0; i < n; i ++) {
            build(words[i], costs[i]);
        }
        vector<int> dp(m+1, -1);
        int ans = dfs(target, 0, dp, costs);
        if (ans == INT_MAX) {
            ans = -1;
        }
        return ans;
    }
};
```
