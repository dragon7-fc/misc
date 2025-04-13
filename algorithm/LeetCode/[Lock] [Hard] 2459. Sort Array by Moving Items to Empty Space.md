2459. Sort Array by Moving Items to Empty Space

You are given an integer array `nums` of size `n` containing each element from `0` to `n - 1` (**inclusive**). Each of the elements from `1` to `n - 1` represents an item, and the element `0` represents an empty space.

In one operation, you can move any item to the empty space. `nums` is considered to be sorted if the numbers of all the items are in **ascending** order and the empty space is either at the beginning or at the end of the array.

For example, if `n = 4`, `nums` is sorted if:

* `nums = [0,1,2,3]` or
* `nums = [1,2,3,0]`
...and considered to be unsorted otherwise.

Return the minimum number of operations needed to sort `nums`.

 

**Example 1:**
```
Input: nums = [4,2,0,3,1]
Output: 3
Explanation:
- Move item 2 to the empty space. Now, nums = [4,0,2,3,1].
- Move item 1 to the empty space. Now, nums = [4,1,2,3,0].
- Move item 4 to the empty space. Now, nums = [0,1,2,3,4].
It can be proven that 3 is the minimum number of operations needed.
```

**Example 2:**
```
Input: nums = [1,2,3,4,0]
Output: 0
Explanation: nums is already sorted so return 0.
```

**Example 3:**
```
Input: nums = [1,0,2,4,3]
Output: 2
Explanation:
- Move item 2 to the empty space. Now, nums = [1,2,0,4,3].
- Move item 3 to the empty space. Now, nums = [1,2,3,4,0].
It can be proven that 2 is the minimum number of operations needed.
```

**Constraints:**

* `n == nums.length`
* `2 <= n <= 10^5`
* `0 <= nums[i] < n`
* All the values of nums are unique.

# Submissions
---
**Solution 1: (Greedy)**

    m[0] = 2,  m[m[0]] = 1
    4,  2,  0,  3,  1
m   2   4   1   3   0
    1       2
    4   1
    0           4
    4,  2,  0,  3,  1
            3   0
    0           4
    1               0
m   2   4   1   3   0
    3           2
    0               3
    4   0
        
    

>   0   1   2   3   4      |  3
    1   3   4   4   0      |  3

    1   2   3   4   0
    ------------------
    0   1   2   3   4      | 4
    1   2   3   4   0      | 0

    1   0   2   4   3
    ------------------
m   1   0   2   4   3
    0   1
    4           0
                3   0
    0               4
m   1   0   2   4   3
        2   0
            3       0
m[0] = 1, m[m[0]+1] = 3
m   1   0   2   4   3
        2   0
            3       0
    

    0   1   2   3   4      | x
    1   2   3   4   0      | 2
2 option
step1 -> replace
step2 -> check

        
    3,  2,  1,  6,  7,  4,  5,  0
                    0           7
                    4   0
                        5   0
                0           6
    0           3
    2   0
        1   0
    0       2
    
        

    3,  2,  1,  6,  7,  4,  5,  0

    0   1   2   3   4   5   6   7


    4   3   1   2   0
    0               4
    3   0
        1   0
            2   0
    0           3

    0   1   2   3   4

```
Runtime: 1464 ms, Beats 7.14%
Memory: 69.48 MB, Beats 96.43%
```
```c++
class Solution {
public:
    int sortArray(vector<int>& nums) {
        int n = nums.size(), i, a = 0, b = 0;
        bool flag = true;
        vector<int> dp(n);
        for (i = 0; i < n; i ++) {
            dp[nums[i]] = i;
        }
        while (flag) {
            while (dp[0] != 0) {
                swap(dp[0], dp[dp[0]]);
                a += 1;
            }
            flag = false;
            for (i = 1; i < n; i ++) {
                if (dp[i] != i) {
                    swap(dp[0], dp[i]);
                    a += 1;
                    flag = true;
                    break;
                }
            }
        }
        for (i = 0; i < n; i ++) {
            dp[nums[i]] = i;
        }
        flag = true;
        while (flag) {
            while (dp[0] != n-1) {
                swap(dp[0], dp[dp[0]+1]);
                b += 1;
            }
            flag = false;
            for (i = 1; i < n; i ++) {
                if (dp[i] != i-1) {
                    swap(dp[i], dp[0]);
                    b += 1;
                    flag = true;
                    break;
                }
            }
        }
        return min(a, b);
    }
};
```

**Solution 2: (choose position of zero)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 74.60 MB, Beats 67.86%
```
```c++
class Solution {
public:
    int sortArray(vector<int>& nums) {
        int n = nums.size();
		
        vector<int> npos(n);
        for (int i = 0; i < n; ++i) npos[nums[i]] = i;
        
        // note that 'npos' is passed by value INTENTIONALLY,
        // because it calls copy constructor;
        // if we pass it by referece then the same 'npos'
        // will be used for both s=0 and s=1
        auto permute = [n](vector<int> npos, int s) -> int
        {
            int cnt = 0, nxt = 1, ni;
            while (nxt < n)
            {
                if (npos[0] == s * (n-1))
                {
                    while (npos[nxt] == nxt-s)
                        if (++nxt == n) return cnt;
                    ni = nxt;
                } else ni = npos[0] + s;
                swap(npos[0], npos[ni]);
                ++cnt;
            }
            return cnt;
        };
        
        return min(permute(npos, 0), permute(npos, 1));
    }
};
```
