403. Frog Jump

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

**Note:**

* The number of stones is `≥ 2` and is `< 1,100`.
* Each stone's position will be a non-negative integer `< 231`.
* The first stone's position is always `0`.

**Example 1:**
```
[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
```

**Example 2:**
```
[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 272 ms
Memory Usage: 21.2 MB
```
```python
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones)
        if stones[1] - stones[0] != 1: return False
        
        @functools.lru_cache(None)
        def dfs(i, k):
            if i == N-1:
                return True
            elif i > N-1:
                return False
            j = i+1
            step = stones[j] - stones[i]
            while step <= k+1:
                if step in [k-1, k, k+1]:
                    if dfs(j, step): return True
                j += 1
                if j >= N: break
                step = stones[j] - stones[i]
            return False
        
        return dfs(1, 1)
```

**Solution 2: (DP Top-Down, Set)**
```
Runtime: 100 ms
Memory Usage: 22.7 MB
```
```python
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        setOfStones = set(stones)

        @lru_cache(None)
        def canJump(stonePosition, jumpUnits):
            if jumpUnits <= 0 or stonePosition not in setOfStones:
                return False
            if stonePosition == target:
                return True
            # Try the three possible jumps with k-1, k and k+1 units from
            # the current stone.
            return (canJump(stonePosition + jumpUnits - 1, jumpUnits - 1) or
                    canJump(stonePosition + jumpUnits, jumpUnits) or
                    canJump(stonePosition + jumpUnits + 1, jumpUnits + 1))
        return canJump(1, 1)
```

**Solution 3: (DP Top-Down)**
```
Runtime: 42 ms
Memory: 21.7 MB
```
```c++
class Solution {
    int dfs(int i, int k, vector<unordered_map<int, int>> &dp, vector<int> &stones) {
        if (i == stones.size()-1) {
            dp[i][k] = 1;
            return 1;
        }
        if (i > stones.size()) {
            dp[i][k] = -1;
            return -1;
        }
        if (dp[i][k]) {
            return dp[i][k];
        }
        int j = i+1;
        int step = stones[j]-stones[i];
        while (step <= k+1) {
            if ((step == k-1 || step == k || step == k+1) && dfs(j, step, dp, stones) == 1) {
                dp[i][k] = 1;
                return 1;
            }
            j += 1;
            if (j >= stones.size()) {
                break;
            }
            step = stones[j] - stones[i];
        }
        dp[i][k] = -1;
        return -1;
    }
public:
    bool canCross(vector<int>& stones) {
        if (stones[1] - stones[0] != 1) {
            return false;
        }
        vector<unordered_map<int, int>> dp(stones.size());
        return dfs(1, 1, dp, stones) == 1;
    }
};
```
