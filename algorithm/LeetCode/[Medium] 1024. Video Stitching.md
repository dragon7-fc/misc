1024. Video Stitching

You are given a series of video clips from a sporting event that lasted `T` seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time `clips[i][0]` and ends at time `clips[i][1]`.  We can cut these clips into segments freely: for example, a clip `[0, 7]` can be cut into segments `[0, 1] + [1, 3] + [3, 7]`.

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event `([0, T])`.  If the task is impossible, return `-1`.

 

**Example 1:**

```
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
```

**Example 2:**

```
Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation: 
We can't cover [0,5] with only [0,1] and [0,2].
```

**Example 3:**

```
Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation: 
We can take clips [0,4], [4,7], and [6,9].
```

**Example 4:**

```
Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation: 
Notice you can have extra video after the event ends.
```

**Note:**

1. `1 <= clips.length <= 100`
1. `0 <= clips[i][0], clips[i][1] <= 100`
1. `0 <= T <= 100`

# Submissions
---
**Solution 1 (DP Bottom-Up)**
```
Runtime: 28 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        N = len(clips)
        dp = [float('inf') for _ in range(T+1)]
        dp[0] = 0
        for videoLen in range(1, T+1):
            for clipStart, clipEnd in clips:
                if clipStart <= videoLen <= clipEnd:
                    dp[videoLen] = min(dp[videoLen], 1 + dp[clipStart])

        return -1 if dp[T] == float('inf') else dp[T]
```

**Solution 2: (Greedy)**
```
Runtime: 36 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        rst = 1; st = end = 0
        for i, j in clips:
            if i <= st: end = max(end, j)
            else: 
                if i > end: return -1
                st, end, rst = end, max(end, j), rst+1
            if end >= T: return rst
        return -1
```

**Solution 3: (DP Top-Down, Sort)**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        N = len(clips)
        clips.sort()
        
        @functools.lru_cache(None)
        def dp (i, t):
            if t >= T:
                return 0
            rst = float('inf')
            for j in range(i+1, N):
                clipStart = clips[j][0]
                clipEnd = clips[j][1]
                if clipStart <= t <= clipEnd:
                    rst = min(rst, 1 + dp(j, clipEnd))
            return rst
        
        ans = dp(-1, 0)
        
        return -1 if ans == float('inf') else ans
```