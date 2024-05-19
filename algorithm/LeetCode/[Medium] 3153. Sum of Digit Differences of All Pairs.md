3153. Sum of Digit Differences of All Pairs

You are given an array `nums` consisting of positive integers where all integers have the same number of digits.

The **digit difference** between two integers is the count of different digits that are in the same position in the two integers.

Return the sum of the **digit differences** between all pairs of integers in nums.

 

**Example 1:**
```
Input: nums = [13,23,12]

Output: 4

Explanation:
We have the following:
- The digit difference between 13 and 23 is 1.
- The digit difference between 13 and 12 is 1.
- The digit difference between 23 and 12 is 2.
So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.
```

**Example 2:**
```
Input: nums = [10,10,10,10]

Output: 0

Explanation:
All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.
```
 

**Constraints:**

* `2 <= nums.length <= 10^5`
* `1 <= nums[i] < 10^9`
* All integers in `nums` have the same number of digits.

# Submissions
---
**Solution 1: (Counter, count digit)**
```
Runtime: 111 ms
Memory: 102.87 MB
```
```c++
class Solution {
public:
    long long sumDigitDifferences(vector<int>& nums) {
        int n = nums.size(), m = to_string(nums[0]).size(), cnt[10], b = 1, cur;
        long long ans = 0;
        while (m > 0) {
            memset(cnt, 0, sizeof(cnt));
            for (int i = 0; i < n; i ++) {
                cnt[(nums[i]/b)%10] += 1;
            }
            cur = 0;
            for (int i = 0; i < 10; i ++) {
                ans += cnt[i]*cur;
                cur += cnt[i];
            }
            b *= 10;
            m -= 1;
        }
        return ans;
    }
};
```
