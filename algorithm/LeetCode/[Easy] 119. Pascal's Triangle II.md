119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the $k^{th}$ index row of the Pascal's triangle.

Note that the row index starts from 0.

![PascalTriangleAnimated2](img/119_PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example:**
```
Input: 3
Output: [1,3,3,1]
```

**Follow up:**

Could you optimize your algorithm to use only O(k) extra space?

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 32 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = []
        
        for row_number in range(rowIndex+1):
            row = [None for _ in range(row_number+1)]
            row[0], row[-1] = 1,1
            for column_number in range(1,len(row)-1):
                row[column_number] = prev_row[column_number-1] + prev_row[column_number]
            prev_row = row
        return prev_row
```

**Solution 2: (DP, Bottom-Up)**
```
Runtime: 0 ms
Memory Usage: 6.5 MB
```
```c++
class Solution {
public:
    vector<int> getRow(int rowIndex) {
         vector<int> curr, prev = {1};

        for (int i = 1; i <= rowIndex; i++) {
          curr.assign(i + 1, 1);

          for (int j = 1; j < i; j++)
            curr[j] = prev[j - 1] + prev[j];

          prev = move(curr);  // This is O(1)
        }

        return prev;
    }
};
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory: 6.6 MB
```
```c++
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> dp(rowIndex+1);
        for (int i = 0; i <= rowIndex; i ++) {
            for (int j = i; j >= 0; j --) {
                if (j == 0 || j == i) {
                    dp[j] = 1;
                } else {
                    dp[j] += dp[j-1];
                }
            }
        }
        return dp;
    }
};
```
