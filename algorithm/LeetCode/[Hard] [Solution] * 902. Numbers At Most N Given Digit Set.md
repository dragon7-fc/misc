902. Numbers At Most N Given Digit Set

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if `D = {'1','3','5'}`, we may write numbers such as `'13', '551', '1351315'`.

Return the number of positive integers that can be written (using the digits of `D`) that are less than or equal to `N`.

 

**Example 1:**
```
Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
```

**Example 2:**
```
Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.
```

**Note:**

* `D` is a subset of digits `'1'-'9'` in sorted order.
* `1 <= N <= 10^9`

# Solution
---
## Approach 1: Dynamic Programming + Counting
**Intuition**

First, call a positive integer `X` valid if `X <= N` and `X` only consists of digits from `D`. Our goal is to find the number of valid integers.

Say `N` has `K` digits. If we write a valid number with `k` digits (`k < K`), then there are $(D\text{.length})^k$ possible numbers we could write, since all of them will definitely be less than `N`.

Now, say we are to write a valid `K` digit number from left to right. For example, `N = 2345, K = 4`, and `D = '1', '2', ..., '9'`. Let's consider what happens when we write the first digit.

* If the first digit we write is less than the first digit of `N`, then we could write any numbers after, for a total of $(D\text{.length})^{K-1}$ valid numbers from this one-digit prefix. In our example, if we start with `1`, we could write any of the numbers `1111` to `1999` from this prefix.

* If the first digit we write is the same, then we require that the next digit we write is equal to or lower than the next digit in `N`. In our example (with `N = 2345`), if we start with `2`, the next digit we write must be `3` or less.

* We can't write a larger digit, because if we started with eg. `3`, then even a number of `3000` is definitely larger than N.

**Algorithm**

Let dp[i] be the number of ways to write a valid number if N became `N[i], N[i+1], ....` For example, if `N = 2345`, then dp[0] would be the number of valid numbers at most `2345`, dp[1] would be the ones at most `345`, `dp[2]` would be the ones at most `45`, and `dp[3]` would be the ones at most `5`.

Then, by our reasoning above, `dp[i] = (number of d in D with d < S[i]) * ((D.length) ** (K-i-1))`, plus `dp[i+1]` if `S[i]` is in `D`.

```python
class Solution:
    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in xrange(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(D) ** i for i in xrange(1, K))
```

**Complexity Analysis**

* Time Complexity: $O(\log N)$, and assuming $D\text{.length}$ is constant. (We could make this better by pre-calculating the number of `d < S[i]` for all possible digits `S[i]`, but this isn't necessary.)

* Space Complexity: $O(\log N)$, the space used by `S` and `dp`. (Actually, we could store only the last `2` entries of `dp`, but this isn't necessary.)

## Approach 2: Mathematical
**Intuition**

As in Approach #1, call a positive integer `X` valid if `X <= N` and `X` only consists of digits from `D`.

Now let `B = D.length`. There is a bijection between valid integers and so called "bijective-base-B" numbers. For example, if `D = ['1', '3', '5', '7']`, then we could write the numbers `'1', '3', '5', '7', '11', '13', '15', '17', '31', ...` as (bijective-base-B) numbers `'1', '2', '3', '4', '11', '12', '13', '14', '21', ....`

It is clear that both of these sequences are increasing, which means that the first sequence is a contiguous block of valid numbers, followed by invalid numbers.

Our approach is to find the largest valid integer, and convert it into bijective-base-B from which it is easy to find its rank (position in the sequence.) Because of the bijection, the rank of this element must be the number of valid integers.

Continuing our example, if `N = 64`, then the valid numbers are `'1', '3', ..., '55', '57'`, which can be written as bijective-base-4 numbers `'1', '2', ..., '33', '34'.` Converting this last entry `'34'` to decimal, the answer is `16 (3 * 4 + 4)`.

**Algorithm**

Let's convert `N` into the largest possible valid integer `X`, convert `X` to bijective-base-B, then convert that result to a decimal answer. The last two conversions are relatively straightforward, so let's focus on the first part of the task.

Let's try to write `X` one digit at a time. Let's walk through an example where `D = ['2', '4', '6', '8']`. There are some cases:

* If the first digit of `N` is in `D`, we write that digit and continue. For example, if `N = 25123`, then we will write `2` and continue.

* If the first digit of `N` is larger than `min(D)`, then we write the largest possible number from `D` less than that digit, and the rest of the numbers will be big. For example, if `N = 5123`, then we will write `4888` (`4` then `888`).

* If the first digit of `N` is smaller than `min(D)`, then we must "subtract `1`" (in terms of `X`'s bijective-base-B representation), and the rest of the numbers will be big.

For example, if `N = 123`, we will write `88`. If `N = 4123`, we will write `2888`. And if `N = 22123`, we will write `8888`. This is because "subtracting `1`" from `'', '4', '22'` yields `'', '2', '8'` (can't go below `0`).

Actually, in our solution, it is easier to write in bijective-base-B, so instead of writing digits of `D`, we'll write the index of those digits (1-indexed). For example, `X = 24888` will be `A = [1, 2, 4, 4, 4]`. Afterwards, we convert this to decimal.

```python
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        B = len(D) # bijective-base B
        S = str(N)
        K = len(S)
        A = []  #  The largest valid number in bijective-base-B.

        for c in S:
            if c in D:
                A.append(D.index(c) + 1)
            else:
                i = bisect.bisect(D, c)
                A.append(i)
                # i = 1 + (largest index j with c >= D[j], or -1 if impossible)
                if i == 0:
                    # subtract 1
                    for j in xrange(len(A) - 1, 0, -1):
                        if A[j]: break
                        A[j] += B
                        A[j-1] -= 1

                A.extend([B] * (K - len(A)))
                break

        ans = 0
        for x in A:
            ans = ans * B + x
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(\log N)$, and assuming $D\text{.length}$ is constant.

* Space Complexity: $O(\log N)$, the space used by `A`.

# Submissions
---
**Solution 1: (Dynamic Programming + Counting Bottom-up)**
```
Runtime: 32 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in range(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(D) ** i for i in range(1, K))
```

**Solution 2: (Mathematical)**
```
Runtime: 20 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        B = len(D) # bijective-base B
        S = str(N)
        K = len(S)
        A = []  #  The largest valid number in bijective-base-B.

        for c in S:
            if c in D:
                A.append(D.index(c) + 1)
            else:
                i = bisect.bisect(D, c)
                A.append(i)
                # i = 1 + (largest index j with c >= D[j], or -1 if impossible)
                if i == 0:
                    # subtract 1
                    for j in range(len(A) - 1, 0, -1):
                        if A[j]: break
                        A[j] += B
                        A[j-1] -= 1

                A.extend([B] * (K - len(A)))
                break

        ans = 0
        for x in A:
            ans = ans * B + x
        return ans
```

**Solution 3: (DP Top-Down)**

This problem can be devided into two part, one is to count the numbers that is shorter than N in length and less than N, another one to count the numbers that is in the same length with N and less than N.

* For the former one, the answer is easy as all the digits are less than N, so just one line `sum([len(D) ** i for i in range(1, len(str(N)))])`.

* For the latter one it's a little bit complex, I construct a recursion function and compare every digit of the number to the corresponding digit in N, then count the numbers.

```
Runtime: 28 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)

        def dfs(idx):
            ans = 0
            if idx >= K:
                return 1
            for d in digits:
                if d < S[idx]:          
                    # not need to consider the following digits since all is less than N 
                    ans += len(digits) ** (K - idx - 1)
                elif d == S[idx]:  
                    # compare the following digits to N
                    ans += dfs(idx + 1)
                else:      
                    # not need to consider the following digits since all is more than N 
                    break
            return ans

        return dfs(0) + sum([len(digits) ** i for i in range(1, K)])
```

**Solution 4: (DP Top-Down, Digit DP)**

Theory: https://codeforces.com/blog/entry/53960

More of the same approach:  
* 1012. Numbers With Repeated Digits
* 788. Rotated Digits
* 1397. Find All Good Strings
* 233. Number of Digit One
* 357. Count Numbers with Unique Digits

Variable i is the current position in N, isPrefix tells if the current number is the prefix of N, isBigger tells if the current number will be bigger than N when we reach full length. If we are sure that the current number will never be bigger than N we can be sure that result will be the same for all candidate digits. At the end we need to remove 1 for zero which we start from.

```
Runtime: 36 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        D = list(map(int, D))
        N = list(map(int, str(N)))

        @functools.lru_cache(None)
        def dp(i, isPrefix, isBigger):
            if i == len(N):
                return not isBigger
            if not isPrefix and not isBigger:
                return 1 + len(D) * dp(i + 1, False, False)
            return 1 + sum(dp(i + 1, isPrefix and d == N[i], isBigger or (isPrefix and d > N[i])) for d in D)

        return dp(0, True, False) - 1
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory Usage: 6 MB
```
```c


int atMostNGivenDigitSet(char ** digits, int digitsSize, int n){
    char S[11] = {0};
    sprintf(S, "%d", n);
    int K = strlen(S);
    int* dp = calloc(1, (K+1)*sizeof(int));
    dp[K] = 1;
    for (int i = K-1; i >= 0; i--) {
        for (int j = 0; j < digitsSize; j ++) {
            if (digits[j][0] < S[i])
                dp[i] += pow(digitsSize, K-i-1);
            if (digits[j][0] == S[i])
                dp[i] += dp[i+1];
        }
    }
    for (int i = 1; i < K; i ++)
        dp[0] += pow(digitsSize, i);
    return dp[0];
}
```
