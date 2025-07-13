967. Numbers With Same Consecutive Differences

Return all **non-negative** integers of length `N` such that the absolute difference between every two consecutive digits is K.

Note that **every** number in the answer **must** not have leading zeros **except** for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

**Example 1:**

```
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
```

**Example 2:**

```
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

**Note:**

1. `1 <= N <= 9`
1. `0 <= K <= 9`

# Solution
---
## Approach 1: Brute Force
**Intuition**

Let's try to write some number in the answer digit by digit.

For each digit except the first, there are at most `2` choices for that digit. This means that there are at most $9 * 2^8$ possible `9` digit numbers, for example. This is small enough to brute force.

**Algorithm**

An $N$ digit number is just an $N-1$ digit number with a final digit added. If the $N-1$ digit number ends in a digit $d$, then the $N$ digit number will end in $d-K$ or d+Kd+K (provided these are digits in the range $[0,9]$). We store these numbers in a Set structure to avoid duplicates.

Also, we should be careful about leading zeroes -- only 1 digit numbers will start with `0`.

```python
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        ans = {x for x in range(1, 10)}
        for _ in xrange(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)
```

**Complexity Analysis**

* Time Complexity: $O(2^N)$.

* Space Complexity: $O(2^N)$.

# Submissions
---
**Solution: (Brute Force, DP Bottom-Up)**
```
Runtime: 40 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        ans = {x for x in range(1, 10)}
        for _ in range(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)
```

**Solution 2: (DFS)**
```
Runtime: 56 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        ans = set()
        
        def dfs(i, num, path):
            if i == N:
                if path[0] != '0':
                    ans.add(path)
                return
            for nei in [num + K, num - K]:
                if nei >= 0 and nei <= 9:
                    dfs(i+1, nei, path + str(num))
                
        for n in range(1, 10):
            dfs(0, n, '')
        return list(map(int, ans))
```

**Solution 3; (DFS)**
```
Runtime: 48 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        seen = set()
        
        def dfs(path, cur, remain):
            if remain == 0:
                seen.add(path)
                return 
            if cur + K < 10:
                dfs(path*10+cur, cur + K, remain-1)
            if cur - K >=0:
                dfs(path*10+cur, cur - K, remain-1)
        for i in range(1, 10):
            dfs(0, i, N)
            
        return list(seen)
    
    
        if N == 1:
            return list(range(10))
        ans = set()
```

**Solution 4: (DFS)**
```
Runtime: 40 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]

        ans = []
        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10: 
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)
```

**Solution 5:(BFS)**
```
Runtime: 40 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for level in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # using set() to avoid duplicates when K == 0
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10: 
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            # start the next level
            queue = next_queue

        return queue
```

**Solution 6: (Backtracking)**
```
Runtime: 8 ms
Memory Usage: 7 MB
```
```c++
class Solution {
public:
    void helper(vector<int>&v,int n,int k,int idx,string &s){
        if(idx==n-1){
            
            v.push_back(stoi(s));
            return;
        }
       
        for(int i=0;i<=9;i++){
             
            int k1=s.back()-'0';
            //cout<<abs(i-k1)<<endl;
            if(abs(i-k1)==k){
                
                s+=to_string(i);
                idx+=1;
                helper(v,n,k,idx,s);
                idx-=1;
                s.pop_back();
            }
        }
        return;
    }
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int>v;
        string s="";
        for(int i=1;i<=9;i++)
        {
            s+=to_string(i);
            helper(v,n,k,0,s);
            s.pop_back();
        }
        
        return v;
    }
};
```

**Solution 7: (BFS)**
```
Runtime: 3 ms
Memory Usage: 7.1 MB
```
```c++
class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> ans;
        vector<int> q;
        int cur, cn, sz;
        for (int i = 1; i <= 9; i ++) {
            q.push_back(i);
            cn = 1;
            while(!q.empty() && cn < n) {
                sz = q.size();
                for (int j = 0; j < sz; j ++) {
                    cur = q.at(0);
                    q.erase(q.begin());
                    if (cur%10 + k < 10)
                        q.push_back(cur*10 + (cur%10+k));
                    if (k == 0)
                        break;
                    if (cur%10 - k >= 0)
                        q.push_back(cur*10 + (cur%10-k));
                }
                cn += 1;
            }
            for (int j = 0; j < q.size(); j ++)
                ans.push_back(q.at(j));
            q.clear();
        }
        return ans;
    }
};
```

**Solution 8: (BFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 11.45 MB, Beats 39.05%
```
```c++
class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        int a;
        queue<array<int,2>> q;
        vector<int> ans;
        for (a = 1; a <= 9; a ++) {
            q.push({a, 1});
        }
        while (q.size()) {
            auto [num, cn] = q.front();
            q.pop();
            if (cn == n) {
                ans.push_back(num);
                continue;
            }
            if (num%10 + k < 10) {
                a = num*10 + num%10 + k;
                q.push({a, cn + 1});
            }
            if (k == 0) {
                continue;
            }
            if (num%10 - k >= 0) {
                a = num*10 + num%10 - k;
                q.push({a, cn + 1});
            }
        }
        return ans;
    }
};
```
