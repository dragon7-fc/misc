686. Repeated String Match

Given two strings `A` and `B`, find the minimum number of times `A` has to be repeated such that `B` is a substring of it. If no such solution, return `-1`.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

**Note:**

* The length of A and B will be between `1` and `10000`.

# Solution
---
## Approach #1: Ad-Hoc [Accepted]
**Intuition**

The question can be summarized as "What is the smallest `k` for which `B` is a substring of `A * k`?" We can just try every `k`.

**Algorithm**

Imagine we wrote `S = A+A+A+....` If `B` is to be a substring of `S`, we only need to check whether some `S[0:], S[1:], ..., S[len(A) - 1:]` starts with `B`, as `S` is long enough to contain `B`, and `S` has period at most `len(A)`.

Now, suppose `q` is the least number for which `len(B) <= len(A)*q`. We only need to check whether `B` is a substring of `A * q` or `A * (q+1)`. If we try `k < q`, then `B` has larger length than `A * q` and therefore can't be a substring. When `k = q+1`, `A * k` is already big enough to try all positions for `B`; namely, `A[i:i+len(B)] == B` for `i = 0, 1, ..., len(A) - 1`.

```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
```

**Complexity Analysis**

* Time Complexity: $O(N*(N+M))$, where $M, N$ are the lengths of strings `A`, `B`. We create two strings `A * q`, `A * (q+1)` which have length at most O(M+N). When checking whether `B` is a substring of `A`, this check takes naively the product of their lengths.

* Space complexity: As justified above, we created strings that used $O(M+N)$ space

## Approach #2: Rabin-Karp (Rolling Hash) [Accepted]
**Intuition**

As in Approach #1, we've reduced the problem to deciding whether `B` is a substring of some `A * k`. Using the following technique, we can decide whether `B` is a substring in $O(len(A) * k)$ time.

**Algorithm**

For strings $S$, consider each $S[i]$ as some integer ASCII code. Then for some prime $p$, consider the following function modulo some prime modulus $\mathcal{M}$:

$\text{hash}(S) = \sum_{0 \leq i < len(S)} p^i * S[i]$

Notably, $\text{hash}(S[1:] + x) = \frac{(\text{hash}(S) - S[0])}{p} + p^{n-1} x$. This shows we can get the hash of every substring of `A * q` in time complexity linear to it's size. (We will also use the fact that $p^{-1} = p^{\mathcal{M}-2} \mod \mathcal{M}$

However, hashes may collide haphazardly. To be absolutely sure in theory, we should check the answer in the usual way. The expected number of checks we make is in the order of $1 + \frac{s}{\mathcal{M}}$ where $s$ is the number of substrings we computed hashes for (assuming the hashes are equally distributed), which is effectively 1.

```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        def check(index):
            return all(A[(i + index) % len(A)] == x
                       for i, x in enumerate(B))

        q = (len(B) - 1) // len(A) + 1

        p, MOD = 113, 10**9 + 7
        p_inv = pow(p, MOD-2, MOD)
        power = 1

        b_hash = 0
        for x in map(ord, B):
            b_hash += power * x
            b_hash %= MOD
            power = (power * p) % MOD

        a_hash = 0
        power = 1
        for i in xrange(len(B)):
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            power = (power * p) % MOD

        if a_hash == b_hash and check(0): return q

        power = (power * p_inv) % MOD
        for i in xrange(len(B), (q+1) * len(A)):
            a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if a_hash == b_hash and check(i - len(B) + 1):
                return q if i < q * len(A) else q+1

        return -1
```

**Complexity Analysis**

* Time Complexity: $O(M+N)$ (at these sizes), where $M, N$ are the lengths of strings `A`, `B`. As in Approach #1, we justify that `A * (q+1)` will be of length $O(M + N)$, and computing the rolling hashes was linear work. We will also do a linear $O(N)$ final check of our answer $1 + O(M) / \mathcal{M}$ times. In total, this is $O(M+N + N(1 + \frac{M}{\mathcal{M}}))$ work. Since $M \leq 10000 < \mathcal{M} = 10^9 + 7$, we can consider this to be linear behavior.

* Space complexity: $O(1)$. Only integers were stored with additional memory.

# Submissions
---
**Solution: (Ad-Hoc)**
```
Runtime: 104 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
```

**Solution 1: (String)**
```
Runtime: 168 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        int len1 = a.length(), len2 = b.length();
        for(int i=0;i<len1;i++){
            if( b[0] == a[i] ){
                int bIndex = 0, aIndex = i, repeats = 0;
                bool isMatch = true;
                while( bIndex < len2 ){
                    if( b[bIndex] != a[aIndex] ){
                        isMatch = false;
                        break;
                    }
                    aIndex +=1, bIndex += 1;
                    if( aIndex >= len1 && bIndex < len2 ) repeats+=1, aIndex = 0;
                }
                if( isMatch ) return repeats+1;
            }
        }
        return -1;
    }
};
```

**Solution 2: (String)**
```
Runtime: 22 ms
Memory Usage: 6.9 MB
```
```c++
class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        string temp = a;
        int count = 1;
        while(a.length()<b.length())
        {
           a += temp;
           count++;
        }
        if(a.find(b)!=-1)
           return count;
        a += temp;
        if(a.find(b)!=-1)
           return count+1;
        return -1;
    }
};
```
