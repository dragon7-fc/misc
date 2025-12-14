2448. Minimum Cost to Make Array Equal

You are given two **0-indexed** array `nums` and `cost` consisting each of `n` **positive** integers.

You can do the following operation **any** number of times:

* Increase or decrease **any** element of the array `nums` by `1`.
The cost of doing one operation on the `i`th element is `cost[i]`.

Return the **minimum** total cost such that all the elements of the array `nums` become **equal**.

 

**Example 1:**
```
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
```

**Example 2:**
```
Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.
```

**Constraints:**

* `n == nums.length == cost.length`
* `1 <= n <= 10^5`
* `1 <= nums[i], cost[i] <= 10^6`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 3624 ms
Memory: 32.4 MB
```
```python
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def f(x):
            return sum(abs(a - x) * c for a,c in zip(nums, cost))

        l, r = min(nums), max(nums)
        res = f(l)
        while l < r:
            x = (l + r) // 2
            y1, y2 = f(x), f(x + 1)
            res = min(y1, y2)
            if y1 < y2:
                r = x
            else:
                l = x + 1
        return res
```

**Solution 2: (Binary Search)**
```
Runtime: 711 ms
Memory: 76.8 MB
```
```c++
class Solution {
    long long f(vector<int>& A, vector<int>& cost, int x) {
        long long res = 0;
        for (int i = 0; i < A.size(); ++i)
            res += 1L * abs(A[i] - x) * cost[i];
        return res;
    }
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        long long l = 1, r = 1000000, res = f(nums, cost, 1), x;
        while (l < r) {
            x = (l + r) / 2;
            long long y1 = f(nums, cost, x), y2 = f(nums, cost, x + 1);
            res = min(y1, y2);
            if (y1 < y2)
                r = x;
            else
                l = x + 1;
        }
        return res;
    }
};
```

**Solution 3: (Weighted Median)**
```
Runtime: 969 ms
Memory: 38.7 MB
```
```python
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total, cnt = sum(cost), 0
        for num, c in arr:
            cnt += c
            if cnt > total // 2:
                target = num
                break
        return sum(c * abs(num - target) for num, c in arr)
```

**Solution 4: (Binary Search, compare cost difference between mid and mid + 1)**
```
Runtime: 11 ms, Beats 71.83%
Memory: 42.40 MB, Beats 56.11%
```
```c++
class Solution {
    long long getCost(int mid, vector<int> &nums, vector<int> &cost) {
        int n = nums.size(), i;
        long long rst = 0;
        for (i = 0; i < n; i ++) {
            rst += 1LL * abs(nums[i] - mid) * cost[i];
        }
        return rst;
    }
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int left = *min_element(nums.begin(), nums.end()), right = *max_element(nums.begin(), nums.end()), mid;
        long long ans = LONG_LONG_MAX;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (getCost(mid, nums, cost) > getCost(mid + 1, nums, cost)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return getCost(left, nums, cost);
    }
};
```
