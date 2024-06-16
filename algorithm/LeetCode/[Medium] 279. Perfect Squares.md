279. Perfect Squares

Given a positive integer `n`, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to `n`.

**Example 1:**
```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 2268 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = min([dp[i - j*j] for j in range(1, int(i**.5)+1)]) + 1
        return dp[n]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 6096 ms
Memory Usage: 27.5 MB
```
```python
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        
        @functools.lru_cache(None)
        def dfs(i):
            if i <= 0:
                return 0
            return min(dfs(i - j**2) + 1 for j in range(int(i**.5), 0, -1))
        
        return dfs(n)
```

**Solution 3: (BFS)**
```
Runtime: 1476 ms
Memory Usage: 199 MB
```
```python
class Solution:
    def numSquares(self, n: int) -> int:
        level = 0
        queue = collections.deque()
        queue.append(n)
        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                counter = 1;
                nxt = 1
                while nxt > 0:
                    nxt = current - (counter * counter)
                    if nxt == 0:
                        return level + 1
                    if nxt > 0:
                        queue.append(nxt)
                    counter += 1
            level += 1
        return level
```

**Solution 4: (BFS)**
```
Runtime: 205 ms
Memory Usage: 51.2 MB
```
```c++
class Solution {
public:
    int numSquares(int n) {
        std::queue <int> q;
        if (n <= 1) return 1;
        int steps = 0; // to keep track of the steps we take in subtraction
        q.push(n);  // initial push for the while condition
        while(!q.empty())
        {   
            int s = q.size(); // to make sure we only do 1 layer at a time.
            for(int k=0; k<s; k++) // for each layer of element, we shall compute
            {
                int i = 0;
                int top = q.front(); // taking each element in a layer
                for(int j=1; j*j <= top; j++)
                {   
                    if (top - j*j < 0)
                        break; // no need to go further, as j*j will be larger only.
                    q.push(top -j*j);
                    if (top - j*j == 0)
                        return steps+1;
                }
                q.pop(); // done with the element's further computation, so remove it

            }
            steps++;
            
        }
        return steps;
    }
};
```
**Solution 5: (DP Bottom-Up)**
```
Runtime: 95 ms
Memory: 10.35 MB
```
```c++
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= int(sqrt(i)); j ++) {
                dp[i] = min(dp[i], dp[i-j*j]+1);
            }
        }
        return dp[n];
    }
};
```

