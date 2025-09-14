1733. Minimum Number of People to Teach

On a social network consisting of `m` users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer `n`, an array `languages`, and an array `friendships` where:

* There are `n` languages numbered 1 through n,
* `languages[i]` is the set of languages the `i`th user knows, and
* `friendships[i] = [ui, vi]` denotes a friendship between the users `ui` and `vi`.

You can choose **one** language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if `x` is a friend of `y` and `y` is a friend of `z`, this doesn't guarantee that `x` is a friend of `z`.
 

**Example 1:**
```
Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
```

**Example 2:**
```
Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
```

**Constraints:**

* `2 <= n <= 500`
* `languages.length == m`
* `1 <= m <= 500`
* `1 <= languages[i].length <= n`
* `1 <= languages[i][j] <= n`
* `1 <= ui < vi <= languages.length`
* `1 <= friendships.length <= 500`
* All tuples `(ui, vi)` are unique
* `languages[i]` contains only unique values

# Submissions
---
**Solution 1: (brute Force, Set)**
```
Runtime: 8364 ms
Memory Usage: 27.6 MB
```
```python
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        A = list(map(set, languages))
        res = m = len(friendships)
        for k in range(1, n + 1):
            teach = set()
            for i, j in friendships:
                if A[i - 1] & A[j - 1]: continue
                if k not in A[i - 1]: teach.add(i)
                if k not in A[j - 1]: teach.add(j)
            res = min(res, len(teach))
        return res
```

**Solution 2: (Brute Force)**
```
Runtime: 36 ms, Beats 81.18%
Memory: 63.52 MB, Beats 100.00%
```
```c++
class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        unordered_set<int> usersToTeach;

        // Step 1: Identify users who can't communicate
        for (auto& friendship : friendships) {
            int user1 = friendship[0] - 1; // Convert to 0-based index
            int user2 = friendship[1] - 1;
            bool canCommunicate = false;

            for (int lang1 : languages[user1]) {
                for (int lang2 : languages[user2]) {
                    if (lang1 == lang2) {
                        canCommunicate = true;
                        break;
                    }
                }
                if (canCommunicate) break;
            }

            if (!canCommunicate) {
                usersToTeach.insert(user1);
                usersToTeach.insert(user2);
            }
        }

        // Step 2: Try teaching each language
        int minUsersToTeach = languages.size() + 1;

        for (int language = 1; language <= n; language++) {
            int count = 0;

            for (int user : usersToTeach) {
                bool knowsLanguage = false;
                for (int lang : languages[user]) {
                    if (lang == language) {
                        knowsLanguage = true;
                        break;
                    }
                }
                if (!knowsLanguage) count++;
            }

            minUsersToTeach = min(minUsersToTeach, count);
        }

        return minUsersToTeach;
    }
};
```
