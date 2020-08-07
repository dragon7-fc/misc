311. Sparse Matrix Multiplication

Given two sparse matrices **A** and **B**, return the result of **AB**.

You may assume that **A**'s column number is equal to **B**'s row number.

**Example:**
```
Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
```

**Constraints:**

* `1 <= A.length, B.length <= 100`
* `1 <= A[i].length, B[i].length <= 100`
* `-100 <= A[i][j], B[i][j] <= 100`

# Submissions
---
**Solution 1: (Hash Table, value = non-zero element index)**
```
Runtime: 64 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        dict1 = {i:[] for i in range(len(A))}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]!=0:
                    dict1[i].append(j)
                    
        dict2 = {i:[] for i in range(len(B[0]))}
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]!=0:
                    dict2[j].append(i)
        
        for i in range(len(A)):
            for j in range(len(B[0])):
                set1 = set(dict1[i])
                set2 = set(dict2[j])
                mul = list(set1.intersection(set2))                
                for t in mul:
                    ans[i][j]+=A[i][t]*B[t][j]
        return ans
```