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
Runtime: 0 ms
Memory: 10.48 MB
```
```c++
class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        int n = strings.size();
        unordered_map<string, vector<string>> m;
        string cur;
        for (auto s: strings) {
            cur = "";
            for (int i = 1; i < s.size(); i ++) {
                cur += (((s[i]-s[i-1])%26 + 26)%26) + 'a';
            }
            m[cur].push_back(s);
        }
        vector<vector<string>> ans;
        for (auto [_, v]: m) {
            ans.push_back(v);
        }
        return ans;
    }
};
```
