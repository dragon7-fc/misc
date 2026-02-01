1296. Divide Array in Sets of K Consecutive Numbers

Given an array of integers `nums` and a positive integer `k`, find whether it's possible to divide this array into sets of `k` consecutive numbers
Return `True` if its possible otherwise return `False`.

 

**Example 1:**
```
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
```

**Example 2:**
```
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
```

**Example 3:**
```
Input: nums = [3,3,2,2,1,1], k = 3
Output: true
```

**Example 4:**
```
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= nums.length`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 444 ms
Memory Usage: 27.4 MB
```
```python
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        keys = sorted(count.keys())
        for n in keys:
            if count[n] > 0:
                minus = count[n]
                for i in range(n,n+k):
                    if count[i] < minus:
                        return False
                    count[i] -= minus
        return True
```

**Solution 2: (Greedy, Counter)**
```
Runtime: 168 ms, Beats 16.60%
Memory: 72.86 MB, Beats 32.15%
```
```c++
class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        map<int, int> cnt;
        for (auto &num: nums) {
            cnt[num] += 1;
        }
        for (auto &[a, ck]: cnt) {
            if (ck) {
                for (int i = k - 1; i >= 0; i --) {
                    if (cnt[a + i] < ck) {
                        return false;
                    }
                    cnt[a + i] -= ck;
                }
            }
        }
        return true;
    }
};
```
