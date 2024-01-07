1910. Remove All Occurrences of a Substring

Given two strings `s` and `part`, perform the following operation on `s` until all occurrences of the substring `part` are removed:

* Find the **leftmost** occurrence of the substring `part` and remove it from `s`.

Return `s` after removing all occurrences of `part`.

A **substring** is a contiguous sequence of characters in a string.

 

**Example 1:**
```
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
```

**Example 2:**
```
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
```

**Constraints:**

* `1 <= s.length <= 1000`
* `1 <= part.length <= 1000`
* `s` and `part` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 52 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        N = len(part)
        cur = []
        for c in s:
            cur += [c]
            while cur and len(cur) >= N and ''.join(cur[-N:]) == part:
                i = N
                while i > 0:
                    cur.pop()
                    i -= 1
        return ''.join(cur)
```

**Solution 2: (String)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        r = ''
        for ch in s:
            r = (r + ch).removesuffix(part)
        return r
```

**Solution 3: (reduce)**
```
Runtime: 36 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        return reduce(lambda a, b: (a + b).removesuffix(part), s, '')
```

**Solution 3: (String)**
```
Runtime: 0 ms
Memory: 7.1 MB
```
```c++
class Solution {
public:
    string removeOccurrences(string s, string part) {
        int pos=s.find(part);
        while(pos!=string::npos)
        {
            s.erase(pos,part.length());
            pos=s.find(part);
        }
        return s;
    }
};
```
