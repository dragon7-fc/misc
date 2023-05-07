1456. Maximum Number of Vowels in a Substring of Given Length

Given a string `s` and an integer `k`.

Return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are (`a, e, i, o, u`).

 

**Example 1:**
```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

**Example 2:**
```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

**Example 3:**
```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

**Example 4:**
```
Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
```

**Example 5:**
```
Input: s = "tryhard", k = 4
Output: 1
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of lowercase English letters.
* `1 <= k <= s.length`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 204 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            ans  = max(cnt, ans)
        return ans  
```

**Solution 2: (Sliding Window)**
```
Runtime: 19 ms
Memory: 10 MB
```
```c++
class Solution {
public:
    int maxVowels(string s, int k) {
        int cnt = 0, ans = 0;
        for (int i = 0; i < s.size(); i ++) {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o'  || s[i] == 'u') {
                cnt += 1;
            }
            if (i >= k) {
                if (s[i-k] == 'a' || s[i-k] == 'e' || s[i-k] == 'i' || s[i-k] == 'o'  || s[i-k] == 'u') {
                    cnt -= 1;
                }
            }
            ans = max(ans, cnt);
        }
        return ans;
    }
};
```
