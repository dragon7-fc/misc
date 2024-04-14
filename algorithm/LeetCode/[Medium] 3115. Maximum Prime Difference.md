3115. Maximum Prime Difference

You are given an integer array `nums`.

Return an integer that is the **maximum** distance between the **indices** of two (not necessarily different) prime numbers in `nums`.

 

**Example 1:**
```
Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.
```

**Example 2:**
```
Input: nums = [4,8,2,8]

Output: 0

Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.
```
 

**Constraints:**

* `1 <= nums.length <= 3 * 10^5`
* `1 <= nums[i] <= 100`
* The input is generated such that the number of prime numbers in the `nums` is at least one.

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 93 ms
Memory: 106.93 MB
```
```c++
class Solution {
public:
    int maximumPrimeDifference(vector<int>& nums) {
        int left = -1, right = -1;
        bool is_prime;
        for (int i = 0; i < nums.size(); i ++) {
            is_prime = true;
            for (int j = 2; j <= (nums[i]+1)/2; j ++) {
                if (nums[i]%j == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (nums[i] > 1 && is_prime) {
                if (left == -1) {
                    left = i;
                }
                right = i;
            }
        }
        return right - left;
    }
};
```
