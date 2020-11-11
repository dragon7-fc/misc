593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

**Example:**
```
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
```

**Note:**

1. All the input integers are in the range `[-10000, 10000]`.
1. A valid square has four equal sides with positive length and four equal angles (90-degree angles).
1. Input points have no order.

# Solution
---
## Approach #1 Brute Force [Accepted]
The idea behind determining whether 4 given set of points constitute a valid square or not is really simple. Firstly, we need to determine if the sides of the qaudrilateral formed by these 4 points are equal. But checking only this won't suffice. Since, this condition will be satisfied even in the case of a rhombus, where all the four sides are equal but the adjacent sides aren't perpendicular to each other. Thus, we also need to check if the lengths of the diagonals formed between the corners of the quadrilateral are equal. If both the conditions are satisfied, then only the given set of points can be deemed appropriate for constituting a square.

Now, the problem arises in determining which pairs of points act as the adjacent points on the square boundary. So, the simplest method is to consider every possible case. For the given 4 points, $[p_0, p_1, p_2, p_3]$, there are a total of `4!` ways in which these points can be arranged to be considered as the square's boundaries. We can generate every possible permutation and check if any permutation leads to the valid square arrangement of points.

```java
public class Solution {
    public double dist(int[] p1, int[] p2) {
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0]);
    }
    public boolean check(int[] p1, int[] p2, int[] p3, int[] p4) {
        return dist(p1,p2) > 0 && dist(p1, p2) == dist(p2, p3) && dist(p2, p3) == dist(p3, p4) && dist(p3, p4) == dist(p4, p1) && dist(p1, p3) == dist(p2, p4);
    }
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] p = {p1,p2,p3,p4};
        return checkAllPermutations(p, 0);
    }
    boolean checkAllPermutations(int[][] p, int l) {
        if (l == 4) {
            return check(p[0], p[1], p[2], p[3]);
        } else {
            boolean res = false;
            for (int i = l; i < 4; i++) {
                swap(p, l, i);
                res |= checkAllPermutations(p, l + 1);
                swap(p, l, i);
            }
            return res;
        }
    }
    public void swap(int[][] p, int x, int y) {
        int[] temp = p[x];
        p[x] = p[y];
        p[y] = temp;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(1)$. Constant number of permutations($4!$) are generated.

* Space complexity : $O(1)$. Constant space is required.

## Approach #2 Using Sorting [Accepted]
Instead of considering all the permutations of arrangements possible, we can make use of maths to simplify this problem a bit. If we sort the given set of points based on their x-coordinate values, and in the case of a tie, based on their y-coordinate value, we can obtain an arrangement, which directly reflects the arrangement of points on a valid square boundary possible.

Consider the only possible cases as shown in the figure below:

![593_Valid_Square_1.png](img/593_Valid_Square_1.png)

In each case, after sorting, we obtain the following conclusion regarding the connections of the points:

* $p_0p_1$, $p_1p_3$, $p_3p_2$ and $p_2p_0$ form the four sides of any valid square.

* $p_0p_3$ and $p_1p_2$ form the diagonals of the square.

Thus, once the sorting of the points is done, based on the above knowledge, we can directly compare $p_0p_1$, $p_1p_3$, $p_3p_2$ and $p_2p_0$ for equality of lengths(corresponding to the sides); and $p_0p_3$ and $p_1p_2$ for equality of lengths(corresponding to the diagonals).

```java
public class Solution {
    public double dist(int[] p1, int[] p2) {
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0]);
    }
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] p={p1,p2,p3,p4};
        Arrays.sort(p, (l1, l2) -> l2[0] == l1[0] ? l1[1] - l2[1] : l1[0] - l2[0]);
        return dist(p[0], p[1]) != 0 && dist(p[0], p[1]) == dist(p[1], p[3]) && dist(p[1], p[3]) == dist(p[3], p[2]) && dist(p[3], p[2]) == dist(p[2], p[0])   && dist(p[0],p[3])==dist(p[1],p[2]);
    }
}

```

**Complexity Analysis**

* Time complexity : $O(1)$. Sorting 4 points takes constant time.

* Space complexity : $O(1)$. Constant space is required.

## Approach #3 Checking every case [Accepted]
**Algorithm**

If we consider all the permutations descripting the arrangement of points as in the brute force approach, we can come up with the following set of 24 arrangements:

![593_Valid_Square_2.png](img/593_Valid_Square_2.png)

In this figure, the rows with the same shaded color indicate that the corresponding arrangements lead to the same set of edges and diagonals. Thus, we can see that only three unique cases exist. Thus, instead of generating all the 24 permutations, we check for the equality of edges and diagonals for only the three distinct cases.

```java
public class Solution {
    public double dist(int[] p1, int[] p2) {
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0]);
    }
    public boolean check(int[] p1, int[] p2, int[] p3, int[] p4) {
        return dist(p1,p2) > 0 && dist(p1, p2) == dist(p2, p3) && dist(p2, p3) == dist(p3, p4) && dist(p3, p4) == dist(p4, p1) && dist(p1, p3) == dist(p2, p4);
    }
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        return check(p1, p2, p3, p4) || check(p1, p3, p2, p4) || check(p1, p2, p4, p3);
    }
}
```

**Complexity Analysis**

* Time complexity : $O(1)$. A fixed number of comparisons are done.

* Space complexity : $O(1)$. No extra space required.

# Submissions
---
**Solution 1: (Using Sorting)**
```
Runtime: 24 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = sorted([p1, p2, p3, p4])
        dist = lambda i, j: (p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2
        return dist(0, 1) != 0 and dist(0, 1) == dist(1, 3) == dist(3, 2) == dist(2, 0) and dist(0, 3) == dist(1, 2)
```