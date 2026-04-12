3899. Angles of a Triangle

You are given a positive integer array `sides` of length 3.

Determine if there exists a triangle with positive area whose three side lengths are given by the elements of `sides`.

If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in degrees), sorted in non-decreasing order. Otherwise, return an empty array.

Answers within `10^-5` of the actual answer will be accepted.

 

**Example 1:**
```
Input: sides = [3,4,5]

Output: [36.86990,53.13010,90.00000]

Explanation:

You can form a right-angled triangle with side lengths 3, 4, and 5. The internal angles of this triangle are approximately 36.869897646, 53.130102354, and 90 degrees respectively.
```

**Example 2:**
```
Input: sides = [2,4,2]

Output: []

Explanation:

You cannot form a triangle with positive area using side lengths 2, 4, and 2.
```
 

**Constraints:**

* `sides.length == 3`
* `1 <= sides[i] <= 1000`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 28.98 MB, Beats 75.27%
```
```c++
class Solution {
public:
    vector<double> internalAngles(vector<int>& sides) {
        /*
        sum of two sides should be greater than third

        cos(A) = (b^2+c^2-a^2) /(2bc)
        */

        double a = sides[0];
        double b = sides[1];
        double c = sides[2];

        // triangle inequality check (positive area)
        if (a + b <= c || b + c <= a || c + a <= b)
            return {};

        // Law of Cosines
        double A = acos((b*b + c*c - a*a) / (2*b*c)) * 180.0 / M_PI;
        double B = acos((a*a + c*c - b*b) / (2*a*c)) * 180.0 / M_PI;
        double C = acos((a*a + b*b - c*c) / (2*a*b)) * 180.0 / M_PI;

        vector<double> ans = {A, B, C};
        sort(ans.begin(), ans.end());
        return ans;
    }
};
```
