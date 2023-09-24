1048. Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say `word1` is a predecessor of `word2` if and only if we can add exactly one letter anywhere in `word1` to make it equal to `word2`.  For example, `"abc"` is a predecessor of `"abac"`.

A word chain is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a predecessor of `word_2`, `word_2` is a predecessor of `word_3`, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

**Example 1:**

```
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
```

**Note:**

1. `1 <= words.length <= 1000`
1. `1 <= words[i].length <= 16`
1. `words[i]` only consists of English lowercase letters.

# Submissions
---
**Solution 1: (DP Bottom-Up, Hash Table, Delete One at Once)**

**Algorithm:**

* we define a dictionary: word: longest length of its string chain
* sort the input array `words` by length
* starting from the shortest word, generating all possible predecessor (a shorter word with exactly one letter missing) from the current word
* if one of the predecessor already exsit in the dp array, which means we already calculated the longest string chain for its precessor. Now all we need to do is add the current word to the word chain by increament the length of the longest string chain by 1. We do this for all the predecessor of the current word. i.e. we update the longest string chain of each branch (each predecessor) for the current word by adding the current word. *The longest string chain for current word is the maximum of the longest string chains of all branches.
* We do this for each word.
* we can find the word with the longest string chain by calling dp[-1], no, just kidding, by finding the largest value in this dictionary, which is the longest string chain existing in the input.

```
Runtime: 156 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key = len):
            maxLen = 0
            for i in range(len(w)):
                predecessor = w[:i] + w[i+1:]
                maxLen = max(maxLen, dp.get(predecessor, 0) + 1)
            dp[w] = maxLen
        return max(dp.values())
```

* Time: $O(M * N)$ where $M$ is the length of the input array and $N$ is the avg length of each word.
* Space: $O(M)$

**Solution 2:(DP Top-Down)**
```
Runtime: 124 ms
Memory Usage: 17.4 MB
```
```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        @functools.lru_cache(None)
        def dfs(word):
            count = 0
            for i in range(len(word)):
                cur = word[:i] + word[i+1:]  # Delete One at Once
                if cur in s: 
                    count = max(count, dfs(cur))
            return count + 1
        
        rst, s, history = 1, set(words), {}
        for word in words:
            rst = max(rst, dfs(word))
        return rst
```

**Solution 1: (DP Bottom-Up, Hash Table, Delete One at Once)**
```
Runtime: 80 ms
Memory Usage: 17.3 MB
```
```c++
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        unordered_map<string, int> dp;
        int res = 1;
        sort(words.begin(), words.end(), [](const string &l, const string &r) { return l.size() < r.size(); });
        for (string word : words) {
            dp[word] = 1;
            for (int i = 0; i < word.size(); i++) {
                string prev = word.substr(0, i) + word.substr(i + 1);
                if (dp.find(prev) != dp.end()) {
                    dp[word] = dp[prev] + 1;
                    res = max(res, dp[word]);
                }
            }
        }
        return res;
    }
};
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 80 ms
Memory: 27.8 MB
```
```c++
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), [](string s1, string s2){return s1.size() < s2.size();});
        unordered_map<int, unordered_map<string, int>> m;
        int ans = 1, sz, j;
        for (string cur: words) {
            sz = cur.size();
            m[sz][cur] = 1;
            for (auto [pre, cnt]: m[sz-1]) {
                j = 0;
                for (int i = 0; i < sz; i++) {
                    if (pre[j] == cur[i]) {
                        j += 1;
                        if (j == sz-1) {
                            m[sz][cur] = max(m[sz][cur], cnt + 1);
                            ans = max(ans, m[sz][cur]);
                            break;
                        }
                    }
                }
            }
        }
        return ans;
    }
};
```
