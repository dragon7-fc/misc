683. K Empty Slots

You have `n` bulbs in a row numbered from `1` to `n`. Initially, all the bulbs are turned off. We turn on exactly one bulb every day until all bulbs are on after `n` days.

You are given an array bulbs of length `n` where `bulbs[i] = x` means that on the `(i+1)`th day, we will turn on the bulb at position `x` where `i` is **0-indexed** and `x` is **1-indexed**.

Given an integer `k`, return the **minimum day number** such that there exists two turned on bulbs that have **exactly** `k` bulbs between them that are **all turned off**. If there isn't such day, return `-1`.

 

**Example 1:**
```
Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
Example 2:

Input: bulbs = [1,2,3], k = 1
Output: -1
```

**Constraints:**

* `n == bulbs.length`
* `1 <= n <= 2 * 10^4`
* `1 <= bulbs[i] <= n`
* `bulbs` is a permutation of numbers from `1` to `n`.
* `0 <= k <= 2 * 10^4`

# Submissions
---
**Solution 1: (Set, sorted set)**
```
Runtime: 40 ms, Beats 62.22%
Memory: 94.48 MB, Beats 36.67%
```
```c++
class Solution {
public:
    int kEmptySlots(vector<int>& bulbs, int k) {
        int n = bulbs.size(), i;
        set<int> st;
        for (i = 0; i < n; i ++) {
            auto it = st.insert(bulbs[i]).first;
            if (it != st.begin() && bulbs[i] - *prev(it) == k+1 || next(it) != st.end() && *next(it) - bulbs[i] == k+1) {
                return i+1;
            }
            
        }
        return -1;
    }
};
```

**Solution 2: (Sliding Window)**
```
Runtime: 4 ms, Beats 94.44%
Memory: 88.34 MB, Beats 70.00%
```
```c++
class Solution {
public:
    int kEmptySlots(vector<int>& bulbs, int k) {
        vector<int> days(bulbs.size());
        for(int i=0; i<bulbs.size();i++)days[bulbs[i] - 1] = i + 1;
        int left = 0, right = k + 1, res = INT_MAX;
        for(int i = 0; right < days.size(); i++){
            if(days[i] < days[left] || days[i] <= days[right]){   
                if(i == right)res = min(res, max(days[left], days[right]));    //we get a valid subarray
                left = i, right = k + 1 + i;
            }
        }
        return (res == INT_MAX)?-1:res;
    }
};
```
