1525. Number of Good Ways to Split a String

You are given a string `s`, a split is called good if you can split `s` into 2 non-empty strings `p` and `q` where its concatenation is equal to `s` and the number of distinct letters in `p` and `q` are the same.

Return the number of good splits you can make in `s`.

 

**Example 1:**
```
Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
```

**Example 2:**
```
Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
```

**Example 3:**
```
Input: s = "aaaaa"
Output: 4
Explanation: All possible splits are good.
```

**Example 4:**
```
Input: s = "acbadbaada"
Output: 2
```

**Constraints:**

* `s` contains only lowercase English letters.
* `1 <= s.length <= 10^5`

# Submissions
---
**Solution 1: (Set, Counter)**
```
Runtime: 188 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def numSplits(self, s: str) -> int:
        p, total = set(), collections.Counter(s)
        res, total_cnt = 0, len(total)
        for i, x in enumerate(s[::-1]):
            p.add(x)
            total[x] -= 1
            total_cnt -= not total[x]
            res += len(p) == total_cnt
        return res 
```

**Solution 2: (Set, Hash Table)**
```
Runtime: 156 ms
Memory Usage: 8.5 MB
```
```c++
class Solution {
public:
    int numSplits(string s) {
        unordered_map<char, int> total;
        for (auto c: s) total[c]++;
        int total_size = (int)total.size(), res = 0;
        set<char> p;
        for (auto c: s) {
            p.insert(c);
            total[c]--;
            total_size -= !total[c];
            res += (total_size == p.size());
        }
        return res;
    }
};
```