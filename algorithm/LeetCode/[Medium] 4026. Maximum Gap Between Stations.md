4026. Maximum Gap Between Stations

You are given two strings `skill` and `station` of lengths `n` and `m`, respectively.

`skill[i]` represents the skill of worker `i`, and `station[j]` represents the skill supported by station `j`.

You must assign every worker to a distinct station. Let `j_i` be the index of the station assigned to worker `i`. A valid assignment must satisfy:

* `station[ji] == skill[i]` for every `0 <= i < n`.
* The assigned station indices must be **strictly** increasing in worker order, meaning j`0 < j_1 < ... < j_(n - 1)`.

The **gap** of an assignment is the **maximum difference** between the station indices assigned to two consecutive workers. In other words, it is `max(j_i - j_(i - 1))` over all `1 <= i < n`.

If there is only one worker, the gap is 0.

Return the **maximum** possible gap among all valid assignments. It is guaranteed that at least one valid assignment exists.

 

**Example 1:**
```
Input: skill = "aa", station = "aaaa"

Output: 3

Explanation:

The two workers must be assigned to two different 'a' stations.
Assigning them to stations [0, 3] gives a gap of 3.
```

**Example 2:**
```
Input: skill = "xyz", station = "xyzz"

Output: 2

Explanation:

Assign worker 0 to station j = 0, and worker 1 to station j = 1.
To maximize the gap, assign worker 2 to station j = 3.
This gives the assignment [0, 1, 3] with gaps [1, 2], so the gap is 2.
```

**Example 3:**
```
Input: skill = "cbc", station = "cbcdbc"

Output: 4

Explanation:

Assign worker 0 to station j = 0, and worker 1 to station j = 1.
To maximize the gap, assign worker 2 to station j = 5.
This gives the assignment [0, 1, 5] with gaps [1, 4], so the gap is 4.
```

**Constraints:**

* `skill.length == n`
* `station.length == m`
* `1 <= n <= m <= 10^5`
* `skill` and `station` consist of lowercase English letters.
* It is guaranteed that a valid assignment exists for every worker.

# Submissions
---
**Solution 1: (Prefix Sum, latest - earliest)**
```
Runtime: 56 ms, Beats 52.70%
Memory: 72.19 MB, Beats 81.11%
```
```c++
class Solution {
public:
    int maximumGap(string skill, string station) {
        int n = skill.length();
        int m = station.length();
        int j;

        vector<int> left(n);
        j = 0;
        for (int i = 0; i < n; i ++) {
            while (station[j] != skill[i]) {
                j += 1;
            }
            left[i] = j;
            j += 1;
        }

        vector<int> right(n);
        j = m - 1;
        for (int i = n - 1; i >= 0; --i) {
            while (station[j] != skill[i]) {
                j -= 1;
            }
            right[i] = j;
            j -= 1;
        }

        int res = 0;
        for (int i = 0; i < n - 1; ++i) {
            res = max(res, right[i + 1] - left[i]);
        }
        return res;
    }
};
```
