440. K-th Smallest in Lexicographical Order

Given integers `n` and `k`, find the lexicographically k-th smallest integer in the range from 1 to n.

**Note:** `1 ≤ k ≤ n ≤ 10^9`.

**Example:**
```
Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1 
        while k > 1:
            s = 0 
            left = right = curr
            while left <= n:
                s += min(right, n) - left  +1
                left *= 10 
                right = right * 10 + 9
            if k > s:
                curr += 1
                k -= s 
            else:
                curr = curr * 10  
                k -= 1
        return curr
```

**Solution 2: (DFS)**
```
Runtime: 48 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count_nodes(root: int, n: int) -> int:
            count = 0
            next_node = root + 1
            while root <= n:
                count += min(next_node, n + 1) - root
                root *= 10
                next_node *= 10
            return count

        def dfs(root: int, n: int, k: int) -> int:
            if k == 0:
                return root
            count = count_nodes(root, n)
            if count > k:
                return dfs(10 * root, n, k - 1)
            else:
                return dfs(root + 1, n, k - count)
        
        return dfs(1, n, k - 1)
```

**Solution 3: (Divide And Conquer, Prefix Tree, O((long (n))^2))**

n = 130, k = 42
                    vans
           1        2 3 4 5 6 7 8 9      <- 1    1
       /   \   \  \   
    10     11   12 13 ... 19             <- 10
   / \     / \  .. /        \ 
 100 109 110 119  130        199         <- 30
  ^left            n           ^right        

---------------------------------------------------------
n = 13, k = 3

                                 left right   a   k  ans
            1                                 0   3   1
            ^lr                    1    1    +1        
       / /             \
     10 11  12 13 ...  19         10   19    +4
     ^l  ^ans   n      ^r
 100   ...                199     100x 199
                                                  2 10
                   vans         ------------------------
            10    11                          0
             ^lr                  10   10    +1
         /      \                         
       100      109              100x  109            
                                                 -1 +1
                                              
    1---------------> 2  3 ...
    |    a < k: ans += 1
    | 
    v a > k: ans *= 10
   11 12 ...
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.82 MB, Beats 48.71%
```
```c++
class Solution {
public:
    int findKthNumber(int n, int k) {
        int ans = 1;
        long long left, right, a;
        // O(log (n))
        while (k > 1) {
            a = 0;
            left = right = ans;
            // O(log (n))
            while (left <= n) {
                a += min((long long)n, right) - left + 1;
                left *= 10;
                right = right*10 + 9;
            }
            if (a < k) {
                k -= a;
                ans += 1;
            } else {
                ans *= 10;
                k -= 1;
            }
        }
        return ans;
    }
};
```
