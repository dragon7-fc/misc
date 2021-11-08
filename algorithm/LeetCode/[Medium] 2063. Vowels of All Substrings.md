2063. Vowels of All Substrings

Given a string `word`, return the **sum of the number of vowels** (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) in every substring of word.

A **substring** is a contiguous (non-empty) sequence of characters within a string.

**Note:** Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.

 

**Example 1:**
```
Input: word = "aba"
Output: 6
Explanation: 
All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
- "b" has 0 vowels in it
- "a", "ab", "ba", and "a" have 1 vowel each
- "aba" has 2 vowels in it
Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6. 
```

**Example 2:**
```
Input: word = "abc"
Output: 3
Explanation: 
All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
- "a", "ab", and "abc" have 1 vowel each
- "b", "bc", and "c" have 0 vowels each
Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3. 
```

**Example 3:**
```
Input: word = "ltcd"
Output: 0
Explanation: There are no vowels in any substring of "ltcd".
```

**Example 4:**
```
Input: word = "noosabasboosa"
Output: 237
Explanation: There are a total of 237 vowels in all the substrings.
```

**Constraints:**

* `1 <= word.length <= 10^5`
* `word` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 120 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def countVowels(self, word: str) -> int:
        return sum((i + 1) * (len(word) - i) for i, c in enumerate(word) if c in 'aeiou')
```

**Solution 2: (Math)**
```
Runtime: 52 ms
Memory Usage: 10.9 MB
```
```python
class Solution {
public:
    long long countVowels(string word) {
        long res = 0, n = word.size();
        for (int i = 0; i < n; ++i)
            if (string("aeiou").find(word[i]) != string::npos)
                res += (i + 1) * (n - i);
        return res;
    }
};
```
