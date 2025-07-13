264. Ugly Number II

Write a program to find the `n`-th ugly number.

Ugly numbers are **positive numbers** whose prime factors only include `2, 3, 5`. 

**Example:**
```
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```

**Note:**  

* `1` is typically treated as an ugly number.
* `n does not exceed 1690`.

# Submissions
---
**Solution 1: (DP Bottom-Up)**

* DP approach

The idea is to add the numbers to the uglyNumbers list one-by-one by multiplying 2 or 3 or 5. While adding the values, we must make sure that a value lesser than previously added won't be divisible by the other 2 primes. Hence, increment the pointers such that next minimum value can be added to the list.

```
Runtime: 216 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = [1]
        p2 = p3 = p5 = 0
        
        while len(uglyNumbers) < n:
            #If a value lesser than latest was already added, try finding next least value.
            while uglyNumbers[p2]*2 <= uglyNumbers[-1]:
                p2 += 1
            
            while uglyNumbers[p3]*3 <= uglyNumbers[-1]:
                p3 += 1
            
            while uglyNumbers[p5]*5 <= uglyNumbers[-1]:
                p5 += 1
            
            nextVal = min(uglyNumbers[p2]*2, uglyNumbers[p3]*3, uglyNumbers[p5]*5)
            uglyNumbers.append(nextVal)
        
        return uglyNumbers[-1]
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 160 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 1: return 
        k = [1] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            k[i] = min(k[p2] * 2, k[p3] * 3, k[p5] * 5)
            #cannot use elif, becaude case '6' forward two pointer at the same time, '30' forward all pointer
            if k[i] == k[p2] * 2: p2 += 1
            if k[i] == k[p3] * 3: p3 += 1
            if k[i] == k[p5] * 5: p5 += 1
        return k[-1]
```

**Solution 3: (Heap, Set)**
```
Runtime: 176 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        Set = {2,3,5}
        q = [2,3,5]
        heapq.heapify(q)
        cur = 1
        for _ in range(2, n+1):
            cur = heapq.heappop(q)
            for x in [2*cur, 3*cur, 5*cur]:
                if x not in Set:
                    Set.add(x)
                    heapq.heappush(q, x)
        return cur
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 3 ms
Memory Usage: 5.6 MB
```
```c


int nthUglyNumber(int n){
    int dp[n];
    int i = 0, j = 0, k = 0;
    int min, *m;

    dp[0] = 1;
    for (int l = 1; l < n; l++) {
        if (dp[i] * 2 < dp[j] * 3) {
            min = dp[i] * 2;
            m = &i;
        } else {
            min = dp[j] * 3;
            m = &j;
        }

        if (min > dp[k] * 5) {
            min = dp[k] * 5;
            m = &k;
        }
        
        if (dp[l - 1] != min)
            dp[l] = min;
        else
            l--;
        
        (*m)++;
    }

    return dp[n - 1];
}
```

**Solution 5: (Heap)**
```
Runtime: 79 ms, Beats 29.63%
Memory: 33.17 MB, Beats 25.05%
```
```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        if (n == 1) {
            return 1;
        }
        int i = 1;
        priority_queue<long long,vector<long long>,greater<>> pq;
        unordered_set<long long> visited;
        pq.push(2);
        pq.push(3);
        pq.push(5);
        visited.insert(2);
        visited.insert(3);
        visited.insert(5);
        while (i < n-1) {
            auto a = pq.top();
            pq.pop();
            if (!visited.count(a*2)) {
                pq.push(a*2);
                visited.insert(a*2);
            }
            if (!visited.count(a*3)) {
                pq.push(a*3);
                visited.insert(a*3);
            }
            if (!visited.count(a*5)) {
                pq.push(a*5);
                visited.insert(a*5);
            }
            i += 1;
        }
        return pq.top();
    }
};
```

**Solution 6: (DP Bottom-Up, Two Pointes)**

           v
         0 1 2 3 4 5 6 7 8  9
         1 2 3 4 5 6 8 9 10 12
    p2   0 1   2   3 4    5
    p3   0   1     2   3
    p5   0       1        2

```
Runtime: 1 ms, Beats 88.94%
Memory: 11.44 MB, Beats 52.84%
```
```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n);
        dp[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0, i = 1, ans;
        while (i < n) {
            dp[i] = min({dp[p2]*2, dp[p3]*3, dp[p5]*5});
            if (dp[i] == dp[p2]*2) {
                p2 += 1;
            }
            if (dp[i] == dp[p3]*3) {
                p3 += 1;
            }
            if (dp[i] == dp[p5]*5) {
                p5 += 1;
            }
            i += 1;
        }
        return dp[n-1];
    }
};
```
