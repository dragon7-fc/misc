3296. Minimum Number of Seconds to Make Mountain Height Zero

You are given an integer `mountainHeight` denoting the height of a mountain.

You are also given an integer array `workerTimes` representing the work time of workers in seconds.

The workers work **simultaneously** to **reduce** the height of the mountain. For worker `i`:

* To decrease the mountain's height by `x`, it takes `workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x` seconds. For example:
    * To reduce the height of the mountain by `1`, it takes `workerTimes[i]` seconds.
    * To reduce the height of the mountain by `2`, it takes `workerTimes[i] + workerTimes[i] * 2 seconds`, and so on.

Return an integer representing the **minimum** number of seconds required for the workers to make the height of the mountain 0.

 

**Example 1:**
```
Input: mountainHeight = 4, workerTimes = [2,1,1]

Output: 3

Explanation:

One way the height of the mountain can be reduced to 0 is:

Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2 = 3 seconds.
Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.
```

**Example 2:**
```
Input: mountainHeight = 10, workerTimes = [3,2,2,4]

Output: 12

Explanation:

Worker 0 reduces the height by 2, taking workerTimes[0] + workerTimes[0] * 2 = 9 seconds.
Worker 1 reduces the height by 3, taking workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12 seconds.
Worker 2 reduces the height by 3, taking workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12 seconds.
Worker 3 reduces the height by 2, taking workerTimes[3] + workerTimes[3] * 2 = 12 seconds.
The number of seconds needed is max(9, 12, 12, 12) = 12 seconds.
```

**Example 3:**
```
Input: mountainHeight = 5, workerTimes = [1]

Output: 15

Explanation:

There is only one worker in this example, so the answer is workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15.
```
 

**Constraints:**

* `1 <= mountainHeight <= 10^5`
* `1 <= workerTimes.length <= 10^4`
* `1 <= workerTimes[i] <= 10^6`

# Submissions
---
**Solution 1: (Binary Search, Math, qualdratic formula)**

    qualdratic formula
ax^2 + bx + c == 0, a != 0
-> x = (-b (+/-)sqrt(b^2 - 4ac)) / 2a

```
Runtime: 8 ms, Beats 81.29%
Memory: 29.08 MB, Beats 43.87%
```
```c++
class Solution {
    static constexpr double eps = 1e-7;
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        int maxWorkerTimes =
            *max_element(workerTimes.begin(), workerTimes.end());
        long long l = 1, r = static_cast<long long>(maxWorkerTimes) *
                             mountainHeight * (mountainHeight + 1) / 2;
        long long ans = 0;

        while (l <= r) {
            long long mid = (l + r) / 2;
            long long cnt = 0;
            for (int t : workerTimes) {
                long long work = mid / t;
                // find the largest k such that 1+2+...+k <= work
                long long k = (-1.0 + sqrt(1 + work * 8)) / 2 + eps;
                cnt += k;
            }
            if (cnt >= mountainHeight) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return ans;
    }
};
```

**Solution 2: (Heap)**

    mountainHeight = 4, workerTimes = [2,1,1]


    1 2 3 4
0   ----
1   --====
2   --
-----------------------------------------------------
    mountainHeight = 10, workerTimes = [3,2,2,4]

    1 2 3 4 5 6 7 8 9 10 11 12 13
0   ------============
1   ----========***************
2   ----========***************
3   --------===================
```
Runtime: 203 ms
Memory: 32.70 MB
```
```c++
class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        priority_queue<tuple<long long,int,int>> pq;
        for (int i = 0; i < workerTimes.size(); i ++) {
            pq.push({-workerTimes[i], i, 1});
        }
        long long ans;
        while (mountainHeight) {
            auto [t, i, e] = pq.top();
            ans = -t;
            pq.pop();
            pq.push({t-(long long)workerTimes[i]*(e+1), i, e+1});
            mountainHeight -= 1;
        }
        return ans;
    }
};
```

**Solution 3: (Binary Search)**
```
Runtime: 7 ms, Beats 85.16%
Memory: 28.92 MB, Beats 65.81%
```
```c++
class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        int mx = *max_element(workerTimes.begin(), workerTimes.end());
        long long left = 1, right = (long long)(mx) * mountainHeight * (mountainHeight + 1) / 2, mid;
        long long ans = 0, target, total_reduced, x;
        while (left <= right) {
            mid = left + (right - left) / 2;
            total_reduced = 0;
            for (int t : workerTimes) {
                // t + t*2 + ... * t*x = t * (1 + 2 + ... + x) = t * x * (x + 1) / 2
                // We need to find max x such that t * x * (x + 1) / 2 <= mid
                // x * (x + 1) <= 2 * mid / t
                //                -----------
                //                   target
                target = (2 * mid) / t;

                // Using integer square root as a shortcut to avoid quadratic formula
                // because x^2 is roughly target, so x is roughly sqrt(target)
                x = (int)sqrt(target);

                // Adjust x slightly because sqrt(target) is just an estimate for x(x+1)
                if (x * (x + 1) > target) {
                    x -= 1;
                }

                total_reduced += x;
                if (total_reduced >= mountainHeight) {
                    break;
                }
            }
            if (total_reduced < mountainHeight) {
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
