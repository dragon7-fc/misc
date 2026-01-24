480. Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
`[2,3,4]` , the median is `3`

`[2,3]`, the median is `(2 + 3) / 2 = 2.5`

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

**For example:**
```
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].
```

**Note:**
* You may assume `k` is always valid, ie: `k` is always smaller than input array's size for non-empty array.
* Answers within `10^-5` of the actual value will be accepted as correct.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 176 ms
Memory Usage: 14.7 MB
```
```python
from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList(nums[:k-1])

        for end in range(k-1, len(nums)):
            window.add(nums[end])
            if k % 2:
                result.append(window[k // 2])
            else:
                result.append((window[k // 2] + window[k // 2-1]) / 2)
            window.remove(nums[end-k+1])

        return result
```

**Solution 2: (multiset)**
```
Runtime: 122 ms, Beats 16.40%
Memory: 61.63 MB, Beats 8.15%
````
```c++
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size(), i, j = 0;
        vector<double> ans(n-k+1);
        multiset<double> lo;
        multiset<double,greater<>> hi;
        for (i = 0; i < n; i ++) {
            lo.insert(nums[i]);
            hi.insert(*lo.rbegin());
            lo.erase(prev(lo.end()));
            if (hi.size() - lo.size() > 1) {
                lo.insert(*hi.rbegin());
                hi.erase(prev(hi.end()));
            }
            if (lo.size() + hi.size() == k) {
                if (k%2) {
                    ans[j] = *hi.rbegin();
                } else {
                    ans[j] = (*lo.rbegin() + *hi.rbegin())/2;
                }
                j += 1;
                auto it = lo.find(nums[i - k + 1]);
                if (it != lo.end()) {
                    lo.erase(it);
                    continue;
                }
                it = hi.find(nums[i - k + 1]);
                hi.erase(it);
            }
        }
        return ans;
    }
};
```

**Solution 3: (Multiset and Two Pointers)**

    nums = [ 1, 3,-1,-3, 5, 3, 6, 7], k = 3
window     [-1, 1, 3]
                m
           [-3,-1, 1, 3]
                   x  m
              [-3,-1, 3, 5]
                   m  x
                 [-3,-1, 3, 5]
                      x  m
                     [-3, 3, 5, 6]
                       x     m
                        [ 3, 5, 6, 7]
                             x
                
ans          1 -1 -1  3  5  6
```
Runtime: 47 ms, Beats 71.32%
Memory: 43.07 MB, Beats 58.70%
```
```c++
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> medians;
        multiset<int> window(nums.begin(), nums.begin() + k);

        auto mid = next(window.begin(), k / 2);

        for (int i = k;; i++) {

            // Push the current median
            medians.push_back(((double)(*mid) + *next(mid, k % 2 - 1)) * 0.5);

            // If all done, break
            if (i == nums.size())
                break;

            // Insert incoming element
            window.insert(nums[i]);
            if (nums[i] < *mid)
                mid--;                  // same as mid = prev(mid)

            // Remove outgoing element
            if (nums[i - k] <= *mid)
                mid++;                  // same as mid = next(mid)

            window.erase(window.lower_bound(nums[i - k]));
        }

        return medians;
    }
};
```
