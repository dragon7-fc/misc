256. Paint House

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a `n x 3` cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with color red; `costs[1][2]` is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

**Note:**

All costs are positive integers.

**Example:**
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 72 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def paint_cost(n, color):
            if (n, color) in self.memo:
                return self.memo[(n, color)]
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            self.memo[(n, color)] = total_cost
            return total_cost

        if costs == []:
            return 0

        self.memo = {}
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
```

**Solution 2: (DP Top-Down)**
```
Runtime: 60 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 60 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for n in reversed(range(len(costs) - 1)):
            # Total cost of painting nth house red.
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            # Total cost of painting nth house green.
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            # Total cost of painting nth house blue.
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        if len(costs) == 0: return 0
        return min(costs[0]) # Return the minimum in the first row.
```

**Solution 4: (DP Bottom-Up 1D)**
```
Runtime: 72 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: return 0

        previous_row = costs[-1]
        for n in reversed(range(len(costs) - 1)):

            current_row = copy.deepcopy(costs[n])
            # Total cost of painting nth house red?
            current_row[0] += min(previous_row[1], previous_row[2])
            # Total cost of painting nth house green?
            current_row[1] += min(previous_row[0], previous_row[2])
            # Total cost of painting nth house blue?
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row

        return min(previous_row)
```

**Solution 5: (DP Bottom-Up 1D)**
```
Runtime: 60 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: return 0

        previous_row = costs[-1]
        for n in reversed(range(len(costs) - 1)):

            # PROBLEMATIC CODE IS HERE
            # This line here is NOT making a copy of the original, it's simply
            # making a reference to it Therefore, any writes into current_row
            # will also be written into "costs". This is not what we wanted!    
            current_row = costs[n]

            # Total cost of painting nth house red?
            current_row[0] += min(previous_row[1], previous_row[2])
            # Total cost of painting nth house green?
            current_row[1] += min(previous_row[0], previous_row[2])
            # Total cost of painting nth house blue?
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row

        return min(previous_row)
```

**Solution 6: (DP Bottom-Up 1D)**

     0     1     2
R   17    16    14
B    2<   16     3<
G   17     5<   19

```
Runtime: 0 ms, Beats 100.00%
Memory: 13.24 MB, Beats 67.88%
```
```c++
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int n = costs.size(), i;
        vector<int> pre, dp(3);
        pre = costs[0];
        for (i = 1; i < n; i ++) {
            dp[0] = costs[i][0] + min(pre[1], pre[2]);
            dp[1] = costs[i][1] + min(pre[0], pre[2]);
            dp[2] = costs[i][2] + min(pre[0], pre[1]);
            swap(pre, dp);
        }
        return *min_element(begin(pre), end(pre));
    }
};
```
