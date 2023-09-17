2857. Count Pairs of Points With Distance k

You are given a 2D integer array `coordinates` and an integer `k`, where `coordinates[i] = [xi, yi]` are the coordinates of the `i`th point in a 2D plane.

We define the distance between two points `(x1, y1)` and `(x2, y2)` as `(x1 XOR x2) + (y1 XOR y2)` where `XOR` is the bitwise `XOR` operation.

Return the number of pairs `(i, j)` such that `i < j` and the distance between points `i` and `j` is equal to `k`.

 

**Example 1:**
```
Input: coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5
Output: 2
Explanation: We can choose the following pairs:
- (0,1): Because we have (1 XOR 4) + (2 XOR 2) = 5.
- (2,3): Because we have (1 XOR 5) + (3 XOR 2) = 5.
```

**Example 2:**
```
Input: coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0
Output: 10
Explanation: Any two chosen pairs will have a distance of 0. There are 10 ways to choose two pairs.
```

**Constraints:**

* `2 <= coordinates.length <= 50000`
* `0 <= xi, yi <= 10^6`
* `0 <= k <= 100`

# Submissions
---
**Solution 1: (Math, a xor b = c -> a = c xor b)**

__Intuition__
Imaging a simpler version of this quesiton:
Given an array A, find the pair that A[i] ^ A[j] = k.

Can you solve it?
Then the same approach for this problem.


__Explanation__
In the base question,
we can one pass the input array A,
count the frequency of seen A[i],
and for each A[i],
find it's pair A[i] ^ k,
and update res += count[A[i] ^ k],
then update count[A[i]] += 1.

Exactly same process for this problem,
though this time the xor sum is k.
Notice 0 <= k <= 100 is a small range,
we can enumerate the xor on x and y,
then we transform this question to the base one.


__Complexity__
* Time O(kn)
* Space O(n)

```
Runtime: 606 ms
Memory: 258.8 MB
```
```c++
class Solution {
public:
    int countPairs(vector<vector<int>>& coordinates, int k) {
        unordered_map<int, unordered_map<int, int>> count;
        int res = 0;
        for (auto& c : coordinates) {
            for (int x = 0; x <= k; x++)
                if (count[c[0] ^ x].count(c[1] ^ (k - x)))
                    res += count[c[0] ^ x][c[1] ^ (k - x)];
            count[c[0]][c[1]]++;
        }
        return res;
    }
};
```
