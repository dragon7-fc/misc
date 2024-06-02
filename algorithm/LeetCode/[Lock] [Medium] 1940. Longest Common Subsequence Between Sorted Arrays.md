1940. Longest Common Subsequence Between Sorted Arrays

Given an array of integer arrays `arrays` where each `arrays[i]` is sorted in **strictly increasing** order, return an integer array representing the **longest common subsequence** between **all** the arrays.

A **subsequence** is a sequence that can be derived from another sequence by deleting some elements (possibly none) without changing the order of the remaining elements.

 

**Example 1:**
```
Input: arrays = [[1,3,4],
                 [1,4,7,9]]
Output: [1,4]
Explanation: The longest common subsequence in the two arrays is [1,4].
```

**Example 2:**
```
Input: arrays = [[2,3,6,8],
                 [1,2,3,5,6,7,10],
                 [2,3,4,6,9]]
Output: [2,3,6]
Explanation: The longest common subsequence in all three arrays is [2,3,6].
```

**Example 3:**
```
Input: arrays = [[1,2,3,4,5],
                 [6,7,8]]
Output: []
Explanation: There is no common subsequence between the two arrays.
```

**Constraints:**

* `2 <= arrays.length <= 100`
* `1 <= arrays[i].length <= 100`
* `1 <= arrays[i][j] <= 100`
* `arrays[i]` is sorted in **strictly increasing** order.

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 236 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        s = set(arrays[0])
        for i in range(1, len(arrays)):
            s = s & set(arrays[i])
        return sorted(s)
```

**Solution 2; (reduce)**
```
Runtime: 370 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        return sorted(list(reduce(lambda x, y: set(x) & set(y), arrays)))
```

**Solution 3: (Two Pointers)**
```
Runtime: 23 ms
emory: 18.10 MB
```
```c++
class Solution {
public:
    vector<int> longestCommonSubsequence(vector<vector<int>>& arrays) {
        int m = arrays.size(), n = arrays[0].size();
        vector<int> dp(m), ans;
        int cnt;
        for (int j = 0; j < n; j ++) {
            cnt = 1;
            for (int i = 1; i < m; i ++) {
                while (dp[i] < arrays[i].size() && arrays[i][dp[i]] < arrays[0][j]) {
                    dp[i] += 1;
                }
                if (dp[i] >= arrays[i].size()) {
                    break;
                }
                cnt += arrays[i][dp[i]] == arrays[0][j];
            }
            if (cnt == m) {
                ans.push_back(arrays[0][j]);
            }
        }
        return ans;
    }
};
```

**Solution 4: (Binary Search)**
```
Runtime: 26 ms
Memory: 18.04 MB
```
```c++
class Solution {
public:
    vector<int> longestCommonSubsequence(vector<vector<int>>& arrays) {
        int m = arrays.size(), n = arrays[0].size();
        vector<int>dp(m), ans;
        int cnt;
        for (int j = 0; j < n; j ++) {
            cnt = 1;
            for (int i = 1; i < m; i ++) {
                if (dp[i] >= arrays[i].size()) {
                    break;
                }
                auto it = lower_bound(arrays[i].begin()+dp[i], arrays[i].end(), arrays[0][j]);
                dp[i] = it - arrays[i].begin();
                if (it >= arrays[i].end()) {
                    break;
                }
                if (*it == arrays[0][j]) {
                    cnt += 1;
                }
            }
            if (cnt == m) {
                ans.push_back(arrays[0][j]);
            }
        }
        return ans;
    }
};
```
