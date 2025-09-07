3676. Count Bowl Subarrays

You are given an integer array `nums` with distinct elements.

A subarray `nums[l...r]` of `nums` is called a **bowl** if:

* The subarray has length at least 3. That is, `r - l + 1 >= 3`.
* The **minimum** of its two ends is strictly greater than the **maximum** of all elements in between. That is, `min(nums[l], nums[r]) > max(nums[l + 1], ..., nums[r - 1])`.

Return the number of **bowl** subarrays in `nums`.

 

**Example 1:**
```
Input: nums = [2,5,3,1,4]

Output: 2

Explanation:

The bowl subarrays are [3, 1, 4] and [5, 3, 1, 4].

[3, 1, 4] is a bowl because min(3, 4) = 3 > max(1) = 1.
[5, 3, 1, 4] is a bowl because min(5, 4) = 4 > max(3, 1) = 3.
```

**Example 2:**
```
Input: nums = [5,1,2,3,4]

Output: 3

Explanation:

The bowl subarrays are [5, 1, 2], [5, 1, 2, 3] and [5, 1, 2, 3, 4].
```

**Example 3:**
```
Input: nums = [1000000000,999999999,999999998]

Output: 0

Explanation:

No subarray is a bowl.
```
 

**Constraints:**

* `3 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `nums` consists of distinct elements.

# Submissions
---
**Solution 1: (Mono Stack)**

__Intuition__
Need to find the next bigger element,
a classical mono stack problem.

__Explanation__
It iterates through the array from left to right,
using each element as a potential right endpoint (r) for a bowl.

A stack stores indices of elements in decending order of their values.
When a new element A[r] is processed,
the algorithm pops elements from the stack
that are less than or equal to A[r].
Each popped element's index (l) forms a potential bowl with A[r].
If the length of this potential bowl r - l + 1 >= 3, it's counted.

Finally, the algorithm checks if the new element A[r] forms a bowl
with the new top of the stack.
The current index r is then pushed onto the stack.

__Complexity__
This process efficiently finds all valid "bowl" subarrays
without re-evaluating elements,
as the monotonic stack ensures that
each element is compared and processed correctly only once.

Time O(n)
Space O(n)

```
Runtime: 19 ms, Beats 78.57%
Memory: 127.80 MB, Beats 7.14%
```
```c++
class Solution {
public:
    long long bowlSubarrays(vector<int>& nums) {
        long long res = 0;
        vector<int> s;
        for (int r = 0; r < nums.size(); ++r) {
            int a = nums[r];
            while (!s.empty() && nums[s.back()] <= a) {
                int l = s.back();
                s.pop_back();
                if (r - l + 1 >= 3) {
                    res += 1;
                }
            }
            if (!s.empty() && r - s.back() + 1 >= 3) {
                res += 1;
            }
            s.push_back(r);
        }
        return res;
    }
};
```
