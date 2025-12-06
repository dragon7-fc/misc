689. Maximum Sum of 3 Non-Overlapping Subarrays

In a given array `nums` of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size `k`, and we want to maximize the sum of all `3*k` entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

**Example:**
```
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
```

**Note:**

* `nums.length` will be between `1` and `20000`.
* `nums[i]` will be between `1` and `65535`.
* `k` will be between `1` and `floor(nums.length / 3)`.

# Solution
---
## Approach #1: Ad-Hoc [Accepted]
**Intuition**

It is natural to consider an array `W` of each interval's sum, where each interval is the given length `K`. To create `W`, we can either use prefix sums, or manage the sum of the interval as a window slides along the array.

From there, we approach the reduced problem: Given some array `W` and an integer `K`, what is the lexicographically smallest tuple of indices `(i, j, k)` with `i + K <= j` and `j + K <= k` that maximizes `W[i] + W[j] + W[k]`?

**Algorithm**

Suppose we fixed `j`. We would like to know on the intervals $i \in [0, j-K]$ and $k \in [j+K, \text{len}(W)-1]$, where the largest value of $W[i]$ (and respectively $W[k]$) occurs first. (Here, first means the smaller index.)

We can solve these problems with dynamic programming. For example, if we know that $i$ is where the largest value of $W[i]$ occurs first on $[0, 5]$, then on $[0, 6]$ the first occurrence of the largest $W[i]$ must be either $i$ or $6$. If say, $6$ is better, then we set `best = 6`.

At the end, `left[z]` will be the first occurrence of the largest value of `W[i]` on the interval $i \in [0, z]$, and `right[z]` will be the same but on the interval $i \in [z, \text{len}(W) - 1]$. This means that for some choice `j`, the candidate answer must be `(left[j-K], j, right[j+K]).` We take the candidate that produces the maximum `W[i] + W[j] + W[k]`.

```python
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of the array. Every loop is bounded in the number of steps by $N$, and does $O(1)$ work.

* Space complexity: $O(N)$. W, left, and right all take $O(N)$ memory.

# Submissions
---
**Solution 1: (Ad-Hoc, Prefix Sum, DP)**
```
Runtime: 212 ms
Memory Usage: 15.3 MB
```
```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], K: int) -> List[int]:
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory: 31.26 MB
```
```c++
class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();

        // Prefix sum array to calculate sum of any subarray in O(1) time
        vector<int> prefixSum(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1];
        }

        // Arrays to store the best sum and starting indices for up to 3
        // subarrays
        vector<vector<int>> bestSum(4, vector<int>(n + 1, 0));
        vector<vector<int>> bestIndex(4, vector<int>(n + 1, 0));

        // Compute the best sum and indices for 1, 2, and 3 subarrays
        for (int subarrayCount = 1; subarrayCount <= 3; subarrayCount++) {
            for (int endIndex = k * subarrayCount; endIndex <= n; endIndex++) {
                int currentSum = prefixSum[endIndex] - prefixSum[endIndex - k] +
                                 bestSum[subarrayCount - 1][endIndex - k];

                // Check if the current configuration gives a better sum
                if (currentSum > bestSum[subarrayCount][endIndex - 1]) {
                    bestSum[subarrayCount][endIndex] = currentSum;
                    bestIndex[subarrayCount][endIndex] = endIndex - k;
                } else {
                    bestSum[subarrayCount][endIndex] =
                        bestSum[subarrayCount][endIndex - 1];
                    bestIndex[subarrayCount][endIndex] =
                        bestIndex[subarrayCount][endIndex - 1];
                }
            }
        }

        // Trace back the indices of the three subarrays
        vector<int> result(3, 0);
        int currentEnd = n;
        for (int subarrayIndex = 3; subarrayIndex >= 1; subarrayIndex--) {
            result[subarrayIndex - 1] = bestIndex[subarrayIndex][currentEnd];
            currentEnd = result[subarrayIndex - 1];
        }

        return result;
    }
};
```

**Solution 3: (Sliding Window)**
```
Runtime: 0 ms
Memory: 23.83 MB
```
```c++
class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        // Variables to track the best indices for one, two, and three subarray
        // configurations
        int bestSingleStart = 0;
        vector<int> bestDoubleStart = {0, k};
        vector<int> bestTripleStart = {0, k, k * 2};

        // Compute the initial sums for the first three subarrays
        int currentWindowSumSingle = 0;
        for (int i = 0; i < k; i++) {
            currentWindowSumSingle += nums[i];
        }

        int currentWindowSumDouble = 0;
        for (int i = k; i < k * 2; i++) {
            currentWindowSumDouble += nums[i];
        }

        int currentWindowSumTriple = 0;
        for (int i = k * 2; i < k * 3; i++) {
            currentWindowSumTriple += nums[i];
        }

        // Track the best sums found so far
        int bestSingleSum = currentWindowSumSingle;
        int bestDoubleSum = currentWindowSumSingle + currentWindowSumDouble;
        int bestTripleSum = currentWindowSumSingle + currentWindowSumDouble +
                            currentWindowSumTriple;

        // Sliding window pointers for the subarrays
        int singleStartIndex = 1;
        int doubleStartIndex = k + 1;
        int tripleStartIndex = k * 2 + 1;

        // Slide the windows across the array
        while (tripleStartIndex <= nums.size() - k) {
            // Update the sums using the sliding window technique
            currentWindowSumSingle = currentWindowSumSingle -
                                     nums[singleStartIndex - 1] +
                                     nums[singleStartIndex + k - 1];
            currentWindowSumDouble = currentWindowSumDouble -
                                     nums[doubleStartIndex - 1] +
                                     nums[doubleStartIndex + k - 1];
            currentWindowSumTriple = currentWindowSumTriple -
                                     nums[tripleStartIndex - 1] +
                                     nums[tripleStartIndex + k - 1];

            // Update the best single subarray start index if a better sum is
            // found
            if (currentWindowSumSingle > bestSingleSum) {
                bestSingleStart = singleStartIndex;
                bestSingleSum = currentWindowSumSingle;
            }

            // Update the best double subarray start indices if a better sum is
            // found
            if (currentWindowSumDouble + bestSingleSum > bestDoubleSum) {
                bestDoubleStart[0] = bestSingleStart;
                bestDoubleStart[1] = doubleStartIndex;
                bestDoubleSum = currentWindowSumDouble + bestSingleSum;
            }

            // Update the best triple subarray start indices if a better sum is
            // found
            if (currentWindowSumTriple + bestDoubleSum > bestTripleSum) {
                bestTripleStart[0] = bestDoubleStart[0];
                bestTripleStart[1] = bestDoubleStart[1];
                bestTripleStart[2] = tripleStartIndex;
                bestTripleSum = currentWindowSumTriple + bestDoubleSum;
            }

            // Move the sliding windows forward
            singleStartIndex += 1;
            doubleStartIndex += 1;
            tripleStartIndex += 1;
        }

        // Return the starting indices of the three subarrays with the maximum
        // sum
        return bestTripleStart;
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 4 ms, Beats 55.81%
Memory: 31.38 MB, Beats 34.29%
```
```c++
class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();

        vector<int> pre(n + 1);
        for (int i = 0; i < n; i ++) {
            pre[i + 1] = pre[i] + nums[i];
        }

        vector<vector<int>> dp(4, vector<int>(n + 1)), dpi(4, vector<int>(n + 1));

        for (int ck = 1; ck <= 3; ck ++) {
            for (int i = k * ck; i <= n; i ++) {
                int cur = pre[i] - pre[i - k] + dp[ck - 1][i - k];

                if (cur > dp[ck][i - 1]) {
                    dp[ck][i] = cur;
                    dpi[ck][i] = i - k;
                } else {
                    dp[ck][i] = dp[ck][i - 1];
                    dpi[ck][i] = dpi[ck][i - 1];
                }
            }
        }

        vector<int> ans(3);
        int i = n;
        for (int ck = 3; ck >= 1; ck --) {
            ans[ck - 1] = dpi[ck][i];
            i = ans[ck - 1];
        }

        return ans;
    }
};
```

**Solution 5: (Two Pointers, left right)**

       0  1  2              7
       1, 2, 1, 2, 6, 7, 5, 1
       ^^^^     ^^^^  ^^^^
dp     3  3  3  8 13 12  6  1
                ^  ^
right  4  4  4  4  4  5  6  7
                      ^  ^
left   0  0  0  4  5  5  5  5
          ^  ^


```
Runtime: 8 ms
Memory: 26.33 MB
```
```c++
class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size(), i, j = n-1, cur = 0, mx = INT_MIN;
        vector<int> dp(n), left(n), right(n), ans;
        right[n-1] = n-1;
        for (i = n-1; i >= 0; i --) {
            cur += nums[i];
            if (i < n-k) {
                cur -= nums[j];
                j -= 1;
            }
            dp[i] = cur;
            if (i < n-1) {
                if (dp[i] >= dp[right[i+1]]) {
                    right[i] = i;
                } else {
                    right[i] = right[i+1];
                }
            }
        }
        for (i = 0; i <= n-2*k; i ++) {
            if (i >= k) {
                cur = dp[i] + dp[left[i-k]] + dp[right[i+k]];
                if (cur > mx) {
                    mx = cur;
                    ans = {left[i-k], i, right[i+k]};
                }
            }
            if (i) {
                if (dp[i] > dp[left[i-1]]) {
                    left[i] = i;
                } else {
                    left[i] = left[i-1];
                }
            }
        }
        return ans;
    }
};
```
