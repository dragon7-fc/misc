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

**Solution 3: (Greedy)**
```
Runtime: 527 ms
Memory Usage: 43.8 MB
```
```c
int cmp(const void *x, const void *y) {
	return *(int *) x - *(int *) y;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findOriginalArray(int* changed, int changedSize, int* returnSize){
    if(changedSize % 2){*returnSize = 0;return NULL;};
    int count[200002] = {0};
    int* ans = (int*)malloc(sizeof(int) * 100000);
    int ptr = 0;
    qsort(changed,changedSize,sizeof(int),cmp);
    for(int i = 0 ; i < changedSize ; i++){
        count[changed[i]]++;
    }
    for(int i = 0 ; i < changedSize ; i++){
        if(count[changed[i]] < 0){*returnSize = 0;return NULL;}
        while(count[changed[i]] > 0){
            count[changed[i]]--;
            count[2*changed[i]]--;
            if(count[changed[i]] >= 0){
                ans[ptr++] = changed[i];
            }
            if(count[changed[i]] < 0 || count[2*changed[i]] < 0){*returnSize = 0;return NULL;}
        }
        
    }
    if(ptr != (changedSize / 2)){*returnSize = 0;return NULL;};
    *returnSize = ptr;
    return ans;
}
```

**Solution 4: (Counter, Greedy)**
```
Runtime: 573 ms
Memory Usage: 144.2 MB
```
```c++
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        int n = changed.size();
        if (n % 2 == 1) return {};
        sort(changed.begin(), changed.end());
        vector<int> ans;
        map<int, int> mp;
        for (int i = 0; i < n; i++) {
            mp[changed[i]]++;
        }
        for (int i = 0; i < n; i++) {
          if (mp[changed[i]] == 0) continue;
          if (mp[changed[i] * 2] == 0) return {};
          ans.push_back(changed[i]);
          mp[changed[i]]--;
          mp[changed[i] * 2]--;
        }
        return ans;
    }
};
```
