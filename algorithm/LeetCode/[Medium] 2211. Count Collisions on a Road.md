2211. Count Collisions on a Road

There are `n` cars on an infinitely long road. The cars are numbered from `0` to `n - 1` from left to right and each car is present at a **unique** point.

You are given a **0-indexed** string `directions` of length `n`. `directions[i]` can be either `'L'`, `'R'`, or `'S'` denoting whether the `i`th car is moving towards the **left**, towards the **right**, or **staying** at its current point respectively. Each moving car has the **same speed**.

The number of collisions can be calculated as follows:

* When two cars moving in opposite directions collide with each other, the number of collisions increases by `2`.
* When a moving car collides with a stationary car, the number of collisions increases by `1`.

After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the **total number of collisions** that will happen on the road.

 

**Example 1:**
```
Input: directions = "RLRSLL"
Output: 5
Explanation:
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5. 
```

**Example 2:**
```
Input: directions = "LLRR"
Output: 0
Explanation:
No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.
```

**Constraints:**

* `1 <= directions.length <= 10^5`
* `directions[i]` is either `'L'`, `'R'`, or `'S'`.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 128 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def countCollisions(self, directions: str) -> int:
        return sum(d!='S' for d in directions.lstrip('L').rstrip('R'))
```

**Solution 2: (Greedy)**
```
Runtime: 66 ms
Memory Usage: 16.2 MB
```
```c++
class Solution {
public:
    int countCollisions(string directions) {
        int res(0), n(size(directions)), i(0), carsFromRight(0);
        
        while (i < n and directions[i] == 'L') i++; // skipping all the cars going to left from beginning as they will never collide
        
        for ( ; i<n; i++) {
            if (directions[i] == 'R')  carsFromRight++;
            else {
                // if dir[i] == 'S' then there will be carsFromRight number of collission
                // if dir[i] == 'L' then there will be carsFromRight+1 number of collision (one collision for the rightmost cars and carsFromRight collision for the cars coming from left)
                res += (directions[i] == 'S') ? carsFromRight : carsFromRight+1;
                carsFromRight = 0;
            }
        }
        return res;
    }
};
```

**Solution 3: (left and right)**
```
Runtime: 28 ms, Beats 41.45%
Memory: 19.13 MB, Beats 84.64%
```
```c++
class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.length(), i, ans = 0;
        for (i = 0; i < n - 1; i ++) {
            if (directions[i] == 'R' && directions[i + 1] == 'S') {
                directions[i] = 'S';
                ans += 1;
            } else if (directions[i] == 'R' && directions[i + 1] == 'L') {
                directions[i] = 'S';
                directions[i + 1] = 'S';
                ans += 2;
            } else if (directions[i] == 'S' && directions[i + 1] == 'L') {
                directions[i + 1] = 'S';
                ans += 1;
            }
        }
        for (i = n - 2; i >= 0; i --) {
            if (directions[i] == 'R' && directions[i + 1] == 'S') {
                directions[i] = 'S';
                ans += 1;
            } else if (directions[i] == 'R' && directions[i + 1] == 'L') {
                directions[i] = 'S';
                directions[i + 1] = 'S';
                ans += 2;
            } else if (directions[i] == 'S' && directions[i + 1] == 'L') {
                directions[i + 1] = 'S';
                ans += 1;
            }
        }
        return ans;
    }
};
```

**Solution 4: (Counting)**

    LLLRLRRSLLRRR
       1234 56

```
Runtime: 12 ms, Beats 62.32%
Memory: 19.31 MB, Beats 50.72%
```
```c++
class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.size();
        int l = 0, r = n - 1;

        while (l < n && directions[l] == 'L') {
            l++;
        }

        while (r >= l && directions[r] == 'R') {
            r--;
        }

        int res = 0;
        for (int i = l; i <= r; i++) {
            if (directions[i] != 'S') {
                res++;
            }
        }
        return res;
    }
};
```

**Solution 5: (Greedy, buffered right value)**
```
Runtime: 8 ms, Beats 78.26%
Memory: 19.30 MB, Beats 64.06%
```
```c++
class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.size(), i = 0, right = 0, ans = 0;
        while (i < n && directions[i] == 'L') {
            i += 1;
        }
        while (i < n) {
            if (directions[i] == 'R') {
                right += 1;
            } else {
                if (directions[i] == 'L') {
                    right += 1;
                }
                ans += right;
                right = 0;
            }
            i += 1;
        }
        return ans;
    }
};
```
