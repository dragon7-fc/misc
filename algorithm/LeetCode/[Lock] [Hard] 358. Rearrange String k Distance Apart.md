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
**Solution 1: (Heap, greedy queue element in buffer)**
```
Runtime: 10 ms
Memory: 10.7 MB
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
            q.push({f-1, c});
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
