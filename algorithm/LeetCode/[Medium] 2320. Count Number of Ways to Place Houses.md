2320. Count Number of Ways to Place Houses

There is a street with `n * 2` **plots**, where there are `n` plots on each side of the street. The plots on each side are numbered from `1` to `n`. On each plot, a house can be placed.

Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it **modulo** `10^9 + 7`.

Note that if a house is placed on the `i`th plot on one side of the street, a house can also be placed on the `i`th plot on the other side of the street.

 

**Example 1:**
```
Input: n = 1
Output: 4
Explanation: 
Possible arrangements:
1. All plots are empty.
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.
```

**Example 2:**

!{2320_arrangements.png](img/2320_arrangements.png)
```
Input: n = 2
Output: 9
Explanation: The 9 possible arrangements are shown in the diagram above.
```

**Constraints:**

* `1 <= n <= 10^4`

# Submissions
---
**SOlution 1: (DP Bottom-Up, fibonacci series)**
```
Runtime: 177 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def countHousePlacements(self, n: int) -> int:
        a, b, mod = 1, 1, 10**9 + 7
        for i in range(n):
            a, b = b, (a + b) % mod
        return b * b % mod
```

**Solution 2: (DP Top-Down)**
```
Runtime: 1332 ms
Memory Usage: 415.8 MB
```
```python
class Solution:
    def countHousePlacements(self, n: int) -> int:
        
        @lru_cache(None)
        def rec(i, k):
            
            # i is the index of the house 
            # k is the state of last house, 1 if there was a house on the last index else 0
            
            if i>=n:
                return 1
            
            elif k==0:
                return rec(i+1,1) + rec(i+1,0)
            
            else:
                return rec(i+1,0)
        
        
        
        #l1 are the combinations possible in lane 1, the final answer will be the square 
		#of of l1 as for every combination of l1 there will be "l1" combinations in lane2.
        
        l1 = rec(1,0) + rec(1,1)
        
        
        mod = 10**9 +7
        return pow(l1, 2, mod) #use this when there is mod involved along with power 
```

**SOlution 3: (DP, fibonacci series)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int countHousePlacements(int n) {
        int a = 1, b = 1, c = 2, mod = 1e9 + 7;
        for (int i = 0; i < n; ++i) {
            c = (a + b) % mod;
            a = b;
            b = c;
        }
        return 1L * b * b % mod;
    }
};
```
