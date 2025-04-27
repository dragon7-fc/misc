2145. Count the Hidden Sequences

You are given a **0-indexed** array of `n` integers `differences`, which describes the differences between each pair of **consecutive** integers of a **hidden sequence** of length (`n + 1`). More formally, call the hidden sequence `hidden`, then we have that `differences[i] = hidden[i + 1] - hidden[i]`.

You are further given two integers `lower` and `upper` that describe the inclusive range of values `[lower, upper]` that the hidden sequence can contain.

* For example, given `differences = [1, -3, 4]`, `lower = 1`, `upper = 6`, the hidden sequence is a sequence of length `4` whose elements are in between `1` and `6` (**inclusive**).
    * `[3, 4, 1, 5]` and `[4, 5, 2, 6]` are possible hidden sequences.
    * `[5, 6, 3, 7]` is not possible since it contains an element greater than 6.
    * `[1, 2, 3, 4]` is not possible since the differences are not correct.

Return the number of **possible** hidden sequences there are. If there are no possible sequences, return `0`.

 

**Example 1:**
```
Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2
Explanation: The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.
```

**Example 2:**
```
Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
Output: 4
Explanation: The possible hidden sequences are:
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
Thus, we return 4.
```

**Example 3:**
```
Input: differences = [4,-7,2], lower = 3, upper = 6
Output: 0
Explanation: There are no possible hidden sequences. Thus, we return 0.
```

**Constraints:**

* `n == differences.length`
* `1 <= n <= 10^5`
* `-10^5 <= differences[i] <= 10^5`
* `-10^5 <= lower <= upper <= 10^5`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 1879 ms
Memory Usage: 29 MB
```
```python
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        A = list(accumulate(differences, initial = 0))
        return max(0, (upper - lower) - (max(A) - min(A)) + 1)
```

**Solution 2: (Math)**
```
Runtime: 382 ms
Memory Usage: 106.4 MB
```
```c++
class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long a = 0, ma = 0, mi = 0;
        for (int d: differences) {
            a += d;
            ma = max(ma, a);
            mi = min(mi, a);
        }
        return max(0L, (upper - lower) - (ma - mi) + 1);
    }
};
```

**Solution 3: (Math)**

    differences = [1,-3,4], lower = 1, upper = 6

         1 <- 3
         v
    0 1 -2 2
           ^
           6 -> 4


    differences = [3,-4,5,1,-2], lower = -4, upper = 5
    
         -4 -> -3
         v
    0 3 -1 4 5 3
             ^
             5 -> 0

    differences = [4,-7,2], lower = 3, upper = 6

      6 -> 2
      v
    0 4 -3 -1
         ^
         3 -> 6

```
Runtime: 0 ms, Beats 100.00%
Memory: 112.58 MB, Beats 75.00%
```
```c++
class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long long cur = 0, mx = 0, mn = 0, a, b;
        for (auto d: differences) {
            cur += d;
            mx = max(mx, cur);
            mn = min(mn, cur);
        }
        a = lower - mn;
        b = upper - mx;
        if (a > b) {
            return 0;
        }
        return b - a + 1;
    }
};
```
