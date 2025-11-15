3542. Minimum Operations to Convert All Elements to Zero

You are given an array `nums` of size `n`, consisting of **non-negative** integers. Your task is to apply some (possibly zero) operations on the array so that **all** elements become 0.

In one operation, you can select a **subarray** `[i, j]` (where `0 <= i <= j < n`) and set all occurrences of the **minimum non-negative** integer in that subarray to 0.

Return the **minimum** number of operations required to make all elements in the array 0.

 

**Example 1:**
```
Input: nums = [0,2]

Output: 1

Explanation:

Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
Thus, the minimum number of operations required is 1.
```

**Example 2:**
```
Input: nums = [3,1,2,1]

Output: 3

Explanation:

Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
Thus, the minimum number of operations required is 3.
```

**Example 3:**
```
Input: nums = [1,2,1,2,1,2]

Output: 4

Explanation:

Select subarray [0,5] (which is [1,2,1,2,1,2]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [0,2,0,2,0,2].
Select subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,2,0,2].
Select subarray [3,3] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,2].
Select subarray [5,5] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,0].
Thus, the minimum number of operations required is 4.
```

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `0 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Mono Stack)**
```
Runtime: 63 ms, Beats 57.89%
Memory: 222.24 MB, Beats 73.68%
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ans = 0;
        stack<int> stk;
        stk.push(0);
        for (auto num: nums) {
            while (stk.size() && stk.top() > num) {
                stk.pop();
            }
            if (!stk.size() || stk.top() < num) {
                ans += 1;
                stk.push(num);
            }
        }
        return ans;
    }
};
```

**Solution 2: (Mono Stack)**
```
Runtime: 39 ms, Beats 63.48%
Memory: 222.52 MB, Beats 43.82%
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ans = 0;
        stack<int> stk;
        for (auto &num: nums) {
            while (stk.size() && stk.top() >= num) {
                if (stk.top() > num) {
                    ans += 1;
                }
                stk.pop();
            }
            stk.push(num);
        }
        while (stk.size() && stk.top()) {
            ans += 1;
            stk.pop();
        }
        return ans;
    }
};
```
