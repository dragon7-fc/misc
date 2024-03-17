3084. Count Substrings Starting and Ending with Given Character

You are given a string `s` and a character `c`. Return the total number of **substrings** of `s` that start and end with `c`.

 

**Example 1:**
```
Input: s = "abada", c = "a"

Output: 6

Explanation: Substrings starting and ending with "a" are: "abada", "abada", "abada", "abada", "abada", "abada".
```

**Example 2:**
```
Input: s = "zzz", c = "z"

Output: 6

Explanation: There are a total of 6 substrings in s and all start and end with "z".
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` and `c` consist only of lowercase English letters.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 15 ms
Memory: 11.06 MB
```
```c++
class Solution {
public:
    long long countSubstrings(string s, char c) {
        long long count = 0;
        for(auto ch: s) count += (ch == c);
        return count * (count + 1)/2;
    }
};
```
