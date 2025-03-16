3306. Count of Substrings Containing Every Vowel and K Consonants II

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

* `5 <= word.length <= 2 * 10^5`
* `word` consists only of lowercase English letters.
* `0 <= k <= word.length - 5`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 244 ms
Memory: 57.60 MB
```
```c++
class Solution {
    bool isVowel(char ch) {
        return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
    }
public:
    long long countOfSubstrings(string word, int k) {
        int n = word.size();
        unordered_map<char, int> vowels;
        int consonantCount = 0;
        long long result = 0;

        // Precompute next consonant positions
        vector<int> nextConsonant(n);
        int lastConsonant = n;
        for (int i = n - 1; i >= 0; i--) {
            nextConsonant[i] = lastConsonant;
            if (!isVowel(word[i])) lastConsonant = i;
        }

        // Sliding window
        int left = 0, right = 0;
        while (right < n) {
            // Expand window
            if (isVowel(word[right])) {
                vowels[word[right]]++;
            } else {
                consonantCount++;
            }

            // Shrink window if too many consonants
            while (left <= right && consonantCount > k) {
                if (isVowel(word[left])) {
                    if (--vowels[word[left]] == 0) vowels.erase(word[left]);
                } else {
                    consonantCount--;
                }
                left++;
            }

            // Count valid substrings
            while (left < right && vowels.size() == 5 && consonantCount == k) {
                result += (nextConsonant[right] - right);
                if (isVowel(word[left])) {
                    if (--vowels[word[left]] == 0) vowels.erase(word[left]);
                } else {
                    consonantCount--;
                }
                left++;
            }

            right++;
        }

        return result;
    }
};
```

**Solution 2: (Sliding Window)**

     0  1  2  3  4  5  6  7  8  9 
     a  a  e  i  o  u  q  a  e  q, k = 1
pre  6  6  6  6  6  6  9  9  9 10
    i^                j^-- 3  --|        
        ^              ^-- 3  --|
          ^               ^- 2 -|
             ^               ^ 1| 
ans                    6  8  9  9

```
Runtime: 442 ms, Beats 20.00%
Memory: 50.68 MB, Beats 46.30%
```
```c++
class Solution {
public:
    long long countOfSubstrings(string word, int k) {
        int n = word.size(), i, j, c = 0;
        unordered_map<char, int> cnt{
            {'a', 0},
            {'e', 0},
            {'i', 0},
            {'o', 0},
            {'u', 0}
        };
        long long ans = 0;
        vector<int> pre(n);
        j = n;
        for (i = n - 1; i >= 0; i--) {
            pre[i] = j;
            if (!cnt.count(word[i])) {
                j = i;
            }
        }
        i = 0;
        j = 0;
        while (j < n) {
            if (cnt.count(word[j])) {
                cnt[word[j]] += 1;
            } else {
                c += 1;
            }
            while (c > k) {
                if (cnt.count(word[i])) {
                    cnt[word[i]] -= 1;
                } else {
                    c -= 1;
                }
                i += 1;
            }
            while (cnt['a'] && cnt['e'] && cnt['i'] && cnt['o'] && cnt['u'] && c == k) {
                ans += pre[j] - j;
                if (cnt.count(word[i])) {
                    cnt[word[i]] -= 1;
                } else {
                    c -= 1;
                }
                i += 1;
            }
            j += 1;
        }
        return ans;
    }
};
```

**Solution 3: (Sliding Window (Relaxed Constraints))**
```
Runtime: 183 ms, Beats 65.75%
Memory: 48.71 MB, Beats 53.15%
```
```c++
class Solution {
    long atLeastK(string word, int k) {
        long numValidSubstrings = 0;
        int start = 0;
        int end = 0;
        // Keep track of counts of vowels and consonants.
        unordered_map<char, int> vowelCount;
        int consonantCount = 0;

        // Start sliding window.
        while (end < word.length()) {
            // Insert new letter.
            char newLetter = word[end];

            // Update counts.
            if (isVowel(newLetter)) {
                vowelCount[newLetter]++;
            } else {
                consonantCount++;
            }

            // Shrink window while we have a valid substring.
            while (vowelCount.size() == 5 and consonantCount >= k) {
                numValidSubstrings += word.length() - end;
                char startLetter = word[start];
                if (isVowel(startLetter)) {
                    if (--vowelCount[startLetter] == 0) {
                        vowelCount.erase(startLetter);
                    }
                } else {
                    consonantCount--;
                }
                start++;
            }

            end++;
        }

        return numValidSubstrings;
    }

    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
public:
    long long countOfSubstrings(string word, int k) {
        return atLeastK(word, k) - atLeastK(word, k + 1);
    }
};
```
