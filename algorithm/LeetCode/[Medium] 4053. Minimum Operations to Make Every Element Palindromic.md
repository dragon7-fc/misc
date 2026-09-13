4053. Minimum Operations to Make Every Element Palindromic

You are given an integer array `nums`.

In one operation, you may choose an index `i` and either increment or decrement `nums[i]` by 2.

Return the **minimum** number of operations required to make every element in `nums` a **positive palindrome**. Different elements may be changed into different palindromic integers.

 

**Example 1:**
```
Input: nums = [10,12,14,16]

Output: 9

Explanation:

One optimal sequence of operations is:

Decrement nums[0] by 2 once to change it from 10 to 8.
Decrement nums[1] by 2 twice to change it from 12 to 8.
Decrement nums[2] by 2 three times to change it from 14 to 8.
Increment nums[3] by 2 three times to change it from 16 to 22.
After 1 + 2 + 3 + 3 = 9 operations, nums = [8, 8, 8, 22], and every element is a positive palindromic integer.

It can be shown that fewer than 9 operations cannot achieve this.
```

**Example 2:**
```
Input: nums = [9,10,11,10]

Output: 2

Explanation:

Decrement nums[1] and nums[3] by 2 once each.

After 2 operations, nums = [9, 8, 11, 8], and every element is a positive palindromic integer.

At least one operation is needed for each of these two elements, so the minimum number of operations is 2.
```

**Example 3:**
```
Input: nums = [125]

Output: 2

Explanation:

Decrement nums[0] by 2 twice to change it from 125 to 121, which is a positive palindromic integer.

A single operation would change it to 123 or 127, neither of which is palindromic. Thus, the minimum number of operations is 2.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum, Binary Search)**

__Intuition__
Because the allowed operation adds or subtracts 2,
the parity of each number in the array can never change.

Therefore,
a number can only be transformed into a palindrome
that shares its same even/odd parity.

Precomputes all palindromic numbers
and groups them by their parity (even or odd).

__Explanation__
During initialization,
we construct palindromes of both odd and even lengths
using string reflection.
We convert them to integers and place them in two separate
sorted arrays based on their least significant bit.

For each number in the input array,
we use binary search to find its closest parity-matching palindrome.
We check the closest palindromes on both sides of the number
and calculate the minimum absolute difference.

Dividing this optimal difference by 2
gives the minimum operations required for that element.
We sum these up for the total cost.

__Complexity__
For precomputes
Time O(mlogm)
Space O(m), where m = 100000

For minOperations
Time O(nlogm)
Space O(1)

```
Runtime: 76 ms, Beats 77.73%
Memory: 138.56 MB, Beats 77.15%
```
```c++
vector<long long> P[2];

int init = []() {
    long long M = 1e9;
    for (int v = 1; v < 100000; ++v) {
        string s = to_string(v);
        string r = s;
        reverse(r.begin(), r.end());
        long long a1 = stoll(s.substr(0, s.size() - 1) + r);
        long long a2 = stoll(s + r);
        if (a1 < M) P[a1 & 1].push_back(a1);
        if (a2 < M) P[a2 & 1].push_back(a2);
    }
    sort(P[0].begin(), P[0].end());
    sort(P[1].begin(), P[1].end());
    return 0;
}();

class Solution {
public:
    long long minOperations(vector<int>& nums) {
        long long res = 0;
        for (int a : nums) {
            auto& p = P[a & 1];
            int i = lower_bound(p.begin(), p.end(), a) - p.begin();
            if (i >= p.size()) i = p.size() - 1;
            long long d1 = abs(a - p[i]);
            long long d2 = i > 0 ? abs(a - p[i - 1]) : d1;
            res += min(d1, d2) / 2;
        }
        return res;
    }
};
```
