351. Android Unlock Patterns

Given an Android **3x3** key lock screen and two integers **m** and **n**, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of **m** keys and maximum **n** keys.

 

Rules for a valid pattern:

* Each pattern must connect at least **m** keys and at most **n** keys.
* All the keys must be distinct.
* If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
* The order of keys used matters.
 
![351_android-unlock.png](img/351_android-unlock.png)

**Explanation:**
```
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
```
 

**Example:**
```
Input: m = 1, n = 1
Output: 9
```

# Solution
---
## Summary

After Android launched its "unlock pattern" system to protect our smart phones from unauthorized access, the most common question that comes to one's mind is: How secure exactly are these patterns? The current article gives an answer to this question, as presenting an algorithm, which computes the number of all valid pattern combinations. It is intended for intermediate users and introduces the following ideas: Backtracking, Arrays.

## Approach #1: (Backtracking) [Accepted]
**Algorithm**

The algorithm uses backtracking technique to enumerate all possible $k$ combinations of numbers $[1\dots 9]$ where $m \leq k \leq n$. During the generation of the recursive solution tree, the algorithm cuts all the branches which lead to patterns which doesn't satisfy the rules and counts only the valid patterns. In order to compute a valid pattern, the algorithm performs the following steps:

* Select a digit $i$ which is not used in the pattern till this moment. This is done with the help of a $used$ array which stores all available digits.

* We need to keep last inserted digit $last$. The algorithm makes a check whether one of the following conditions is valid.

    * There is a knight move (as in chess) from $last$ towards $i$ or $last$ and $i$ are adjacent digits in a row, in a column. In this case the sum of both digits should be an odd number.

    * The middle element midmid in the line which connects $i$ and $last$ was previously selected. In case $i$ and $last$ are positioned at both ends of the diagonal, digit midmid = 5 should be previously selected.

    * lastlast and $i$ are adjacent digits in a diagonal

In case one of the conditions above is satisfied, digit $i$ becomes part of partially generated valid pattern and the algorithm continues with the next candidate digit till the pattern is fully generated. Then it counts it. In case none of the conditions are satisfied, the algorithm rejects the current digit $i$, backtracks and continues to search for other valid digits among the unused ones.

```java

public class Solution {

    private boolean used[] = new boolean[9];

    public int numberOfPatterns(int m, int n) {	        
        int res = 0;
        for (int len = m; len <= n; len++) {	            
            res += calcPatterns(-1, len);
            for (int i = 0; i < 9; i++) {	                
                used[i] = false;
            }            
        }
        return res;
    }

    private boolean isValid(int index, int last) {
        if (used[index])
            return false;
        // first digit of the pattern    
        if (last == -1)
            return true;
        // knight moves or adjacent cells (in a row or in a column)	       
        if ((index + last) % 2 == 1)
            return true;
        // indexes are at both end of the diagonals for example 0,0, and 8,8          
        int mid = (index + last)/2;
        if (mid == 4)
            return used[mid];
        // adjacent cells on diagonal  - for example 0,0 and 1,0 or 2,0 and //1,1
        if ((index%3 != last%3) && (index/3 != last/3)) {
            return true;
        }
        // all other cells which are not adjacent
        return used[mid];
    }

    private int calcPatterns(int last, int len) {
        if (len == 0)
            return 1;    
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            if (isValid(i, last)) {
                used[i] = true;
                sum += calcPatterns(i, len - 1);
                used[i] = false;                    
            }
        }
        return sum;
    }
}
```

**Complexity Analysis**

* Time complexity : $O( n!)$, where nn is maximum pattern length

The algorithm computes each pattern once and no element can appear in the pattern twice. The time complexity is proportional to the number of the computed patterns. One upper bound of the number of all possible combinations is :

$\sum_{i=m}^{n} {_9}P_i = \sum_{i=m}^{n} \frac{9!}{(9 - i)!}$
 

* Space complexity : $O(n)$, where nn is maximum pattern length In the worst case the maximum depth of recursion is $n$. Therefore we need $O( n)$ space used by the system recursive stack

## Further Thoughts
The algorithm above could be optimized if we consider the symmetry property of the problem. We notice that the number of valid patterns with first digit 1, 3, 7, 9 are the same. A similar observation is true for patterns which starts with digit 2, 4, 6, 8. Hence we only need to calculate one among each group and multiply by 4.

You can find the optimized solution here.

Analysis written by: @elmirap.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 864 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        # I.e. to move from 1->3, 2 must be chosen earlier.
        reach_conditions = {
            # 4 corners: 1, 3, 7, 9 to reach another corner.
            (1,3): 2, (1,7): 4, (1,9): 5,            
            (3,1): 2, (3,7): 5, (3,9): 6,
            (7,1): 4, (7,3): 5, (7,9): 8,
            (9,1): 5, (9,3): 6, (9,7): 8,
			
			# 2, 4, 6, 8 can reach anywhere except its opposite side, which need to cross 5.
            (4,6): 5, (6,4): 5, (2,8): 5, (8,2): 5
        }

        def backtrack(chosen):
            count = 0

            for i in range(1, 10):
                if i in chosen:
                    continue
                 
                # If not first time (empty chosen), subject to the condition above
                if chosen:
                    move = (chosen[-1], i)
                    if move in reach_conditions and reach_conditions[move] not in chosen:
                        continue
                        
                chosen.append(i)
                
                # Valid pattern
                if len(chosen) >= m and len(chosen) <= n:
                    count += 1
                    
                # Can add more
                if len(chosen) < n:
                    count += backtrack(chosen)
                    
                chosen.pop()
            return count
                
        return backtrack([])
```

**Solution 2: (Backtracking, O(3 * 8^n))**
```
Runtime: 15 ms, Beats 45.26%
Memory: 8.10 MB, Beats 68.95%
```
```c++
class Solution {
    int countPatternsFromNumber(int currentNumber, int currentLength,
                                int minLength, int maxLength,
                                vector<vector<int>>& jump,
                                vector<bool>& visitedNumbers) {
        // Base case: if current pattern length exceeds maxLength, stop
        // exploring
        if (currentLength > maxLength) return 0;

        int validPatterns = 0;
        // If current pattern length is within the valid range, count it
        if (currentLength >= minLength) {
            validPatterns++;
        }

        visitedNumbers[currentNumber] = true;

        // Explore all possible next numbers
        for (int nextNumber = 1; nextNumber <= 9; nextNumber++) {
            int jumpOverNumber = jump[currentNumber][nextNumber];
            // Check if the next number is unvisited and either:
            // 1. There's no number to jump over, or
            // 2. The number to jump over has been visited
            if (!visitedNumbers[nextNumber] &&
                (jumpOverNumber == 0 || visitedNumbers[jumpOverNumber])) {
                validPatterns += countPatternsFromNumber(
                    nextNumber, currentLength + 1, minLength, maxLength, jump,
                    visitedNumbers);
            }
        }

        // Backtrack: unmark the current number before returning
        visitedNumbers[currentNumber] = false;

        return validPatterns;
    }
public:
    int numberOfPatterns(int m, int n) {
        vector<vector<int>> jump(10, vector<int>(10, 0));

        // Initialize the jump over numbers for all valid jumps
        jump[1][3] = jump[3][1] = 2;
        jump[4][6] = jump[6][4] = 5;
        jump[7][9] = jump[9][7] = 8;
        jump[1][7] = jump[7][1] = 4;
        jump[2][8] = jump[8][2] = 5;
        jump[3][9] = jump[9][3] = 6;
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5;

        vector<bool> visitedNumbers(10, false);
        int totalPatterns = 0;

        // Count patterns starting from corner numbers (1, 3, 7, 9) and multiply
        // by 4 due to symmetry
        totalPatterns +=
            countPatternsFromNumber(1, 1, m, n, jump, visitedNumbers) * 4;

        // Count patterns starting from edge numbers (2, 4, 6, 8) and multiply
        // by 4 due to symmetry
        totalPatterns +=
            countPatternsFromNumber(2, 1, m, n, jump, visitedNumbers) * 4;

        // Count patterns starting from the center number (5)
        totalPatterns +=
            countPatternsFromNumber(5, 1, m, n, jump, visitedNumbers);

        return totalPatterns;
    }
};
```

**Solution 3: (DP Top-Down)**
```
Runtime: 0 ms Beats, 100.00%
Memory: 8.50 MB, Beats 51.05%
```
```c++
class Solution {
    int countPatternsFromNumber(int currentNumber, int currentLength,
                                int minLength, int maxLength, int jump[10][10],
                                int visitedNumbers, int dp[10][1 << 10]) {
        // Base case: if current pattern length exceeds maxLength, stop
        // exploring
        if (currentLength > maxLength) return 0;

        if (dp[currentNumber][visitedNumbers] != -1)
            return dp[currentNumber][visitedNumbers];

        int validPatterns = 0;
        // If current pattern length is within the valid range, count it
        if (currentLength >= minLength) {
            validPatterns++;
        }

        visitedNumbers = setBit(visitedNumbers, currentNumber);

        // Explore all possible next numbers
        for (int nextNumber = 1; nextNumber <= 9; nextNumber++) {
            int jumpOverNumber = jump[currentNumber][nextNumber];
            // Check if the next number is unvisited and either:
            // 1. There's no number to jump over, or
            // 2. The number to jump over has been visited
            if (!isSet(visitedNumbers, nextNumber) &&
                (jumpOverNumber == 0 ||
                 isSet(visitedNumbers, jumpOverNumber))) {
                validPatterns += countPatternsFromNumber(
                    nextNumber, currentLength + 1, minLength, maxLength, jump,
                    visitedNumbers, dp);
            }
        }

        // Backtrack: unmark the current number before returning
        visitedNumbers = clearBit(visitedNumbers, currentNumber);

        return dp[currentNumber][visitedNumbers] = validPatterns;
    }

    int setBit(int num, int position) {
        num |= 1 << (position - 1);
        return num;
    }

    int clearBit(int num, int position) {
        num ^= 1 << (position - 1);
        return num;
    }

    bool isSet(int num, int position) {
        int bitAtPosition = (num >> (position - 1)) & 1;
        return bitAtPosition == 1;
    }
public:
    int numberOfPatterns(int m, int n) {
        int jump[10][10] = {0};

        // Initialize the jump over numbers for all valid jumps
        jump[1][3] = jump[3][1] = 2;
        jump[4][6] = jump[6][4] = 5;
        jump[7][9] = jump[9][7] = 8;
        jump[1][7] = jump[7][1] = 4;
        jump[2][8] = jump[8][2] = 5;
        jump[3][9] = jump[9][3] = 6;
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5;

        int visitedNumbers = 0;
        int totalPatterns = 0;
        int dp[10][1 << 10] = {0};
        memset(dp, -1, sizeof(dp));

        // Count patterns starting from corner numbers (1, 3, 7, 9) and multiply
        // by 4 due to symmetry
        totalPatterns +=
            countPatternsFromNumber(1, 1, m, n, jump, visitedNumbers, dp) * 4;

        // Count patterns starting from edge numbers (2, 4, 6, 8) and multiply
        // by 4 due to symmetry
        totalPatterns +=
            countPatternsFromNumber(2, 1, m, n, jump, visitedNumbers, dp) * 4;

        // Count patterns starting from the center number (5)
        totalPatterns +=
            countPatternsFromNumber(5, 1, m, n, jump, visitedNumbers, dp);

        return totalPatterns;
    }
};
```

**Solution 4: (DP Bottom-Up)**

    dp[currentNumber][visitedNumbers]

                          1                           2                           3
dp 256 128 64 32 16 8 4 2 1    256 128 64 32 16 8 4 2 1    256 128 64 32 16 8 4 2 1
0                         1
1                                                   1
2                                                                             1
                          4                           5                           6
dp 256 128 64 32 16 8 4 2 1    256 128 64 32 16 8 4 2 1    256 128 64 32 16 8 4 2 1
3                   1      
4                                             1      
2                                                                      1
                          7                           8                           9
dp 256 128 64 32 16 8 4 2 1    256 128 64 32 16 8 4 2 1    256 128 64 32 16 8 4 2 1
6           1              
7                                    1               
8                                                            1          

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.75 MB, Beats 30.60%
```
```c++
class Solution {
public:
    int numberOfPatterns(int m, int n) {
        int i, j, a, d, mid, cnt, ans;
        vector<vector<int> > dp(9, vector<int>(1 << 9, 0));
        for (i = 0; i < 9; i++) {
            dp[i][1 << i] = 1;
        }
        for (a = 0; a < (1 << 9); a ++) {
            for (i = 0; i < 9; i ++) {
                if (a & (1 << i)) {
                    for (j = 0; j < 9; j ++) {
                        if ((a & (1 << j))) {
                            continue;
                        }
                        d = max(abs(i / 3 - j / 3), abs(i % 3 - j % 3));
                        if (d > 1) {
                            if ((i + j) % 2 == 0) {
                                mid = (i + j) / 2;
                                if (!(a & (1 << mid))) {
                                    continue;
                                }
                            }
                        }
                        dp[j][a | (1 << j)] += dp[i][a];
                    }
                }
            }
        }
        ans = 0;
        for (a = 0; a < (1 << 9); a++) {
            cnt = 0;
            for (i = 0; i < 9; i++) {
                if (a & (1 << i)) {
                    cnt += 1;
                }
            }
            if (cnt >= m && cnt <= n) {
                for (i = 0; i < 9; i ++) {
                    ans += dp[i][a];
                }
            }
        }
        return ans;
    }
};
```
