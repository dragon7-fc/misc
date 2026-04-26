3913. Sort Vowels by Frequency

You are given a string `s` consisting of lowercase English characters.

Rearrange only the **vowels** in the string so that they appear in **non-increasing** order of their frequency.

If multiple vowels have the same frequency, order them by the position of their **first occurrence** in `s`.

Return the modified string.

Vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

The **frequency** of a letter is the number of times it occurs in the string.

 

**Example 1:**
```
Input: s = "leetcode"

Output: "leetcedo"

Explanation:

Vowels in the string are ['e', 'e', 'o', 'e'] with frequencies: e = 3, o = 1.
Sorting in non-increasing order of frequency and placing them back into the vowel positions results in "leetcedo".
```

**Example 2:**
```
Input: s = "aeiaaioooa"

Output: "aaaaoooiie"

Explanation:

Vowels in the string are ['a', 'e', 'i', 'a', 'a', 'i', 'o', 'o', 'o', 'a'] with frequencies: a = 4, o = 3, i = 2, e = 1.
Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in "aaaaoooiie".
```

**Example 3:**
```
Input: s = "baeiou"

Output: "baeiou"

Explanation:

Each vowel appears exactly once, so all have the same frequency.
Thus, they retain their relative order based on first occurrence, and the string remains unchanged.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of lowercase English letters

# Submissions
---
**Solution 1: (Counter, Sort)**
```
Runtime: 20 ms, Beats 64.72%
Memory: 19.25 MB, Beats 50.61%
```
```c++
class Solution {
public:
    string sortVowels(string s) {
        int n = s.length(), i, j;
        vector<pair<int, int>> cnt(26);
        string vowel = "aeiou";
        for (i = 0; i < n; i ++) {
            if (vowel.find(s[i]) != string::npos) {
                if (cnt[s[i] - 'a'].first == 0) {
                    cnt[s[i] - 'a'] = {1, i};
                } else {
                    cnt[s[i] - 'a'].first += 1;
                }
            }
        }
        sort(vowel.begin(), vowel.end(), [&](const auto &a, const auto &b){
            if (cnt[a - 'a'].first != cnt[b - 'a'].first) {
                return cnt[a - 'a'].first > cnt[b - 'a'].first;
            } else {
                return cnt[a - 'a'].second < cnt[b - 'a'].second;
            }
        });
        j = 0;
        string ans;
        for (i = 0; i < n; i ++) {
            if (vowel.find(s[i]) == string::npos) {
                ans += s[i];
            } else {
                if (cnt[vowel[j] - 'a'].first == 0) {
                    j += 1;
                }
                ans += vowel[j];
                cnt[vowel[j] - 'a'].first -= 1;
            }
        }
        return ans;
    }
};
```
