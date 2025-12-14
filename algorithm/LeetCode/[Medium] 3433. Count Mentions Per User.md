3433. Count Mentions Per User

You are given an integer `numberOfUsers` representing the total number of users and an array `events` of size `n x 3`.

Each `events[i]` can be either of the following two types:

**Message Event**: `["MESSAGE", "timestampi", "mentions_stringi"]`
    * This event indicates that a set of users was mentioned in a message at `timestampi`.
    * The `mentions_stringi` string can contain one of the following tokens:
        * `id<number>`: where `<number>` is an integer in range `[0,numberOfUsers - 1]`. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
        * `ALL`: mentions all users.
        * `HERE`: mentions all online users.
**Offline Event**: `["OFFLINE", "timestampi", "idi"]`
    * This event indicates that the user `idi` had become offline at `timestampi` for **60 time units**. The user will automatically be online again at time `timestampi + 60`.

Return an array `mentions` where `mentions[i]` represents the number of mentions the user with id `i` has across all `MESSAGE` events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.

Note that a user can be mentioned multiple times in a **single** message event, and each mention should be counted **separately**.

 

**Example 1:**
```
Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 71, id0 comes back online and "HERE" is mentioned. mentions = [2,2]
```

**Example 2:**
```
Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 12, "ALL" is mentioned. This includes offline users, so both id0 and id1 are mentioned. mentions = [2,2]
```

**Example 3:**
```
Input: numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]

Output: [0,1]

Explanation:

Initially, all users are online.

At timestamp 10, id0 goes offline.

At timestamp 12, "HERE" is mentioned. Because id0 is still offline, they will not be mentioned. mentions = [0,1]
```
 

**Constraints:**

* `1 <= numberOfUsers <= 100`
* `1 <= events.length <= 100`
* `events[i].length == 3`
* `events[i][0]` will be one of `MESSAGE` or `OFFLINE`.
* `1 <= int(events[i][1]) <= 10^5`
* The number of `id<number>` mentions in any `"MESSAGE"` event is between `1` and `100`.
* `0 <= <number> <= numberOfUsers - 1`
* It is guaranteed that the user id referenced in the `OFFLINE` event is **online** at the time the event occurs.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 19 ms, Beats 90.78%
Memory: 42.29 MB, Beats 65.96%
```
```c++
class Solution {
public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        string type, timestamp, content, s;
        vector<bool> online(numberOfUsers, 1);
        queue<pair<int, int>> q;  // timestamp, user
        int t, user;
        vector<int> users, ans(numberOfUsers);
        sort(events.begin(), events.end(), [](auto &ea, auto &eb){
            int ta = stoi(ea[1]);
            int tb = stoi(eb[1]);
            if (ta != tb) {
                return ta < tb;
            } else {
                return ea[0] > eb[0];  // "OFFLINE" > "MESSAGE"
            }
        });
        for (auto &event: events) {
            type = event[0];
            timestamp = event[1];
            content = event[2];
            t = stoi(timestamp);
            while (q.size() && q.front().first <= t) {
                auto [_, user] = q.front();
                q.pop();
                online[user] = true;
            }
            if (type == "MESSAGE") {
                if (content == "ALL") {
                    for (user = 0; user < numberOfUsers; user ++) {
                        ans[user] += 1;
                    }
                } else if (content == "HERE") {
                    for (user = 0; user < numberOfUsers; user ++) {
                        if (online[user]) {
                            ans[user] += 1;
                        }
                    }
                } else {
                    users.clear();
                    stringstream ss(content);
                    while (getline(ss, s, ' ')) {
                        s = s.substr(2);
                        user = stoi(s);
                        users.push_back(user);
                    }
                    for (auto &u: users) {
                        ans[u] += 1;
                    }
                }
            } else {
                user = stoi(content);
                q.push({t + 60, user});
                online[user] = false;
            }
        }
        return ans;
    }
};
```
