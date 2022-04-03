2225. Find Players With Zero or One Losses

You are given an integer array `matches` where `matches[i] = [winneri, loseri]` indicates that the player `winneri` defeated player `loseri` in a match.

Return a list `answer` of size `2` where:

* `answer[0]` is a list of all players that have **not** lost any matches.
* `answer[1]` is a list of all players that have lost exactly **one** match.

The values in the two lists should be returned in **increasing** order.

**Note:**

You should only consider the players that have played **at least one** match.
The testcases will be generated such that **no** two matches will have the **same** outcome.
 

**Example 1:**
```
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
```

**Example 2:**
```
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
```

**Constraints:**

* `1 <= matches.length <= 10^5`
* `matches[i].length == 2`
* `1 <= winneri, loseri <= 10^5`
* `winneri != loseri`
* All `matches[i]` are **unique**.

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 2396 ms
Memory Usage: 68.8 MB
```
```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_set = set()
        loser_set = set()
        loss_map = defaultdict(int)
        
        for winner, loser in matches:
            winner_set.add(winner)
            loser_set.add(loser)
            loss_map[loser] += 1
        
        return [sorted(list(winner_set - loser_set)), sorted([k for k,v in loss_map.items() if v == 1])]
```

**Solution 2: (Set)**
```
Runtime: 664 ms
Memory Usage: 171.6 MB
```
```c++
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        set<int> win;
        map<int, int> lose; // person, count
        for (auto &m : matches) {
            win.insert(m[0]);
            lose[m[1]]++;
        }
        vector<int> oneLose;
        for (auto &[p, cnt] : lose) {
            if (cnt == 1) oneLose.push_back(p);
            win.erase(p);
        }
        return {vector<int>(begin(win), end(win)), oneLose};
    }
};
```
