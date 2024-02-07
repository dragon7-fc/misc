2731. Movement of Robots


Some robots are standing on an infinite number line with their initial coordinates given by a **0-indexed** integer array `nums` and will start moving once given the command to move. The robots will move a unit distance each second.

You are given a string `s` denoting the direction in which robots will move on command. `'L'` means the robot will move towards the left side or negative side of the number line, whereas `'R'` means the robot will move towards the right side or positive side of the number line.

If two robots collide, they will start moving in opposite directions.

Return the sum of distances between all the pairs of robots d seconds after the command. Since the sum can be very large, return it modulo `10^9 + 7`.

**Note:**

* For two robots at the index `i` and `j`, pair `(i,j)` and pair `(j,i)` are considered the same pair.
* When robots collide, they instantly change their directions without wasting any time.
* Collision happens when two robots share the same place in a moment.
    * For example, if a robot is positioned in `0` going to the right and another is positioned in `2` going to the left, the next second they'll be both in `1` and they will change direction and the next second the first one will be in `0`, heading left, and another will be in `2`, heading right.
    * For example, if a robot is positioned in `0` going to the right and another is positioned in `1` going to the left, the next second the first one will be in `0`, heading left, and another will be in `1`, heading right.
 

**Example 1:**
```
Input: nums = [-2,0,2], s = "RLL", d = 3
Output: 8
Explanation: 
After 1 second, the positions are [-1,-1,1]. Now, the robot at index 0 will move left, and the robot at index 1 will move right.
After 2 seconds, the positions are [-2,0,0]. Now, the robot at index 1 will move left, and the robot at index 2 will move right.
After 3 seconds, the positions are [-3,-1,1].
The distance between the robot at index 0 and 1 is abs(-3 - (-1)) = 2.
The distance between the robot at index 0 and 2 is abs(-3 - 1) = 4.
The distance between the robot at index 1 and 2 is abs(-1 - 1) = 2.
The sum of the pairs of all distances = 2 + 4 + 2 = 8.
```

**Example 2:**
```
Input: nums = [1,0], s = "RL", d = 2
Output: 5
Explanation: 
After 1 second, the positions are [2,-1].
After 2 seconds, the positions are [3,-2].
The distance between the two robots is abs(-2 - 3) = 5.
```

**Constraints:**

* `2 <= nums.length <= 10^5`
* `-2 * 109 <= nums[i] <= 2 * 10^9`
* `0 <= d <= 10^9`
* `nums.length == s.length `
* `s` consists of `'L'` and `'R'` only
* `nums[i]` will be unique.

# Submissions
---
**Solution 1: (Pass Through + Prefix Sum)**

__Intuition__
If two objects collide then it appears that they have pass through

>>> In short if the ith robot is moving left then after time d it's position would be nums[i] - d and if it is moving right then it's position would be nums[i] + d

__Approach__
1. We change the final positions using pass through property.
```
for(ll i = 0; i < n; i ++){
    if(s[i] == 'L'){
        nums[i] -= d;
    }else{
        nums[i] += d;
    }
}
```
1. To calculate absolute diff between every pair in O(N). We can sort the distance array.
    * The index j contribution would be sum of abs(nums[j] - nums[0]) + abs(nums[j] - nums[1]) + abs(nums[j] - nums[2]) + ...... + abs(nums[j] - nums[j - 1]).
    * But we know `for (i<j) nums[i] < nums[j]` (Sorted array)
    * So we can open the abs() as nums[j] - nums[i]
    * The index j contribution would be sum of `nums[j] - nums[0] + nums[j] - nums[1] + nums[j] - nums[2] + ..... + nums[j] - nums[j - 1]`.
    * If we notice then this converts into `j * nums[j] - sum(nums[i] i belongs from 0 to j - 1)`
Sum of [0, j- 1] can be calculated in O(1) using prefix sum.
```
for(ll i = 1; i < n; i++){
    ll temp = (MOD + i * nums[i] - pre[i - 1])%MOD;
    ans = ((ans%MOD) + (temp%MOD))%MOD;
}
```
__Complexity__
* Time complexity: O(N * Log(N))
* Space complexity: O(N)

```
Runtime: 576 ms
Memory: 29.3 MB
```
```python
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n, m = len(nums), int(1e9 + 7)
        # Ignore the Collisions
        for i in range(n):
            if s[i] == 'L':
                nums[i] -= d
            else: 
                nums[i] += d
        
        # Sort according to position to calculate abs sum of each pair in O(N)
        nums.sort()

        pre = nums.copy()
        # Calculate Prefix Sum
        for i in range(1, n):
            pre[i] += pre[i - 1]
            pre[i] %= m

        ans = 0
        for i in range(1, n):
            # each jth index contributes to j * nums[j] - pre[j - 1]
            ans += i * nums[i] - pre[i - 1]
            ans %= m
        return ans
```
