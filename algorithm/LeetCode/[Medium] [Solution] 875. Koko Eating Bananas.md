875. Koko Eating Bananas

Koko loves to eat bananas.  There are N `piles` of bananas, the `i`-th pile has `piles[i]` bananas.  The guards have gone and will come back in `H` hours.

Koko can decide her bananas-per-hour eating speed of `K`.  Each hour, she chooses some pile of bananas, and eats `K` bananas from that pile.  If the pile has less than `K` bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer `K` such that she can eat all the bananas within `H` hours.

 

**Example 1:**
```
Input: piles = [3,6,7,11], H = 8
Output: 4
```

**Example 2:**
```
Input: piles = [30,11,23,4,20], H = 5
Output: 30
```

**Example 3:**
```
Input: piles = [30,11,23,4,20], H = 6
Output: 23
```

**Note:**

* `1 <= piles.length <= 10^4`
* `piles.length <= H <= 10^9`
* `1 <= piles[i] <= 10^9`

# Solution
---
## Approach 1: Binary Search
**Intuition**

If Koko can finish eating all the bananas (within H hours) with an eating speed of `K`, she can finish with a larger speed too.

If we let `possible(K)` be `true` if and only if Koko can finish with an eating speed of `K`, then there is some `X` such that `possible(K) = True` if and only if `K >= X`.

For example, with piles = `[3, 6, 7, 11]` and `H = 8`, there is some `X = 4` so that `possible(1) = possible(2) = possible(3) = False`, and `possible(4) = possible(5) = ... = True`.

**Algorithm**

We can binary search on the values of possible(K) to find the first X such that `possible(X)` is `True`: that will be our answer. Our loop invariant will be that `possible(hi)` is always `True`, and `lo` is always less than or equal to the answer. For more information on binary search, please visit [LeetCode Explore - Binary Search](https://leetcode.com/explore/learn/card/binary-search/).

To find the value of `possible(K)`, (ie. whether Koko with an eating speed of `K` can eat all bananas in H hours), we simulate it. For each pile of size `p > 0`, we can deduce that Koko finishes it in `Math.ceil(p / K) = ((p-1) // K) + 1` hours, and we add these times across all piles and compare it to `H`.

```python
class Solution(object):
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p-1) / K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) / 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Complexity Analysis**

* Time Complexity: $O(N \log W)$, where $N$ is the number of piles, and WW is the maximum size of a pile.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution:**
```
Runtime: 460 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p-1) // K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Solution 2: (Binary Search)**
```
Runtime: 36 ms
Memory Usage: 7.1 MB
```
```c
// Can Koko eat all bananas in H hours with eating speed K?
bool possible(int *piles, int pilesSize, int H, int K) {
    int time = 0;
    for (int i = 0; i < pilesSize; i ++)
        time += (piles[i] - 1) / K + 1;
    return time <= H;
}

int minEatingSpeed(int* piles, int pilesSize, int h){
    int lo = 1, hi = pow(10, 9);
    while (lo < hi) {
        int mi = lo + (hi - lo) / 2;
        if (!possible(piles, pilesSize, h, mi))
            lo = mi + 1;
        else
            hi = mi;
    }

    return lo;
}
```

**Solution 3: (Binary Search)**
```
Runtime: 32 ms
Memory Usage: 18.9 MB
```
```c++
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // Initalize the left and right boundaries 
        int left = 1, right = *max_element(piles.begin(), piles.end());

        while (left < right) {
            // Get the middle index between left and right boundary indexes.
            // hourSpent stands for the total hour Koko spends.
            int middle = (left + right) / 2;
            int hourSpent = 0;

            // Iterate over the piles and calculate hourSpent.
            // We increase the hourSpent by ceil(pile / middle).
            for (int pile : piles) {
                hourSpent += pile / middle + (pile % middle != 0);
            }

            // Check if middle is a workable speed, and cut the search space by half.
            if (hourSpent <= h) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }

        // Once the left and right boundaries coincide, we find the target value,
        // that is, the minimum workable eating speed.
        return right;
    }
};
```

**Solution 4: (Binary Search)**
```
Runtime: 54 ms
Memory: 18.8 MB
```
```c++
class Solution {
    int check(int k, vector<int>& piles) {
        int rst = 0;
        for (int p: piles) {
            rst += p/k + (p%k != 0); // rst += ceil((double)p / k);
        }
        return rst;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int lo = 1, hi = *max_element(piles.begin(), piles.end()), mid;
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            if (check(mid, piles) > h) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
};
```
