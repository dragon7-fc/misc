3305. Count of Substrings Containing Every Vowel and K Consonants I

You are given a string `word` and a non-negative integer `k`.

Return the total number of **substrings** of `word` that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) **at least** once and **exactly** `k` consonants.

 

**Example 1:**
```
Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.
```

**Example 2:**
```
Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
```

**Example 3:**
```
Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
```

**Constraints:**

`5 <= word.length <= 250`
`word` consists only of lowercase English letters.
`0 <= k <= word.length - 5`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 256 ms
Memory: 17.88 MB
```
```c++
class Solution {
    bool is_vow(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
public:
    int countOfSubstrings(string word, int k) {
        unordered_map<char,int> cnt;
        int n = word.size(), ans = 0;
        for (int i = 0; i < n; i ++) {
            cnt.clear();
            for (int j = i; j < n; j ++) {
                if (is_vow(word[j])) {
                    cnt[word[j]] += 1;
                } else {
                    cnt['c'] += 1;
                }
                if (cnt['a'] && cnt['e'] && cnt['i'] && cnt['o'] && cnt['u'] && cnt['c'] == k) {
                    ans += 1;
                }
            }
        }
        return ans;
    }
};
```
