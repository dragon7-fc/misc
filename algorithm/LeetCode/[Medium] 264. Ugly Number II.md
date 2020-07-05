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
**Solution 1: (DP)**

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

**Solution 2: (Three Pointers)**
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
        for i in range(2, n+1):
            cur = heapq.heappop(q)
            for x in [2*cur, 3*cur, 5*cur]:
                if x not in Set:
                    Set.add(x)
                    heapq.heappush(q, x)
        return cur
```

**Solution 4: (Three Pointers)**
```
Runtime: 4 ms
Memory Usage: 7.6 MB
```
```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        if (n == 1)
            return 1;
        vector<int> uglies(n);
        uglies[0] = 1;
        int l2 = 0, l3 = 0, l5 = 0; //indexes for respective list
        for (int i=1; i<n; i++)
        {
            uglies[i] = min(2 * uglies[l2], min(3 * uglies[l3], 5 * uglies[l5]));
            if (uglies[i] == 2 * uglies[l2])
                l2++;
            if (uglies[i] == 3 * uglies[l3])
                l3++;
            if (uglies[i] == 5 * uglies[l5])
                l5++;
        }
        return uglies[n - 1];
    }
};
```