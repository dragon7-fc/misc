3282. Reach End of Array With Max Score

You are given an integer array `nums` of length `n`.

Your goal is to start at index `0` and reach index `n - 1`. You can only jump to indices greater than your current index.

The score for a jump from index `i` to index `j` is calculated as `(j - i) * nums[i]`.

Return the **maximum** possible total score by the time you reach the last index.

 

**Example 1:**
```
Input: nums = [1,3,1,5]

Output: 7

Explanation:

First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.
```

**Example 2:**
```
Input: nums = [4,3,1,3,2]

Output: 16

Explanation:

Jump directly to the last index. The final score is 4 * 4 = 16.
```
 

**Constraints:**

`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Mono Stack)**
```
Runtime: 262 ms
Memory: 177.04 MB
```
```c++
class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return 0;
        }
        stack<tuple<int,int,long long>> stk;
        for (int i = n-2; i >= 0; i --) {
            while (stk.size() && get<0>(stk.top()) < nums[i]) {
                stk.pop();
            }
            if (stk.size()) {
                stk.push({nums[i], i, (get<1>(stk.top()) - i)*(long long)nums[i] + get<2>(stk.top())});
            } else {
                stk.push({nums[i], i, (n-1-i)*(long long)nums[i]});
            }
        }
        return get<2>(stk.top());
    }
};
```

**Solution 2: (Greedy)**

(j - i) * A[i]
-> same to add A[i] for each step [i...j).

    [1, 3, 1, 5]
ma   1  3  3  3
res  0  1  4  7  

```
Runtime: 210 ms
Memory: 171.24 MB
```
```c++
class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        long long res = 0;
        int ma = 0;
        for (int a: nums) {
            res += ma;
            ma = max(ma, a);
        }
        return res;
    }
};
```
