2537. Count the Number of Good Subarrays

Given an integer array `nums` and an integer `k`, return the number of **good** subarrays of `nums`.

A subarray `arr` is **good** if it there are at least `k` pairs of indices `(i, j)` such that `i < j` and `arr[i] == arr[j]`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
```

**Example 2:**
```
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i], k <= 10^9`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 815 ms
Memory: 31.9 MB
```
```python
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cnt = collections.Counter()
        cur = 0
        i = 0
        ans = 0
        for j in range(N):
            cur += cnt[nums[j]]
            cnt[nums[j]] += 1
            while cur >= k:
                ans += N-j
                cur -= cnt[nums[i]]-1
                cnt[nums[i]] -= 1
                i += 1
        return ans
```

**Solution 2: (Sliding Window)**

                    vvvvv
    [3, 1, 4, 3, 2, 2, 4]
                    ^
     ^      
        ^              ^
           ^  ^
                    
     ^        ^
                 ^  ^
           ^           ^
    [                ]
    [                   ]
       [                ]
          [             ]

```
Runtime: 77 ms, Beats 75.12%
Memory: 79.22 MB, Beats 36.26%
```
```c++
class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        int n = nums.size(), i = 0, j, ck = 0, a;
        long long ans = 0;
        unordered_map<int,int> cnt;
        for (j = 0; j < n; j ++) {
            ck += cnt[nums[j]];
            cnt[nums[j]] += 1;
            while (ck >= k) {
                ans += n - j;
                ck -= cnt[nums[i]] - 1;
                cnt[nums[i]] -= 1;
                i += 1;
            }
        }
        return ans;
    }
};
```
