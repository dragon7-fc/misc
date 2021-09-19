2007. Find Original Array From Doubled Array

An integer array `original` is transformed into a doubled array `changed` by appending **twice the value** of every element in `original`, and then randomly **shuffling** the resulting array.

Given an array `changed`, return `original` if `changed` is a **doubled** array. If `changed` is not a **doubled** array, return an empty array. The elements in original may be returned in **any** order.

 

**Example 1:**
```
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
```

**Example 2:**
```
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
```

**Example 3:**
```
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
```

**Constraints:**

* `1 <= changed.length <= 10^5`
* `0 <= changed[i] <= 10^5`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 1296 ms
Memory Usage: 32.4 MB
```
```python
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        if c[0] % 2:
            return []
        for x in sorted(c):
            if c[x] > c[2 * x]:
                return []
            c[2 * x] -= c[x] if x else c[x] // 2
        return list(c.elements())
```

**Solution 2: (Greedy)**
```
Runtime: 332 ms
Memory Usage: 146.3 MB
```
```c++
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        if (changed.size() % 2) return {};
        unordered_map<int, int> c;
        for (int a : changed) c[a]++;
        vector<int> keys;
        for (auto it : c)
            keys.push_back(it.first);
        sort(keys.begin(), keys.end(), [](int i, int j) {return abs(i) < abs(j);});
        vector<int> res;
        for (int x : keys) {
            if (c[x] > c[2 * x]) return {};
            for (int i = 0; i < c[x]; ++i, c[2 * x]--)
                res.push_back(x);
        }
        return res;
    }
};
```
