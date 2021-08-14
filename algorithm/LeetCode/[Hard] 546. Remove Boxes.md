546. Remove Boxes

Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get `k*k` points.
Find the maximum points you can get.

**Example 1:**
```
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
```

**Note:** The number of boxes `n` would not exceed `100`.

# Submissions
---
**Solution 1: (DP Top-Down)**

`dp(i,j,k)` means the max points you can earn between boxes "i" and "j", with "k" boxes before i that has the same color as "i".

But there are a few important facts that are not clearly mentioned in other posts:

1. At the point of "dp(i,j,k)", all boxes before "i" are already removed. "ALL" removed, except for the "k" boxes that has same color as "i". So, literally, at "dp(i,j,k)" you are seeing "k+1" continuous boxes of "i" in the front.
2. For dp(i,j,k), we can have 2 choices, either remove box "i", or not.
3. If we remove box "i", then we earn the points of "i" together with "k" boxes before it. And the rest dp becomes "dp(i+1,j,0)". "k" becomes zero for the rest becase there are not a single box ahead anymore after removing "i".
4. If we don't remove box "i", then k becomes "k+1". In order to use this "k+1", we have to find another box that has the same color as these "k+1" boxes. If there is no such box, then there is no point keeping box "i". If there is such box, then we remove all boxes along the way until this box of same color, so that this box can join "k+1" and makes a pattern in #1

```
Runtime: 1484 ms
Memory Usage: 33.9 MB
```
```python
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        @functools.lru_cache(None)
        def dfs(i, j, k):
            if i > j: return 0
            cnt=0
            while (i+cnt) <= j and boxes[i] == boxes[i+cnt]:
                cnt+=1
            i2 = i+cnt
            res = dfs(i2, j, 0) + (k + cnt)**2
            for m in range(i2,j+1):
                if boxes[m] == boxes[i]:
                    res = max(res, dfs(i2, m-1, 0) + dfs(m, j, k+cnt))
            return res
        
        return dfs(0, len(boxes)-1, 0)
```
