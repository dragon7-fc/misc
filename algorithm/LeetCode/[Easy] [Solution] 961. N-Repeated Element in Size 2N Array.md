961. N-Repeated Element in Size 2N Array

In a array `A` of size `2N`, there are `N+1` unique elements, and exactly one of these elements is repeated `N` times.

Return the element repeated `N` times.

 

**Example 1:**
```
Input: [1,2,3,3]
Output: 3
```

**Example 2:**
```
Input: [2,1,2,5,3,2]
Output: 2
```

**Example 3:**
```
Input: [5,1,5,2,5,3,5,4]
Output: 5
``` 

**Note:**

* `4 <= A.length <= 10000`
* `0 <= A[i] < 10000`
* `A.length` is even

# Solution
---
## Approach 1: Count
**Intuition and Algorithm**

Let's count the number of elements. We can use a `HashMap` or an array - here, we use a `HashMap`.

After, the element with a count larger than `1` must be the answer.

```python
class Solution(object):
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution:**
```
Runtime: 236 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
```

**Solution 1: (Compare, try all solution)**

    a b c x x x
case 1: k = 1
    a x
    |-|
case 2: k = 2
    a b a
    |---|
case 3: k = 3
    a b c a
    |-----|

```
Runtime: 0 ms, Beats 100.00%
Memory: 28.21 MB, Beats 97.60%
```
```c++
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int n = nums.size(), i, k;
        for (k = 1; k <= 3; k ++) {
            for (i = 0; i < n - k; ++i) {
                if (nums[i] == nums[i + k]) {
                    return nums[i];
                }
            }
        }
        throw -1;
    }
};
```
