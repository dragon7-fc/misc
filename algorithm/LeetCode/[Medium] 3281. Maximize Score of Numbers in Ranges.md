3281. Maximize Score of Numbers in Ranges

You are given an array of integers `start` and an integer `d`, representing n intervals `[start[i], start[i] + d]`.

You are asked to choose `n` integers where the `ith` integer must belong to the `ith` interval. The score of the chosen integers is defined as the **minimum** absolute difference between any two integers that have been chosen.

Return the **maximum** possible score of the chosen integers.

 

**Example 1:**
```
Input: start = [6,0,3], d = 2

Output: 4

Explanation:

The maximum possible score can be obtained by choosing integers: 8, 0, and 4. The score of these chosen integers is min(|8 - 0|, |8 - 4|, |0 - 4|) which equals 4.
```

**Example 2:**
```
Input: start = [2,6,13,13], d = 5

Output: 5

Explanation:

The maximum possible score can be obtained by choosing integers: 2, 7, 13, and 18. The score of these chosen integers is min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|) which equals 5.
```
 

**Constraints:**

* `2 <= start.length <= 10^5`
* `0 <= start[i] <= 10^9`
* `0 <= d <= 10^9`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 203 ms
Memory: 109.62 MB
```
```c++
class Solution {
    bool check(const vector<int> &start, int d, int mid){
        long long prev = start[0], cur;
        for (int i=1 ;i < start.size(); i++) {
            cur = max(prev + mid, (long long)start[i]);
            if (cur > start[i] + d) { 
                return false;
            }
            prev = cur;
        }
        return true;
    }
public:
    int maxPossibleScore(vector<int>& start, int d) {
        int n = start.size();
        sort(start.begin(), start.end());
        int lo = 0, hi = start.back() - start.front() + d, mid;
        while (lo < hi) {
            mid = hi - (hi-lo)/2;
            if (!check(start, d, mid)){
                hi = mid-1;
            } else {
                lo = mid;
            }
        }

        return lo;
    }
};
```
