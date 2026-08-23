4032. Longest Subarray With at Most K Distinct Prime Factors

You are given an integer array `nums` consisting of positive integers and an integer `k`.

The **prime factor set** of a **subarray** is the union of the distinct prime factors of all its elements.

Return the length of the **longest** subarray whose prime factor set contains at most `k` distinct prime factors. If no such subarray exists, return 0.

 

**Example 1:**
```
Input: nums = [7,6,10,12,11], k = 3

Output: 3

Explanation:

Consider the subarray [6, 10, 12]:

The distinct prime factors of 6 are {2, 3}.
The distinct prime factors of 10 are {2, 5}.
The distinct prime factors of 12 are {2, 3}.
The union of these sets is {2, 3, 5}, which contains 3 distinct prime factors.
No longer subarray satisfies the condition. Therefore, the answer is 3.
```

**Example 2:**
```
Input: nums = [4,6,9,18], k = 4

Output: 4

Explanation:

Consider the entire array [4, 6, 9, 18]:

The distinct prime factors of 4 are {2}.
The distinct prime factors of 6 are {2, 3}.
The distinct prime factors of 9 are {3}.
The distinct prime factors of 18 are {2, 3}.
The union of these sets is {2, 3}, which contains 2 distinct prime factors.
Since 2 <= 4, the entire array is valid. Therefore, the answer is 4.
```

**Example 3:**
```
Input: nums = [6,10,15], k = 2

Output: 1

Explanation:

Every subarray of length at least 2 has prime factor set {2, 3, 5}, which contains 3 distinct prime factors.

Since 3 > 2, only subarrays of length 1 are valid. Therefore, the answer is 1.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `2 <= nums[i] <= 10^5`
* `1 <= k <= 10^4`

# Submissions
---
**Solution 1: (Sliding Window, Math, sieve)**

Intuition
We precompute the prime factors for all numbers
up to the maximum possible value in the array.
This is done using a sieve-like approach once.

Explanation
We iterate through the array and
add the prime factors of each element to a frequency map.

If our map has more than k distinct prime factors,
we slide the left pointer of our window forward.
We remove the prime factors of the left element from the map,
deleting keys when their count hits 0.

Notice we don't shrink the window in a while loop.
The window size either grows or stays the same.

At the end, the length of the array minus the
left pointer gives the maximum window size seen.

Complexity
Time O(nlogM)
Space O(k)

```
Runtime: 281 ms, Beats 93.99%
Memory: 175.05 MB, Beats 89.33%
```
```c++
const int MX = 100001;
vector<vector<int>> factors(MX + 1);

// O(mlog(log(m)))
int init = []() {
    // Code here runs at global initialization time
    for (int i = 2; i <= MX; ++i) {
        if (factors[i].empty()) {
            factors[i].push_back(i);
            for (int j = i * 2; j <= MX; j += i) {
                factors[j].push_back(i);
            }
        }
    }
    return 0;
}();  // Immediatly Invoked Lambda Expression (IIFE)

class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int i = 0;
        unordered_map<int, int> cnt;
        for (const auto &num: nums) {
            for (const auto &f: factors[num]) {
                cnt[f] += 1;
            }
            if (cnt.size() > k) {
                for (const auto &f: factors[nums[i]]) {
                    cnt[f] -= 1;
                    if (cnt[f] == 0) {
                        cnt.erase(f);
                    }
                }
                i += 1;
            }
        }
        return nums.size() - i;
    }
};
```

