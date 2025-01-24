1975. Maximum Matrix Sum

You are given an `n x n` integer `matrix`. You can do the following operation any number of times:

* Choose any two adjacent elements of `matrix` and multiply each of them by `-1`.

Two elements are considered **adjacent** if and only if they share a **border**.

Your goal is to **maximize** the summation of the matrix's elements. Return the **maximum** sum of the matrix's elements using the operation mentioned above.

 

**Example 1:**

![1975_pc79-q2ex1.png)](img/1975_pc79-q2ex1.png)
```
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
```

**Example 2:**

![1975_pc79-q2ex2.png](img/1975_pc79-q2ex2.png)

```
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
```

**Constraints:**

* `n == matrix.length == matrix[i].length`
* `2 <= n <= 250`
* `-10^5 <= matrix[i][j] <= 10^5`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 908 ms
Memory Usage: 23.1 MB
```
```python
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        num = [j for i in matrix for j in i] #make all as plain list
        negative = (sum(1 for i in num if i<0))%2 #see the number of negative is odd or even
        num = [abs(i) for i in num] #turn all to positive
        
        if negative: #if odd, only 1 will become negative
            min_ = min(num) #get the minimum 
            return sum(num) - min_*2 #substract it from the sum
        else:
            return sum(num) #return sum
```

**Solution 2: (Math, Case Study, Greedy, Journey From Minus to Plus)**

even: can turn every number to positive
     -1 -2 -3 -4
      ----  -----
      +  +   +  +

odd: can turn every number to positive except smallest
    -1 -2 -3 -4 -5
        ----  ----
    -   +  +  +  +
    -2 -1 -3 -4 -5
        ----  ----
    -----
    +  -  +   +  +

    -2 -3 -1 -4 -5
    -----    -----
    +   +  -  +  +

```
Runtime: 0 ms
Memory: 38.39 MB
```
```c++
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long totalSum = 0;
        int minAbsVal = INT_MAX;
        int negativeCount = 0;

        for (auto& row : matrix) {
            for (int val : row) {
                totalSum += abs(val);
                if (val < 0) {
                    negativeCount++;
                }
                minAbsVal = min(minAbsVal, abs(val));
            }
        }

        // Adjust if the count of negative numbers is odd
        if (negativeCount % 2 != 0) {
            totalSum -= 2 * minAbsVal;
        }

        return totalSum;
    }
};
```
