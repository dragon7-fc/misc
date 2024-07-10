1823. Find the Winner of the Circular Game

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in clockwise order. More formally, moving clockwise from the `i`th friend brings you to the `(i+1)`th friend for `1 <= i < n`, and moving clockwise from the `n`th friend brings you to the `1st` friend.

The rules of the game are as follows:

1. Start at the `1st` friend.
1. Count the next `k` friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
1. The last friend you counted leaves the circle and loses the game.
1. If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
1. Else, the last friend in the circle wins the game.

Given the number of friends, `n`, and an integer `k`, return the winner of the game.

 

**Example 1:**

![1823_ic234-q2-ex11.png](img/1823_ic234-q2-ex11.png)
```
Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
```

**Example 2:**
```
Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
```

**Constraints:**

* `1 <= k <= n <= 500`

# Submissions
---
**Solution 1: (Simulation)**
```
Runtime: 28 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(n))
        i = 0 
        while len(nums) > 1: 
            i = (i + k-1) % len(nums)
            nums.pop(i)
        return nums[0] + 1
```

**Solution 2: (Simulation with List, O(n^2), O(n))**

    1  2  3  4  5
       x
             x
    x
                x
```
Runtime: 4 ms
Memory: 7.36 MB
```
```c++
class Solution {
public:
    int findTheWinner(int n, int k) {
        // Initialize vector of N friends, labeled from 1-N
        vector<int> circle;
        for (int i = 1; i <= n; i++) {
            circle.push_back(i);
        }

        // Maintain the index of the friend to start the count on
        int startIndex = 0;

        // Perform eliminations while there is more than 1 friend left
        while (circle.size() > 1) {
            // Calculate the index of the friend to be removed
            int removalIndex = (startIndex + k - 1) % circle.size();

            // Erase the friend at removalIndex
            circle.erase(circle.begin() + removalIndex);

            // Update startIndex for the next round
            startIndex = removalIndex;
        }

        return circle.front();
    }
};
```

**Solution 3: (Simulation, List, Double Link List)**
```
Runtime: 6 ms
Memory: 8.19 MB
```
```c++
class Solution {
public:
    int findTheWinner(int n, int k) {
        list<int> dp;
        for (int i = 1; i <= n; i ++) {
            dp.push_back(i);
        }
        int ck;
        auto it = dp.begin();
        while (dp.size() > 1) {
            ck = k;
            while (ck > 1) {
                ++it;
                if (it == dp.end()) {
                    it = dp.begin();
                }
                ck -= 1;
            }
            it = dp.erase(it);
            if (it == dp.end()) {
                it = dp.begin();
            }
        }
        return *it;
    }
};
```
**Solution 4: (Simulation with Queue, O(nk), O(n))**

    1  2  3  4  5  1  3  5  3
    ^           ^ 
          ^        ^ 
                ^     ^ 
                      ^  ^ 
                            ^
```
Runtime: 20 ms
Memory: 25.55 MB
```
```c++
class Solution {
public:
    int findTheWinner(int n, int k) {
        // Initialize queue with n friends
        queue<int> circle;
        for (int i = 1; i <= n; i++) {
            circle.push(i);
        }

        // Perform eliminations while more than 1 player remains
        while (circle.size() > 1) {
            // Process the first k-1 friends without eliminating them
            for (int i = 0; i < k - 1; i++) {
                circle.push(circle.front());
                circle.pop();
            }
            // Eliminate the k-th friend
            circle.pop();
        }

        return circle.front();
    }
};
```

**Solution 5: (Recursion, O(n), O(n))**

   0  1  2  3  4  (0->0, n=5)
   ^  x             
   3     0  1  2  (2->0, n=4)
      x  ^  x       
   1     2     0  (4->0, n=3)
   x  x     x  ^    
         0     1  (2->0, n=2)
   x  x  ^  x  x
         ^        (2->0, n=1)

f(n,k) = (f(n−1,k)+k) mod n    

```
Runtime: 2 ms
Memory: 7.22 MB
```
```c++
class Solution {
     int winnerHelper(int n, int k) {
        if (n == 1) return 0;
        return (winnerHelper(n - 1, k) + k) % n;
    }
public:
    int findTheWinner(int n, int k) {
        return winnerHelper(n, k) + 1;
    }
};
```

**Solution 6: (Iterative, O(n), O(1))**

    0  1  2  3  4
   [^] ^i
   [^   ] ^i
   [      ^] ^i
   [^         ] ^i
   [      ^      ] ^i
```
Runtime: 3 ms
Memory: 7.14 MB
```
```c++
class Solution {
public:
    int findTheWinner(int n, int k) {
        int ans = 0;
        for (int i = 2; i <= n; i++) {
            ans = (ans + k) % i;
        }
        // add 1 to convert back to 1 indexing
        return ans + 1;
    }
};
```
