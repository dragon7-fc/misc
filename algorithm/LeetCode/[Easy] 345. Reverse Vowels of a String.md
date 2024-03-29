345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

**Example 1:**
```
Input: "hello"
Output: "holle"
```

**Example 2:**
```
Input: "leetcode"
Output: "leotcede"
```

**Note:**

* The vowels does not include the letter "y".

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 56 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        i, j = 0, len(s)-1
        s = list(s)
        while i < j:
            while i<j and s[i].lower() not in vowels:
                i += 1
            while j>i and s[j].lower() not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i,j = i+1, j-1
        return ''.join(s)
```

**Solution 2: (Two Pointers)**
```
Runtime: 17 ms
Memory: 8.2 MB
```
```c++
class Solution {
public:
    string reverseVowels(string s) {
        set<char> vwls = {'a','e','i','o','u','A','E','I','O','U'};
        for (int l = 0, r = s.size()-1; l < r; )
        {
            while (l < r && !vwls.count(s[l])) ++l;
            while (l < r && !vwls.count(s[r])) --r;
            swap(s[l++], s[r--]);
        }
        return s;
    }
};
```
