1471. The k Strongest Values in an Array

Given an array of integers `arr` and an integer `k`.

A value `arr[i]` is said to be stronger than a value `arr[j]` if `|arr[i] - m| > |arr[j] - m|` where `m` is the median of the array.
If `|arr[i] - m| == |arr[j] - m|`, then `arr[i]` is said to be stronger than `arr[j]` if `arr[i] > arr[j]`.

Return a list of the strongest `k` values in the array. return the answer in any arbitrary order.

**Median** is the middle value in an ordered integer list. More formally, if the length of the list is n, the median is the element in position `((n - 1) / 2)` in the sorted list **(0-indexed)**.

* For `arr = [6, -3, 7, 2, 11], n = 5` and the median is obtained by sorting the array `arr = [-3, 2, 6, 7, 11]` and the median is `arr[m]` where `m = ((5 - 1) / 2) = 2` The median is `6`.
* For `arr = [-7, 22, 17, 3], n = 4` and the median is obtained by sorting the array arr = [-7, 3, 17, 22] and the median is `arr[m]` where `m = ((4 - 1) / 2) = 1`. The median is `3`.
 

**Example 1:**
```
Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.
```

**Example 2:**
```
Input: arr = [1,1,3,5,5], k = 2
Output: [5,5]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].
```

**Example 3:**
```
Input: arr = [6,7,11,7,6,8], k = 5
Output: [11,8,6,6,7]
Explanation: Median is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is accepted.
```

**Example 4:**
```
Input: arr = [6,-3,7,2,11], k = 3
Output: [-3,11,2]
```

**Example 5:**
```
Input: arr = [-7,22,17,3], k = 2
Output: [22,17]
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `-10^5 <= arr[i] <= 10^5`
* `1 <= k <= arr.length`

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 1048 ms
Memory Usage: 27.2 MB
```
```python
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        arr.sort()
        i, j = 0, N - 1
        median = arr[(N - 1) // 2]
        while N - (j - i) <= k:
            if abs(arr[i] - median) > abs(arr[j] - median):
                i = i + 1
            else:
                j = j - 1
        return arr[:i] + arr[j + 1:]
```

**Solution 2: (Two Pointers)**
```
Runtime: 119 ms
Memory: 83.94 MB
```
```c++
class Solution {
public:
    vector<int> getStrongest(vector<int>& arr, int k) {
        sort(begin(arr), end(arr));
        int i = 0, j = arr.size() - 1;
        int med = arr[(arr.size() - 1) / 2];
        while (--k >= 0)
            if (med - arr[i] > arr[j] - med)
                ++i;  
            else
                --j;
        arr.erase(begin(arr) + i, begin(arr) + j + 1);
        return arr;
    }
};
```
