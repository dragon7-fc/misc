985. Sum of Even Numbers After Queries

We have an array `A` of integers, and an array `queries` of queries.

For the `i`-th query `val = queries[i][0]`, `index = queries[i][1]`, we add `val` to `A[index]`.  Then, the answer to the `i`-th query is the sum of the even values of A.

(Here, the given `index = queries[i][1]` is a 0-based index, and each query permanently modifies the array `A`.)

Return the answer to all queries.  Your answer array should have `answer[i]` as the answer to the `i`-th query.

 

**Example 1:**
```
Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
```

**Note:**

1. 1 <= `A.length` <= 10000
1. -10000 <= `A[i]` <= 10000
1. 1 <= `queries.length` <= 10000
1. -10000 <= `queries[i][0]` <= 10000
1. 0 <= `queries[i][1]` < `A.length`

# Solution
---
## Approach 1: Maintain Array Sum
**Intuition and Algorithm**

Let's try to maintain `S`, the sum of the array throughout one query operation.

When acting on an array element `A[index]`, the rest of the values of `A` remain the same. Let's remove `A[index]` from `S` if it is even, then add `A[index] + val`back (if it is even.)

Here are some examples:

* If we have `A = [2,2,2,2,2]`, `S = 10`, and we do `A[0] += 4`: we will update `S -= 2`, then `S += 6`. At the end, we will have `A = [6,2,2,2,2]` and `S = 14`.

* If we have `A = [1,2,2,2,2]`, `S = 8`, and we do `A[0] += 3`: we will skip updating S (since `A[0]` is odd), then `S += 4`. At the end, we will have `A = [4,2,2,2,2]` and `S = 12`.

* If we have `A = [2,2,2,2,2]`, `S = 10` and we do `A[0] += 1`: we will update `S -= 2`, then skip updating `S` (since `A[0] + 1` is odd.) At the end, we will have `A = [3,2,2,2,2]` and `S = 8`.

* If we have `A = [1,2,2,2,2]`, `S = 8` and we do `A[0] += 2`: we will skip updating `S` (since `A[0]` is odd), then skip updating `S` again (since `A[0] + 2` is odd.) At the end, we will have `A = [3,2,2,2,2]` and `S = 8`.

These examples help illustrate that our algorithm actually maintains the value of `S` throughout each query operation.

```python
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ans.append(S)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N+Q)$, where $N$ is the length of `A` and $Q$ is the number of `queries`.

* Space Complexity: $O(Q)$, though we only allocate $O(1)$ additional space.

# Submissions
---
**Solution: (Maintain Array Sum)**
```
Runtime: 608 ms
Memory Usage: 19.7 MB
```
```python
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ans.append(S)
            
        return ans
```

**Solution 1: (Maintain Array Sum)**
```
Runtime: 104 ms
Memory Usage: 45.3 MB
```
```c++
class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int N = nums.size(), cur = 0, val, index;
        vector<int> ans(N);
        for (int num: nums) {
            if (num%2 == 0)
                cur += num;
        }
        for (int i = 0; i < queries.size(); i ++) {
            val = queries[i][0];
            index = queries[i][1];
            if (nums[index]%2 == 0)
                cur -= nums[index];
            nums[index] += val;
            if (nums[index]%2 == 0)
                cur += nums[index];
            ans[i] = cur;
        }
        return ans;
    }
};
```
