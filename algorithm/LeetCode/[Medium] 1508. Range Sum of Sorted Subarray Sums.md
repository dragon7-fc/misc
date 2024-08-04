1508. Range Sum of Sorted Subarray Sums

Given the array `nums` consisting of `n` positive integers. You computed the sum of all non-empty continous subarrays from the array and then sort them in non-decreasing order, creating a new array of `n * (n + 1) / 2` numbers.

Return the sum of the numbers from index `left` to index `right` (indexed from `1`), inclusive, in the new array. Since the answer can be a huge number return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 
```

**Example 2:**
```
Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
```

**Example 3:**
```
Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50
```

**Constraints:**

* `1 <= nums.length <= 10^3`
* `nums.length == n`
* `1 <= nums[i] <= 100`
* `1 <= left <= right <= n * (n + 1) / 2`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 388 ms
Memory Usage: 35.4 MB
```
```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(len(nums)):
            prefix = 0
            for ii in range(i, len(nums)):
                prefix += nums[ii]
                ans.append(prefix)
        ans.sort()
        return sum(ans[left-1:right]) % 1_000_000_007
```

**Solution 2: (Heap)**
```
Runtime: 32 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = [(x, i) for i, x in enumerate(nums)] #min-heap 
        heapify(h)
        
        ans = 0
        for k in range(1, right+1): #1-indexed
            x, i = heappop(h)
            if k >= left: ans += x
            if i+1 < len(nums): 
                heappush(h, (x + nums[i+1], i+1))
                
        return ans % 1_000_000_007
```

**Solution 3: (Heap, O(n^2 log n))**
```
Runtime: 12 ms
Memory Usage: 7.9 MB
```
```c++
class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> mqueue;
        for (int i=0; i<n; i++)
            mqueue.push({nums[i], i+1});

        int ans = 0, mod = 1e9+7;
        for (int i=1; i<=right; i++) {
            auto p = mqueue.top();
            mqueue.pop();
            if (i >= left)
                ans = (ans + p.first) % mod;
            if (p.second < n) {
                p.first += nums[p.second++];
                mqueue.push(p);
            }
        }
        return ans;
    }
};
```

**Solution 4: (Binary Search and Sliding Window, O(n log sum))**
```
Runtime: 5 ms
Memory: 10.07 MB
```
```c++
class Solution {
    int mod = 1e9 + 7;
    // Helper function to count subarrays with sum <= target and their total
    // sum.
    pair<int, long long> countAndSum(vector<int>& nums, int n, int target) {
        int count = 0;
        long long currentSum = 0, totalSum = 0, windowSum = 0;
        for (int j = 0, i = 0; j < n; ++j) {
            currentSum += nums[j];
            windowSum += nums[j] * (j - i + 1);
            while (currentSum > target) {
                windowSum -= currentSum;
                currentSum -= nums[i++];
            }
            count += j - i + 1;
            totalSum += windowSum;
        }
        return {count, totalSum};
    }

    // Helper function to find the sum of the first k smallest subarray sums.
    long long sumOfFirstK(vector<int>& nums, int n, int k) {
        int minSum = *min_element(nums.begin(), nums.end());
        int maxSum = accumulate(nums.begin(), nums.end(), 0);
        int left = minSum, right = maxSum;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (countAndSum(nums, n, mid).first >= k)
                right = mid - 1;
            else
                left = mid + 1;
        }
        auto [count, sum] = countAndSum(nums, n, left);
        // There can be more subarrays with the same sum of left.
        return sum - left * (count - k);
    }
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        long result =
            (sumOfFirstK(nums, n, right) - sumOfFirstK(nums, n, left - 1)) %
            mod;
        // Ensure non-negative result
        return (result + mod) % mod;
    }
};
```
