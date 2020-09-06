1578. Minimum Deletion Cost to Avoid Repeating Letters


Given a string `s` and an array of integers `cost` where `cost[i]` is the cost of deleting the character `i` in `s`.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

**Example 1:**
```
Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
```

**Example 2:**
```
Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
```

**Example 3:**
```
Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
```

**Constraints:**

* `s.length == cost.length`
* `1 <= s.length, cost.length <= 10^5`
* `1 <= cost[i] <= 10^4`
* `s` contains only lowercase English letters.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 1240 ms
Memory Usage: 114.3 MB
```
```python
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        N = len(s)
        
        def dfs(i):
            if i >= N:
                return 0
            j = i+1
            while j < N and s[i] == s[j]:
                j += 1
            if j == i+1:
                return dfs(j)
            else:
                return sum(cost[i:j]) - max(cost[i:j]) + dfs(j)
            
        return dfs(0)
```

**Solution 2: (Greedy)**
```
Runtime: 1172 ms
Memory Usage: 24.1 MB
```
```python
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = prev = 0 # index of previously retained letter 
        for i in range(1, len(s)): 
            if s[prev] != s[i]: prev = i
            else: 
                ans += min(cost[prev], cost[i])
                if cost[prev] < cost[i]: prev = i
        return ans
```