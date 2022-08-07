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
```
Runtime: 232 ms
Memory Usage: 83.7 MB
```
```c++
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        long long ans = 0;
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            ans += i - m[nums[i] - i];
            m[nums[i] - i]++;
        }
        return ans;
    }
};
```
