2155. All Divisions With the Highest Score of a Binary Array

You are given a **0-indexed** binary array `nums` of length `n`. `nums` can be divided at index `i` (where `0 <= i <= n`) into two arrays (possibly empty) `numsleft` and `numsright`:

* `numsleft` has all the elements of nums between index `0` and `i - 1` (**inclusive**), while `numsright` has all the elements of `nums` between index `i` and `n - 1` (**inclusive**).
* If `i == 0`, `numsleft` is **empty**, while `numsright` has all the elements of `nums`.
* If `i == n`, `numsleft` has all the elements of `nums`, while `numsright` is **empty**.

The **division score** of an index `i` is the **sum** of the number of `0`'s in `numsleft` and the number of `1`'s in `numsright`.

Return **all distinct indices** that have the **highest** possible **division score**. You may return the answer in **any order**.

 

**Example 1:**
```
Input: nums = [0,0,1,0]
Output: [2,4]
Explanation: Division at index
- 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 = 1.
- 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 = 2.
- 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 = 3.
- 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 = 2.
- 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3.
Note the answer [4,2] would also be accepted.
```

**Example 2:**
```
Input: nums = [0,0,0]
Output: [3]
Explanation: Division at index
- 0: numsleft is []. numsright is [0,0,0]. The score is 0 + 0 = 0.
- 1: numsleft is [0]. numsright is [0,0]. The score is 1 + 0 = 1.
- 2: numsleft is [0,0]. numsright is [0]. The score is 2 + 0 = 2.
- 3: numsleft is [0,0,0]. numsright is []. The score is 3 + 0 = 3.
Only index 3 has the highest possible division score 3.
```

**Example 3:**
```
Input: nums = [1,1]
Output: [0]
Explanation: Division at index
- 0: numsleft is []. numsright is [1,1]. The score is 0 + 2 = 2.
- 1: numsleft is [1]. numsright is [1]. The score is 0 + 1 = 1.
- 2: numsleft is [1,1]. numsright is []. The score is 0 + 0 = 0.
Only index 0 has the highest possible division score 2.
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 10^5`
* `nums[i]` is either `0` or `1`.

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 7270 ms
Memory Usage: 24.7 MB
```
```python
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_div_score = 0
        right_div_score = sum(nums)
        
        div_sum = [left_div_score+right_div_score]
        
        for i in range(len(nums)):
            if nums[i]==0:
                left_div_score+=1
            if nums[i]==1:
                right_div_score-=1
            div_sum.append(left_div_score+right_div_score)
                
        max_val = max(div_sum)
        
        return( [i for i, v in enumerate(div_sum) if v==max_val])
```

**Solution 2: (Prefix Sum)**
```
Runtime: 692 ms
Memory Usage: 286.6 MB
```
```c++
class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        int N = nums.size(), one = accumulate(begin(nums), end(nums), 0), zero = 0, mx = 0;
        vector<int> ans;
        for (int i = 0; i <= N; ++i) {
            int score = one + zero;
            if (score > mx) {
                ans = {i};
                mx = score;
            } else if (score == mx) ans.push_back(i);
            if (i < N) {
                one -= nums[i] == 1;
                zero += nums[i] == 0;
            }
        }
        return ans;
    }
};
```
