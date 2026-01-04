1101. The Earliest Moment When Everyone Become Friends

There are n people in a social group labeled from `0` to `n - 1`. You are given an array `logs` where `logs[i] = [timestampi, xi, yi]` indicates that `xi` and `yi` will be friends at the time `timestampi`.

Friendship is **symmetric**. That means if `a` is friends with `b`, then `b` is friends with `a`. Also, person `a` is acquainted with a person `b` if `a` is friends with `b`, or `a` is a friend of someone acquainted with `b`.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return `-1`.

 

**Example 1:**
```
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friends anything happens.
The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.
```

**Example 2:**
```
Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
```

**Constraints:**

* `2 <= n <= 100`
* `1 <= logs.length <= 10^4`
* `logs[i].length == 3`
* `0 <= timestampi <= 10^9`
* `0 <= xi, yi <= n - 1`
* `xi != yi`
* All the values timestampi are unique.
* All the pairs `(xi, yi)` occur at most one time in the input.

# Submissions
---
**Solution 1: (Union-Find)**
```
Runtime: 180 ms
Memory Usage: 14.7 MB
```
```python
class UnionFind:

    def __init__(self, size):
        self.group = [group_id for group_id in range(size)]
        self.rank = [0] * size

    def find(self, person):
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, a, b):
        """
            return: true if a and b are not connected before
                otherwise, connect a with b and then return false
        """
        group_a = self.find(a)
        group_b = self.find(b)
        is_merged = False
        if group_a == group_b:
            return is_merged

        is_merged = True
        # Merge the lower-rank group into the higher-rank group.
        if self.rank[group_a] > self.rank[group_b]:
            self.group[group_b] = group_a
        elif self.rank[group_a] < self.rank[group_b]:
            self.group[group_a] = group_b
        else:
            self.group[group_a] = group_b
            self.rank[group_b] += 1

        return is_merged

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # First, we need to sort the events in chronological order.
        logs.sort(key = lambda x: x[0])

        uf = UnionFind(n)
        # Initially, we treat each individual as a separate group.
        group_cnt = n

        # We merge the groups along the way.
        for timestamp, friend_a, friend_b in logs:
            if uf.union(friend_a, friend_b):
                group_cnt -= 1

            # The moment when all individuals are connected to each other.
            if group_cnt == 1:
                return timestamp

        # There are still more than one groups left,
        #  i.e. not everyone is connected.
        return -1
```

**Solution 2: (Union-Find)**

    logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
                                                                                             v
    sort   [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6

    0  1  2  3  4  5
p   0  1  2  3  4  5
    1
             4
          4
       5
                   4
k 6 5  2  3  4     1
                   ^
```
Runtime: 0 ms, Beats 100.00%
Memory: 17.02 MB, Beats 83.44%
```
```c++
class Solution {
    vector<int> p;
    int find(int x) {
        if (x != p[x]) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    bool uni(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) {
            return false;
        }
        p[xr] = yr;
        return true;
    }
public:
    int earliestAcq(vector<vector<int>>& logs, int n) {
        int i, t, a, b, k = n;
        p.resize(n);
        for (i = 0; i < n; i ++) {
            p[i] = i;
        }
        sort(logs.begin(), logs.end());
        for (auto &log: logs) {
            t = log[0];
            a = log[1];
            b = log[2];
            if (uni(a, b)) {
                k -= 1;
                if (k == 1) {
                    return t;
                }
            }
        }
        return -1;
    }
};
```
