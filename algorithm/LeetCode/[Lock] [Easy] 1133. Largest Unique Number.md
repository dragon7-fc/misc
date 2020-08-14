1133. Largest Unique Number

Given an array of integers `A`, return the largest integer that only occurs once.

If no integer occurs once, return `-1`.

 

**Example 1:**
```
Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
```

**Example 2:**
```
Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
```

**Note:**

* `1 <= A.length <= 2000`
* `0 <= A[i] <= 1000`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 40 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        for k in sorted(cnt, reverse=True):
            if cnt[k] == 1:
                return k
        return -1
```

**Solution 2: (Hash Table)**
```
Runtime: 12 ms
Memory Usage: 9.1 MB
```
```c++
class Solution {
public:
    int largestUniqueNumber(vector<int>& A) {
        unordered_map<int, int> fre; // frequency for array A
        for (int x : A) fre[x]++;

        int res = -1;
        for (auto& p : fre)
          if (p.second == 1) res = max(res, p.first);

        return res;
    }
};
```