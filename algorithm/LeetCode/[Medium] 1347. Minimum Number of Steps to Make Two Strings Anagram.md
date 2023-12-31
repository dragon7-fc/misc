1347. Minimum Number of Steps to Make Two Strings Anagram

Given two equal-size strings `s` and `t`. In one step you can choose any character of `t` and replace it with another character.

Return the minimum number of steps to make `t` an anagram of `s`.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

**Example 1:**
```
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
```

**Example 2:**
```
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
```

**Example 3:**
```
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
```

**Example 4:**
```
Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
```

**Example 5:**
```
Input: s = "friend", t = "family"
Output: 4
```

**Constraints:**

* `1 <= s.length <= 50000`
* `s.length == t.length`
* `s` and `t` contain lower-case English letters only.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 112 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        S, T = map(collections.Counter, (s, t))
        return sum((S - T).values())
```

**Solution 2: (HashMap)**
```
Runtime: 51 ms
Memory: 16.8 MB
```
```c++
class Solution {
public:
    int minSteps(string s, string t) {
        int count[26] = {0};
        // Storing the difference of frequencies of characters in t and s.
        for (int i = 0; i < s.size(); i++) {
            count[t[i] - 'a']++;
            count[s[i] - 'a']--;
        }

        int ans = 0;
        // Adding the difference where string t has more instances than s.
        // Ignoring where t has fewer instances as they are redundant and
        // can be covered by the first case.
        for (int i = 0; i < 26; i++) {
            ans += max(0, count[i]);
        }
        
        return ans;
    }
};
```
