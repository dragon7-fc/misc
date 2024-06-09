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

**Solution 2: (Greedy + Hashing)**
```
Runtime: 3 ms
Memory: 8.76 MB
```
```c++
class Solution {
public:
    bool canConvert(string str1, string str2) {
        if (str1 == str2) {
            return true;
        }
        
        unordered_map<char, char> conversionMappings;
        unordered_set<char> uniqueCharactersInStr2;
        
        // Make sure that no character in str1 is mapped to multiple characters in str2.
        for (int i = 0; i < str1.size(); i++) {
            if (conversionMappings.find(str1[i]) == conversionMappings.end()) {
                conversionMappings[str1[i]] = str2[i];
                uniqueCharactersInStr2.insert(str2[i]);
            } else if (conversionMappings[str1[i]] != str2[i]) {
                // this letter maps to 2 different characters, so str1 cannot transform into str2.
                return false;
            }
        }
        
        // No character in str1 maps to 2 or more different characters in str2 and there
        // is at least one temporary character that can be used to break any loops.
        if (uniqueCharactersInStr2.size() < 26) {
            return true;
        }
        
        // The conversion mapping forms one or more cycles and there are no temporary 
        // characters that we can use to break the loops, so str1 cannot transform into str2.
        return false;
    }
};
```
