1183. Maximum Number of Ones

Consider a matrix `M` with dimensions `width * height`, such that every cell has value `0` or `1`, and any square sub-matrix of `M` of size `sideLength * sideLength` has at most `maxOnes` ones.

Return the maximum possible number of ones that the matrix `M` can have.

 

**Example 1:**
```
Input: width = 3, height = 3, sideLength = 2, maxOnes = 1
Output: 4
Explanation:
In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
The best solution that has 4 ones is:
[1,0,1]
[0,0,0]
[1,0,1]
```

**Example 2:**
```
Input: width = 3, height = 3, sideLength = 2, maxOnes = 2
Output: 6
Explanation:
[1,0,1]
[1,0,1]
[1,0,1]
```

**Constraints:**

* `1 <= width, height <= 100`
* `1 <= sideLength <= width, height`
* `0 <= maxOnes <= sideLength * sideLength`

# Submissions
---
**Solution 1: (Greedy, Math)**

Consider the sidelegth * sidelegth square submatrix in the upper left. If we select the (i,j) position to be one, where i <sidelegth && j < sidelegth, all the other cells in the big matrix with position (p,q) where p%sidelegth == i % sidelegth && q%sidelegth == j%sidelength can be set to one without increasing the number of ones in the upper left submatrix. The point (p,q) shares similar position with (i,j) respect to sidelegth.

Thus, to get most ones out of the big matrix, for each (i,j) in the sub matrix, we calculate the number of points that share similar position with (i,j) respect to sidelegth. Then, we select the maxOnes points with largest number of points at similar position; the answer is the sum of the number of points. 

    width = 3, height = 3, sideLength = 2, maxOnes = 2

    [1, 0, 1]
    [1, 0, 1]
    [1, 0, 1]

res  4 2 2 1
         ^maxOnes


```
Runtime: 5 ms
Memory: 7.7 MB
```
```c++
class Solution {
public:
    int maximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        vector<int> res;
        for(int i = 0;i < sideLength; i++) {
            for(int j =0; j < sideLength; j++) {
                res.push_back(((width-i-1)/sideLength + 1)*((height-j-1)/sideLength + 1));
            }
        }
        sort(res.begin(), res.end(), greater<int>());
        int ans = 0;
        for(int i = 0;i < maxOnes; i++) ans += res[i];
        return ans;
    }
};
```
