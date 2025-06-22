3443. Maximum Manhattan Distance After K Changes

You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and `'W'`, where `s[i]` indicates movements in an infinite grid:

* `'N'` : Move north by 1 unit.
* `'S'` : Move south by 1 unit.
* `'E'` : Move east by 1 unit.
* `'W'` : Move west by 1 unit.

Initially, you are at the origin `(0, 0)`. You can change at most `k` characters to any of the four directions.

Find the **maximum Manhattan distance** from the origin that can be achieved at any time while performing the movements in order.

The **Manhattan Distance** between two cells `(xi, yi)` and `(xj, yj)` is `|xi - xj| + |yi - yj|`.
 

**Example 1:**
```
Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.
```

**Example 2:**
```
Input: s = "NSWWEW", k = 3

Output: 6

Explanation:

Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `0 <= k <= s.length`
* `s` consists of only `'N'`, `'S'`, `'E'`, and `'W'`.

# Submissions
---
**Solution 1: (Brute Force, Explore Directions)**
```
Runtime: 210 ms, Beats 36.36%
Memory: 65.63 MB, Beats 9.09%
```
```c++
class Solution {
    int helper(string &str , string s , int k ) {
        int plus = 0 , minus = 0 , maxi = -1 ;
        int n =s.size() ;
        for(int i =0; i < n ; i++) {
            if( s[i] == str[0] || s[i] == str[1]  ) plus ++ ;
            else if( (s[i] == str[2] || s[i] == str[3]) && k > 0 ){ plus ++ ; k-- ; }
            else minus -- ;

            maxi = max(abs(plus + minus) , maxi) ;
        }
        return maxi ;
    }
public:
    int maxDistance(string s, int k) {
        int K = k ;
        int n = s.size() ;
        int ans = 0 , plus = 0 , minus = 0, maxi = -1 ;

        vector<string> v = {"NWSE" , "SENW" , "NESW" , "SWNE"} ;
        for(int i = 1 ; i<=4 ; i++) {
            maxi = max(maxi , helper(v[i-1] , s , k)) ;
        }
        return maxi ;
    }
};
```

**Solution 2: (Step-by-step Solution, math, case study)**

    s = "NWSE", k = 1

                 |
          x   <  x  (0,1)
          v      ^
     -----x--->--x-----------
        (-1,0) (0,0)
n   1
s   1
e   1
w   1
t1  1
t2  0
ans 2

    s = "NSWWEW", k = 3
                   x (-4,2)
                   |
                   t1
                   |
                   -
                   |                            x  | 1 |
                   t1                          v^  |   t1
                   |-t2----|-t2----x  <   x  <  x  | 0 |
                                      >            |
                                      <
---------------------------------------------------
     -6     -5     -4     -3      -2     -1     0
                                  ----t2----       
n   1
s   1
e   1
w   3
t1  1
t2  1
ans 6
```
Runtime: 143 ms, Beats 50.61%
Memory: 38.17 MB, Beats 74.85%
```
```c++
class Solution {
    int count(int drt1, int drt2, int times) {
        return abs(drt1 - drt2) + times * 2;
    }  // Calculate modified Manhattan distance
public:
    int maxDistance(string s, int k) {
        int ans = 0;
        int north = 0, south = 0, east = 0, west = 0;
        for (char it : s) {
            switch (it) {
                case 'N':
                    north++;
                    break;
                case 'S':
                    south++;
                    break;
                case 'E':
                    east++;
                    break;
                case 'W':
                    west++;
                    break;
            }
            int times1 =
                min({north, south, k});  // modification times for N and S
            int times2 = min(
                {east, west, k - times1});  // modification times for E and W
            ans = max(ans,
                      count(north, south, times1) + count(east, west, times2));
        }
        return ans;
    }
};
```

**Solution 3: (Overall Solution, math, case study)**
```
Runtime: 51 ms, Beats 91.52%
Memory: 38.15 MB, Beats 74.85%
```
```C++
class Solution {
public:
    int maxDistance(string s, int k) {
        int latitude = 0, longitude = 0, ans = 0;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            switch (s[i]) {
                case 'N':
                    latitude++;
                    break;
                case 'S':
                    latitude--;
                    break;
                case 'E':
                    longitude++;
                    break;
                case 'W':
                    longitude--;
                    break;
            }
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1));
//                         ------------------------------------------  -----
// case                        less element > k                        less element <= k
//                             NW / NE / SW / SE
        }
        return ans;
    }
};
```
