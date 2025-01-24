2657. Find the Prefix Common Array of Two Arrays

You are given two **0-indexed** integer permutations `A` and `B` of length `n`.

A **prefix common array** of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return the **prefix common array** of `A` and `B`.

A sequence of n integers is called a **permutation** if it contains all integers from `1` to `n` exactly once.

 

**Example 1:**
```
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
```

**Example 2:**
```
Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
```

**Constraints:**

* `1 <= A.length == B.length == n <= 50`
* `1 <= A[i], B[i] <= n`
* It is guaranteed that `A` and `B` are both a permutation of `n` integers.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 140 ms
Memory: 16.5 MB
```
```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        cnt = [0]*n
        ans = [0]*n
        cur = 0
        for i in range(n):
            cnt[A[i]-1] += 1
            cur += 1 if cnt[A[i]-1] == 2 else 0
            cnt[B[i]-1] += 1
            cur += 1 if cnt[B[i]-1] == 2 else 0
            ans[i] = cur
        return ans
```

**Solution 2: (Counter)**
```
Runtime: 45 ms
Memory: 81.9 MB
```
```c++
class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        vector<int> res, cnt(51);
        for (int i = 0; i < A.size(); ++i)
            res.push_back((++cnt[A[i]] == 2) + (++cnt[B[i]] == 2));
        partial_sum(begin(res), end(res), begin(res));
        return res;
    }
};
```

**Solution 3: (Counter)**
```
Runtime: 0 ms
Memory: 85.74 MB
```
```c++
class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size(), i;
        vector<int> cnt(n+1), ans(n);
        for (i = 0; i < n; i ++) {
            if (i) {
                ans[i] = ans[i-1];
            }
            cnt[A[i]] += 1;
            if (cnt[A[i]] == 2) {
                ans[i] += 1;
            }
            cnt[B[i]] += 1;
            if (cnt[B[i]] == 2) {
                ans[i] += 1;
            }
        }
        return ans;
    }
};
```
