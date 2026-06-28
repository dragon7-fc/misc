1846. Maximum Element After Decreasing and Rearranging

You are given an array of positive integers `arr`. Perform some operations (possibly none) on `arr` so that it satisfies these conditions:

* The value of the first element in arr must be `1`.
* The absolute difference between any 2 adjacent elements must be **less than or equal to** `1`. In other words, `abs(arr[i] - arr[i - 1]) <= 1` for each `i` where `1 <= i < arr.length` (**0-indexed**). `abs(x)` is the absolute value of `x`.

There are 2 types of operations that you can perform any number of times:

* **Decrease** the value of any element of `arr` to a **smaller positive integer**.
* **Rearrange** the elements of `arr` to be in any order.

Return the **maximum** possible value of an element in `arr` after performing the operations to satisfy the conditions.

 

**Example 1:**
```
Input: arr = [2,2,1,2,1]
Output: 2
Explanation: 
We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
The largest element in arr is 2.
```

**Example 2:**
```
Input: arr = [100,1,1000]
Output: 3
Explanation: 
One possible way to satisfy the conditions is by doing the following:
1. Rearrange arr so it becomes [1,100,1000].
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now arr = [1,2,3], which satisfies the conditions.
The largest element in arr is 3.
```

**Example 3:**
```
Input: arr = [1,2,3,4,5]
Output: 5
Explanation: The array already satisfies the conditions, and the largest element is 5.
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^9`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 484 ms
Memory Usage: 25 MB
```
```python
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        arr.sort()
        arr = [1] + arr[1:]
        for i in range(1, N):
            if arr[i] > arr[i-1]+1:
                arr[i] = arr[i-1]+1
        return arr[-1]
```

**Solution 1: (Greedy, simulation)**
```
Runtime: 73 ms
Memory: 51.5 MB
```
```c++
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int ans = 1;
        
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] >= ans + 1) {
                ans++;
            }
        }
        
        return ans;
    }
};
```

**Solution 2: (No Sort, bucket sort)**
```
Runtime: 65 ms
Memory: 53.5 MB
```
```c++
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        int n = arr.size();
        vector<int> counts = vector(n + 1, 0);
        
        for (int num : arr) {
            counts[min(num, n)]++;
        }
        
        int ans = 1;
        for (int num = 2; num <= n; num++) {
            ans = min(ans + counts[num], num);
        }
        
        return ans;
    }
};
```

**Solution 3: (Counter)**

    arr = [2,2,1,2,1]
cnt                    ans
                        1
1              1   2
2          1 2   3      2< ans
3
4
5

-------------------------------
    arr = [1,2,3,4,5]
cnt                     ans
                         1
1          1
2            1           2
3              1         3
4                1       4
5                  1     5< ans

```
Runtime: 4 ms, Beats 88.98%
Memory: 57.24 MB, Beats 4.52%
```
```c++
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        int n = arr.size();
        vector<int> cnt = vector(n + 1, 0);
        for (const auto &num : arr) {
            cnt[min(num, n)] += 1;
        }
        int ans = 1;
        for (int num = 2; num <= n; num += 1) {
            ans = min(ans + cnt[num], num);
        }
        return ans;
    }
};
```
