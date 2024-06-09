2936. Number of Equal Numbers Blocks

You are given a **0-indexed** array of integers, `nums`. The following property holds for `nums`:

All occurrences of a value are adjacent. In other words, if there are two indices `i < j` such that `nums[i] == nums[j]`, then for every index `k` that `i < k < j, nums[k] == nums[i]`.

Since `nums` is a very large array, you are given an instance of the class `BigArray` which has the following functions:

`int at(long long index)`: Returns the value of `nums[i]`.
`void size()`: Returns `nums.length`.

Let's partition the array into maximal blocks such that each block contains **equal values**. Return the number of these blocks.

Note that if you want to test your solution using a custom test, behavior for tests with `nums.length > 10` is undefined.

 

**Example 1:**
```
Input: nums = [3,3,3,3,3]
Output: 1
Explanation: There is only one block here which is the whole array (because all numbers are equal) and that is: [3,3,3,3,3]. So the answer would be 1. 
```

**Example 2:**
```
Input: nums = [1,1,1,3,9,9,9,2,10,10]
Output: 5
Explanation: There are 5 blocks here:
Block number 1: [1,1,1,3,9,9,9,2,10,10]
Block number 2: [1,1,1,3,9,9,9,2,10,10]
Block number 3: [1,1,1,3,9,9,9,2,10,10]
Block number 4: [1,1,1,3,9,9,9,2,10,10]
Block number 5: [1,1,1,3,9,9,9,2,10,10]
So the answer would be 5.
```

**Example 3:**
```
Input: nums = [1,2,3,4,5,6,7]
Output: 7
Explanation: Since all numbers are distinct, there are 7 blocks here and each element representing one block. So the answer would be 7. 
```

**Constraints:**

* `1 <= nums.length <= 10^15`
* `1 <= nums[i] <= 10^9`
* The input is generated such that all equal values are adjacent.
* The sum of the elements of `nums` is at most `10^15.`

# Submissions
---
**Solution 1: (Binary Search, upper_bound)**
```
Runtime: 691 ms
Memory: 95.66 MB
```
```c++
/**
 * Definition for BigArray.
 * class BigArray {
 * public:
 *     BigArray(vector<int> elements);
 *     int at(long long index);
 *     long long size();
 * };
 */
class Solution {
public:
    int countBlocks(BigArray* nums) {
        long long n = nums->size(), left, right, mid, i = 0;
        int ans = 0;
        while (i < n) {
            left = i, right = n - 1;
            while (left < right) {
                mid = right - (right-left)/2;
                if (nums->at(mid) != nums->at(i)) {
                    right = mid - 1;
                } else {
                    left = mid;
                }
            }
            i = left + 1;
            ans += 1;
        }
        return ans;
        
    }
};
```

**Solution 2: (Exponential Advance)**
```
Runtime: 321 ms
Memory: 95.44 MB
```
```c++
/**
 * Definition for BigArray.
 * class BigArray {
 * public:
 *     BigArray(vector<int> elements);
 *     int at(long long index);
 *     long long size();
 * };
 */
class Solution {
public:
    int countBlocks(BigArray* nums) {
        long long res = 0, sz = nums->size(), prev = 0;
        for (long long i = 0, j = 0; i < sz; ++i) {
            int val = nums->at(i);
            res += prev != val;
            prev = val;
            for (j = 1; i + j < sz && val == nums->at(i + j); j *= 2)
                i += j;
        }
        return res;
    }
};
```

**Solution 3: (Divide and Conquer)**
```
Runtime: 185 ms
Memory: 95.50 MB
```
```c++
/**
 * Definition for BigArray.
 * class BigArray {
 * public:
 *     BigArray(vector<int> elements);
 *     int at(long long index);
 *     long long size();
 * };
 */
class Solution {
    int search(BigArray* nums, long long l, int lval, long long r, int rval) {
        if (lval == rval)
            return 1;
        if (l + 1 == r)
            return 2;
        long long m = (l + r) / 2, mval = nums->at(m);
        return search(nums, l, lval, m, mval) + search(nums, m, mval, r, rval) - 1;
    }
public:
    int countBlocks(BigArray* nums) {
        return search(nums, 0, nums->at(0), nums->size() - 1, nums->at(nums->size() - 1));
    }
};
```
