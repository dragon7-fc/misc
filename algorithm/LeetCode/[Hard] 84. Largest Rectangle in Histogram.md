84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![84_histogram.png](img/84_histogram.png)
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![84_histogram_area.png](img/84_histogram_area.png)
The largest rectangle is shown in the shaded area, which has area = 10 unit.

**Example:**
```
Input: [2,1,5,6,2,3]
Output: 10
```

# Submissions
---
**Solution 1: (Stack)**

Maintain a strict increasing stack
```
Runtime: 112 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, max_area = [-1], 0
        for i, h in enumerate(heights + [-1]):
            while stack and stack[-1] >= 0 and h <= heights[stack[-1]]:
                max_area = max(heights[stack.pop()] * (i - stack[-1] - 1), max_area)
            stack.append(i)
        return max_area
```

**Solution 2: (Stack, mono inc stack)**
```
Runtime: 105 ms
Memory: 79.46 MB
```
```c++
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> stk;
        int i, j, ans = INT_MIN;
        for (j = 0; j < n; j ++) {
            while (stk.size() && heights[stk.top()] > heights[j]) {
                i = stk.top();
                stk.pop();
                ans = max(ans, heights[i]*(stk.empty() ? j : j-stk.top()-1));
            }
            stk.push(j);
        }
        while (stk.size()) {
            i = stk.top();
            stk.pop();
            ans = max(ans, heights[i]*(stk.empty() ? j : j-stk.top()-1));
        }
        return ans;
    }
};
```
