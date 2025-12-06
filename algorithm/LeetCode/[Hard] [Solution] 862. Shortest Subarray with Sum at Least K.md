862. Shortest Subarray with Sum at Least K

Return the **length** of the shortest, non-empty, contiguous subarray of `A` with sum at least `K`.

If there is no non-empty subarray with sum at least `K`, return `-1`.

 

**Example 1:**
```
Input: A = [1], K = 1
Output: 1
```

**Example 2:**
```
Input: A = [1,2], K = 4
Output: -1
```

**Example 3:**
```
Input: A = [2,-1,2], K = 3
Output: 3
```

**Note:**

* `1 <= A.length <= 50000`
* `-10 ^ 5 <= A[i] <= 10 ^ 5`
* `1 <= K <= 10 ^ 9`

# Solution
---
## Approach 1: Sliding Window
**Intuition**

We can rephrase this as a problem about the prefix sums of `A`. Let `P[i] = A[0] + A[1] + ... + A[i-1]`. We want the smallest `y-x` such that `y > x` and `P[y] - P[x] >= K`.

Motivated by that equation, let `opt(y)` be the largest `x` such that `P[x] <= P[y] - K`. We need two key observations:

* If `x1 < x2` and `P[x2] <= P[x1]`, then `opt(y)` can never be `x1`, as if `P[x1] <= P[y] - K`, then `P[x2] <= P[x1] <= P[y] - K` but `y - x2` is smaller. This implies that our candidates `x` for `opt(y)` will have increasing values of `P[x]`.

* If `opt(y1) = x`, then we do not need to consider this `x` again. For if we find some `y2 > y1` with `opt(y2) = x`, then it represents an answer of `y2 - x` which is worse (larger) than `y1 - x`.

**Algorithm**

Maintain a "monoqueue" of indices of `P`: a deque of indices `x_0, x_1, ...` such that `P[x_0], P[x_1], ...` is increasing.

When adding a new index `y`, we'll pop `x_i` from the end of the deque so that `P[x_0], P[x_1], ..., P[y]` will be increasing.

If `P[y] >= P[x_0] + K`, then (as previously described), we don't need to consider this `x_0` again, and we can pop it from the front of the deque.

```python
class Solution(object):
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 868 ms
Memory Usage: 19.5 MB
```
```python
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1
```

**Solution 2: (Heap)**
```
Runtime: 99 ms
Memory: 119.78 MB
```
```c++
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size(), ans = INT_MAX;
        long long cur = 0;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        for (int i = 0; i < n; i++) {
            cur += nums[i];
            if (cur >= k) {
                ans = min(ans, i + 1);
            }
            while (!pq.empty() && cur - pq.top().first >= k) {
                ans = min(ans, i - pq.top().second);
                pq.pop();
            }
            pq.emplace(cur, i);
        }

        return ans == INT_MAX ? -1 : ans;
    }
};
```

**Solution 4: (Binary Search, mono stack)**
```
Runtime: 46 ms
Memory: 110.29 MB
```
```c++
class Solution {
    int check(const vector<pair<long long, int>>& nums, long long target) {
        int left = 0, right = nums.size() - 1, mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (nums[mid].first <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size(), i, j, ans = INT_MAX;;
        vector<pair<long long, int>> stk;
        stk.emplace_back(0LL, -1);
        long long cur = 0;
        for (j = 0; j < n; j++) {
            cur += nums[j];
            while (!stk.empty() && cur <= stk.back().first) {
                stk.pop_back();
            }
            stk.emplace_back(cur, j);
            i = check(stk, cur - k);
            if (i-1 != -1) {
                ans = min(ans, j - stk[i-1].second);
            }
        }

        return ans == INT_MAX ? -1 : ans;
    }
};
```

**Solution 5: (Deque, mono stack, prefix sum)**

             v
    2 -1  2
pre 0  2  1  3
dq  0  01 02 023
ans          3


```
Runtime: 30 ms, Beats 57.36%
Memory: 109.18 MB, Beats 60.78%
``
```c++
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size(), i, ans = INT_MAX;
        vector<long long> pre(n+1);
        deque<int> dq;
        for (i = 0; i < n ; i ++) {
            pre[i+1] = pre[i] + nums[i];
        }
        // greedy over pre
        for (i = 0; i <= n; i ++) {
            while (dq.size() && pre[i] - pre[dq[0]] >= k) {
                ans = min(ans, i - dq[0]);
                dq.pop_front();
            }
            while (dq.size() && pre[i] <= pre[dq.back()]) {
                dq.pop_back();
            }
            dq.push_back(i);
        }
        return ans != INT_MAX ? ans : -1;
    }
};
```
