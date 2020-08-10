1153. String Transforms Into Another String

Given two strings `str1` and `str2` of the same length, determine whether you can transform `str1` into `str2` by doing zero or more conversions.

In one conversion you can convert **all** occurrences of one character in `str1` to any other lowercase English character.

Return `true` if and only if you can transform `str1` into `str2`.

 

**Example 1:**
```
Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
```

**Example 2:**
```
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
```

**Note:**

* `1 <= str1.length == str2.length <= 10^4`
* Both str1 and str2 contain only lowercase English letters.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 44 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        unique = {}
        graph = defaultdict(set)
        
        for s1, s2 in zip(str1, str2):
            graph[s1].add(s2)
            if s2 not in unique:
                unique[s2] = True
        
        if len(unique.keys()) >= 26:
            return False
        
        for neighbors in graph.values():
            if len(neighbors) > 1:
                return False
            
        return True
```

**Solution 2: (Hash Table)**
```
Runtime: 12 ms
Memory Usage: 7.8 MB
```
```c++
class Solution {
public:
    bool canConvert(string str1, string str2) {
        unordered_map<char, char> vmap;
        if (str1 == str2)   return true;
        if (str1.length() != str2.length()) return false;
        for (int i = 0; i < str1.length(); i++) {
            if (str1[i] != str2[i]) {
                if (vmap.find(str1[i]) == vmap.end()) {
                    vmap[str1[i]] = str2[i];
                } else if (vmap[str1[i]] != str2[i]){
                    return false;
                }
            }
        }
        
        return set(str2.begin(), str2.end()).size() < 26;
    }
};
```