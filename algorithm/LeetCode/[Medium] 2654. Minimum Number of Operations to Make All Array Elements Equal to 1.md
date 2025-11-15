2654. Minimum Number of Operations to Make All Array Elements Equal to 1

You are given a **0-indexed** array `nums` consisiting of positive integers. You can do the following operation on the array any number of times:

* Select an index `i` such that `0 <= i < n - 1` and replace either of `nums[i]` or `nums[i+1]` with their gcd value.

Return the minimum number of operations to make all elements of `nums` equal to `1`. If it is impossible, return `-1`.

The gcd of two integers is the greatest common divisor of the two integers.

 

**Example 1:**
```
Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
```

**Example 2:**
```
Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
```

**Constraints:**

* `2 <= nums.length <= 50`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Math, Greedy, Minimum size subarray with gcd = 1)**
```
Runtime: 3 ms
Memory: 27.7 MB
```
```c++
class Solution {
    int GCD(int a,int b)
    {
        if(b == 0)
            return a;
        return GCD(b,a%b);
    }
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int countone = 0;
        for (int i = 0; i < n; i ++)
        {
            if (nums[i] == 1) {
                countone++;
            }
        }
        if (countone > 0)
             return n-countone;
        int minop = INT_MAX;
        for (int i = 0; i < n-1; i ++)
        {
            int gcdres = nums[i];
            for (int j = i+1; j < n; j ++) {
                gcdres = GCD(nums[j],gcdres);
                if(gcdres == 1)
                {
                    minop = min(minop,j-i+1);
                    break;
                }
            }
        }
        if(minop == INT_MAX) {
            return -1;
        }
        return n+minop-2;
    }
};
```

**Solution 2: (Math, Greedy, Brute Froce, Minimum size subarray with gcd = 1, gcd(0, a) = a)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 31.56 MB, Beats 93.06%
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size(), i, j, k = 0, g = 0;
        for (auto &x : nums) {
            if (x == 1) {
                k += 1;
            }
            g = gcd(g, x);
        }
        if (k > 0) {
            return n - k;
        }
        if (g > 1) {
            return -1;
        }
        int min_len = n;
        for (i = 0; i < n; i++) {
            int g = 0;
            for (j = i; j < n; j++) {
                g = gcd(g, nums[j]);
                if (g == 1) {
                    min_len = min(min_len, j - i + 1);
                    break;
                }
            }
        }
        return min_len + n - 2;
    }
};
```
