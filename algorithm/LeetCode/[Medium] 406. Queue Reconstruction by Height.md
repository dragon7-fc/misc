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

**Solution 2: (Greedy)**
```
Runtime: 245 ms
Memory Usage: 11.9 MB
```
```c++
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](vector<int> &p1, vector<int> &p2){
            if (p1[0] != p2[0]) {
                return p1[0] > p2[0];
            } else {
                return p1[1] <= p2[1];
            }
        });
        vector<vector<int>> ans;
        for (auto &p: people) {
            ans.insert(ans.begin()+p[1], p);
        }
        return ans;
    }
};
```
