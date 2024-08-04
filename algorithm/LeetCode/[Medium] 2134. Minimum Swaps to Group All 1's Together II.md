2134. Minimum Swaps to Group All 1's Together II

A **swap** is defined as taking two distinct positions in an array and swapping the values in them.

A **circular** array is defined as an array where we consider the **first** element and the **last** element to be **adjacent**.

Given a binary circular array `nums`, return the minimum number of swaps required to group all `1`'s present in the array together at **any location**.

 

**Example 1:**
```
Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
```

**Example 2:**
```
Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
```

**Example 3:**
```
Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `nums[i] is either `0` or `1`.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 1422 ms
Memory: 17.8 MB
```
```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        ones = nums.count(1)
        ans = cur = nums[:ones].count(0)
        for i in range(ones, N + ones):
            cur += nums[i % N] == 0
            cur -= nums[(i-ones) % N] == 0
            ans = min(ans, cur)
        return ans
```

**Solution 2: (Using Suffix Sum)**
```
Runtime: 72 ms
Memory: 90.06 MB
```
```c++
class Solution {
     int minSwapsHelper(const vector<int>& data, int val) {
        int length = data.size();
        vector<int> rightSuffixSum(length + 1, 0);

        // Construct the suffix sum array for counting opposite values
        // (val ^ 1)
        for (int i = length - 1; i >= 0; i--) {
            rightSuffixSum[i] = rightSuffixSum[i + 1];
            if (data[i] == (val ^ 1)) rightSuffixSum[i]++;
        }

        // Total zeros in the array if `val` is 1 (or vice versa)
        int totalSwapsNeeded = rightSuffixSum[0];
        // Track current number of required swaps in the current segment
        int currentSwapCount = 0;
        int minimumSwaps =
            totalSwapsNeeded - rightSuffixSum[length - totalSwapsNeeded];

        // Iterate to find the minimum swaps by sliding the potential block of
        // grouped `val`
        for (int i = 0; i < totalSwapsNeeded; i++) {
            if (data[i] == (val ^ 1)) currentSwapCount++;
            int remaining = (totalSwapsNeeded - i - 1);
            int requiredSwaps =
                ((i + 1) - currentSwapCount) +
                (remaining - rightSuffixSum[length - remaining]);
            minimumSwaps = min(minimumSwaps, requiredSwaps);
        }
        return minimumSwaps;
    }
public:
    int minSwaps(vector<int>& nums) {
        int op1 = minSwapsHelper(nums, 0);  // Grouping all 0s together
        int op2 = minSwapsHelper(nums, 1);  // Grouping all 1s together
        return min(op1, op2);
    }
};
```

**Solution 3: (Using Sliding Window)**
```
Runtime: 66 ms
Memory: 83.12 MB
```
```c++
class Solution {
    // Helper function to calculate the minimum swaps required to group all
    // `val` together
    int minSwapsHelper(vector<int>& data, int val) {
        int length = data.size();
        int totalValCount = 0;

        // Count the total number of `val` in the array
        for (int i = length - 1; i >= 0; i--) {
            if (data[i] == val) totalValCount++;
        }

        // If there is no `val` or the array is full of `val`, no swaps are
        // needed
        if (totalValCount == 0 || totalValCount == length) return 0;

        int start = 0, end = 0;
        int maxValInWindow = 0, currentValInWindow = 0;

        // Initial window setup: count the number of `val` in the first window
        // of size `totalValCount`
        while (end < totalValCount) {
            if (data[end++] == val) currentValInWindow++;
        }
        maxValInWindow = max(maxValInWindow, currentValInWindow);

        // Slide the window across the array to find the maximum number of
        // `val` in any window
        while (end < length) {
            if (data[start++] == val) currentValInWindow--;
            if (data[end++] == val) currentValInWindow++;
            maxValInWindow = max(maxValInWindow, currentValInWindow);
        }

        // Minimum swaps are the total `val` minus the maximum found in any
        // window
        return totalValCount - maxValInWindow;
    }
public:
    int minSwaps(vector<int>& nums) {
        // Calculate the minimum swaps needed to group all 1s or all 0s
        // together
        int op1 = minSwapsHelper(nums, 0);  // Grouping all 0s together
        int op2 = minSwapsHelper(nums, 1);  // Grouping all 1s together
        return min(op1, op2);
    }
};
```

**Solution 4: (Cleaner and More Intuitive Sliding Window)**
```
Runtime: 75 ms
Memory: 83.06 MB
```
```c++
class Solution {
public:
    int minSwaps(vector<int>& nums) {
         // Initialize minimum swaps to a large value
        int minimumSwaps = INT_MAX;

        // Calculate the total number of 1s in the array
        int totalOnes = accumulate(nums.begin(), nums.end(), 0);

        // Initialize the count of 1s in the current window
        int onesCount = nums[0];
        int end = 0;

        // Slide the window across the array
        for (int start = 0; start < nums.size(); ++start) {
            // Adjust onesCount by removing the element that is sliding out of
            // the window
            if (start != 0) {
                onesCount -= nums[start - 1];
            }

            // Expand the window to the right until it reaches the desired size
            while (end - start + 1 < totalOnes) {
                end++;
                onesCount += nums[end % nums.size()];
            }

            // Update the minimum number of swaps needed
            minimumSwaps = min(minimumSwaps, totalOnes - onesCount);
        }

        return minimumSwaps;
    }
};
```

**Solution 5: (Sliding Window)**
```
Runtime: 71 ms
Memory: 83.08 MB
```
```c++
class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size(), cnt = 0, cur = 0, ans;
        for (int i = 0; i < n; i ++) {
            cnt += nums[i] == 1 ? 1 : 0;
        }
        ans = cnt;
        for (int i = 0; i < 2*n; i ++) {
            cur += nums[i%n] == 0 ? 1 : 0;
            if (i >= cnt) {
                cur -= nums[(i+n-cnt)%n] == 0 ? 1 : 0;
                ans = min(ans, cur);
            }
        }
        return ans;
    }
};
```
