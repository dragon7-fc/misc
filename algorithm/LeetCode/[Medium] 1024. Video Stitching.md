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
**Solution 1 (DP)**
```
Runtime: 40 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [T+1 for _ in range(T+1)]
        dp[0] = 0
        for videoLen in range(1, T+1):
            for c in range(len(clips)):
                clipStart = clips[c][0]
                cliepEnd = clips[c][1]
                if clipStart <= videoLen and cliepEnd >= videoLen:
                    dp[videoLen] = min(dp[videoLen], 1 + dp[clipStart])
                    
        return -1 if dp[T] == T+1 else dp[T]
```

**Solution 2: (Greedy)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips)
        end = 0
        L = len(clips)
        i = 0
        mx = 0
        res = 0
        while end < T and i < L:
            if clips[i][0] > end:
                return -1
            while i < L and clips[i][0] <= end:
                mx = max(mx, clips[i][1])
                i += 1
            end = mx
            res += 1
        return -1 if end < T else res

```