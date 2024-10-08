2491. Divide Players Into Teams of Equal Skill

You are given a positive integer array `skill` of **even** length `n` where `skill[i]` denotes the skill of the `i`th player. Divide the players into `n / 2` teams of size `2` such that the total skill of each team is **equal**.

The **chemistry** of a team is equal to the **product** of the skills of the players on that team.

Return the sum of the **chemistry** of all the teams, or return `-1` if there is no way to divide the players into teams such that the total skill of each team is equal.

 

**Example 1:**
```
Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
```

**Example 2:**
```
Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.
```

**Example 3:**
```
Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.
```

**Constraints:**

* `2 <= skill.length <= 10^5`
* `skill.length` is even.
* `1 <= skill[i] <= 1000`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 1701 ms
Memory: 27.9 MB
```
```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i, j = 0, len(skill)-1
        skill.sort()
        ans = prev = 0
        while i < j:
            cur = skill[i] + skill[j]
            if prev == 0:
                prev = cur
            elif prev != cur:
                return -1
            ans += skill[i]*skill[j]
            i += 1
            j -= 1
        return ans
```

**Solution 2: (Hash Table)**
```
Runtime: 62 ms
Memory: 56.97 MB
```
```c++
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        unordered_map<int, int> cnt;
        int n = skill.size(), cur = 0;
        long long ans = 0;
        for (int sk: skill) {
            cur += sk;
            cnt[sk] += 1;
        }
        cur /= (n/2);
        for (int sk: skill) {
            if (cnt[sk] == 0) {
                continue;
            }
            if (cnt[cur-sk] == 0) {
                return -1;
            }
            cnt[sk] -= 1;
            cnt[cur-sk] -= 1;
            ans += sk*(cur-sk);
        }
        return ans;
    }
};
```

**Solution 3: (Counter, bucket sort)**
```
Runtime: 39 ms
Memory: 56.11 MB
```
```c++
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int cnt[10001] = {0}, pre = 0, i = 1, j = 1000;
        for (auto sk: skill) {
            cnt[sk] += 1;
        }
        long long ans = 0;
        while (i <= j) {
            while (cnt[i] == 0) {
                i += 1;
            }
            while (cnt[j] == 0) {
                j -= 1;
            }
            if (i > j) {
                break;
            }
            if (pre == 0) {
                pre = i+j;
            }
            if (i+j != pre || cnt[i] != cnt[j] || i == j && cnt[i]%2) {
                return -1;
            }
            if (i != j) {
                ans += (long long)i*j*cnt[i];
            } else {
                ans += (long long)i*j*cnt[i]/2;
            }
            i += 1;
            j -= 1;
        }
        return ans;
    }
};
```
