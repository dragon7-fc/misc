2644. Find the Maximum Divisibility Score

You are given two **0-indexed** integer arrays `nums` and `divisors`.

The **divisibility score** of `divisors[i]` is the number of indices `j` such that `nums[j]` is divisible by `divisors[i]`.

Return the integer `divisors[i]` with the maximum divisibility score. If there is more than one integer with the maximum score, return the minimum of them.

 

**Example 1:**
```
Input: nums = [4,7,9,3,9], divisors = [5,2,3]
Output: 3
Explanation: The divisibility score for every element in divisors is:
The divisibility score of divisors[0] is 0 since no number in nums is divisible by 5.
The divisibility score of divisors[1] is 1 since nums[0] is divisible by 2.
The divisibility score of divisors[2] is 3 since nums[2], nums[3], and nums[4] are divisible by 3.
Since divisors[2] has the maximum divisibility score, we return it.
```

**Example 2:**
```
Input: nums = [20,14,21,10], divisors = [5,7,5]
Output: 5
Explanation: The divisibility score for every element in divisors is:
The divisibility score of divisors[0] is 2 since nums[0] and nums[3] are divisible by 5.
The divisibility score of divisors[1] is 2 since nums[1] and nums[2] are divisible by 7.
The divisibility score of divisors[2] is 2 since nums[0] and nums[3] are divisible by 5.
Since divisors[0], divisors[1], and divisors[2] all have the maximum divisibility score, we return the minimum of them (i.e., divisors[2]).
```

**Example 3:**
```
Input: nums = [12], divisors = [10,16]
Output: 10
Explanation: The divisibility score for every element in divisors is:
The divisibility score of divisors[0] is 0 since no number in nums is divisible by 10.
The divisibility score of divisors[1] is 0 since no number in nums is divisible by 16.
Since divisors[0] and divisors[1] both have the maximum divisibility score, we return the minimum of them (i.e., divisors[0]).
```

**Constraints:**

* `1 <= nums.length, divisors.length <= 1000`
* `1 <= nums[i], divisors[i] <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 5362 ms
Memory: 14.3 MB
```
```python
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        pre = []
        for divisor in divisors:
            cnt = 0
            for num in nums:
                cnt += num%divisor == 0
            pre += [[cnt, divisor]]
        return max(pre, key=lambda x: [x[0], -x[1]])[1]
```

**Solution 2: (Brute Force)**
```
Runtime: 518 ms
Memory: 29.4 MB
```
```c++
class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        int res = 0, curr = -1;
        for(auto &d: divisors){
            int score = 0;
            for(auto &it: nums)     
                score += (it % d == 0);
            if(score >= curr){
                if(score == curr)       
                    res = min(res, d);
                else                    
                    res = d;                    
                curr = score;
            }
        }
        return res;
    }
};
```
