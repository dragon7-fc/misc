291. Word Pattern II

Given a `pattern` and a string `s`, return `true` if `s` **matches** the `pattern`.

A string `s` **matches** a `pattern` if there is some **bijective mapping** of single characters to strings such that if each character in `pattern` is replaced by the string it maps to, then the resulting string is `s`. A **bijective mapping** means that no two characters map to the same string, and no character maps to two different strings.

 

**Example 1:**
```
Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
```

**Example 2:**
```
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
```

**Example 3:**
```
Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
```

**Constraints:**

* `1 <= pattern.length, s.length <= 20`
* `pattern` and `s` consist of only lowercase English letters.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 39 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(cur: str, pattern: str, mappings: dict):
            # if the pattern is empty, we've exhausted our search
            if not pattern:
                # if the string is also empty, we've found a bijective mapping
                return not cur
            # if the pattern is already mapped, we must use the provided mapping
            if pattern[0] in mappings:
                # if this isn't a valid mapping, return false
                if cur[:len(mappings[pattern[0]])] != mappings[pattern[0]]:
                    return False
                # otherwise continue backtracking
                return backtrack(cur[len(mappings[pattern[0]]):], pattern[1:], mappings)
            # try each subset of the remaining string as a mapping
            for i in range(len(cur)):
                # if the current substring maps to another value, it isn't valid
                if cur[:i+1] in mappings.values():
                    continue
                # map the pattern to the substring
                mappings[pattern[0]] = cur[:i+1]
                # backtrack
                if backtrack(cur[i+1:], pattern[1:], mappings):
                    return True
                # delete the invalid mapping
                del mappings[pattern[0]]
            # none of the substrings were valid, so there is no valid mapping
            return False
        return backtrack(s, pattern, {})
```

**Solution 2; (Backtracking)**
```
Runtime: 0 ms
Memory Usage: 6.5 MB
```
```c++
class Solution {
    unordered_map<char, string> mymap;
    unordered_map<string, char> mymap1;
    
public:
    bool wordPatternMatch(string pattern, string s) {
        if (pattern.length() == 0 && s.length() == 0) {
            return true;
        }
        
        if (pattern.length() == 0 || s.length() == 0) {
            return false;
        }
        
        char p = pattern[0];
        pattern.erase(0, 1);
        if (mymap.find(p) != mymap.end()) {
            string temp = mymap[p];
            size_t pos = s.find(temp);
            if (pos != 0) {
                return false;
            }
            s.erase(0, temp.length());
            return wordPatternMatch(pattern, s);
        }
        
        for (int i = 1; i <= s.length(); i++) {
            string temp = s.substr(0, i);
            if (mymap1.find(temp) != mymap1.end()) {
                continue;
            }
            string s1 = s;
            mymap[p] = temp;
            mymap1[temp] = p;
            s1.erase(0, i);
            if (wordPatternMatch(pattern, s1)) {
                return true;
            }
            mymap.erase(p);
            mymap1.erase(temp);
        }
        
        return false;
    }
};
```
