791. Custom Sort String

`S` and `T` are strings composed of lowercase letters. In `S`, no letter occurs more than once.

`S` was sorted in some custom order previously. We want to permute the characters of `T` so that they match the order that `S` was sorted. More specifically, if `x` occurs before `y` in `S`, then `x` should occur before `y` in the returned string.

Return any permutation of `T` (as a string) that satisfies this property.

**Example :**
```
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
```

**Note:**

* `S` has length at most `26`, and no character is repeated in `S`.
* `T` has length at most `200`.
* `S` and `T` consist of lowercase letters only.

# Submissions
---
**Solution 1: (String, Counter)**
```
Runtime: 32 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        cnt, ans = Counter(str), ""
        for c in order:
            if c in cnt:
                ans += c*cnt[c]
                cnt.pop(c)
                
        return ans + "".join(c*cnt[c] for c in cnt) 
```

**Solution 2: (Sort, Hash Table)**
```
Runtime: 6 ms
Memory Usage: 6.3 MB
```
```c++
class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char,int> mp;
        
        for(int i=0;i<order.size();i++)
            mp[order[i]]=i;
        
        sort(s.begin(),s.end(),[&](const char &a,const char &b)
            {
                return mp[a]<mp[b];
            }
        );
        return s;
    }
};
```
