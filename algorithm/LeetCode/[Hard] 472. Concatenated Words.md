472. Concatenated Words

Given a list of words (**without duplicates**), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

**Example:**
```
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

**Note:**

* The number of elements of the given array will not exceed `10,000`
* The length sum of elements in the given array will not exceed `600,000`.
* All the input string will only include lower case letters.
* The returned elements order does not matter.

# Submissions
---
> **Solution 1: (Set, DFS, Time: O(M^3 * N), Space: O(N * M))**
```
Runtime: 344 ms
Memory Usage: 29.2 MB
```
```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        ans = []
        
        def dfs(w, cnt):
            if not w:
                if cnt <= 1:
                    return False
                else:
                    return True
            elif w in s and cnt >= 1:
                return True
            for i in range(1, len(w)):
                if w[:i] in s and dfs(w[i:], cnt+1):
                    return True
            return False
            
        for word in words:
            if dfs(word, 0):
                ans.append(word)
        
        return ans
```

**Solution 2: (Trie, DFS)**
```
Runtime: 904 ms
Memory Usage: 37.4 MB
```
```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            t = trie
            for c in word:
                t = t.setdefault(c, {})
            t['#'] = {}
        ans = []

        def dfs(w, cnt):
            if not w:
                if cnt <= 1:
                    return False
                else:
                    return True
            t = trie
            for i, c in enumerate(w):
                if c in t:
                    t = t[c]
                    if '#' in t:
                        if dfs(w[i+1:], cnt+1):
                            return True
                else:
                    break
            return False      

        for word in words:
            if dfs(word, 0):
                ans.append(word)
            
        return ans
```

**Solution 3: (Trie, DP Top-Down)**
```
Runtime: 375 ms, Beats 12.60%
Memory: 351.30 MB, Beats 5.01%
```
```c++
class Solution {
    struct TrieNode {
        TrieNode *child[26] = {nullptr};
        bool is_end = false;
    };
    TrieNode *root;
    void build(string &word) {
        TrieNode *node = root;
        for (auto &c: word) {
            if (!node->child[c - 'a']) {
                node->child[c - 'a'] = new TrieNode();
            }
            node = node->child[c - 'a'];
        }
        node->is_end = true;
    }
    bool find(string &word, int i) {
        TrieNode *node = root;
        for (auto j = i; j < word.size(); j ++) {
            if (!node->child[word[j] - 'a']) {
                return false;
            }
            node = node->child[word[j] - 'a'];
        }
        return node->is_end;
    }
    bool dfs(string &word, int left, int right, vector<vector<int>> &dp) {
        if (left > right) {
            return false;
        }
        if (dp[left][right] != -1) {
            return dp[left][right];
        }
        TrieNode *node = root;
        dp[left][right] = 0;
        for (int i = left; i <= right; i ++) {
            if (node->child[word[i] - 'a']) {
                node = node->child[word[i] - 'a'];
                if (node->is_end && (find(word, i + 1) || dfs(word, i + 1, right, dp))) {
                    dp[left][right] = 1;
                    break;
                }
            } else {
                break;
            }
        }
        return dp[left][right];
    }
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        vector<string> ans;
        root = new TrieNode();
        for (auto &word: words) {
            build(word);
        }
        for (auto &word: words) {
            vector<vector<int>> dp(word.size(), vector<int>(word.size(), -1));
            if (dfs(word, 0, word.length() - 1, dp)) {
                ans.push_back(word);
            }
        }
        return ans;
    }
};
```

**Solution 4: (Sort, DP Bottom-Up)**

    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
sort          cat dog rat cats dogcatsdog catsdogcats ratcatdogcat hippopotamuses 
                                  ^
st            cat dog rat cats
dp                            [10010001001]
                               i
```
Runtime: 276 ms, Beats 20.81%
Memory: 47.11 MB, Beats 98.09%
```
```c++
class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        int n = words.size(), m, i, k;
        unordered_set<string> st;
        sort(words.begin(), words.end(), [](auto &w1, auto &w2){return w1.length() < w2.length();});
        vector<bool> dp(31);
        vector<string> ans;
        for (auto &word: words) {
            m = word.size();
            fill(dp.begin(), dp.end(), false);
            dp[m] = true;
            for (i = m - 1; i >= 0; i --) {
                for (k = 1; i + k <= m; k ++) {
                    if (st.count(word.substr(i, k))) {
                        dp[i] = dp[i] | dp[i + k];
                    }
                }
            }
            if (dp[0]) {
                ans.push_back(word);
            }
            st.insert(word);
        }
        return ans;
    }
};
```
