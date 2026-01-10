358. Rearrange String k Distance Apart

Given a string `s` and an integer `k`, rearrange `s` such that the same characters are **at least** distance `k` from each other. If it is not possible to rearrange the string, return an empty string `""`.

 

**Example 1:**
```
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
```

**Example 2:**
```
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
```

**Example 3:**
```
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
```

**Constraints:**

* `1 <= s.length <= 3 * 10^5`
* `s` consists of only lowercase English letters.
* `0 <= k <= s.length`

# Submissions
---
**Solution 1: (Heap, greedy queue element in sized k buffer)**

    s = "a a b b c c", k = 3
pq
    2,a 2,b 2,c 
     x   x   x  1,a
                 x  1,b
                     x  1,c
                         x
q
    1,a 1,b 1,c
     x   x   x  0,a
                    0,b
                        0,c

ans 
     a   b   c   a   b   c
```
Runtime: 3 ms, Beats 97.30%
Memory: 13.92 MB, Beats 40.54%
```
```c++
class Solution {
public:
    string rearrangeString(string s, int k) {
        int cnt[26] = {0};
        for (char c: s) {
            cnt[c-'a'] += 1;
        }
        priority_queue<pair<int, int>> pq;
        queue<pair<int, int>> q;
        for (int i = 0; i < 26; i ++) {
            if (cnt[i]) {
                pq.push({cnt[i], i});
            }
        }
        string ans = "";
        while (!pq.empty()) {
            auto [f, c] = pq.top();
            pq.pop();
            ans += 'a' + c;
            q.push({f - 1, c});
            if (q.size() >= k) {
                auto [nf, nc] = q.front();
                q.pop();
                if (nf) {
                    pq.push({nf, nc});
                }
            }
        }
        return ans.size() == s.size() ? ans : "";
    }
};
```
