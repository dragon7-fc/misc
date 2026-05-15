1674. Minimum Moves to Make Array Complementary

You are given an integer array `nums` of even length `n` and an integer `limit`. In one move, you can replace any integer from `nums` with another integer between 1 and `limit`, inclusive.

The array `nums` is **complementary** if for all indices `i` (**0-indexed**), `nums[i] + nums[n - 1 - i]` equals the same number. For example, the array `[1,2,3,4]` is **complementary** because for all indices `i`, `nums[i] + nums[n - 1 - i] = 5`.

Return the minimum number of moves required to make `nums` **complementary**.

 

**Example 1:**
```
Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
```

**Example 2:**
```
Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
```

**Example 3:**
```
Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.
```

**Constraints:**

* `n == nums.length`
* `2 <= n <= 10^5`
* `1 <= nums[i] <= limit <= 10^5`
* `n` is even.

# Submissions
---
**Solution 1: (O(max(n, k)) method)**

**Idea**

If we want to make the nums complementary, having all the pairs A = nums[i], B = nums[n - 1 - i] with A + B = T. Considering a pair A = nums[i], B = nums[n - 1 - i], there are 5 different situation for every such pair (A, B), given different target T.

* 2 <= T < min(A, B) + 1, we need 2 operations to make both A, B smaller
* min(A, B) + 1 <= T < A + B, we need 1 operation to make the larger one out of A and B smaller
* T = A + B, we need 0 operation
* A + B < T < max(A, B) + limit, we need 1 operation to make the smaller one out of A and B larger
* max(A, B) + limit < T <= 2 * limit, we need 2 operation to make both A, B larger

We calculate the boundary for each pair (A, B) and note down the corresponding operation changes as delta. delta[i] = x means we need x more operations when target T change from i - 1 to i.

**Complexity**

* Time: O(max(n, k))
* Space: O(k)

```
Runtime: 1732 ms
Memory Usage: 36.3 MB
```
```python
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = collections.Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
            
        curr = 0            
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res   
```

**Solution 2: (Binary Search)**
```
Runtime: 444 ms, Beats 11.50%
Memory: 210.74 MB, Beats 16.81%
```
```c++
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        unordered_map<int, int> sum_count;
        vector<int> min_arr, max_arr;
        min_arr.reserve(n / 2);
        max_arr.reserve(n / 2);

        for (int i = 0; i < n / 2; ++i) {
            int a = std::min(nums[i], nums[n - 1 - i]);
            int b = std::max(nums[i], nums[n - 1 - i]);

            sum_count[a + b]++;
            min_arr.push_back(a);
            max_arr.push_back(b);
        }

        std::sort(min_arr.begin(), min_arr.end());
        std::sort(max_arr.begin(), max_arr.end());

        int min_ops = n;

        for (int c = 2; c <= 2 * limit; ++c) {
            int add_left =
                n / 2 - (lower_bound(min_arr.begin(), min_arr.end(), c) -
                         min_arr.begin());
            int add_right =
                lower_bound(max_arr.begin(), max_arr.end(), c - limit) -
                max_arr.begin();

            int current_ops = n / 2 + add_left + add_right - sum_count[c];
            min_ops = min(min_ops, current_ops);
        }

        return min_ops;
    }
};
```

**Solution 3: (Prefix Sum, Math, summarize all possible modification)**

          (1,1)   (a,1)   (a,b)         (b,limit)          (limit,limit) (limit,limit+1)
        1 2 ...   a+1 ... a+b a+b+1 ... b+limit  b+limit+1...                          
          ------- -------     -----------------  ---------------------------------------
             2       1     0          1                 2
diff  0   +2      -1      -1  +1                  +1

       nums = [1,2,4,3], limit = 4
        
        a   b
        1 2 3 4 5 6 7 8 9
diff     +2
         -1  -1+1    +1
          1 1 0 1 1 1 2
          a   b
        1 2 3 4 5 6 7 8 9
diff     +2
           -1    -1+1  +1
          2 1 1 1 0 1 1 2

current   3 2 1 2 1 2 3 
              min
```
Runtime: 3 ms, Beats 87.61%
Memory: 93.42 MB, Beats 61.06%
```
```c++
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<int> diff(2 * limit + 2, 0);

        for (int i = 0; i < n / 2; ++i) {
            int a = min(nums[i], nums[n - 1 - i]);
            int b = max(nums[i], nums[n - 1 - i]);

            diff[2] += 2;
            diff[a + 1] -= 1;
            diff[a + b] -= 1;
            diff[a + b + 1] += 1;
            diff[b + limit + 1] += 1;
        }

        int min_ops = n;
        int current_ops = 0;

        for (int c = 2; c <= 2 * limit; ++c) {
            current_ops += diff[c];
            min_ops = min(min_ops, current_ops);
        }

        return min_ops;
    }
};
```
