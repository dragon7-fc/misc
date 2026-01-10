265. Paint House II

There are a row of `n` houses, each house can be painted with one of the `k` colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a `n x k` cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with color 0; `costs[1][2]` is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

**Note:**

All costs are positive integers.

**Example:**
```
Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
```

**Follow up:**

* Could you solve it in O(nk) runtime?

# Submissions
---
**Solution 1: (Memoization)**
```
Runtime: 260 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        # Start by defining n and k to make the following code cleaner.
        n = len(costs)
        if n == 0: return 0 # No houses is a valid test case!
        k = len(costs[0])

        # If you're not familiar with lru_cache, look it up in the docs as it's
        # essential to know about.
        @lru_cache(maxsize=None)
        def memo_solve(house_num, color):

            # Base case.
            if house_num == n - 1:
                return costs[house_num][color]

            # Recursive case.
            cost = math.inf
            for next_color in range(k):
                if next_color == color:
                    continue # Can't paint adjacent houses the same color!
                cost = min(cost, memo_solve(house_num + 1, next_color))
            return costs[house_num][color] + cost

        # Consider all options for painting house 0 and find the minimum.
        cost = math.inf
        for color in range(k):
            cost = min(cost, memo_solve(0, color))
        return cost
```

**Solution 1-1: (DP Top-Down)**
```
Runtime: 264 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N = len(costs)
        if N == 0:
            return 0
        k = len(costs[0])
        
        @functools.lru_cache(None)
        def dp(c, i):
            if i == N-1:
                return costs[i][c]
            rst = float('inf')
            for nc in range(k):
                if nc != c:
                    rst = min(rst, dp(nc, i+1))
            if i >= 0:
                rst += costs[i][c]
            return rst
            
        return dp(-1, -1)
```

**Solution 2: (Dynamic Programming)**
```
Runtime: 216 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        if n == 0: return 0
        k = len(costs[0])

        for house in range(1, n):
            for color in range(k):
                best = math.inf
                for previous_color in range(k):
                    if color == previous_color: continue
                    best = min(best, costs[house - 1][previous_color])
                costs[house][color] += best

        return min(costs[-1])
```

**Solution 3: (Dynamic Programming with O(k) additional Space)**
```
Runtime: 200 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        if n == 0: return 0
        k = len(costs[0])

        previous_row = costs[0]

        for house in range(1, n):
            current_row = [0] * k
            for color in range(k):
                best = math.inf
                for previous_color in range(k):
                    if color == previous_color: continue
                    best = min(best, previous_row[previous_color])
                current_row[color] += costs[house][color] + best
            previous_row = current_row

        return min(previous_row)
```

**Solution 4: (Dynamic programming with Optimized Time)**
```
Runtime: 108 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        if n == 0: return 0
        k = len(costs[0])

        for house in range(1, n):
            # Find the colors with the minimum and second to minimum
            # in the previous row.
            min_color = second_min_color = None
            for color in range(k):
                cost = costs[house - 1][color]
                if min_color is None or cost < costs[house - 1][min_color]:
                    second_min_color = min_color
                    min_color = color
                elif second_min_color is None or cost < costs[house - 1][second_min_color]:
                    second_min_color = color
            # And now update the costs for the current row.
            for color in range(k):
                if color == min_color:
                    costs[house][color] += costs[house - 1][second_min_color]
                else:
                    costs[house][color] += costs[house - 1][min_color]

        #The answer will now be the minimum of the last row.
        return min(costs[-1])
```

**Solution 5: (Dynamic programming with Optimized Time and Space)**
```
Runtime: 104 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        if n == 0: return 0 # This is a valid case.
        k = len(costs[0])

        # Firstly, we need to determine the 2 lowest costs of
        # the first row. We also need to remember the color of
        # the lowest.
        prev_min_cost = prev_second_min_cost = prev_min_color = None
        for color, cost in enumerate(costs[0]):
            if prev_min_cost is None or cost < prev_min_cost:
                prev_second_min_cost = prev_min_cost
                prev_min_color = color
                prev_min_cost = cost
            elif prev_second_min_cost is None or cost < prev_second_min_cost:
                prev_second_min_cost = cost

        # And now, we need to work our way down, keeping track of the minimums.
        for house in range(1, n):
            min_cost = second_min_cost = min_color = None
            for color in range(k):
                # Determime cost for this cell (without writing it into input array.)
                cost = costs[house][color]
                if color == prev_min_color:
                    cost += prev_second_min_cost
                else:
                    cost += prev_min_cost
                # And work out whether or not it is a current minimum.
                if min_cost is None or cost < min_cost:
                    second_min_cost = min_cost
                    min_color = color
                    min_cost = cost
                elif second_min_cost is None or cost < second_min_cost:
                    second_min_cost = cost
            # Transfer currents to be prevs.
            prev_min_cost = min_cost
            prev_min_color = min_color
            prev_second_min_cost = second_min_cost

        return prev_min_cost
```

**Solution 6: (DP Bottom-Up)**

    costs = [[1,5,3],[2,9,4]]

costs    0      1
0        1 <1   2<2
1        5      9
2        3 <2   4<1

```
Runtime: 0 ms, Beats 100.00%
Memory: 14.49 MB, Beats 87.61%
```
```c++
class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int n = costs.size(), k = costs[0].size(), i, j, pj, a;
        if (n == 1) {
            return *min_element(costs[0].begin(), costs[0].end());
        }
        int ans = INT_MAX;
        for (i = 1; i < n; i ++) {
            for (j = 0; j < k; j ++) {
                a = INT_MAX;
                for (int pj = 0; pj < k; pj++) {
                    if (pj == j) {
                        continue;
                    }
                    a = min(a, costs[i - 1][pj]);
                }
                costs[i][j] += a;
                if (i == n-1) {
                    ans = min(ans, costs[i][j]);
                }
            }
        }
        return ans;
    }
};
```
