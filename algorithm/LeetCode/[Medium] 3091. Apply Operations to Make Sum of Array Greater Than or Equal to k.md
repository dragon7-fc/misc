3091. Apply Operations to Make Sum of Array Greater Than or Equal to k

You are given a positive integer `k`. Initially, you have an array `nums = [1]`.

You can perform any of the following operations on the array any number of times (possibly zero):

* Choose any element in the array and **increase** its value by `1`.
* Duplicate any element in the array and add it to the end of the array.

Return the minimum number of operations required to make the sum of elements of the final array greater than or equal to `k`.

 

**Example 1:**
```
Input: k = 11

Output: 5

Explanation:

We can do the following operations on the array nums = [1]:

Increase the element by 1 three times. The resulting array is nums = [4].
Duplicate the element two times. The resulting array is nums = [4,4,4].
The sum of the final array is 4 + 4 + 4 = 12 which is greater than or equal to k = 11.
The total number of operations performed is 3 + 2 = 5.
```

**Example 2:**
```
Input: k = 1

Output: 0

**Explanation:**

The sum of the original array is already greater than or equal to 1, so no operations are needed.
```
 

**Constraints:**

* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 4 ms
Memory: 7.27 MB
```
```c++
class Solution {
public:
    int minOperations(int k) {
        int a = sqrt(k);
        return a + (k - 1) / a - 1;
    }
};
```

**Solution 2: (Brute Force)**
```
Runtime: 6 ms
Memory: 7.44 MB
```
```c++
class Solution {
public:
    int minOperations(int k) {
        if (k == 1) return 0;
        int ans = k;
        for(int i = 1; i <= k/2; ++i){
            int t = (i - 1) + (ceil((double)k/(double)i) - 1);
            ans = min(ans, t);
        }
        return ans;
    }
};
```
