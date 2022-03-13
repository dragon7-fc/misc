954. Array of Doubled Pairs

Given an array of integers `A` with even length, return `true` if and only if it is possible to reorder it such that `A[2 * i + 1] = 2 * A[2 * i]` for every `0 <= i < len(A) / 2`.

**Example 1:**
```
Input: [3,1,3,6]
Output: false
```

**Example 2:**
```
Input: [2,1,2,6]
Output: false
```

**Example 3:**
```
Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
```

**Example 4:**
```
Input: [1,2,4,16,8,4]
Output: false
```

**Note:**

1. `0 <= A.length <= 30000`
1. `A.length` is even
1. `-100000 <= A[i] <= 100000`

# Solution
---
## Approach 1: Greedy
**Intuition**

If `x` is currently the array element with the least absolute value, it must pair with `2*x`, as there does not exist any other `x/2` to pair with it.

**Algorithm**

Let's try to (virtually) "write" the final reordered array.

Let's check elements in order of absolute value. When we check an element `x` and it isn't used, it must pair with `2*x`. We will attempt to write `x, 2x` - if we can't, then the answer is `false`. If we write everything, the answer is `true`.

To keep track of what we have not yet written, we will store it in a `count`.

```python
class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 1016 ms
Memory Usage: 16 MB
```
```python
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True
```

**Solution 1: (Greedy, Counter)**
```
Runtime: 186 ms
Memory Usage: 58.1 MB
```
```c++
class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        map<int,int> cnt;
        for (auto a: arr) {
            cnt[a] += 1;
        }
        sort(arr.begin(), arr.end(), [](int &a, int &b){
            return abs(a) < abs(b);
        });
        for (int i = 0; i < arr.size(); i ++) {
            if (cnt[arr[i]] == 0)
                continue;
            if (cnt[2*arr[i]] == 0)
                return false;
            cnt[arr[i]] -= 1;
            cnt[2*arr[i]] -= 1;
        }
        return true;
    }
};
```
