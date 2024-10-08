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
Runtime: 103 ms
Memory Usage: 10.7 MB
```
```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        priority_queue<long> minHeap;
        minHeap.push(-1 * 1);
        int nth = 0;
        long val = 1;
        while (!minHeap.empty() && nth < n) {
            val = -1 * minHeap.top();
            minHeap.pop();
            while (!minHeap.empty() && val == (-1 * minHeap.top())) {
                minHeap.pop();
            }
            nth++;
            minHeap.push(-1 * val * 2);
            minHeap.push(-1 * val * 3);
            minHeap.push(-1 * val * 5);
        }
        
        return val;
    }
};
```

**Solution 6: (Min-Heap/Priority Queue)**
```
Runtime: 89 ms
Memory: 34.14 MB
```
```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        // Min-heap to store and retrieve the smallest ugly number
        priority_queue<long, vector<long>, greater<long>> minHeap;
        unordered_set<long> seenNumbers;  // Set to avoid duplicates
        vector<int> primeFactors = {
            2, 3, 5};  // Factors for generating new ugly numbers

        minHeap.push(1);
        seenNumbers.insert(1);

        long currentUgly = 1;
        for (int i = 0; i < n; ++i) {
            currentUgly = minHeap.top();  // Get the smallest number
            minHeap.pop();                // Remove it from the heap

            // Generate and push the next ugly numbers
            for (int prime : primeFactors) {
                long nextUgly = currentUgly * prime;
                if (seenNumbers.find(nextUgly) ==
                    seenNumbers.end()) {  // Avoid duplicates
                    minHeap.push(nextUgly);
                    seenNumbers.insert(nextUgly);
                }
            }
        }

        return static_cast<int>(currentUgly);  // Return the nth ugly number
    }
};
```

**Solution 7: (Dynamic Programming (DP))**
```
Runtime: 0 ms
Memory: 9.73 MB
```
```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> uglyNumbers(n);  // DP array to store ugly numbers
        uglyNumbers[0] = 1;          // The first ugly number is 1

        // Three pointers for the multiples of 2, 3, and 5
        int indexMultipleOf2 = 0, indexMultipleOf3 = 0, indexMultipleOf5 = 0;
        int nextMultipleOf2 = 2, nextMultipleOf3 = 3, nextMultipleOf5 = 5;

        // Generate ugly numbers until we reach the nth one
        for (int i = 1; i < n; i++) {
            // Find the next ugly number as the minimum of the next multiples
            int nextUglyNumber =
                min(nextMultipleOf2, min(nextMultipleOf3, nextMultipleOf5));
            uglyNumbers[i] = nextUglyNumber;

            // Update the corresponding pointer and next multiple
            if (nextUglyNumber == nextMultipleOf2) {
                indexMultipleOf2++;
                nextMultipleOf2 = uglyNumbers[indexMultipleOf2] * 2;
            }
            if (nextUglyNumber == nextMultipleOf3) {
                indexMultipleOf3++;
                nextMultipleOf3 = uglyNumbers[indexMultipleOf3] * 3;
            }
            if (nextUglyNumber == nextMultipleOf5) {
                indexMultipleOf5++;
                nextMultipleOf5 = uglyNumbers[indexMultipleOf5] * 5;
            }
        }

        return uglyNumbers[n - 1];  // Return the nth ugly number
    }
};
```

**Solution 7: (DP Bottom-Up, Two Pointes)**
```
Runtime: 0 ms
Memory: 9.74 MB
```
```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n); 
        dp[0] = 1;

        int p2 = 0, p3 = 0, p5 = 0;

        for (int i = 1; i < n; i++) {
            int cur = min({dp[p2]*2, dp[p3]*3, dp[p5]*5});
            dp[i] = cur;

            if (cur == dp[p2]*2) {
                p2 += 1;
            }
            if (cur == dp[p3]*3) {
                p3 += 1;
            }
            if (cur == dp[p5]*5) {
                p5 += 1;
            }
        }

        return dp[n - 1];
    }
};
```
