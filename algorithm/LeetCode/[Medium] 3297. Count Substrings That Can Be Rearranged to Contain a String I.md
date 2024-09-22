3297. Count Substrings That Can Be Rearranged to Contain a String I

You are given two strings `word1` and `word2`.

A string `x` is called **valid** if `x` can be rearranged to have `word2` as a **prefix**.

Return the total number of **valid substrings** of `word1`.

 

**Example 1:**
```
Input: word1 = "bcca", word2 = "abc"

Output: 1

Explanation:

The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.
```

**Example 2:**
```
Input: word1 = "abcabc", word2 = "abc"

Output: 10

Explanation:

All the substrings except substrings of size 1 and size 2 are valid.
```

**Example 3:**
```
Input: word1 = "abcabc", word2 = "aaabc"

Output: 0
```
 

**Constraints:**

* `1 <= word1.length <= 10^5`
* `1 <= word2.length <= 10^4`
* `word1` and `word2` consist only of lowercase English letters.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 32 ms
Memory: 13.54 MB
```
```c++
class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        int m = word1.size(), n = word2.size(), i, j, k = 0, ck, cnt[26] = {0}, cnt2[26] = {0};
        bool flag;
        long long ans = 0;
        for (i = 0; i < n; i ++) {
            cnt2[word2[i]-'a'] += 1;
            if (cnt2[word2[i]-'a'] == 1) {
                k += 1;
            }
        }
        i = 0, j = 0;
        while (j < m) {
            cnt[word1[j]-'a'] += 1;
            ck = 0;
            for (int ii = 0; ii < 26; ii ++) {
                if (cnt2[ii] && cnt[ii] >= cnt2[ii]) {
                    ck += 1;
                }
            }
            while (ck == k && cnt[word1[i]-'a'] > cnt2[word1[i]-'a']) {
                cnt[word1[i]-'a'] -= 1;
                i += 1;
            }
            if (ck == k) {
                ans += i+1;
            }
            j += 1;
        }
        return ans;
    }
};
```
