383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

**Note:**

You may assume that both strings contain only lowercase letters.
```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 48 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = collections.Counter(ransomNote)
        magazineCounter = collections.Counter(magazine)
        magazineCounter.subtract(ransomCounter)
        return all([counts >=  0 for counts in magazineCounter.values()])
```

**Solution 2: (Counter)**
```
Runtime: 52 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(collections.Counter(ransomNote) - collections.Counter(magazine)) == 0
```

**Solution 3: (Counter)**
```
Runtime: 20 ms
Memory Usage: 9 MB
```
```c++
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> rm;
        unordered_map<char, int> mz;
        
        for(auto x: ransomNote) rm[x]++;
        for(auto x: magazine) mz[x]++;
        
        for(auto x : rm)
        {
            if(mz[x.first]<x.second)
                return false;
        }
        return true;
    }
};
```
