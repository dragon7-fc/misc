3170. Lexicographically Minimum String After Removing Stars

You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

* Delete the leftmost `'*'` and the smallest non-`'*'` character to its left. If there are several smallest characters, you can delete any of them.
Return the **lexicographically smallest** resulting string after removing all `'*'` characters.

 

**Example 1:**
```
Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.
```

**Example 2:**
```
Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists only of lowercase English letters and `'*'`.
* The input is generated such that it is possible to delete all `'*'` characters.

# Submissions
---
**Solution 1: (Heap, sort)**
```
Runtime: 214 ms
Memory: 25.63 MB
```
```c++
class Solution {
public:
    string clearStars(string s) {
        priority_queue<pair<int,int>, vector<pair<int,int>>> pq;
        for (int i = 0; i < s.size(); i ++) {
            if (s[i] == '*') {
                if (pq.size()) {
                    pq.pop();
                }
            } else {
                pq.push({-s[i], i});
            }
        }
        vector<pair<char,int>> dp;
        while (pq.size()) {
            auto [c, i] = pq.top();
            dp.push_back({-c, i});
            pq.pop();
        }
        sort(dp.begin(), dp.end(), [](auto pa, auto pb){return pa.second < pb.second;});
        string ans;
        for (auto [c, _]: dp) {
            ans += c;
        }
        return ans;
    }
};
```

**Solution 2: (Counter, Greedy)**

    a a b a *
            ^
cnt
            a:0,1,3
                  x
            b:2
vis 0 0 0 1 1
```
Runtime: 73 ms, Beats 69.48%
Memory: 35.10 MB, Beats 41.23%
```
```c++
class Solution {
public:
    string clearStars(string s) {
        int n = s.size(), i, j;
        vector<vector<int>> dp(26);
        vector<int> visited(n);
        string ans;
        for (i = 0; i < n; i ++) {
            if (s[i] == '*') {
                visited[i] = 1;
                for (j = 0; j < 26; j ++) {
                    if (dp[j].size()) {
                        visited[dp[j].back()] = 1;
                        dp[j].pop_back();
                        break;
                    }
                }
            } else {
                dp[s[i] - 'a'].push_back(i);
            }
        }
        for (i = 0; i < n; i ++) {
            if (visited[i] == 0) {
                ans += s[i];
            }
        }
        return ans;
    }
};
```
