1524. Number of Sub-arrays With Odd Sum

Given an array of integers `arr`. Return the number of sub-arrays with odd sum.

As the answer may grow large, the answer must be computed modulo `10^9 + 7`.

 

**Example 1:**
```
Input: arr = [1,3,5]
Output: 4
Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
```

**Example 2:**
```
Input: arr = [2,4,6]
Output: 0
Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
```

**Example 3:**
```
Input: arr = [1,2,3,4,5,6,7]
Output: 16
```

**Example 4:**
```
Input: arr = [100,100,99,99]
Output: 4
```

**Example 5:**
```
Input: arr = [7]
Output: 1
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 100`

# Submissions
---
**Solution 1: (Math, Greedy, Prefix Sum)**

* cur = 0 if current prefix sum is even
* cur = 1 if current prefix sum is odd
* count[0] is the number of even prefix sum
* count[1] is the number of odd prefix sum

For each element in A:
* if current prefix sum is even, res += the number of odd prefix sum
* if current prefix sum is odd, res += the number of even prefix sum

```
Runtime: 1340 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = [1, 0]
        cur = res = 0
        for a in arr:
            cur ^= a & 1
            res += count[1 - cur]
            count[cur] += 1
        return res % (10**9 + 7)
```

**Solution 2: (Math, Greedy, Prefix Sum)**
```
Runtime: 360 ms
Memory Usage: 108.3 MB
```
```c++
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int cur = 0, res = 0, count[] = {1, 0}, mod = (int)1e9 + 7;
        for (int a: arr) {
            cur ^= a & 1;
            res = (res + count[1 - cur]) % mod;
            count[cur]++;
        }
        return res;
    }
};
```