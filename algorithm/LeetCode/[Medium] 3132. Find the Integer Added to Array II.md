3132. Find the Integer Added to Array II

You are given two integer arrays `nums1` and `nums2`.

From nums1 two elements have been removed, and all other elements have been increased (or decreased in the case of negative) by an integer, represented by the variable `x`.

As a result, `nums1` becomes equal to `nums2`. Two arrays are considered **equal** when they contain the same integers with the same frequencies.

Return the **minimum** possible integer `x` that achieves this equivalence.

 

**Example 1:**
```
Input: nums1 = [4,20,16,12,8], nums2 = [14,18,10]

Output: -2

Explanation:

After removing elements at indices [0,4] and adding -2, nums1 becomes [18,14,10].
```

**Example 2:**
```
Input: nums1 = [3,5,5,3], nums2 = [7,7]

Output: 2

Explanation:

After removing elements at indices [0,3] and adding 2, nums1 becomes [7,7].
```
 

**Constraints:**

* `3 <= nums1.length <= 200`
* `nums2.length == nums1.length - 2`
* `0 <= nums1[i], nums2[i] <= 1000`
* The test cases are generated in a way that there is an integer `x` such that `nums1` can become equal to `nums2` by removing two elements and adding `x` to each element of `nums1`.

# Submissions
---
**Solution 1: (logics)**

Intuition: the value is either:

n2[0] - n1[0], or
n2[0] - n1[1] if we remove the first element, or
n2[0] - n1[2] if we remove first two elements.
For each potential value, we match the rest of the array.

If there is a mismatch, we skip that element, incrementing skip.

If we match the entire array and skip < 3, we consider that value and track the minimum one.

```
Runtime: 6 ms
Memory: 32.27 MB
```
```c++
class Solution {
public:
    int minimumAddedInteger(vector<int>& nums1, vector<int>& nums2) {
        sort(begin(nums1), end(nums1));
        sort(begin(nums2), end(nums2));
        int res = INT_MAX;
        for (int i = 0; i < 3; ++i) {
            int skip = i;
            for (int j = i + 1; skip < 3 && j - skip < nums2.size(); ++j)
                skip += nums2[j - skip] - nums1[j] != nums2[0] - nums1[i];
            if (skip < 3)
                res = min(res, nums2[0] - nums1[i]);
        }
        return res;
    }
};
```
