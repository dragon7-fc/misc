313. Super Ugly Number

Write a program to find the n^th super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list `primes` of size `k`.

**Example:**
```
Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
```

**Note:**

* `1` is a super ugly number for any given primes.
* The given numbers in primes are in ascending order.
* `0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000`.
* The n^th super ugly number is guaranteed to fit in a 32-bit signed integer.

# Submissions
---
**Solution 1: (DP)**
```
Runtime: 1096 ms
Memory Usage: 16.5 MB
```
```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglyNumbers = [1]
        N_p = len(primes)
        prime_index = [0]*N_p

        while len(uglyNumbers) < n:
            #If a value lesser than latest was already added, try finding next least value.
            for i in range(N_p):
                while uglyNumbers[prime_index[i]]*primes[i] <= uglyNumbers[-1]:
                    prime_index[i] += 1

            nextVal = min(uglyNumbers[prime_index[i]]*primes[i] for i in range(N_p))
            uglyNumbers.append(nextVal)

        return uglyNumbers[-1]
```

**Solution 2: (Heap, Set)**

Somehow I find the available solutions are not that straight forward to understand.
This one is using heap. What it does is:

* Maintain a heap for all generated ugly numbers.
* Once at a time, pop the minimal number from the heap. (for n times)
* For each new generated number, we push it into the heap if it has never show up. We use a set to make sure that the number in the heap is not duplicated.

This one is slow by the way. But it is easier to understand.
O(N log(N*k))

```
Runtime: 1052 ms
Memory Usage: 109.9 MB
```
```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n==1: return 1
        hp = [1] +  [_ for _ in primes]
        used = set(hp)
        heapq.heapify(hp)
        num = 1
        while n:
            n -= 1
            num = heapq.heappop(hp)
            for p in primes:
                if num*p not in used:
                    heapq.heappush(hp, num*p)
                    used.add(num*p)
        return num
```

**Solution 3: (DP)**
```
Runtime: 1916 ms
Memory Usage: 18.6 MB
```
```c++
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<int> uglyNumbers({1});
        int N_p = primes.size(), nextVal;
        vector<int> prime_index(N_p);
        while (uglyNumbers.size() < n) {
            //If a value lesser than latest was already added, try finding next least value.
            for (int i = 0; i < N_p; i++)
                while (uglyNumbers[prime_index[i]]*primes[i] <= uglyNumbers.back())
                    prime_index[i] += 1;

            int nextVal = INT_MAX;
            for (int i = 0; i < N_p; i ++)
                nextVal = min(nextVal, uglyNumbers[prime_index[i]]*primes[i]);
            uglyNumbers.push_back(nextVal);
        }                     
        return uglyNumbers.back();
    }
};
```
