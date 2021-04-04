1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class `SparseVector`:

* `SparseVector(nums)` Initializes the object with the vector `nums`
* `dotProduct(vec)` Compute the dot product between the instance of `SparseVector` and `vec`

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two `SparseVector`.

**Follow up:** What if only one of the vectors is sparse?

 

**Example 1:**

```
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
```

**Example 2:**

```
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
```

**Example 3:**

```
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
```

**Constraints:**

* `n == nums1.length == nums2.length`
* `1 <= n <= 10^5`
* `0 <= nums1[i], nums2[i] <= 100`

# Submissions
---
**Solution 1: (Index-Value Pairs)**
```
Runtime: 1844 ms
Memory Usage: 18.3 MB
```
```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
```