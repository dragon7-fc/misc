1366. Rank Teams by Votes

In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

 

**Example 1:**
```
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.
```

**Example 2:**
```
Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 
```

**Example 3:**
```
Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter so his votes are used for the ranking.
```

**Example 4:**
```
Input: votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
Output: "ABC"
Explanation: 
Team A was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team B was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team C was ranked first by 2 voters, second by 2 voters and third by 2 voters.
There is a tie and we rank teams ascending by their IDs.
```

**Example 5:**
```
Input: votes = ["M","M","M","M"]
Output: "M"
Explanation: Only team M in the competition so it has the first rank.
```

**Constraints:**

* `1 <= votes.length <= 1000`
* `1 <= votes[i].length <= 26`
* `votes[i].length == votes[j].length for 0 <= i, j < votes.length`.
* `votes[i][j]` is an English upper-case letter.
* All characters of `votes[i]` are unique.
* All the characters that occur in `votes[0]` also occur in `votes[j]` where `1 <= j < votes.length`.

# Submissions
---
**Solution 1: (Counter, sort, compare vector)**

**Explanation**

Count the rank of vote for each candidate.  
Sort all teams according to the ranking system.


**Complexity**

Time `O(NMlogM)`  
Space `O(NM)`  
where `N = votes.length` and `M = votes[0].length <= 26`
```
Runtime: 80 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {v: [0] * len(votes[0]) for v in votes[0]}  # {team1: [rank1_count, rank2_count, ...]}
        for a in votes:
            for i, v in enumerate(a):
                count[v][i] -= 1
        return ''.join(sorted(votes[0], key=lambda v: count[v] + [v]))
```

**Solution 2: (Counter, sort, compare vector)**
```
Runtime: 15 ms
Memory: 14.02 MB
```
```c++
class Solution {
public:
    string rankTeams(vector<string>& votes) {
        string ans(votes[0]);
        const int n(votes[0].length());
        vector<vector<int>> ranks(26, vector<int>(n));
        
        for (const string& vote: votes)
            for (int i = 0; i < n; ++i)
                ranks[vote[i] - 'A'][i]++;
        /*
        function<bool(const char&, const char&)> compare = [&](const char& x, const char& y) {
            for (int i = 0; i < n; ++i) {
                if (ranks[x - 'A'][i] == ranks[y - 'A'][i]) continue;
                return ranks[x - 'A'][i] > ranks[y - 'A'][i];
            }
            return x < y;
        };
        
        sort(ans.begin(), ans.end(), compare);
		*/
		// credits: @grokus, @plustone
		// vectors are comparable, runs faster if your compiler can optimize the comparisons
		sort(ans.begin(), ans.end(), [&](const char& x, const char& y) { return ranks[x - 'A'] > ranks[y - 'A'] || ranks[x - 'A'] == ranks[y - 'A'] && x < y; });
        return ans;
    }
};
```
