3960. Frequency Balance Subarray

You are given an integer array `nums`.

Define a frequency balance **subarray** as follows:

* If the subarray contains only one distinct value, it is frequency balanced.
* Otherwise, there must exist a positive integer `f` such that every distinct value in the subarray occurs either `f` or `2 * f` times, and both **frequencies** occur among the distinct values.

Return an integer denoting the length of the **longest** frequency balance subarray.

 

**Example 1:**
```
Input: nums = [1,2,2,1,2,3,3,3]

Output: 5

Explanation:

The longest frequency balance subarray is [2, 1, 2, 3, 3].
The elements that appear most frequently are 2 and 3, both appearing twice.
The remaining element 1 appears once, meeting the requirements.
```

**Example 2:**
```
Input: nums = [5,5,5,5]

Output: 4

Explanation:

The longest frequency balance subarray is [5, 5, 5, 5].
The element that appears most frequently is 5.
There are no other elements meeting the requirements.
```

**Example 3:**
```
Input: nums = [1,2,3,4]

Output: 1

Explanation:

Since all elements appear only once, the length of the longest frequency balance subarray is 1.
```
 

**Constraints:**

* `1 <= nums.length <= 10^3`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Brute Force, Counter)**
```
Runtime: 1620 ms, Beats 31.91%
Memory: 473.05 MB, Beats 37.53%
```
```c++
class Solution {
public:
    int getLength(vector<int>& nums) {
        int n = nums.size();
        int ans = 1;
        for (int i = 0; i < n; i ++) {
            unordered_map<int, int> cnt;
            unordered_map<int, int> freq;
            for (int j = i; j < n; j ++) {
                if (cnt.count(nums[j])) {
                    freq[cnt[nums[j]]] -= 1;
                    if (freq[cnt[nums[j]]] == 0) {
                        freq.erase(cnt[nums[j]]);
                    }
                }
                cnt[nums[j]] += 1;
                freq[cnt[nums[j]]] += 1;
                if (cnt.size() == 1) {
                    ans = max(ans, j - i + 1);
                } else if (cnt.size() > 1 && freq.size() == 2) {
                    int mn = min(freq.begin()->first, next(freq.begin())->first);
                    int mx = max(freq.begin()->first, next(freq.begin())->first);
                    if (mx == mn * 2) {
                        ans = max(ans, j - i + 1);
                    }
                }
            }
        }

        return ans;
    }
};
```
