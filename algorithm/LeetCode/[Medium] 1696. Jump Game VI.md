1696. Jump Game VI

You are given a **0-indexed** integer array `nums` and an integer `k`.

You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. That is, you can jump from index `i` to any index in the range `[i + 1, min(n - 1, i + k)]` inclusive.

You want to reach the last index of the array (index `n - 1`). Your score is the sum of all `nums[j]` for each index `j` you visited in the array.

Return the maximum score you can get.

 

**Example 1:**
```
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
```

**Example 2:**
```
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
```

**Example 3:**
```
Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
```

**Constraints:**

* `1 <= nums.length, k <= 10^5`
* `-104 <= nums[i] <= 10^4`

# Submissions
---
**Solution 1: (Sliding window, Mono decresing queue)**
```
Runtime: 684 ms
Memory Usage: 28.2 MB
```
```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = [float('-inf')] * n
        best[0] = nums[0]
        dec = collections.deque([0])
        
        for i in range(1, n):
            # lazy deletion
            while dec and dec[0] < i - k:
                dec.popleft()
            # calculate the best score up until i
            best[i] = best[dec[0]] + nums[i]
            # maintain the mono dec deque
            while dec and best[dec[-1]] <= best[i]:
                dec.pop()
            dec.append(i)
            
        return best[-1]
```

**Solution 2: (Heap)**
```
Runtime: 784 ms
Memory Usage: 33.3 MB
```
```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        pq = [] # max heap 
        for i in reversed(range(len(nums))): 
            while pq and pq[0][1] - i > k: heappop(pq)
            ans = nums[i] - pq[0][0] if pq else nums[i]
            heappush(pq, (-ans, i))
        return ans
```