1306. Jump Game III

Given an array of non-negative integers `arr`, you are initially positioned at start index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach to any index with value `0`.

Notice that you can not jump outside of the array at any time.

 

**Example 1:**
```
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
```

**Example 2:**
```
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
```

**Example 3:**
```
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
```

**Constraints:**

* `1 <= arr.length <= 5 * 10^4`
* `0 <= arr[i] < arr.length`
* `0 <= start < arr.length`

# Submissions
---
**Solution 1:**
```
Runtime: 260 ms
Memory Usage: 19 MB
```
```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        q = collections.deque()
        seen = set()

        q.append(start)

        while q:
            ind = q.popleft()
            seen.add(ind)
            if arr[ind] == 0:
                return True 
            for x in (ind - arr[ind], ind + arr[ind]):
                if 0 <= x < N and x not in seen:
                    q.append(x)

        return False 
        
```