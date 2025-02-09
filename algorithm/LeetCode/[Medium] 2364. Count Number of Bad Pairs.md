2364. Count Number of Bad Pairs

You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a bad pair if `i < j` and `j - i != nums[j] - nums[i]`.

Return the total number of **bad pairs** in `nums`.

 

**Example 1:**
```
Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
```

**Example 2:**
```
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Hash Table)**

* Find difference of nums[i] and i
* Use a hashmap to store count of elements that have nums[i] - i difference
* Elements which have the same difference(nums[i] - i) will be good pairs. Elements which have different differences will form bad pairs

```
Runtime: 779 ms
Memory Usage: 33.5 MB
```
```python
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        m, ans = defaultdict(int), 0
        for i in range(len(nums)):
            ans += i - m[nums[i] - i]
            m[nums[i] - i] += 1
        return ans
```

**Solution 2: (Hash Table)**

    j - i != nums[j] - nums[i]
    -> j - nums[j] != i - nums[i]
    4, 1, 3, 3
             ^
ans 0  1  3  5
cnt
    -3: 1
    0: 1
    -1: 1

    i - cnt[i-nums[i]]

```
Runtime: 69 ms, Beats 56.08%
Memory: 87.56 MB, Beats 81.46%
```
```c++
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n = nums.size(), i;
        long long ans = 0;
        unordered_map<int, int> cnt;
        for (i = 0; i < n; i ++) {
            ans += i - cnt[i - nums[i]];
            cnt[i - nums[i]] += 1;
        }
        return ans;
    }
};
```
