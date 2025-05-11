2918. Minimum Equal Sum of Two Arrays After Replacing Zeros

You are given two arrays `nums1` and `nums2` consisting of positive integers.

You have to replace all the `0`'s in both arrays with strictly positive integers such that the sum of elements of both arrays becomes **equal**.

Return the **minimum** equal sum you can obtain, or `-1` if it is impossible.

 

**Example 1:**
```
Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
Output: 12
Explanation: We can replace 0's in the following way:
- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.
```

**Example 2:**
```
Input: nums1 = [2,0,2,0], nums2 = [1,4]
Output: -1
Explanation: It is impossible to make the sum of both arrays equal.
```

**Constraints:**

* `1 <= nums1.length, nums2.length <= 10^5`
* `0 <= nums1[i], nums2[i] <= 10^6`

# Submissions
---
**Solution 1: (Greedy, case study)**
```
Runtime: 139 ms
Memory: 130.8 MB
```
```c++
class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long sa = 0, sb = 0, a0 = 0, b0 = 0;
        for (int a: nums1) {
            a0 += a == 0;
            sa += max(a, 1);
        }
        for (int b: nums2) {
            b0 += b == 0;
            sb += max(b, 1);
        }
        if (sa < sb && a0 == 0) return -1;
        if (sa > sb && b0 == 0) return -1;
        return max(sa, sb);
    }
};
```

**Solution 2: (Classified Discussion)**
```
Runtime: 131 ms, Beats 57.97%
Memory: 135.53 MB, Beats 15.59%
```
```c++
class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long sum1 = 0, sum2 = 0;
        long long zero1 = 0, zero2 = 0;
        for (int i : nums1) {
            sum1 += i;
            if (i == 0) {
                sum1++;
                zero1++;
            }
        }
        for (int i : nums2) {
            sum2 += i;
            if (i == 0) {
                sum2++;
                zero2++;
            }
        }
        if (!zero1 && sum2 > sum1 || !zero2 && sum1 > sum2) {
            return -1;
        }
        return max(sum1, sum2);
    }
};
```

**Solution 3: (Math)**
```
Runtime: 125 ms, Beats 78.30%
Memory: 135.20 MB, Beats 99.32%
```
```c++
class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size(), i, zm = 0, zn = 0;
        long long a = 0, b = 0;
        for (i = 0; i < m; i ++) {
            a += nums1[i];
            zm += nums1[i] == 0;
        }
        for (i = 0; i < n; i ++) {
            b += nums2[i];
            zn += nums2[i] == 0;
        }
        if (a + zm < b + zn) {
            swap(a, b);
            swap(zm, zn);
        }
        if (a + zm != b + zn && zn == 0) {
            return -1;
        } 
        return a + zm;
    }
};
```
