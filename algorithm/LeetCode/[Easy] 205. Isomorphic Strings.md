205. Isomorphic Strings

Given two strings **s** and **t**, determine if they are isomorphic.

Two strings are isomorphic if the characters in **s** can be replaced to get **t**.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

**Example 1:**
```
Input: s = "egg", t = "add"
Output: true
```

**Example 2:**
```
Input: s = "foo", t = "bar"
Output: false
```

**Example 3:**
```
Input: s = "paper", t = "title"
Output: true
```

**Note:**

* You may assume both **s** and **t** have the same length.

# Submissions
---
**Solution 1: (Character Mapping with Dictionary)**
```
Runtime: 32 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping_s_t = {}
        mapping_t_s = {}
        
        for c1, c2 in zip(s, t):
            
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
            
        return True
```

**Solution 2: (First occurence transformation)**
```
Runtime: 72 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def transformString(self, s: str) -> str:
        
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            
            if c not in index_mapping:
                index_mapping[c] = i
                
            new_str.append(str(index_mapping[c]))
        
        return "".join(new_str)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
```

**Solution 3: (Hash Table)**
```
Runtime: 52 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for p, q in zip(s, t):
            if p not in d:
                if q in d.values():
                    return False
                d[p] = q
            elif d[p] != q:
                return False
        return True
```

**Solution 4: (2 Hash Table)**
```
Runtime: 3 ms
Memory: 9.37 MB
```
```c++
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> m, m2;
        for (int i = 0; i < s.size(); i ++) {
            if (m.count(s[i])) {
                if (m[s[i]] != t[i]) {
                    return false;
                }
            } else if (m2.count(t[i])) {
                if (m2[t[i]] != s[i]) {
                    return false;
                }
            } else {
                m[s[i]] = t[i];
                m2[t[i]] = s[i];
            }
        }
        return true;
    }
};
```
