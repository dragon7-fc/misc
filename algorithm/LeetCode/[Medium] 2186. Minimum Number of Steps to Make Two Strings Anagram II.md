2186. Minimum Number of Steps to Make Two Strings Anagram II

You are given two strings `s` and `t`. In one step, you can append **any character** to either `s` or `t`.

Return the minimum number of steps to make `s` and `t` **anagrams** of each other.

An **anagram** of a string is a string that contains the same characters with a different (or the same) ordering.

 

**Example 1:**
```
Input: s = "leetcode", t = "coats"
Output: 7
Explanation: 
- In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
- In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
"leetcodeas" and "coatsleede" are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
```

**Example 2:**
```
Input: s = "night", t = "thing"
Output: 0
Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.
```

**Constraints:**

* `1 <= s.length, t.length <= 2 * 10^5`
* `s` and `t` consist of lowercase English letters.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 364 ms
Memory Usage: 16.5 MB
```
```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = collections.Counter(s)
        t_cnt = collections.Counter(t)
        return sum((s_cnt-t_cnt).values()) + sum((t_cnt-s_cnt).values())
```

**Solution 2: (Hash Table)**
```
Runtime: 123 ms
Memory Usage: 28.9 MB
```
```c++
class Solution {
public:
    int minSteps(string s, string t) {
        int cnt[26] = {}, ans = 0;
        for (char c : s) cnt[c - 'a']++;
        for (char c : t) cnt[c - 'a']--;
        for (int n : cnt) ans += abs(n);
        return ans;
    }
};
```
