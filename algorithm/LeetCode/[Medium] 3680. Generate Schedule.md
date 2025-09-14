3680. Generate Schedule

You are given an integer `n` representing `n` teams. You are asked to generate a schedule such that:

* Each team plays every other team **exactly twice**: once at home and once away.
* There is exactly one match per day; the schedule is a list of consecutive days and `schedule[i]` is the match on day `i`.
* No team plays on **consecutive** days.

Return a 2D integer array `schedule`, where `schedule[i][0]` represents the home team and `schedule[i][1]` represents the away team. If multiple schedules meet the conditions, return any one of them.

If no schedule exists that meets the conditions, return an empty array.

 

**Example 1:**
```
Input: n = 3

Output: []

Explanation:

Since each team plays every other team exactly twice, a total of 6 matches need to be played: [0,1],[0,2],[1,2],[1,0],[2,0],[2,1].

It's not possible to create a schedule without at least one team playing consecutive days.
```

**Example 2:**
```
Input: n = 5

Output: [[0,1],[2,3],[0,4],[1,2],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[2,0],[3,1],[4,0],[2,1],[4,3],[1,0],[3,2],[4,1],[3,0],[4,2]]

Explanation:

Since each team plays every other team exactly twice, a total of 20 matches need to be played.

The output shows one of the schedules that meet the conditions. No team plays on consecutive days.
```
 

**Constraints:**

* `2 <= n <= 50`

# Submissions
---
**Solution 1: (Brute Force)**

__Intuition__
For any day d , find all the available teams from (0 to n) who did not play the lastmatch . Among them filter out those pair (i,j) who had played already or in past days and from the remaining valid teams , chose the team with minimumgmaes played played till now .

__Approach__
A. There are n teams.

Each day we want to schedule one match (two teams playing).

B. Keep track of:

gamesPlayed[i] → how many matches team i has played so far.

teams[i] -> denotes the ith team

matches[i][j] → whether team i has already played with team j.

lastPlayedTeam1, lastPlayedTeam2 → the two teams who played the last match.

C. For each day:

First, find the available teams:
All teams except the two that played yesterday.

From these available teams, check all possible pairs (i, j).

Skip the pair if they already played before.

For every valid pair, compute gamesPlayed[i] + gamesPlayed[j].
This value tells how “busy” the two teams are.

Pick the pair with the smallest sum (so that less active teams get more chances).

If no such pair is found return {}

D. Schedule that match:

Mark that (i, j) match as played.

Increase both teams gamesPlayed count.

Update lastPlayedTeam1, lastPlayedTeam2 for the next day.

__Complexity__
Time complexity:
O(n^4)
Space complexity:
O(n^2)

```
Runtime: 643 ms, Beats 75.00%
Memory: 128.93 MB, Beats 12.50%
```
```c++
class Solution {
public:
    vector<vector<int>> generateSchedule(int n) {
        if (n <= 4) {
            return {};
        }
        int total_matches = n * (n - 1);
        unordered_set<int> teams;
        vector<int> gamesPlayed(n, 0);
        vector<vector<bool>> matches(n, vector<bool>(n, false));
        int lastPlayedTeam1 = -1 , lastPlayedTeam2 = -1;
        for (int i = 0 ; i < n ;  i++){
            teams.insert(i);
        }
        vector<vector<int>> schedule;
        for (int day = 0 ; day < total_matches ; day++) {
            unordered_set<int> available;
            for (int team : teams){
                if (team != lastPlayedTeam1 && team != lastPlayedTeam2){
                    available.insert(team);
                }
            }
            int miniScore = INT_MAX;
            int Firstteam = -1;
            int Secondteam = -1;

            for (int team1 : available){
                for (int team2 : available){
                    if (team1 == team2) continue;
                    if (matches[team1][team2]) continue;
                    int score = gamesPlayed[team1] + gamesPlayed[team2];
                    if (score < miniScore){
                        miniScore = score;
                        Firstteam = team1;
                        Secondteam = team2;
                    }
                }
            }
            if (Firstteam == -1 || Secondteam == -1) return {};
            schedule.push_back({Firstteam , Secondteam});
            matches[Firstteam][Secondteam] = true;
            lastPlayedTeam1 = Firstteam;
            lastPlayedTeam2 = Secondteam;
            gamesPlayed[Firstteam]++;
            gamesPlayed[Secondteam]++;
        }
        return schedule;
    }
};
```
