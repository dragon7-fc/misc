1750. Minimum Length of String After Deleting Similar Ends

Given a string `s` consisting only of characters `'a'`, `'b'`, and `'c'`. You are asked to apply the following algorithm on the string any number of times:

* Pick a **non-empty** prefix from the string s where all the characters in the prefix are equal.
* Pick a **non-empty** suffix from the string s where all the characters in this suffix are equal.
* The prefix and the suffix should not intersect at any index.
* The characters from the prefix and suffix must be the same.
* Delete both the prefix and the suffix.

Return the minimum length of `s` after performing the above operation any number of times (possibly zero times).

 

**Example 1:**
```
Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
```

**Example 2:**
```
Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
```

**Example 3:**
```
Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` only consists of characters `'a'`,` 'b'`, and `'c'`.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 100 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)
```

**Solution 2: (Two Pointers)**
```
Runtime: 23 ms
Memory: 13.2 MB
```
```c++
class Solution {
public:
    int minimumLength(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j && s[i] == s[j]) {
            auto ch = s[i];
            while (i <= j && s[i] == ch)
                ++i;
            while (i <= j && s[j] == ch)
                --j;
        }
        return j - i + 1;
    }
};
```
