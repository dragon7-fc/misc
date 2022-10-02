2425. Bitwise XOR of All Pairings

You are given two **0-indexed** arrays, `nums1` and `nums2`, consisting of non-negative integers. There exists another array, `nums3`, which contains the bitwise XOR of **all pairings** of integers between `nums1` and `nums2` (every integer in `nums1` is paired with every integer in `nums2` exactly once).

Return the **bitwise XOR** of all integers in `nums3`.

 

**Example 1:**
```
Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
```

**Example 2:**
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
```

**Constraints:**

* `1 <= nums1.length, nums2.length <= 10^5`
* `0 <= nums1[i], nums2[j] <= 10^9`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 1349 ms
Memory: 32.9 MB
```
```python
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        rst = 0
        if n2%2:
            rst ^= functools.reduce(operator.xor, nums1)
        if n1%2:
            rst ^= functools.reduce(operator.xor, nums2)
        return rst
```

**Solution 2: (Math)**
```
Runtime: 183 ms
Memory: 60.5 MB
```
```c++
class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int x1 = 0, x2 = 0;
        for(int i = 0; i<nums1.size();++i) x1 = x1^nums1[i];
        for(int i = 0; i<nums2.size();++i) x2 = x2^nums2[i];
        int re = 0;
        if(nums2.size()%2) re = re^x1;
        if(nums1.size()%2) re = re^x2;
        return re;
    }
};
```
