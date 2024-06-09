2539. Count the Number of Good Subsequences

A **subsequence** of a string is good if it is not empty and the frequency of each one of its characters is the same.

Given a string `s`, return the number of good subsequences of `s`. Since the answer may be too large, return it modulo `10^9 + 7`.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

**Example 1:**
```
Input: s = "aabb"
Output: 11
Explanation: The total number of subsequences is 24. There are five subsequences which are not good: "aabb", "aabb", "aabb", "aabb", and the empty subsequence. Hence, the number of good subsequences is 24-5 = 11.
```

**Example 2:**
```
Input: s = "leet"
Output: 12
Explanation: There are four subsequences which are not good: "leet", "leet", "leet", and the empty subsequence. Hence, the number of good subsequences is 24-4 = 12.
```

**Example 3:**
```
Input: s = "abcd"
Output: 15
Explanation: All of the non-empty subsequences are good subsequences. Hence, the number of good subsequences is 24-1 = 15.
```

**Constraints:**

* `1 <= s.length <= 104`
* `s` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (Math, binomial coefficient)**

Here, the key observation is that given we have x0 occurrence of a and x1 occurrence of b, the number of good subsequence with k frequency is (1+(x0 choose k)) * (1 + (x1 choose k)) - 1. The +1 in multiplication is to account for the case where the given character doesn't appear in the answer and the -1 is to remove the case of empty string.
This implementation is strictly O(N). The key to achieve that is to update (x choose k) on-the-fly.

```
Runtime: 35 ms
Memory: 10.17 MB
```
```c++

class Solution {
public:
    int countGoodSubsequences(string s) {
        const int mod = 1'000'000'007; 
        vector<int> freq(26); 
        for (auto& ch : s) ++freq[ch-'a']; 
        long ans = 0; 
        vector<long> coef(26, 1), inv(s.size()+1); 
        inv[0] = inv[1] = 1; 
        for (int x = 1; x <= s.size(); ++x) {
            long val = 1; 
            if (x >= 2) inv[x] = mod - mod/x * inv[mod%x] % mod; 
            for (int i = 0; i < 26; ++i) {
                coef[i] = coef[i] * (freq[i]-x+1) % mod; 
                coef[i] = coef[i] * inv[x] % mod; 
                val = val * (1+coef[i]) % mod; 
            }
            ans = (ans + val - 1) % mod; 
        }
        return ans; 
    }
};
```
