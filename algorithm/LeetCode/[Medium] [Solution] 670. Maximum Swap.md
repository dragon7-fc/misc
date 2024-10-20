670. Maximum Swap

Given a non-negative integer, you could swap two digits **at most** once to get the maximum valued number. Return the maximum valued number you could get.

**Example 1:**
```
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
```
**Example 2:**
```
Input: 9973
Output: 9973
Explanation: No swap.
```
**Note:**

1. The given number is in the range [0, $10^8$]

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition**

The number only has at most 8 digits, so there are only $\text{C}_{2}^{8}$ = 28 available swaps. We can easily brute force them all.

**Algorithm**

We will store the candidates as lists of length $\text{len(num)}$. For each candidate swap with positions $\text{(i, j)}$, we swap the number and record if the candidate is larger than the current answer, then swap back to restore the original number.

The only detail is possibly to check that we didn't introduce a leading zero. We don't actually need to check it, because our original number doesn't have one.

```python
def maximumSwap(self, num):
    A = list(str(num))
    ans = A[:]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            A[i], A[j] = A[j], A[i]
            if A > ans: ans = A[:]
            A[i], A[j] = A[j], A[i]

    return int("".join(ans))
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the total number of digits in the input number. For each pair of digits, we spend up to $O(N)$ time to compare the final sequences.

* Space Complexity: $O(N)$, the information stored in $\text{A}$.

## Approach #2: Greedy [Accepted]
**Intuition**

At each digit of the input number in order, if there is a larger digit that occurs later, we know that the best swap must occur with the digit we are currently considering.

**Algorithm**

We will compute $\text{last[d] = i}$, the index $\text{i}$ of the last occurrence of digit $\text{d}$ (if it exists).

Afterwards, when scanning the number from left to right, if there is a larger digit in the future, we will swap it with the largest such digit; if there are multiple such digits, we will swap it with the one that occurs the latest.

```python
class Solution(object):
    def maximumSwap(self, num):
        A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in xrange(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the total number of digits in the input number. Every digit is considered at most once.

* Space Complexity: $O(1)$. The additional space used by $\text{last}$ only has up to 10 values.

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 40 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) != None and last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num
```

**Solution 2: (Prefix Sum)**
```
Runtime: 0 ms
Memory: 7.56 MB
```
```c++
class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        int n = s.size();
        vector<int> dp(n);
        dp[n-1] = n-1;
        for (int i = n-2; i >= 0; i --) {
            if (s[i] > s[dp[i+1]]) {
                dp[i] = i;
            } else {
                dp[i] = dp[i+1];
            }
        }
        for (int i = 0; i < s.size(); i ++) {
            if (s[i] < s[dp[i]]) {
                swap(s[i], s[dp[i]]);
                break;
            }
        }
        return stoi(s);
    }
};
```
