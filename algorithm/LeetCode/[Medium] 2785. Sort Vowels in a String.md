2785. Sort Vowels in a String


Given a **0-indexed** string `s`, permute s to get a new string `t` such that:

* All consonants remain in their original places. More formally, if there is an index `i` with `0 <= i < s.length` such that `s[i]` is a consonant, then `t[i] = s[i]`.
* The vowels must be sorted in the **nondecreasing** order of their ASCII values. More formally, for pairs of indices `i, j` with `0 <= i < j < s.length` such that `s[i]` and `s[j]` are vowels, then `t[i]` must not have a higher ASCII value than `t[j]`.

Return the resulting string.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

 

**Example 1:**
```
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
```

**Example 2:**
```
Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists only of letters of the English alphabet in **uppercase** and **lowercase**.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 58 ms
Memory: 11.6 MB
```
```c++
class Solution {
    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'o'|| ch == 'u'|| ch == 'i';
    }
public:
    string sortVowels(string s) {
        string v;
        copy_if(begin(s), end(s), back_inserter(v), [&](char ch){ 
            return isVowel(tolower(ch)); 
        });
        sort(begin(v), end(v));
        for (int i = 0, j = 0; i < s.size(); ++i)
            if (isVowel(tolower(s[i])))
                s[i] = v[j++];
        return s;
    }
};
```

**Solution 2: (Counting Sort)**
```
Runtime: 42 ms
Memory: 13.3 MB
```
```c++
class Solution {
    // Returns true if the character is a vowel.
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'o'|| c == 'u'|| c == 'i' 
            || c == 'A' || c == 'E' || c == 'O'|| c == 'U'|| c == 'I';
    }
public:
    string sortVowels(string s) {
        unordered_map<char, int> count;

        // Store the frequencies for each character.
        for (char c : s) {
            if (isVowel(c)) {
                count[c]++;
            }
        }

        // Sorted string having all the vowels.
        string sortedVowel = "AEIOUaeiou";
        string ans;
        int j = 0;
        for (int i = 0; i < s.size(); i++) {
            if (!isVowel(s[i])) {
                ans += s[i];
            } else {
                // Skip to the character which is having remaining count.
                while (count[sortedVowel[j]] == 0) {
                    j++;
                }

                ans += sortedVowel[j];
                count[sortedVowel[j]]--;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Counting Sort)**
```
Runtime: 29 ms, Beats 11.13%
Memory: 17.54 MB, Beats 19.94%
```
```c++
class Solution {
public:
    string sortVowels(string s) {
        int n = s.size(), i, j = 0;
        unordered_map<char, int> cnt;
        unordered_set<char> st = {
            'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'
        };
        string vowels = "AEIOUaeiou";
        for (i = 0; i < n; i ++) {
            if (st.count(tolower(s[i]))) {
                cnt[s[i]] += 1;
                s[i] = '.';
            }
        }
        for (i = 0; i < n; i ++) {
            if (s[i] == '.') {
                while (cnt[vowels[j]] == 0) {
                    j += 1;
                }
                s[i] = vowels[j];
                cnt[vowels[j]] -= 1;
            }
        }
        return s;
    }
};
```
