2604. Minimum Time to Eat All Grains

There are `n` hens and `m` grains on a line. You are given the initial positions of the hens and the grains in two integer arrays `hens` and `grains` of size `n` and `m` respectively.

Any hen can eat a grain if they are on the same position. The time taken for this is negligible. One hen can also eat multiple grains.

In `1` second, a hen can move right or left by `1` unit. The hens can move simultaneously and independently of each other.

Return the **minimum** time to eat all grains if the hens act optimally.

 

**Example 1:**
```
Input: hens = [3,6,7], grains = [2,4,7,9]
Output: 2
Explanation: 
One of the ways hens eat all grains in 2 seconds is described below:
- The first hen eats the grain at position 2 in 1 second. 
- The second hen eats the grain at position 4 in 2 seconds. 
- The third hen eats the grains at positions 7 and 9 in 2 seconds. 
So, the maximum time needed is 2.
It can be proven that the hens cannot eat all grains before 2 seconds.
```

**Example 2:**
```
Input: hens = [4,6,109,111,213,215], grains = [5,110,214]
Output: 1
Explanation: 
One of the ways hens eat all grains in 1 second is described below:
- The first hen eats the grain at position 5 in 1 second. 
- The fourth hen eats the grain at position 110 in 1 second.
- The sixth hen eats the grain at position 214 in 1 second. 
- The other hens do not move. 
So, the maximum time needed is 1.
```

**Constraints:**

* `1 <= hens.length, grains.length <= 2*10^4`
* `0 <= hens[i], grains[j] <= 10^9`

# Submissions
---
**Solution 1: (Binary Search)**

          h     h h
    0 1 2 3 4 5 6 7 8 9
        <-- <---- ---->
        g   g     g   g

    h   h         h       h       h       h
    4 5 6 ...   109 110 111 ... 213 214 215
    -->             <------         <------
      g               g               g

```
Runtime: 22 ms, Beats 84.62%
Memory: 67.60 MB, Beats 76.92%
```
```c++
class Solution {
    bool check(int mid, vector<int> &hens, vector<int> &grains) {
        int m = hens.size(), n = grains.size(), i, j, j2, j3, r;
        for (i = 0, j = 0; i < m && j < n; i ++) {
            if (grains[j] < hens[i]) {
                if (hens[i] - grains[j] > mid) {
                    return false;
                }
                r = mid - (hens[i] - grains[j]);
                j2 = j;
                j3 = j;
                // left right
                // hens      <- i
                // grains   j -----> j2
                //              r
                while (j2 < n && grains[j2] <= grains[j] + r) {
                    j2++;
                }
                // right left
                // hens          i->
                // grains   j <---- j3
                while (j3 < n && 2 * (grains[j3] - hens[i]) + (hens[i] - grains[j]) <= mid) {
                    j3++;
                }
                j = max(j2, j3);
            } else {
                while (j < n && grains[j] - hens[i] <= mid) {
                    j += 1;
                }
            }
        }
        return j == n;
    }
public:
    int minimumTime(vector<int>& hens, vector<int>& grains) {
        sort(begin(hens), end(hens));
        sort(begin(grains), end(grains));
        int left = 0, right = INT_MAX, mid, ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (!check(mid, hens, grains)) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Binary Search)**
```
Runtime: 24 ms, Beats 84.62%
Memory: 67.62 MB, Beats 46.15%
```
```c++
class Solution {
    bool check(int mid, vector<int> &hens, vector<int> &grains) {
        int m = hens.size(), n = grains.size(), i, j, j2, j3, r;
        for (i = 0, j = 0; i < m && j < n; i ++) {
            if (grains[j] < hens[i]) {
                if (hens[i] - grains[j] > mid) {
                    return false;
                }
                r = mid - 2 * (hens[i] - grains[j]);
                j2 = j;
                j3 = j;
                // left right
                while (j2 < n && grains[j2] <= hens[i]) {
                    j2 += 1;
                }
                while (j2 < n && r > 0 && grains[j2] - hens[i] <= r) {
                    j2 += 1;
                }
                // right left
                while (j3 < n && 2 * (grains[j3] - hens[i]) + (hens[i] - grains[j]) <= mid) {
                    j3 += 1;
                }
                j = max(j2, j3);
            } else {
                while (j < n && grains[j] - hens[i] <= mid) {
                    j += 1;
                }
            }
        }
        return j == n;
    }
public:
    int minimumTime(vector<int>& hens, vector<int>& grains) {
        sort(begin(hens), end(hens));
        sort(begin(grains), end(grains));
        int left = 0, right = INT_MAX, mid, ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (!check(mid, hens, grains)) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
