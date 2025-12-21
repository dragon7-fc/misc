406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers `(h, k)`, where `h` is the height of the person and `k` is the number of people in front of this person who have a height greater than or equal to `h`. Write an algorithm to reconstruct the queue.

**Note:**

* The number of people is less than `1,100`.

 
**Example**
```
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 96 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans
```

**Solution 2: (Greedy, sort by height and insert by rank)**
```
Runtime: 16 ms Beats, 71.51%
Memory: 15.95 MB, Beats 79.65%
```
```c++
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](vector<int> &pa, vector<int> &pb){
            if (pa[0] != pb[0]) {
                return pa[0] > pb[0];
            } else {
                return pa[1] <= pb[1];
            }
        });
        vector<vector<int>> ans;
        for (auto &p: people) {
            ans.insert(ans.begin() + p[1], p);
        }
        return ans;
    }
};
```

**Solution 3: (BIT, sort by height and find first unoccupied position)**

    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    sort      [4,4] [5,2] [5,0] [6,1] [7,1] [7,0]
                0     1     2     3     4     5
    bit         0     0     1     1     3     1    2 
    query       0     0     1     2     3     4    5
    [4,4]       0     0     1     1     3    [0]   1
    query       0     0     1     2     3     3    4
    [5,2]       0     0     1    [0]  > 2     0    1
    query       0     0     1     1     2     2    3     
    [5,0]       0   [-1]  > 0     0   > 1     0    1
    query       0    -1     0     0     1     1    2
    [6,1]       0    -1     0     0    [0]    0    1
    query       0    -1     0     0     0     0    1
    [7,1]       0    -1     0     0     0     0   [0]
    query       0    -1     0     0     0     0    0
    [7,0]       0    -1   [-1]    0  > -1     0    0
    query       0    -1    -1    -1    -1    -1   -1
                                              
    ans       [5,0],[7,0],[5,2],[6,1],[4,4],[7,1]
```
Runtime: 4 ms, Beats 95.73%
Memory: 16.10 MB, Beats 61.80%
```
```c++
class BIT {
public:
    vector<int> dp;
    BIT() {}
    void build(int n) {
        dp.resize(n + 1);
        for (int i = 1; i < n; i ++) {
            update(i, 1);
        }
    }
    void update(int i, int val) {
        int j = i + 1;
        while (j < dp.size()) {
            dp[j] += val;
            j += j & (-j);
        }
    }
    int query(int i) {
        int rst = 0;
        int j = i;
        while (j > 0) {
            rst += dp[j];
            j -= j & (-j);
        }
        return rst;
    }
};

class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        int n = people.size(), left, right, mid;
        sort(people.begin(), people.end(), [](vector<int> &pa, vector<int> &pb){
            if (pa[0] != pb[0]) {
                return pa[0] < pb[0];
            } else {
                return pa[1] > pb[1];
            }
        });
        BIT bit;
        bit.build(n);
        vector<vector<int>> ans(n);
        for (auto &p: people) {
            left = 0, right = n - 1;
            while (left < right) {
                mid = left + (right - left) / 2;
                if (bit.query(mid + 1) < p[1]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            ans[left] = p;
            bit.update(left, -1);
        }
        return ans;
    }
};
```
