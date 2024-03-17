57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

**Example 1:**
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Submissions
---
**Solution 1: (Sort, Greedy, Stack)**
```
Runtime: 80 ms
Memory Usage: 17 MB
```
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        ans = [intervals[0]]

        for s, e in intervals[1:]:
            top = ans[-1]
            if top[1] >= s:
                # tops' end is earlier than the start
                ans.pop()
                top[1] = max(e, top[1])
                ans.append(top)
            else:
                ans.append([s, e])

        return ans
```

**Solution 2: (Greedy)**
```
Runtime: 16 ms
Memory Usage: 8.4 MB
```
```c

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes){
    *returnSize = 0;
    int left = newInterval[0];
    int right = newInterval[1];
    bool placed = false;
    int* tmp;
    // One unit larger than the original intervals (since one interval could be added)
    int** result = malloc(sizeof(int*) * (intervalsSize + 1));
    *returnColumnSizes = malloc(sizeof(int*) * (intervalsSize + 1));
    // Iterate through all available intervals
    for (int i = 0; i < intervalsSize; i++)
    {
        int* interval = intervals[i];
        // Check right boundary, if no overlap, add it to the left
        if (interval[0] > right)
        {

            // Check if new interval is been placed or not
            if (!placed)
            {
                // Need mallocate since we want to return this temp value
                tmp = malloc(sizeof(int) * 2);
                // Add the new interval to the result first
                tmp[0] = left; tmp[1] = right;
                // Update return column size array with the (left, right)
                (*returnColumnSizes)[*returnSize] = 2;
                result[(*returnSize)++] = tmp;
                placed = true;
            }
            // If the new interval is been added, copy the interval to the result
            tmp = malloc(sizeof(int) * 2);
            memcpy(tmp, interval, sizeof(int) * 2);
            // Update return column size array with the (left, right)
            (*returnColumnSizes)[*returnSize] = 2;
            result[(*returnSize)++] = tmp;
        }
        // Check for left boundary
        else if (interval[1] < left)
        {
            // Copy the original interval, insert the interval latter
            tmp = malloc(sizeof(int) * 2);
            memcpy(tmp, interval, sizeof(int) * 2);
            // Update return column size array with the (left, right)
            (*returnColumnSizes)[*returnSize] = 2;
            result[(*returnSize)++] = tmp;
        }
        // When overlap
        else
        {
            // Update the combined boundaries
            left = fmin(left, interval[0]);
            right = fmax(right, interval[1]);
        }
    }
    // If the new interval should be added to the end
    if (!placed)
    {
        // Copy the original interval, insert the interval latter
        tmp = malloc(sizeof(int) * 2);
        tmp[0] = left; tmp[1] = right;
        // Update return column size array with the (left, right)
        (*returnColumnSizes)[*returnSize] = 2;
        result[(*returnSize)++] = tmp;
    }
    return result;
 }
```

**Solution 3: (Binary Search)**
```
Runtime: 91 ms
Memory: 17.3 MB
```
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        i = j = bisect.bisect_left(intervals, newInterval)
        if N == 0 or i == 0 and intervals[i][0] > newInterval[1] or i == N and intervals[i-1][1] < newInterval[0] or 0 < i < N and intervals[i-1][1] < newInterval[0] and intervals[i][0] > newInterval[1]:
            intervals.insert(i, newInterval)
            return intervals
        left = newInterval[0]
        while i-1 >= 0 and left <= intervals[i-1][1]:
            i -= 1
        left = min(left, intervals[i][0])
        right = newInterval[1]
        while j < N and right >= intervals[j][0]:
            j += 1
        right = max(right, intervals[j-1][1])
        intervals[i:j] = [[left, right]]
        return intervals
```

**Solution 4: (Binary Search, Greedy)**
```
Runtime: 83 ms
Memory: 17.3 MB
```
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort_left(intervals, newInterval)
        ans = [intervals[0]]
        for s, e in intervals[1:]:
            cur = ans[-1]
            if cur[1] >= s:
                ans.pop()
                cur[1] = max(e, cur[1])
                ans += [cur]
            else:
                ans += [[s, e]]

        return ans
```

**Solution 5: (Binary Search)**
```
Runtime: 7 ms
Memory: 20.43 MB
```
```c++
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // If the intervals vector is empty, return a vector containing the newInterval
        if (intervals.empty()) {
            return {newInterval};
        }

        int n = intervals.size();
        int target = newInterval[0];
        int left = 0, right = n - 1;

        // Binary search to find the position to insert newInterval
        while (left <= right) {
            int mid = (left + right) / 2;
            if (intervals[mid][0] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // Insert newInterval at the found position
        intervals.insert(intervals.begin() + left, newInterval);

        // Merge overlapping intervals
        vector<vector<int>> res;
        for (const auto& interval : intervals) {
            // If res is empty or there is no overlap, add the interval to the result
            if (res.empty() || res.back()[1] < interval[0]) {
                res.push_back(interval);
            // If there is an overlap, merge the intervals by updating the end of the last interval in res
            } else {
                res.back()[1] = max(res.back()[1], interval[1]);
            }
        }

        return res;
    }
};
```
