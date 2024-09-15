1310. XOR Queries of a Subarray

Given the array `arr` of positive integers and the array `queries` where `queries[i] = [Li, Ri]`, for each query `i` compute the **XOR** of elements from `Li` to `Ri` (that is, `arr[Li]` xor `arr[Li+1]` xor ... xor `arr[Ri]` ). Return an array containing the result for the given queries.
 

**Example 1:**
```
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
```

**Example 2:**
```
Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
```

**Constraints:**

* `1 <= arr.length <= 3 * 10^4`
* `1 <= arr[i] <= 10^9`
* `1 <= queries.length <= 3 * 10^4`
* `queries[i].length == 2`
* `0 <= queries[i][0] <= queries[i][1] < arr.length`

# Submissions
---
**Solution 1: (Bit Manipulation)**

A number XOR itself is `0`. Based on this conclusion:

1. Compute the prefix XOR of `arr`;
1. Get the solution for each query from prefix XOR in `1.`

```
Runtime: 412 ms
Memory Usage: 27.2 MB
```
```python
import functools
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        prefixXor = [0] * (N + 1)
        for i, a in enumerate(arr):
            prefixXor[i + 1] = prefixXor[i] ^ a
        return [(prefixXor[Ri + 1] ^ prefixXor[Li]) for Li, Ri in queries]   
```

**Solution 2: (Prefix Sum)**
```
Runtime: 60 ms
Memory: 41.52 MB
```
```c++
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> dp(arr.size()+1), ans(queries.size());
        for (int i = 0; i < arr.size(); i ++) {
            dp[i+1] = dp[i]^arr[i];
        }
        for (int i = 0; i < queries.size(); i ++) {
            ans[i] = dp[queries[i][1]+1]^dp[queries[i][0]];
        }
        return ans;
    }
};
```
