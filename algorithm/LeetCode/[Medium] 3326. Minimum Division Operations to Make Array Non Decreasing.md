3326. Minimum Division Operations to Make Array Non Decreasing

You are given an integer array `nums`.

Any positive divisor of a natural number `x` that is **strictly less** than `x` is called a **proper divisor** of x. For example, 2 is a proper divisor of 4, while 6 is not a proper divisor of 6.

You are allowed to perform an **operation** any number of times on `nums`, where in each operation you select any one element from `nums` and divide it by its **greatest proper divisor**.

Return the **minimum** number of operations required to make the array **non-decreasing**.

If it is **not** possible to make the array non-decreasing using any number of operations, return **-1**.

 

**Example 1:**
```
Input: nums = [25,7]

Output: 1

Explanation:

Using a single operation, 25 gets divided by 5 and nums becomes [5, 7].
```

**Example 2:**
```
Input: nums = [7,7,6]

Output: -1

Example 3:

Input: nums = [1,1,1,1]

Output: 0
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Math)**

The largest perfect divisor of a number will always result in the smallest prime factor of the number. Now the number will not be further divisible because it is prime now.

Maximum one operation can be performed with a single number.

Just iterate over array from backwards.

```
Runtime: 261 ms
Memory: 141.71 MB
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for(int i = n-2; i>=0; i--){
            if(nums[i] > nums[i+1]){
                
                for(int j = 2; j*j <= nums[i]; j++){
                    if(nums[i]%j == 0){
                        nums[i] = j;
                        ans++;
                        break;
                    }
                }

                if(nums[i]>nums[i+1]) return -1;
            }
        }

        return ans;
    }
};
```
