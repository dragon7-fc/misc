1029. Two City Scheduling

There are `2N` people a company is planning to interview. The cost of flying the `i`-th person to city A is `costs[i][0]`, and the cost of flying the `i`-th person to city B is `costs[i][1]`.

Return the minimum cost to fly every person to a city such that exactly `N` people arrive in each city.

 

**Example 1:**
```
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
```

**Note:**

* `1 <= costs.length <= 100`
* It is guaranteed that `costs.length` is even.
* `1 <= costs[i][0], costs[i][1] <= 1000`

# Submissions
---
**Solution 1: (Sort, group difference)**
```
Runtime: 40 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([x[0] if i < len(costs)//2 else x[1] for i, x in enumerate(sorted(costs,key=lambda x: x[0]-x[1]))])
```

**Solution 2: (Sort, group difference)**
```
Runtime: 8 ms
Memory Usage: 7.8 MB
```
```c++
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        sort(costs.begin(), costs.end(), [](vector<int>& a, vector<int>& b){
            return a[0]-a[1] < b[0]-b[1];  // fix a[1], and compare a[0]
        });
        int ans = 0;
        int N = costs.size();
        for (int i = 0; i < N; i++) {
            if (i < N/2)
                ans += costs[i][0];
            else
                ans += costs[i][1];
        }    
        return ans;
    }
};
```
