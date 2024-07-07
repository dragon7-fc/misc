1509. Minimum Difference Between Largest and Smallest Value in Three Moves

Given an array `nums`, you are allowed to choose one element of `nums` and change it by any value in one move.

Return the minimum difference between the largest and smallest value of `nums` after perfoming at most 3 moves.

 

**Example 1:**
```
Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
```

**Example 2:**
```
Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
```

**Example 3:**
```
Input: nums = [6,6,0,1,1,4,6]
Output: 2
```

**Example 4:**
```
Input: nums = [1,5,6,14,15]
Output: 1
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Math)**

**Intuition**

* If we can do 0 move, return max(A) - min(A)
* If we can do 1 move, return min(the second max(A) - min(A), the max(A) - second min(A))
and so on.


**Explanation**

We have 4 plans:

1. kill 3 biggest elements
1. kill 2 biggest elements + 1 smallest elements
1. kill 1 biggest elements + 2 smallest elements
1. kill 3 smallest elements

```
Runtime: 588 ms
Memory Usage: 23.6 MB
```
```python
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))
```

**Solution 2: (Sliding Window, sort)**
```
Runtime: 67 ms
Memory: 38.86 MB
```
```c++
class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        if (n <= 3) {
            return 0;
        }
        sort(nums.begin(), nums.end());
        int ans = INT_MAX;
        for (int i = 0; i < 4; i ++) {
            ans = min(ans, nums[i+n-4] - nums[i]);
        }
        return ans;
    }
};
```

**Solution 3: (Math)**
```
Runtime: 133 ms
Memory Usage: 12.4 MB
```
```c
int cmp(const void *a, const void *b){
    return *(int *)a - *(int *)b;
}
#define MIN(a,b) (a<b?a:b)
int minDifference(int* nums, int numsSize){
    if(numsSize<=3) return 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    
    int min=0;
    
    /* remove 3 at the start and 0 at the end */
    min=nums[numsSize-1]-nums[3];
    
    /* remove 2 at the start and 1 at the end */
    min=MIN(min,nums[numsSize-2]-nums[2]);
    
    /* remove 1 at the start and 2 at the end */
    min=MIN(min,nums[numsSize-3]-nums[1]);
    
    /* remove 0 at the start and 3 at the end */
    min=MIN(min,nums[numsSize-4]-nums[0]);
    
    return min;
}
```

**Solution 4: (Math)**

    . . . . . 
    ^ ^
      ^ ^
        ^ ^
          ^ ^

```
Runtime: 328 ms
Memory Usage: 35.4 MB
```
```c++
class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        if (n < 5) return 0;
        sort(nums.begin(), nums.end());
        return min({nums[n - 1] - nums[3], nums[n - 2] - nums[2], nums[n - 3] - nums[1], nums[n - 4] - nums[0]});
    }
};
```

