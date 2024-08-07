1552. Magnetic Force Between Two Balls

In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the `i`th basket is at `position[i]`, Morty has `m` balls and needs to distribute the balls into the baskets such that the **minimum magnetic force** between any two balls is **maximum**.

Rick stated that magnetic force between two different balls at positions `x` and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`. Return the required force.

 

**Example 1:**

![1552_q3v1.jpg](img/1552_q3v1.jpg)
```
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
```

**Example 2:**
```
Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
```

**Constraints:**

* `n == position.length`
* `2 <= n <= 10^5`
* `1 <= position[i] <= 10^9`
* All integers in `position` are **distinct**.
* `2 <= m <= position.length`

# Solution
---
**Solution 1: (Binary Search)**

**Explaination**

We can use binary search to find the answer.

Define function count(d) that counts the number of balls can be placed in to baskets, under the condition that the minimum distance between any two balls is d.

We want to find the maximum d such that count(d) == m.

* If the count(d) > m , we have too many balls placed, so d is too small.
* If the count(d) < m , we don't have enough balls placed, so d is too large.

Since count(d) is monotonically decreasing with respect to d, we can use binary search to find the optimal d.


**Complexity**

* Time complexity: O(Nlog(10^9)) or O(NlogM), where M = max(position) - min(position)
* Space complexity: O(1)


**Similar Questions**

Many other questions can be solved using similar techniques. I listed some of them below:

* 410. Split Array Largest Sum
* 774. Minimize Max Distance to Gas Station
* 875. Koko Eating Bananas
* 1011. Capacity To Ship Packages Within D Days
* 1231. Divide Chocolate

```
Runtime: 1468 ms
Memory Usage: 27.1 MB
```
```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
```

**Solution 2: (Binary Search, upper bound)**
```
Runtime: 109 ms
Memory: 61.58 MB
```
```c++
class Solution {
    // Check if we can place 'm' balls at 'position'
    // with each ball having at least 'x' gap.
    bool canPlaceBalls(int x, vector<int> &position, int m) {
        // Place the first ball at the first position.
        int prevBallPos = position[0];
        int ballsPlaced = 1;

        // Iterate on each 'position' and place a ball there if we can place it.
        for (int i = 1; i < position.size() && ballsPlaced < m; ++i) {
            int currPos = position[i];
            // Check if we can place the ball at the current position.
            if (currPos - prevBallPos >= x) {
                ballsPlaced += 1;
                prevBallPos = currPos;
            }
        }
        // If all 'm' balls are placed, return 'true'.
        return ballsPlaced == m;
    }
public:
    int maxDistance(vector<int>& position, int m) {
        int answer = 0;
        int n = position.size();
        sort(position.begin(), position.end());

        // Initial search space.
        int low = 1;
        int high = ceil(position[n - 1] / (m - 1.0));
        while (low <= high) {
            int mid = low + (high - low) / 2;
            // If we can place all balls having a gap at least 'mid',
            if (canPlaceBalls(mid, position, m)) {
                // then 'mid' can be our answer,
                answer = mid;
                // and discard the left half search space.
                low = mid + 1;
            } else {
                // Discard the right half search space.
                high = mid - 1;
            }
        }
        return answer;
    }
};
```

**Solution 3: (Binary Search, upper bound)**
```
Runtime: 116 ms
Memory: 61.52 MB
```
```c++
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        int n = position.size(), lo = 1, hi = ceil(position[n-1]/(m-1.0)), mid, cnt, pre;
        while (lo < hi) {
            mid = hi - (hi-lo)/2;
            cnt = 1;
            pre = position[0];
            for (int i = 1; i < n; i ++) {
                if (position[i]-pre >= mid) {
                    cnt += 1;
                    pre = position[i];
                }
            }
            if (cnt < m) {
                hi = mid - 1;
            } else {
                lo = mid;
            }
        }
        return lo;
    }
};
```
