842. Split Array into Fibonacci Sequence

Given a string `S` of digits, such as `S = "123456579"`, we can split it into a Fibonacci-like sequence `[123, 456, 579]`.

Formally, a Fibonacci-like sequence is a list `F` of non-negative integers such that:

1. `0 <= F[i] <= 2^31 - 1`, (that is, each integer fits a `32`-bit signed integer type);
1. `F.length >= 3`;
1. and `F[i] + F[i+1] = F[i+2]` for all `0 <= i < F.length - 2`.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number `0` itself.

Return any Fibonacci-like sequence split from `S`, or return `[]` if it cannot be done.

**Example 1**:
```
Input: "123456579"
Output: [123,456,579]
```

**Example 2:**
```
Input: "11235813"
Output: [1,1,2,3,5,8,13]
```

**Example 3:**
```
Input: "112358130"
Output: []
Explanation: The task is impossible.
```

**Example 4:**
```
Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
```

**Example 5:**
```
Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
```

**Note:**

1. `1 <= S.length <= 200`
1. `S contains only digits`.

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition**

The first two elements of the array uniquely determine the rest of the sequence.

**Algorithm**

For each of the first two elements, assuming they have no leading zero, let's iterate through the rest of the string. At each stage, we expect a number less than or equal to `2^31 - 1` that starts with the sum of the two previous numbers.

```python
class Solution(object):
    def splitIntoFibonacci(self, S):
        for i in xrange(min(10, len(S))):
            x = S[:i+1]
            if x != '0' and x.startswith('0'): break
            a = int(x)
            for j in xrange(i+1, min(i+10, len(S))):
                y = S[i+1: j+1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `S`, and with the requirement that the values of the answer are $O(1)$ in length.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 20 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(min(10, len(S))):
            x = S[:i+1]
            if x != '0' and x.startswith('0'): break
            a = int(x)
            for j in range(i+1, min(i+10, len(S))):
                y = S[i+1: j+1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []
```

**Solution 2: (Backtracking)**
```
Runtime: 48 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def backtrack(seq, path):
            if self.res:
                return
            if not seq and len(path) > 2:
                self.res = path
                return
            for i in range(len(seq)):
                if seq.startswith('0') and i > 0:
                    break
                if int(seq[:i+1]) > 2**31-1:
                    break
                if len(path) < 2 or (len(path) >= 2 and int(seq[:i+1]) == int(path[-1])+int(path[-2])):
                    path.append(seq[:i+1])
                    backtrack(seq[i+1:], path[:])
                    path.pop()
        if not S:
            return None

        self.res = None
        backtrack(S, [])

        return self.res
```