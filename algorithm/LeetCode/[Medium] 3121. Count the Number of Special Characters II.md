3121. Count the Number of Special Characters II

You are given a string `word`. A letter `c` is called **special** if it appears both in lowercase and uppercase in word, and **every** lowercase occurrence of `c` appears before the **first** uppercase occurrence of `c`.

Return the number of special letters in word.

 

**Example 1:**
```
Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.
```

**Example 2:**
```
Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.
```

**Example 3:**
```
Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.
```
 

**Constraints:**

* `1 <= word.length <= 2 * 10^5`
* `word` consists of only lowercase and uppercase English letters.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 70 ms
Memory: 23.08 MB
```
```c++
class Solution {
public:
    int numberOfSpecialChars(string word) {
        vector<int> last(26, INT_MAX);
        vector<int> first(26, INT_MIN);
        for (int i = 0; i < word.size(); i ++) {
            if (word[i] < 'a' && first[word[i]-'A'] == INT_MIN) {
                first[word[i]-'A'] = i; 
            }
            if (word[i] >= 'a') {
                last[word[i]-'a'] = i;
            }
        }
        int ans = 0;
        for (int i = 0; i < 26; i ++) {
            ans += (last[i] < first[i]);
        }
        return ans;
    }
};
```
