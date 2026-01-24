444. Sequence Reconstruction

You are given an integer array `nums` of length `n` where `nums` is a permutation of the integers in the range `[1, n]`. You are also given a 2D integer array `sequences` where `sequences[i]` is a subsequence of `nums`.

Check if `nums` is the shortest possible and the only **supersequence**. The shortest **supersequence** is a sequence **with the shortest length** and has all `sequences[i]` as subsequences. There could be multiple valid **supersequences** for the given array sequences.

* For example, for `sequences = [[1,2],[1,3]`], there are two shortest **supersequences**, `[1,2,3]` and `[1,3,2]`.
* While for `sequences = [[1,2],[1,3],[1,2,3]]`, the only shortest **supersequence** possible is `[1,2,3]`. `[1,2,3,4]` is a possible supersequence but not the shortest.

Return `true` if `nums` is the only shortest **supersequence** for `sequences`, or `false` otherwise.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

**Example 1:**
```
Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
Output: false
Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
The sequence [1,2] is a subsequence of both: [1,2,3] and [1,3,2].
The sequence [1,3] is a subsequence of both: [1,2,3] and [1,3,2].
Since nums is not the only shortest supersequence, we return false.
```

**Example 2:**
```
Input: nums = [1,2,3], sequences = [[1,2]]
Output: false
Explanation: The shortest possible supersequence is [1,2].
The sequence [1,2] is a subsequence of it: [1,2].
Since nums is not the shortest supersequence, we return false.
```

**Example 3:**
```
Input: nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The shortest possible supersequence is [1,2,3].
The sequence [1,2] is a subsequence of it: [1,2,3].
The sequence [1,3] is a subsequence of it: [1,2,3].
The sequence [2,3] is a subsequence of it: [1,2,3].
Since nums is the only shortest supersequence, we return true.
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 10^4`
* `nums` is a permutation of all the integers in the range `[1, n]`.
* `1 <= sequences.length <= 10^4`
* `1 <= sequences[i].length <= 10^4`
* `1 <= sum(sequences[i].length) <= 10^5`
* `1 <= sequences[i][j] <= n`
* All the arrays of `sequences` are **unique**.
* `sequences[i]` is a subsequence of `nums`.

# Submissions
---
**Solution 1: (Topological Sort, once one indegree = 0 node)**
```
Runtime: 712 ms
Memory Usage: 19.4 MB
```
```python
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        N = len(nums)
        g = collections.defaultdict(list)
        indeg = [0]*N
        for seq in sequences:
            for u, v in zip(seq[:], seq[1:]):
                g[u-1] += [v-1]
                indeg[v-1] += 1
        q = collections.deque([i for i, v in enumerate(indeg) if v == 0])
        seen = set()
        while (q):
            if len(q) > 1:
                return False
            v = q.popleft()
            seen.add(v)
            for nv in g[v]:
                indeg[nv] -= 1
                if indeg[nv] == 0:
                    q += [nv]
            
        return len(seen) == N
```

**Solution 2: (Topological Sort)**
```
Runtime: 26 ms, Beats 72.24%
Memory: 50.37 MB, Beats 66.92%
```
```c++
class Solution {
public:
    bool sequenceReconstruction(vector<int>& nums, vector<vector<int>>& sequences) {
        int n = nums.size(), m, i, sz, u;
        vector<int> indeg(n + 1);
        vector<vector<int>> g(n + 1);
        for (auto &seq : sequences){
            m = seq.size();
            for (i = 0; i < m - 1; i ++){
                indeg[seq[i + 1]] += 1;
                g[seq[i]].push_back(seq[i + 1]);
            }
        }
        queue<int> q;
        for (i = 1; i <= n; i++){
            if (indeg[i] == 0) {
                q.push(i);
            }
        }
        vector<int> ans;
        while (q.size()) {
            sz = q.size();
            if (sz > 1) {
                return false;
            }
            for (i = 0; i < sz; i ++) {
                u = q.front();
                q.pop();
                ans.push_back(u);
                for (auto &v : g[u]){
                    indeg[v] -= 1;
                    if (indeg[v] == 0){
                        q.push(v);
                    }
                }
            }
        }
        return ans.size() == nums.size();
    }
};
```
