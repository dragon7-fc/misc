454. 4Sum II

Given four lists `A, B, C, D` of integer values, compute how many tuples `(i, j, k, l)` there are such that `A[i] + B[j] + C[k] + D[l]` is zero.

To make problem a bit easier, all `A, B, C, D` have same length of `N` where `0 ≤ N ≤ 500`. All integers are in the range of `-228` to `228 - 1` and the result is guaranteed to be at most `231 - 1`.

**Example:**
```
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```

# Submissions
---
**Solution 1: (Hash Table)**

first we put sum of C and D values into dict
```
C = [1,2]
D = [1,2]
1 + 1 => {2:1}
1 + 2 => {2:1, 3:1}
2 + 1 => {2:1, 3:2}
2 + 2 => {2:1, 3:2, 4:1}
```

then we iterate over A and B
```
A = [-1,-2]
B = [-1,-2]
-1 -1 => 0 - (-2) => 2 is key we want. (matches += 1)
-1 -2 => 0 - (-3) => 3 is key we want. (matches += 2)
-2 -1 => 0 - (-3) => 3 is key we want. (matches += 2)
-2 -2 => 0 - (-4) => 4 is key we want. (matches += 1)

answer is 6
```

```
Runtime: 260 ms
Memory Usage: 33.6 MB
```
```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        total_sum = 0
        cache = collections.defaultdict(int)
        for i in C:
            for j in D:
                key = i + j
                cache[key] += 1
        for i in A:
            for j in B:
                key = 0 - i - j
                if key in cache:
                    total_sum += cache[key]
        return total_sum
```

**Solution 2: (Hash Table)**
```
Runtime: 919 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        total_sum = 0
        cache = collections.defaultdict(int)
        for n3, n4 in itertools.product(nums3, nums4):
            cache[n3+n4] += 1
        for n1, n2 in itertools.product(nums1, nums2):
            total_sum += cache[-(n1+n2)]
        return total_sum
```

**Solution 3: (Hash Table)**
```
Runtime: 883 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = collections.Counter(a + b for a in nums1 for b in nums2)
        return sum(count[-c-d] for c in nums3 for d in nums4)
```

**Solution 4: (Hash Table)**
```
Runtime: 184 ms
Memory Usage: 24.5 MB
```
```c++
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        int N = nums1.size();
        std::unordered_map<int, int> cache;
        int ans {0};
        for (auto n1: nums1) {
            for (auto n2: nums2) {
                cache[n1+n2] += 1;
            }
        }
        for (auto n3: nums3) {
            for (auto n4: nums4) {
                ans += cache[-(n3+n4)];
            }
        }
        return ans;
    }
};
```
