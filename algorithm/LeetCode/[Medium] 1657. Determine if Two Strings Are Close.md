1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

* Operation 1: Swap any two existing characters.
    * For example, `abcde` -> `aecdb`
* Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    * For example, `aacabb` -> `bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` if `word1` and `word2` are **close**, and `false` otherwise.

__Hint1:__

Operation 1 allows you to freely reorder the string.

__Hint2:__

Operation 2 allows you to freely reassign the letters' frequencies.


**Example 1:**
```
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
```

**Example 2:**
```
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
```

**Example 3:**
```
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
```

**Example 4:**
```
Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.
```

**Constraints:**

* `1 <= word1.length, word2.length <= 105`
* `word1` and `word2` contain only lowercase English letters.

# Submissions
---
**Solution 1: (String)**

To solve this problem, we can find that if 2 strings have same unique characters and the value patterns are same, then we can return true.

```
Runtime: 124 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
```

**Solution 2: (String)**
```
Runtime: 63 ms
Memory: 20.78 MB
```
```c++
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        int cnt1[26] = {0}, cnt2[26] = {0};
        for (char c: word1) {
            cnt1[c-'a'] += 1;
        }
        for (char c: word2) {
            cnt2[c-'a'] += 1;
        }
        vector<int> v1, v2;
        for (int i = 0; i < 26; i ++) {
            if (cnt1[i] && !cnt2[i] || !cnt1[i] && cnt2[i]) {
                return false;
            }
            if (cnt1[i]) {
                v1.push_back(cnt1[i]);
            }
            if (cnt2[i]) {
                v2.push_back(cnt2[i]);
            }
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        return v1 == v2;
    }
};
```
