3660. Jump Game IX

You are given an integer array `nums`.

From any index `i`, you can jump to another index `j` under the following rules:

* Jump to index `j` where `j > i` is allowed only if `nums[j] < nums[i]`.
* Jump to index `j` where `j < i` is allowed only if `nums[j] > nums[i]`.

For each index `i`, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at `i`.

Return an array `ans` where `ans[i]` is the maximum value reachable starting from index i.

 

**Example 1:**
```
Input: nums = [2,1,3]

Output: [2,2,3]

Explanation:

For i = 0: No jump increases the value.
For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
Thus, ans = [2, 2, 3].
```

**Example 2:**
```
Input: nums = [2,3,1]

Output: [3,3,3]

Explanation:

For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.
Thus, ans = [3, 3, 3].
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum, If a bigger value exists on the left and a smaller value exists on the right then those indices become connected and can reach the same maximum value)**

                <---
ans             i i+1
pre     ---x------------->
                ^ ^
                x ^
                  x
                ---
                connect
suff    <---------------x-


          v  v
    5  2  1  8  3
          ^i
    <-----
    ------------>
             <---

3      x
2    x
1        x
pre  2 3 3
suff 1 1 1
ans  3 3 3
    
case1: pre[i] <= suff[i+1]

suff       .
           <-
res    x
       i
       <- 

pre    .
      ->

case 2: pre[i] > suff[i+1]
pre      .
        ->
res      x x
         i i+1
        <-

suff       .
           <-
```
Runtime: 6 ms, Beats 87.50%
Memory: 227.33 MB, Beats 12.50%
```
```c++
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n), suff(n), res(n);

        pre[0] = nums[0], suff[n - 1] = nums[n - 1];
        for (int i = 1; i < n; i++) {
            pre[i] = max(nums[i], pre[i - 1]);
        }

        for (int i = n - 2; i >= 0; i--) {
            suff[i] = min(nums[i], suff[i + 1]);
        }

        res[n - 1] = pre[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            res[i] = pre[i];
            // merge segment
            if (pre[i] > suff[i + 1]) {
                res[i] = res[i + 1];
            }
        }
        return res;
    }
};
```

**Solution 2: (Interval Divide and Conquer)**
```
Runtime: 16 ms, Beats 43.09%
Memory: 225.38 MB, Beats 70.75%
```
```c++
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 0);

        // [value, index]
        using Item = pair<int, int>;
        vector<Item> prevMax(n);

        Item prev = {INT_MIN, -1};
        for (int i = 0; i < n; ++i) {
            if (nums[i] > prev.first) {
                prev = {nums[i], i};
            }
            prevMax[i] = prev;
        }

        auto process = [&](auto& self, int r, int rightMin,
                           int rightMax) -> void {
            auto [pMax, pivotIndex] = prevMax[r];
            int currMax = pMax <= rightMin ? pMax : rightMax;

            int nextRightMin = min(pMax, rightMin);
            for (int i = pivotIndex; i <= r; ++i) {
                ans[i] = currMax;
                nextRightMin = min(nextRightMin, nums[i]);
            }

            if (pivotIndex == 0) {
                return;
            }

            self(self, pivotIndex - 1, nextRightMin, currMax);
        };

        process(process, n - 1, INT_MAX, 0);

        return ans;
    }
};
```

**Solution 3: (Stack, convert to one direction and use mono inc stack to track and merge value range)**
```
Runtime: 15 ms, Beats 47.34%
Memory: 221.74 MB, Beats 76.60%
```
```c++
class Solution {
    struct Item {
        int value;
        int left;
        int right;
    };
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 0);

        vector<Item> stack;

        for (int i = 0; i < n; ++i) {
            Item curr = {nums[i], i, i};

            while (!stack.empty() && stack.back().value > nums[i]) {
                Item top = stack.back();
                stack.pop_back();
                curr.value = max(curr.value, top.value);
                curr.left = top.left;
            }

            stack.push_back(curr);
        }

        for (size_t i = 0; i < stack.size(); ++i) {
            for (int j = stack[i].left; j <= stack[i].right; ++j) {
                ans[j] = stack[i].value;
            }
        }

        return ans;
    }
};
```
