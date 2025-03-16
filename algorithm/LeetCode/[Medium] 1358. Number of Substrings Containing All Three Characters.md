1358. Number of Substrings Containing All Three Characters

Given a string `s` consisting only of characters a, b and c.

Return the number of substrings containing **at least** one occurrence of all these characters a, b and c.

 

**Example 1:**
```
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
```

**Example 2:**
```
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
```

**Example 3:**
```
Input: s = "abc"
Output: 1
```

**Constraints:**

* `3 <= s.length <= 5 x 10^4`
* `s` only consists of a, b or c characters.

# Submissions
---
**Solution 1: (Hash Table, Sliding Window)**
```
Runtime: 236 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in range(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res
```

**Solution 1: (Sliding Window)**
```
Runtime: 152 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, last = 0, [-1] * 3
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
            res += 1 + min(last)  ## the starting index can be in range [0, min(last)],
        return res
```

**Solution 2: (Sliding Window)**

    a b c a b c 
j             ^
i          ^
        4 7 9 10

```
Runtime: 12 ms, Beats 44.87%
Memory: 10.94 MB, Beats 81.05%
```
```c++
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size(), i = 0, j = 0, cnt[3] = {0}, ans = 0;
        while (j < n) {
            while (j < n && (!cnt[0] || !cnt[1] || !cnt[2])) {
                cnt[s[j]-'a'] += 1;
                j += 1;
            }
            while (cnt[0] && cnt[1] && cnt[2]) {
                ans += n-j+1;
                cnt[s[i]-'a'] -= 1;
                i += 1;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Last Position Tracking)**

        0  1  2  3  4  5
        a  b  c  a  b  c
a      |--- 4 ---^      
b                   ^
c                      ^ 
last a  0  0  0  3  3  3
     b -1  1  1  1  4  4
     c -1 -1  2  2  2  5
ans     0  0  1  3  6 10

```
Runtime: 13 ms, Beats 42.54%
Memory: 10.94 MB, Beats 81.05%
```
```c++
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.length(), i, ans = 0, last[3] = {-1, -1, -1};;
        for (i = 0; i < n; i ++) {
            last[s[i] - 'a'] = i;
            ans += 1 + min({last[0], last[1], last[2]});
        }

        return ans;
    }
};
```
