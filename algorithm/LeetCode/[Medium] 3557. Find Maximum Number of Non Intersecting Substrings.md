3557. Find Maximum Number of Non Intersecting Substrings

You are given a string `word`.

Return the **maximum** number of non-intersecting **substrings** of word that are at least four characters long and start and end with the same letter.

 

**Example 1:**
```
Input: word = "abcdeafdef"

Output: 2

Explanation:

The two substrings are "abcdea" and "fdef".
```

**Example 2:**
```
Input: word = "bcdaaaab"

Output: 1

Explanation:

The only substring is "aaaa". Note that we cannot also choose "bcdaaaab" since it intersects with the other substring.
```
 

**Constraints:**

* `1 <= word.length <= 2 * 10^5`
* `word` consists only of lowercase English letters.

# Submissions
---
**Sollution 1: (DP Bottom-Up)**
```
Runtime: 112 ms, Beats 12.50%
Memory: 75.28 MB, Beats 6.25%
```
```c++
class Solution {
public:
    int maxSubstrings(string word) {
        vector<deque<int>> pos(26);
        for (int k = 0; k < 26; ++k) {
            pos[k] = deque<int>();
        }
        int n = word.length();
        vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            int c = word[i] - 'a';
            dp[i + 1] = dp[i];
            for (int j : pos[c])
                if (i - j + 1 >= 4)
                    dp[i + 1] = max(dp[i + 1], dp[j] + 1);
            pos[c].push_back(i); 
            if (pos[c].size() > 4)
                pos[c].pop_front();
        }
        return dp[n];
    }
};
```

**Solution 2: (Greedy)**

    a   b   c   d   e   a   f   d   e   f
    a:0                 x 
        b:1             x
            c:2         x
                d:3     x       d:7     x
                    e:4 x           e:8 x
                            f:6         x
ans                     1               2
                       

```
Runtime: 257 ms, Beats 6.25%
Memory: 75.18 MB, Beats 6.25%
```
```c++
class Solution {
public:
    int maxSubstrings(string word) {
        int res = 0, n = word.length();
        unordered_map<char, int> pos;
        for (int i = 0; i < n; ++i) {
            char c = word[i];
            if (pos.find(c) == pos.end()) {
                pos[c] = i;
            } else if (i - pos[c] + 1 >= 4) {
                ++res;
                pos.clear();
            }
        }
        return res;
    }
};
```
