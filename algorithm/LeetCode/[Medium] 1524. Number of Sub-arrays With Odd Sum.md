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

**Solution 3: (Prefix Sum with Odd-Even Counting)**

              1 2 3  4  5  6  7
prefixSum  0  1 3 6 10 15 21 28
oddCount   0  1 1 2  2  3  4  4
evenCount  1  1 2 2  3  3  3  4
count         1 2 4  6  9 12 16

case 1:
      x1 x2 x3 y1 y2 y3  = even
      -------- ---------
                   odd
      -> sum(x1+x2+x3) = odd

case 1:
      x1 x2 x3 y1 y2 y3  = odd
      -------- ---------
                  odd
      -> sum(x1+x2+x3) = even
```
Runtime: 4 ms, Beats 62.15%
Memory: 112.04 MB, Beats 55.17%
```
```c++
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1e9 + 7;
        int count = 0, prefixSum = 0;
        // evenCount starts as 1 since the initial sum (0) is even
        int oddCount = 0, evenCount = 1;

        for (int num : arr) {
            prefixSum += num;
            // If current prefix sum is even, add the number of odd subarrays
            if (prefixSum % 2 == 0) {
                count += oddCount;
                evenCount++;
            } else {
                // If current prefix sum is odd, add the number of even
                // subarrays
                count += evenCount;
                oddCount++;
            }

            count %= MOD;  // To handle large results
        }

        return count;
    }
};
```

**Solution 4: (DP Bottom-Up)**

         1 2 3 4 5  6  7
dp[0]  0 0 1 1 2 2  3  3
dp[1]  0 1 1 2 2 3  3  4
ans      1 2 4 6 9 12 16

```
Runtime: 2 ms, Beats 76.78%
Memory: 111.90 MB, Beats 80.00%
```
```c++
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int n = arr.size(), i, dp[2] = {0}, MOD=1e9+7;
        long long ans = 0;
        for (i = 0; i < n; i ++) {
            if (arr[i]%2) {
                swap(dp[0], dp[1]);
            }
            dp[arr[i]%2] += 1;
            ans += dp[1];
            ans %= MOD;
        }
        return ans;
    }
};
```
