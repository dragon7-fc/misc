1131. Maximum of Absolute Value Expression

Given two arrays of integers with equal lengths, return the maximum value of:

`|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|`

where the maximum is taken over all `0 <= i, j < arr1.length`.

 

**Example 1:**
```
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
```

**Example 2:**
```
Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
```

**Constraints:**

* `2 <= arr1.length == arr2.length <= 40000`
* `-10^6 <= arr1[i], arr2[i] <= 10^6`

# Submissions
---
**Solution 1: (Math, Bit Manipulation)**

Without loss of generality, we only discuss the scenario when i < j.
below is the discussion about 4 scenarios.
```
if i < j :
    if arr1[i] > arr1[j]:
        if arr2[i] < arr2[j]:
            value = arr1[i] - arr1[j] + arr2[j] - arr2[i] + j - i
            = (arr1[i] - arr2[i] - i) - (arr1[j] - arr2[j] - j)

        else:
            value = arr1[i] - arr1[j] + arr2[i] - arr2[j] + j - i
            = (arr1[i] + arr2[i] - i) - (arr1[j] + arr2[j] - j)

    elif arr1[i] < arr1[j]:
        if arr2[i] < arr2[j]:
            value = arr1[j] - arr1[i] + arr2[j] - arr2[i] + j - i
            = (arr1[j] + arr2[j] + j) - (arr1[i] + arr2[i] + i) 
        else:
            value = arr1[j] - arr1[i] + arr2[i] - arr2[j] + j - i
            = (arr1[j] - arr2[j] + j) - (arr1[i] - arr2[i] + i) 
```
Hence, we only need to consider 4 scenarios to get the maximum.
For the first case, we get the maximum of (arr1[i] - arr2[i] - i) and minimum of (arr1[i] - arr2[i] - i), then we subtract maximum with minimum, and get the value of possible maximum for the first case.
Then we get the max of 4 cases and return.

```
Runtime: 352 ms
Memory Usage: 19.3 MB
```
```python
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max1 = max2 = max3 = max4 = float('-inf')
        min1 = min2 = min3 = min4 = float('inf')

        for i in range(len(arr1)):
            tmp1 = arr1[i] - arr2[i] - i
            max1 = max(max1 , tmp1)
            min1 = min(min1 , tmp1)

            tmp2 = arr1[i] + arr2[i] - i
            max2 = max(max2 , tmp2)
            min2 = min(min2 , tmp2)

            tmp3 = arr1[i] + arr2[i] + i
            max3 = max(max3 , tmp3)
            min3 = min(min3 , tmp3)


            tmp4 = arr1[i] - arr2[i] + i
            max4 = max(max4 , tmp4)
            min4 = min(min4 , tmp4)

        return max((max1 - min1), (max2 - min2),(max3 - min3),(max4 - min4))
```

**Solution 2: (Math)**

__Intuition__
Take |x[i] - x[j]| + |y[i] - y[j]| as Manhattan distance of two points.
x is the coordinate of points on the x-axis,
y is the coordinate of points on the y-axis.


__Explanation 1: Math__
Assume i < j, there are four possible expression:
|x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]|) + (y[i] - y[j]) = (x[i] + y[i]|) - (x[j] + y[j])
|x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]|) - (y[i] - y[j]) = (x[i] - y[i]|) - (x[j] - y[j])
|x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]|) + (y[i] - y[j]) = (-x[i] + y[i]|) - (-x[j] + y[j])
|x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]|) - (y[i] - y[j]) = (-x[i] - y[i]|) - (-x[j] - y[j])

So we can see, the expression
|x[i] - x[j]| + |y[i] - y[j]| + |i - j| = f(j) - f(i)

where f(i) = p * x[i] + q * y[i] + i
with p = 1 or -1, q = 1 or -1


__Explanation 2: Graph__
For 3 points on the plane, we always have |AO| - |BO| <= |AB|.
When AO and BO are in the same direction, we have ||AO| - |BO|| = |AB|.

We take 4 points for point O, left-top, left-bottom, right-top and right-bottom.
Each time, for each point B, and find the smallest A point to O,
the Manhattan distance |AB| >= |AO| - |BO|.


__Complexity__
Time O(N) for 4 passes
Space O(1)

```
Runtime: 28 ms
Memory: 26.69 MB 
```
```c++
class Solution {
public:
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        int res = 0, n = arr1.size(), smallest, cur;
        for (int p : {1, -1}) {
            for (int q : {1, -1}) {
                smallest = p * arr1[0] + q * arr2[0] + 0;
                for (int i = 1; i < n; ++i) {
                    cur = p * arr1[i] + q * arr2[i] + i;
                    res = max(res, cur - smallest);
                    smallest = min(smallest, cur);
                }
            }
        }
        return res;
    }
};
```
