955. Delete Columns to Make Sorted II

We are given an array `A` of `N` lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices `D` such that after deletions, the final array has its elements in **lexicographic** order (`A[0] <= A[1] <= A[2] ... <= A[A.length - 1]`).

Return the minimum possible value of `D.length`.

 

**Example 1:**
```
Input: ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
```

**Example 2:**
```
Input: ["xc","yb","za"]
Output: 0
Explanation: 
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
```

**Example 3:**
```
Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: 
We have to delete every column.
```

**Note:**

* `1 <= A.length <= 100`
* `1 <= A[i].length <= 100`

# Solution
---
## Approach 1: Greedy
**Intuition**

Instead of thinking about column deletions, let's think about which columns we will keep in the final answer.

If the first column isn't lexicographically sorted, we have to delete it.

Otherwise, we will argue that we can keep this first column without consequence. There are two cases:

* If we don't keep the first column, then the final rows of the answer all have to be sorted.

* If we do keep the first column, then the final rows of the answer (minus the first column) only have to be sorted if they share the same first letter (coming from the first column).

    The above statement is hard to digest, so let's use an example:

    Say we have `A = ["axx","ayy","baa","bbb","bcc"]`. When we keep the first column, the final rows are `R = ["xx","yy","aa","bb","cc"]`, and instead of the requirement that these all have to be sorted (ie. `R[0] <= R[1] <= R[2] <= R[3] <= R[4]`), we have a weaker requirement that they only have to be sorted if they share the same first letter of the first column, (ie. `R[0] <= R[1]` and `R[2] <= R[3] <= R[4]`).

Now, we applied this argument only for the first column, but it actually works for every column we could consider taking. If we can't take a column, we have to delete it. Otherwise, we take it because it can only make adding subsequent columns easier.

**Algorithm**

All our effort has led us to a simple algorithmic idea.

Start with no columns kept. For each column, if we could keep it and have a valid answer, keep it - otherwise delete it.

```python
class Solution(object):
    def minDeletionSize(self, A):
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in xrange(len(A) - 1))

        ans = 0
        # cur : all rows we have written
        # For example, with A = ["abc","def","ghi"] we might have
        # cur = ["ab", "de", "gh"].
        cur = [""] * len(A)  

        for col in zip(*A):
            # cur2 : What we potentially can write, including the
            #        newest column 'col'.
            # Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
            # then cur2 = ["abc","def","ghi"].
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(NW^2)$, where $N$ is the length of `A`, and $W$ is the length of `A[i]`.

* Space Complexity: $O(NW)$.

## Approach 2: Greedy with Optimizations
**Explanation**

It is also possible to implement the solution in Approach 1 without using as much time and space.

The key idea is that we will record the "cuts" that each column makes. In our first example from Approach 1 with `A = ["axx","ayy","baa","bbb","bcc"]` (and `R` defined as in Approach 1), the first column cuts our condition from `R[0] <= R[1] <= R[2] <= R[3] <= R[4]` to `R[0] <= R[1]` and `R[2] <= R[3] <= R[4]`. That is, the boundary `"a" == column[1] != column[2] == "b"` has 'cut' one of the conditions for `R` out.

At a high level, our algorithm depends on evaluating whether adding a new column will keep all the rows sorted. By maintaining information about these cuts, we only need to compare characters in the newest column.

```python
class Solution(object):
    def minDeletionSize(self, A):
        # cuts[i] is True : we don't need to check col[i] <= col[i+1]
        cuts = [False] * (len(A) - 1)

        ans = 0
        for col in zip(*A):
            if all(cuts[i] or col[i] <= col[i+1] for i in xrange(len(col) - 1)):
                for i in xrange(len(col) - 1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(NW)$, where $N$ is the length of `A`, and $W$ is the length of `A[i]`.

* Space Complexity: $O(N)$ in additional space complexity. (In Python, zip(*A) uses $O(NW)$ space.)

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 44 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        # cuts[i] is True : we don't need to check col[i] <= col[i+1]
        cuts = [False] * (len(A) - 1)

        ans = 0
        for col in zip(*A):
            if all(cuts[i] or col[i] <= col[i+1] for i in range(len(col) - 1)):
                for i in range(len(col) - 1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                ans += 1
        return ans
```