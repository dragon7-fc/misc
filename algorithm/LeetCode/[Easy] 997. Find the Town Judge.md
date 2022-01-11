997. Find the Town Judge

In a town, there are `N` people labelled from `1` to `N`.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
1. Everybody (except for the town judge) trusts the town judge.
1. There is exactly one person that satisfies properties 1 and 2.

You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that the person labelled `a` trusts the person labelled `b`.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return `-1`.

 

**Example 1:**
```
Input: N = 2, trust = [[1,2]]
Output: 2
```

**Example 2:**
```
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```

**Example 3:**
```
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

**Example 4:**
```
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```

**Example 5:**
```
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```

**Note:**

* `1 <= N <= 1000`
* `trust.length <= 10000`
* `trust[i]` are all different
* `trust[i][0] != trust[i][1]`
* `1 <= trust[i][0], trust[i][1] <= N`

# Submissions
---
**Solution 1: (In-Degree/Out-Degree, Graph)**
```
Runtime: 788 ms
Memory Usage: 17.3 MB
```
```python
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_edges, out_edges = [0]*N, [0]*N
        for t in trust:
            s, d = t[0]-1, t[1]-1
            in_edges[d] += 1
            out_edges[s] += 1
        for i in range(0, N):
            if in_edges[i] == N-1 and out_edges[i] == 0:
                return i+1

        return -1
```

**Solution 2: (Count)**
```
Runtime: 148 ms
Memory Usage: 16.4 MB
```
```c


int findJudge(int n, int** trust, int trustSize, int* trustColSize){
    int count[1000] = {0};
    for (int i = 0; i < trustSize; i ++) {
        count[trust[i][0]-1] -= 1;
        count[trust[i][1]-1] += 1;
    }
    for (int i = 0; i < n; i ++) {
        if (count[i] == n-1) {
            return i+1;
        }
    }
    return -1;
}
```
