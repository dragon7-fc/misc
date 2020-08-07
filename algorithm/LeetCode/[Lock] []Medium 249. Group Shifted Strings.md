249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: `"abc" -> "bcd"`. We can keep "shifting" which forms the sequence:

`"abc" -> "bcd" -> ... -> "xyz"`
Given a list of **non-empty** strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

**Example:**
```
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 28 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for string in strings:
            key = [0]
            for prev, c in zip(string, string[1:]):
                key += [(ord(c) - ord(prev)) % 26]
            d[tuple(key)] += [string]
            
        return [d[p] for p in d]
```

**Solution 2: (Hash Table)**
```
Runtime: 12 ms
Memory Usage: 8.4 MB
```
```c++
class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        std::unordered_map<std::string, std::vector<std::string>> m;
        for(const auto& s: strings) {
            size_t size{s.size()};
            string k{""};
            for(int i{0}; i < size; ++i) k += std::to_string((s[0]-s[i]+26) % 26)+",";
            m[k].emplace_back(s);
        }
        std::vector<std::vector<std::string>> res;
        for(const auto &[_, v]: m) res.emplace_back(v);
        return res;
    }
};
```