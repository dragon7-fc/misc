2405. Optimal Partition of String

Given a string `s`, partition the string into one or more **substrings** such that the characters in each substring are **unique**. That is, no letter appears in a single substring more than **once**.

Return the **minimum** number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

**Example 1:**
```
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
```

**Example 2:**
```
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of only English lowercase letters.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 179 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def partitionString(self, s: str) -> int:
        cur = ""
        ans = 0
        for c in s:
            if not c in cur:
                cur += c
            else:
                cur = c
                ans += 1
        return ans + 1 if cur != "" else ans
```

**Solution 2: (last position)**
```
Runtime: 61 ms
Memory Usage: 10.3 MB
```
```c++
class Solution {
public:
    int partitionString(string s) {
        int pos[26] = {}, res = 0, last = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (pos[s[i] - 'a'] >= last) {
                ++res;
                last = i + 1;
            }
            pos[s[i] - 'a'] = i + 1;
        }
        return res;
    }
};
```
