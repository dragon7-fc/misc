2358. Maximum Number of Groups Entering a Competition

You are given a positive integer array `grades` which represents the grades of students in a university. You would like to enter **all** these students into a competition in ordered non-empty groups, such that the ordering meets the following conditions:

* The sum of the grades of students in the `i`th group is less than the sum of the grades of students in the `(i + 1)`th group, for all groups (except the last).
* The total number of students in the `i`th group is less than the total number of students in the `(i + 1)`th group, for all groups (except the last).

Return the **maximum** number of groups that can be formed.

 

**Example 1:**
```
Input: grades = [10,6,12,7,3,5]
Output: 3
Explanation: The following is a possible way to form 3 groups of students:
- 1st group has the students with grades = [12]. Sum of grades: 12. Student count: 1
- 2nd group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
- 3rd group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
It can be shown that it is not possible to form more than 3 groups.
```

**Example 2:**
```
Input: grades = [8,8]
Output: 1
Explanation: We can only form 1 group, since forming 2 groups would lead to an equal number of students in both groups.
```

**Constraints:**

* `1 <= grades.length <= 10^5`
* `1 <= grades[i] <= 10^5`

# Submissions
---
**Solution 1: (Greedy)**

**Explanation**

Sort all grades,
assign 1 student to the first group,
assign 2 student to the second group...
This can satify ith group < i+1th group for both size and sum.

So we need to find out the maximum result k that
1 + 2 + ... + k <= n

**Prove:**

Sort groups by size,
so the first group has size at least 1
so the second group has size at least 2
kth group has size at least k...

So we proved the upper bound of k and I gave a solution to achieve it.

**Complexity**

* Time `O(sqrt(n))`
* Space `O(1)`

```
Runtime: 1015 ms
Memory Usage: 27.3 MB
```
```python
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        k = 0
        while n >= k + 1:
            k += 1
            n -= k
        return k
```

**Solution 2: (Binary Search)**
```
Runtime: 162 ms
Memory Usage: 56.6 MB
```
```c++
class Solution {
public:
    int maximumGroups(vector<int>& grades) {
        int left = 0, right = 1000, n = grades.size();
        while (left < right) {
            int k = (left + right + 1) / 2;
            if (k * (k + 1) / 2 > n) {
                right = k - 1;
            } else {
                left = k;
            }
        }
        return left;
    }
};
```
