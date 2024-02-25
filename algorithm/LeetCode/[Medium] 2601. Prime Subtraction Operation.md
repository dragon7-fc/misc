2601. Prime Subtraction Operation

You are given a **0-indexed** integer array `nums` of length `n`.

You can perform the following operation as many times as you want:

* Pick an index `i` that you haven’t picked before, and pick a prime `p` **strictly less than** `nums[i]`, then subtract `p` from `nums[i]`.

Return `true` if you can make nums a strictly increasing array using the above operation and false otherwise.

A **strictly increasing array** is an array whose each element is strictly greater than its preceding element.

 

**Example 1:**
```
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
```

**Example 2:**
```
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
```

**Example 3:**
```
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 1000`
* `nums.length == n`

# Submissions
---
**Solution 1: (Greedy, Math)**
```
Runtime: 632 ms
Memory: 13.9 MB
```
```python
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        ps = [2]
        for i in range(3, 1001):
            j = 2
            while j * j <= i:
                if i % j == 0:
                    break
                j += 1
            if i % j == 0:
                continue
            ps.append(i)
        for j, n in enumerate(nums):
            ok = False
            for i in range(bisect_left(ps, n), -1, -1):
                if i >= len(ps) or ps[i] >= n:
                    continue
                if j == 0 and nums[j] > ps[i]:
                    nums[j] -= ps[i]
                    ok = True
                    break
                else:
                    if nums[j] - ps[i] > nums[j-1]:
                        nums[j] -= ps[i]
                        ok = True
                        break
            if j > 0:
                if nums[j] <= nums[j-1]:
                    return False
        return True
```

**Solution 2: (Greedy, Math, Brute Force)**
```
Runtime: 142 ms
Memory: 23.6 MB
```
```c++
class Solution {
    bool isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
public:
    bool primeSubOperation(vector<int>& nums) {
        int n = nums.size(), prev = -1; 
        for(int i = 0; i < n; i++) {
            if (nums[i] <= prev) return false;
            bool found = false;
            for (int curr = nums[i]-1; curr>1; curr--) {
                if (isPrime(curr))
                {
                    if (prev >= nums[i]-curr) {
                        continue;
                    }
                    prev = nums[i] - curr;
                    found = true;
                    break;
                }
            }
            if (!found) {
                if(nums[i] > prev) {
                    prev = nums[i];
                } else {
                    return false;
                }
            }
        }
        return true;
    }
};
```
