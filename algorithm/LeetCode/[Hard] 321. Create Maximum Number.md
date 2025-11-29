321. Create Maximum Number

Given two arrays of length `m` and `n` with digits `0-9` representing two numbers. Create the maximum number of length `k <= m + n` from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the `k` digits.

**Note:** You should try to optimize your time and space complexity.

**Example 1:**
```
Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
```

**Example 2:**
```
Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
```

**Example 3:**
```
Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
```

# Submissions
---
**Solution 1: (DP Top-Down, Merge Sort)**

* I divide the problem into two smaller problems:
* 1st - get the greatest subsequence with length k
* 2nd - merge two unsorted sequences to get maximum number

```
Runtime: 200 ms
Memory Usage: 16.3 MB
```
```python
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n, m = len(nums1), len(nums2)
        # convert the arrays to tuples to use caching
        A, B = map(tuple, [nums1, nums2])
        
        @lru_cache(None)
        def getGreatest(arr, i):
            '''
            Gets the maximal subsequence of A of length i
            (A is a tuple in order to use caching)
            '''
            if i == len(arr):
                return arr
            X = getGreatest(arr, i + 1)
            removeIdx = len(X) - 1
            for j in range(len(X) - 1):
                if X[j + 1] > X[j]:
                    removeIdx = j
                    break
            return X[:removeIdx] + X[removeIdx + 1:]

        @lru_cache(None)
        def dfs(i, j):
            a1 = getGreatest(A, i)
            a2 = getGreatest(B, j)
            l1, l2 = 0, 0
            res = 0
            while l1 < len(a1) and l2 < len(a2):
                if a1[l1] > a2[l2]:
                    res = res * 10 + a1[l1]
                    l1 += 1
                elif a2[l2] > a1[l1]:
                    res = res * 10 + a2[l2]
                    l2 += 1
                else:
                    # Here we check which is the next different element
                    # in order to pop from the correct array
                    starti, startj, startval = l1, l2, a1[l1]
                    endi, endj = starti, startj
                    while (l1 < len(a1) and l2 < len(a2) and 
                            a1[l1] == a2[l2] and a1[l1] == startval):
                        res = res * 10 + a1[l1]
                        l1, l2 = l1 + 1, l2 + 1
                        # Store the last taken element index in endi/j
                        endi, endj=l1, l2
                    while l1 < len(a1) and l2 < len(a2) and a1[l1] == a2[l2]:
                        l1, l2 = l1 + 1, l2 + 1
                    if (l1 < len(a1) and l2 < len(a2) and a1[l1] > a2[l2] or
                            l2 == len(a2)):
                        l1 = endi
                        l2 = startj
                    elif (l1 < len(a1) and l2 < len(a2) and a2[l2] > a1[l1] or
                            l1 == len(a1)):
                        l1 = starti
                        l2 = endj
            while l1 < len(a1):
                res = res * 10 + a1[l1]
                l1 += 1
            while l2 < len(a2):
                res = res * 10 + a2[l2]
                l2 += 1
            return res

        res = 0
        for i in range(min(k + 1, n + 1)):
            if m >= k - i:
                res = max(res, dfs(i, k - i))
        return [int(x) for x in str(res)]
```

**Solution 2: (Brute Force, mono stack, try all valid splits of digits between nums1 and nums2. O(k * (m + n)))**
```
Runtime: 24 ms, Beats 64.19%
Memory: 27.00 MB, Beats 88.06%
```
```c++
class Solution {
    bool greater(vector<int> &a, int i, vector<int> &b, int j) {
        int m = a.size(), n = b.size();
        while (i < m && j < n) {
            if (a[i] != b[j]) {
                return a[i] > b[j];
            }
            i += 1;
            j += 1;
        }
        return (m - i) > (n - j);//else the one with the more length will be considered as greater 
    }
    vector<int> merge(vector<int> &a, vector<int> &b, int k) {
        vector<int> rst(k);
        int i = 0, j = 0, r = 0;
        while (r < k) {
            if (greater(a, i, b, j)) {
                rst[r++] = a[i++];
            } else {
                rst[r++] = b[j++];
            }
        }
        return rst;
    }
    vector<int> get_max_k(vector<int> &nums, int k) {
        if (k == 0) {
            return {0};
        }
        deque<int> dq; 
        int i, toRemove = nums.size() - k; // how many elements we can drop
        for (auto &x: nums) {
            while (dq.size() && dq.back() < x && toRemove > 0) {
                dq.pop_back();
                toRemove -= 1;
            }
            dq.push_back(x);
        }
        vector<int> rst(k);
        for (i = 0; i < k; i ++) {
            rst[i] = dq.front();
            dq.pop_front();
        }
        return rst;
    }
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        int m = nums1.size(), n = nums2.size(), i;
        vector<int> a, b, c, ans;
        for (i = max(0, k - n); i <= min(k, m); i ++) {
            a = get_max_k(nums1, i); 
            b = get_max_k(nums2, k - i);
            c = merge(a, b, k);
            if (greater(c, 0, ans, 0)) {
                ans = c;
            }
        }
        return ans;
    }
};
```
