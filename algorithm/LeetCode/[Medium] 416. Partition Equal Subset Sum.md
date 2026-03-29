416. Partition Equal Subset Sum

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise. 

**Example 1:**
```
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**
```
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```

**Constraints:**

* `1 <= nums.length <= 200`
* `1 <= nums[i] <= 100`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 664 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True

        # in case total is odd, then there is no way for us to evenly divide the sum
        total = sum(nums)

        if total & 1:
            return False

        total >>= 1

        dp = [False] * (total + 1)
        dp[0] = True

        for num in nums:
            for s in range(total, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 1156 ms
Memory Usage: 260.9 MB
```
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        sm = sum(nums)
        if sm%2: return False
        target = sm//2
        
        @functools.lru_cache(None)
        def dfs(i, g1):
            if i == N:
                if g1 == 0:
                    return True
                else:
                    return False
            if dfs(i+1, g1-nums[i]) or dfs(i+1, g1):
                return True
            else:
                return False
            
        return dfs(0, target)
```

**Solution 3: (DP Bottom-UP)**
```
Runtime: 40 ms
Memory Usage: 6.1 MB
```
```c


bool canPartition(int* nums, int numsSize){
    int sum = 0;
    for (int i = 0; i < numsSize; i ++) {
        sum += nums[i];
    }
    if (sum%2)
        return false;
    sum >>= 1;
    bool *dp = calloc(1, (sum+1)*sizeof(bool));
    dp[0] = true;
    for (int i = 0; i < numsSize; i ++) {
        for (int s = sum; s >= nums[i]; s--) {
            dp[s] = dp[s] || dp[s-nums[i]];
        }
    }
    return dp[sum];
}
```

**Solution 4: (DP Bottom-Up)**

    1  5  5 11
a   0  0  0
    1  1  5
       6  1
          6
          11<

    
    1 2 5
    0 0 0
    1 1 1
      2 2
      3 3
        5
        6

```
Runtime: 21 ms, Beats 98.25%
Memory: 14.79 MB, Beats 82.88%
```
```c++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size(), i = 0, j, a = accumulate(nums.begin(), nums.end(), 0), t;
        if (a%2) {
            return false;
        }
        t = a/2;
        vector<int> dp(t+1);
        dp[0] = 1;
        for (i = 0; i < n; i ++) {
            for (j = t-nums[i]; j >= 0; j --) {
                a = j + nums[i];
                dp[a] |= dp[j];
                if (a == t && dp[a]) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

**Solution 5: (DP Bottom-Up)**


    [1, 5, 11, 5]

dp  0  1  2  3  4  5  6  7  8  9  10  11
1   x  x
5                  x  x
11                                     x
5                                  x   x
                                       ^
```
Runtime: 31 ms, Beats 97.53%
Memory: 14.71 MB, Beats 81.82%
```
```c++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size(), i, a, b, mx;
        a = accumulate(nums.begin(), nums.end(), 0);
        if (a%2) {
            return false;
        }
        vector<int> dp(a/2 + 1);
        dp[0] = 1;
        for (i = 0; i < n; i ++) {
            for (b = a/2; b - nums[i] >= 0; b --) {
                dp[b] |= dp[b - nums[i]];
            }
        }
        return dp[a/2];
    }
};
```

**Solution 6: (DP Bottom-Up, bitset)**

                    [       1,       5,       11,       5]
        bitset
       9876543210
     000000000001
1    000000000011
6    000001100011
11   100001100011
5    100001100011


```
Runtime: 3 ms, Beats 99.38%
Memory: 14.41 MB, Beats 77.46%
```
```c++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2 != 0) return false;
        int target = sum / 2;

        // A bitset where bit 'i' is 1 if sum 'i' is possible
        // Max sum is 200 * 100 = 20,000. Half is 10,000.
        bitset<10001> dp(1); // bit 0 is initialized to 1 (sum 0 is always possible)

        for (int num : nums) {
            dp |= (dp << num); // "Cascade" the possible sums using bitwise OR
        }

        return dp[target];
    }
};
```
