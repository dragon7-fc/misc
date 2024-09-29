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

**Solution 2: (DP Bottom-Up, O(n^3))**
```
Runtime: 122 ms
Memory: 86.92 MB
```
```c++
class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.size();
        vector<int> dp(n+1);
        unordered_set<string> st(dictionary.begin(), dictionary.end());
        for (int i = n-1; i >= 0; i --) {  // O(n)
            dp[i] = dp[i+1] + 1;
            for (int k = 1; i+k <= n; k ++) {  // O(n)
                if (st.count(s.substr(i, k))) {
                        //  ^^^^^^^^^^^^^^^
                        //       O(n)
                    dp[i] = min(dp[i], dp[i+k]);
                }
            }
        }
        return dp[0];
    }
};
```

**Solution 3: (DP Bottom-Up, Trie, O(n^2 + m*k)**
```
Runtime: 48 ms
Memory: 111.70 MB
```
```c++
struct TrieNode {
    TrieNode *children[26] = {nullptr};
    bool is_word;
};

class Solution {
    TrieNode* buildTrie(vector<string>& dictionary) {
        auto root = new TrieNode();
        for (auto &word : dictionary) {  // O(m)
            auto node = root;
            for (auto &c : word) {  // O(k)
                if (node->children[c-'a'] == nullptr) {
                    node->children[c-'a'] = new TrieNode();
                }
                node = node->children[c-'a'];
            }
            node->is_word = true;
        }
        return root;
    }
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.size();
        vector<int> dp(n+1);
        auto root = buildTrie(dictionary);  O(m*k)
        for (int i = n-1; i >= 0; i --) {  // O(n)
            dp[i] = dp[i+1] + 1;
            auto node = root;
            for (int k = 1; i+k <= n; k ++) {  // O(n)
                if (node->children[s[i+k-1]-'a'] == nullptr) {
                    break;
                }
                node = node->children[s[i+k-1]-'a'];
                if (node->is_word) {
                    dp[i] = min(dp[i], dp[i+k]);
                }
            }
        }
        return dp[0];
    }
};
```
