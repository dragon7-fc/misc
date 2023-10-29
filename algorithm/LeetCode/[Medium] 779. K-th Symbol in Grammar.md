779. K-th Symbol in Grammar

On the first row, we write a `0`. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

Given row `N` and index `K`, return the `K`-th indexed symbol in row `N`. (The values of `K` are `1`-indexed.) (`1` indexed).

**Examples:**
```
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
```

**Note:**

* `N` will be an integer in the range `[1, 30]`.
* `K` will be an integer in the range `[1, 2^(N-1)]`.

# Submissions
---
**Solution 1: (Recursion, Observation)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        max_len = 2**(N-1)
        mid = max_len // 2
        if K > mid:
            return self.kthGrammar(N-1, K-mid)^1
        else:
            return self.kthGrammar(N-1, K)
```

**Solution 2: (Normal Recursion)**
```
Runtime: 2 ms
Memory: 6.3 MB
```
```c++
class Solution {
    int recursion(int n, int k) {
        // First row will only have one symbol '0'.
        if (n == 1) {
            return 0;
        }

        int totalElements = pow(2, (n - 1));
        int halfElements = totalElements / 2;

        // If the target is present in the right half, we switch to the respective left half symbol.
        if (k > halfElements) {
            return 1 - kthGrammar(n, k - halfElements);
        }

        // Otherwise, we switch to the previous row.
        return recursion(n - 1, k);
    }
public:
    int kthGrammar(int n, int k) {
        return recursion(n, k);
    }
};
```

**Solution 3: (Recursion to Iteration)**
```
Runtime: 2 ms
Memory: 6.4 MB
```
```c++
class Solution {
public:
    int kthGrammar(int n, int k) {
         if (n == 1) {
            return 0;
        }

        // We assume the symbol at the target position is '1'.
        int symbol = 1;

        for (int currRow = n; currRow > 1; --currRow) {
            int totalElements = pow(2, (currRow - 1));
            int halfElements = totalElements / 2;

            // If 'k' lies in the right half symbol, then we flip over to the respective left half symbol.
            if (k > halfElements) {
                // Flip the symbol.
                symbol = 1 - symbol;
                // Change the position after flipping.
                k -= halfElements;
            }
        }

        // We reached the 1st row; if the symbol is not '0', we started with the wrong symbol.
        if (symbol != 0) {
            // Thus, the start symbol was '0' not '1'.
            return 0;
        } 

        // Start symbol was indeed what we started with, a '1'.
        return 1;
    }
};
```
