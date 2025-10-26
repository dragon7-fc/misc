2048. Next Greater Numerically Balanced Number

An integer `x` is **numerically balanced** if for every digit `d` in the number `x`, there are **exactly** `d` occurrences of that digit in `x`.

Given an integer `n`, return the **smallest numerically balanced** number **strictly greater** than `n`.

 

**Example 1:**
```
Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
```

**Example 2:**
```
Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
```

**Example 3:**
```
Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
```

**Constraints:**

* `0 <= n <= 10^6`

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 187 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def backtracking(i, numLen, curNum, counter):
            if i == numLen:
                isBalanceNumber = True
                for d, freq in counter.items():
                    if freq != 0 and d != freq:
                        isBalanceNumber = False
                if isBalanceNumber:
                    yield curNum
                return

            for d in range(1, numLen+1):
                if counter[d] >= d: continue   # Prune if number of occurrences of `d` is greater than `d`
                if counter[d] + (numLen - i) < d: continue  # Prune if not enough number of occurrences of `d`
                counter[d] += 1
                yield from backtracking(i + 1, numLen, curNum * 10 + d, counter)
                counter[d] -= 1

        for numLen in range(len(str(n)), len(str(n)) + 2):
            for num in backtracking(0, numLen, 0, Counter()):
                if num > n:
                    return num
```

**Solution 2: (Backtracking)**
```
Runtime: 76 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
public:
    int nextBeautifulNumber(int n) {
        if (n == 0) return 1;
        int minNumLen = log10(n) + 1;
        for (int numLen = minNumLen; numLen <= minNumLen + 1; ++numLen) {
            vector<int> all;
            unordered_map<int, int> counter;
            backtracking(0, numLen, 0, counter, all);
            for (int num : all)
                if (num > n) return num;
        }
        return -1;
    }
    void backtracking(int i, int numLen, int curNum, unordered_map<int, int>& counter, vector<int>& out) {
        if (i == numLen) {
            bool isBalanceNumber = true;
            for (auto& [d, freq] : counter)
                if (freq > 0 && d != freq)
                    isBalanceNumber = false;
            if (isBalanceNumber) 
                out.push_back(curNum);
            return;
        }
        for (int d = 1; d <= numLen; ++d) {
            if (counter[d] >= d) continue; // Prune if number of occurrences of `d` is greater than `d`
            if (counter[d] + (numLen - i) < d) continue; // Prune if not enough number of occurrences of `d`
            counter[d] += 1;
            backtracking(i + 1, numLen, curNum * 10 + d, counter, out);
            counter[d] -= 1;
        }
    }
};
```

**Solution 3: (Lookup Table + Binary Search)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.31 MB, Beats 87.44%
```
```c++
class Solution {
    const vector<int> balance{
        1,      22,     122,    212,    221,    333,    1333,   3133,   3313,
        3331,   4444,   14444,  22333,  23233,  23323,  23332,  32233,  32323,
        32332,  33223,  33232,  33322,  41444,  44144,  44414,  44441,  55555,
        122333, 123233, 123323, 123332, 132233, 132323, 132332, 133223, 133232,
        133322, 155555, 212333, 213233, 213323, 213332, 221333, 223133, 223313,
        223331, 224444, 231233, 231323, 231332, 232133, 232313, 232331, 233123,
        233132, 233213, 233231, 233312, 233321, 242444, 244244, 244424, 244442,
        312233, 312323, 312332, 313223, 313232, 313322, 321233, 321323, 321332,
        322133, 322313, 322331, 323123, 323132, 323213, 323231, 323312, 323321,
        331223, 331232, 331322, 332123, 332132, 332213, 332231, 332312, 332321,
        333122, 333212, 333221, 422444, 424244, 424424, 424442, 442244, 442424,
        442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 555551,
        666666, 1224444};
public:
    int nextBeautifulNumber(int n) {
        return *upper_bound(balance.begin(), balance.end(), n);
    }
};
```

**Solution 4: (Enumeration)**
```
Runtime: 59 ms, Beats 63.32%
Memory: 7.90 MB, Beats 97.49%
```
```c++
class Solution {
public:
    int nextBeautifulNumber(int n) {
        int i, a, b;
        bool flag;
        int cnt[10] = {0};
        for (a = n + 1; a <= 1224444; a ++) {
            b = a;
            while (b) {
                cnt[b % 10] += 1;
                b /= 10;
            }
            flag = true;
            for (i = 0; i < 10; i ++) {
                if (cnt[i] && cnt[i] != i) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                return a;
            }
            memset(cnt, 0, sizeof(cnt));
        }
        return -1;
    }
};
```
