410. Split Array Largest Sum

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

**Note:**

If n is the length of array, assume the following constraints are satisfied:
* 1 ≤ n ≤ 1000
* 1 ≤ m ≤ min(50, n)

**Examples:**
```
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

# Submissions
---
**Solution: (Top-Down Dynamic Programming)**

* Time complexity: $O(N^2 \cdot M)$
* Space complexity: $O(N \cdot M)$

```
Runtime: 64 ms
Memory Usage: 7.6 MB
```
```c++
class Solution {
    // Defined it as per the maximum size of array and split count
    // But can be defined with the input size as well
    int memo[1001][51];
public:
    int splitArray(vector<int>& nums, int m) {
        // Marking all values to -1 so that we can differentiate 
        // If we have already calculated the answer or not
        memset(memo, -1, sizeof(memo));
        
        // Store the prefix sum of nums array.
        int n = nums.size();
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        return getMinimumLargestSplitSum(prefixSum, 0, m);
    }
    
    int getMinimumLargestSplitSum(vector<int>& prefixSum, int currIndex, int subarrayCount) {
        int n = prefixSum.size() - 1;
        
        // We have already calculated the answer so no need to go into recursion
        if (memo[currIndex][subarrayCount] != -1) {
            return memo[currIndex][subarrayCount];
        }
        
        // Base Case: If there is only one subarray left, then all of the remaining numbers
        // must go in the current subarray. So return the sum of the remaining numbers.
        if (subarrayCount == 1) {
            return memo[currIndex][subarrayCount] = prefixSum[n] - prefixSum[currIndex];
        }
        
        // Otherwise, use the recurrence relation to determine the minimum largest subarray
        // sum between currIndex and the end of the array with subarrayCount subarrays remaining.
        int minimumLargestSplitSum = INT_MAX;
        for (int i = currIndex; i <= n - subarrayCount; i++) {
            // Store the sum of the first subarray.
            int firstSplitSum = prefixSum[i + 1] - prefixSum[currIndex];
            
            // Find the maximum subarray sum for the current first split.
            int largestSplitSum = max(firstSplitSum, 
                                      getMinimumLargestSplitSum(prefixSum, i + 1, subarrayCount - 1));
            
            // Find the minimum among all possible combinations.
            minimumLargestSplitSum = min(minimumLargestSplitSum, largestSplitSum);
             
            if (firstSplitSum >= minimumLargestSplitSum) {
                break;
            }
        }
        
        return memo[currIndex][subarrayCount] = minimumLargestSplitSum;
    }
};
```

**Solution: (Bottom-Up Dynamic Programming)**

* Time complexity: $O(N^2 \cdot M)$
* Space complexity: $O(N \cdot M)$

```
Runtime: 76 ms
Memory Usage: 7.5 MB
```
```c++
class Solution {
    // Defined it as per the maximum size of array and split count
    // But can be defined with the input size as well
    int memo[1001][51];
public:
    int splitArray(vector<int>& nums, int m) {
        int n = nums.size();
        
        // Store the prefix sum of nums array
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        for (int subarrayCount = 1; subarrayCount <= m; subarrayCount++) {
            for (int currIndex = 0; currIndex < n; currIndex++) {
               // Base Case: If there is only one subarray left, then all of the remaining numbers
               // must go in the current subarray. So return the sum of the remaining numbers.
                if (subarrayCount == 1) {
                    memo[currIndex][subarrayCount] = prefixSum[n] - prefixSum[currIndex];
                    continue;
                }

                // Otherwise, use the recurrence relation to determine the minimum largest subarray
                // sum between currIndex and the end of the array with subarrayCount subarray remaining.
                int minimumLargestSplitSum = INT_MAX;
                for (int i = currIndex; i <= n - subarrayCount; i++) {
                    // Store the sum of the first subarray.
                    int firstSplitSum = prefixSum[i + 1] - prefixSum[currIndex];

                    // Find the maximum subarray sum for the current first split.
                    int largestSplitSum = max(firstSplitSum, memo[i + 1][subarrayCount - 1]);

                    // Find the minimum among all possible combinations.
                    minimumLargestSplitSum = min(minimumLargestSplitSum, largestSplitSum);

                    if (firstSplitSum >= minimumLargestSplitSum) {
                        break;
                    }
                }

                memo[currIndex][subarrayCount] = minimumLargestSplitSum;
            }
        }
        
        return memo[0][m];
    }
};
```

**Solution: (Binary Search)**

* Time complexity: $O(N \cdot \log(S))$
* Space complexity: $O(1)$

```
Runtime: 6 ms
Memory Usage: 7.2 MB
```
```c++
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        // Find the sum of all elements and the maximum element
        int sum = 0;
        int maxElement = INT_MIN;
        for (int element : nums) {
            sum += element;
            maxElement = max(maxElement, element);
        }
        
        // Define the left and right boundary of binary search
        int left = maxElement;
        int right = sum;
        int minimumLargestSplitSum = 0;
        while (left <= right) {
            // Find the mid value
            int maxSumAllowed = left + (right - left) / 2;
            
            // Find the minimum splits. If splitsRequired is less than
            // or equal to m move towards left i.e., smaller values
            if (minimumSubarraysRequired(nums, maxSumAllowed) <= m) {
                right = maxSumAllowed - 1;
                minimumLargestSplitSum = maxSumAllowed;
            } else {
                // Move towards right if splitsRequired is more than m
                left = maxSumAllowed + 1;
            }
        }
        
        return minimumLargestSplitSum;
    }
    
    int minimumSubarraysRequired(vector<int>& nums, int maxSumAllowed) {
        int currentSum = 0;
        int splitsRequired = 0;
        
        for (int element : nums) {
            // Add element only if the sum doesn't exceed maxSumAllowed
            if (currentSum + element <= maxSumAllowed) {
                currentSum += element;
            } else {
                // If the element addition makes sum more than maxSumAllowed
                // Increment the splits required and reset sum
                currentSum = element;
                splitsRequired++;
            }
        }
        
        // Return the number of subarrays, which is the number of splits + 1
        return splitsRequired + 1;
    }
};
```

**Solution 1: (DP Top-Down)**
```
Runtime: 4920 ms
Memory Usage: 18.1 MB
```
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefixSum = [0]
        for a in nums:
            prefixSum.append(a + prefixSum[-1])

        @lru_cache(None)
        def dp(i, j):
            # i is number of elements from A
            # j is number of splits
            if j == 1: return prefixSum[i]
            res = float('inf')
            for k in range(j - 1, i):
                res = min(res, max(dp(k, j - 1),
                                   prefixSum[i] - prefixSum[k]))
            return res

        return dp(len(nums), m)
```

**Solution 2: (Binary Search)**
```
Runtime: 44 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        class Lazy:
            def __getitem__(self, sm):
                splits = 1
                cur = 0
                for a in nums:
                    if a > sm: return False
                    if cur + a > sm:
                        splits += 1
                        cur = 0
                    cur += a
                return splits <= m
        return bisect_left(Lazy(), True, 0, int(1e18))
```

**Solution 3: (Binary Search)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c
int getTotalSum(int *nums, int numsSize){
    int count = 0;
    for(int i=0; i<numsSize; i++){
        count += nums[i];
    }
    return count;
}

int getMaxItem(int *nums, int numsSize){
    int count = 0;
    for(int i=0; i<numsSize; i++){
        if(nums[i] > count){
            count = nums[i];
        }
    }
    return count;
}

bool feasible(int *nums, int numsSize, int currentTotal, int numsSplitsLimits){
    size_t total = 0, numsSplits = 1;
    for(int i=0; i<numsSize; i++){
        total += nums[i];
        if(total > currentTotal){
            numsSplits++;
            total = nums[i];
            if(numsSplits > numsSplitsLimits)    return false;
        }
    }
    return true;
}

int splitArray(int* nums, int numsSize, int m){
    int left = getMaxItem(nums,numsSize);
    int right = getTotalSum(nums,numsSize);
    while(left < right){
        int mid = left + (right - left)/2;
        int count = 0, numSplits1=1;
        if(feasible(nums, numsSize, mid, m)){
            right = mid;
        }
        else{
            left = mid+1;
        }
    }
    return left;
}
```

**Solution 4: (Binary Search, lower bound)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 10.36 MB, Beats 87.25%
```
```c++
class Solution {
    bool check(int mid, int k, vector<int> &nums) {
        int ck = 0, a = 0;
        for (auto &num: nums) {
            a += num;
            if (a > mid) {
                ck += 1;
                a = num;
            }
        }
        return ck + (a > 0) <= k;
    }
public:
    int splitArray(vector<int>& nums, int k) {
        int left = *max_element(nums.begin(), nums.end()), right = 1e9, mid, ans = INT_MAX;
        while (left <= right) {
            mid = left + (right - left)/2;
            if (!check(mid, k, nums)) {
                left = mid + 1;
            } else {
                ans = min(ans, mid);
                right = mid - 1;
            }
        }
        return ans;
    }
};

```
