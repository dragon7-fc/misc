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
