375. Guess Number Higher or Lower II

We are playing the Guess Game. The game is as follows:

I pick a number from **1** to **n**. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay **\$x**. You win the game when you guess the number I picked.

**Example:**
```
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
```
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

# Submissions
---
**Solution 1:**

The recursive statement is as follows:
We have func(i, j), which defines the minimum amount you need to have if you have to guess values that are in between i and j.

```
If i >= j: return 0 
'''
Explanation:
i is the start of range.
j is the end of range.
If start == end, pay 0, because you definitely will have a correct guess with just one value 
within your guess range. 
If start > end, it just simply doesn't make sense, so it's also 0.
'''

Else: return min(k + max(func(i, k-1), func(k+1, j))), for i<=k<j.
```

**Explanation:**
You choose a value k within the range. 
2 scenarios are likely to happen: k is too high OR k is too low
To find the worse case scenario, find the max return value between these 2 scenarios
Then, find the best case scenario out of all your choices of k, and hence the min.
'''
Then comes the issue on how to fill up the dp_arr.
Consider n of a decent size, say n=6
And consider at dp_arr[1][6], which is the value we want to return at the end, we'd need the following coordinates (start, end) at each value of k.

```
At k = 1:    1,0    2,6
At k = 2:    1,1    3,6
At k = 3:    1,2    4,6
At k = 4:    1,3    5,6
At k = 5:    1,4    6,6
```
Then observe, we would need to fill out the dp-arr in the following manner, so as to avoid the "index out of range" error, but also for correctness :)
The order is to be read from left to right.

```
1,2     2,3     3,4     4,5     5,6
1,3     2,4     3,5     4,6
1,4     2,5     3,6
1,5     2,6
1,6
```
Hence, the 2 for-loops (with i and j) in the code below will fill up the dp_arr as follows.
Try drawing out the array and it'd make much more sense!

```
Runtime: 696 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp_arr = []
        
        # initialising 2-d DP-arr
        for i in range(n + 1):
            col = [0] * (n + 1)
            dp_arr.append(col)
        
        # diagonally filling up DP-arr
        for i in range(1, n + 1):
            for j in range(1, n - i + 1):
                res = float('inf')
                start = j
                end = j + i
                for k in range(start, end):
                    res = min(res, k + max(dp_arr[start][k-1], \
                                             dp_arr[k+1][end]))
                dp_arr[start][end] = res
        return dp_arr[1][n]
```