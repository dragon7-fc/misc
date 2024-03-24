1124. Longest Well-Performing Interval

We are given `hours`, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

**Example 1:**
```
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
```

**Constraints:**

* `1 <= hours.length <= 10000`
* `0 <= hours[i] <= 16`

# Submissions
---
**Solution 1: (Stack)**

You may have noticed that almost all O(n) hashmap solution posts are based on the +1, -1 property. And these solutions try to find a longest subarrary with sum > 0.

Here I propose a more generalized problem and a solution to it.

**Problem:**

* input: arrary arr in which elements are arbitrary integers.
* output: length of a longest subarray arr[i, j) with sum(arr[i], ... , arr[j-1]) >= K.

**Solution:**

* Compute prefix sum of arr as prefixSum so that prefixSum[j] - prefixSum[i] = sum(arr[i], ... arr[j-1])
* Iterate through prefixSum from begin to end and build a **strictly monotone decreasing stack** smdStack. (smdStack.top() is the smallest)
* Iterate through prefixSum from end to begin. For each prefixSum[i], while smdStack.top() is less than prefixSum[i] by at least K, pop smdStackand try to update result by subarray [index of top,i). Until top element is not less than it by K.
Return result.

**Time complexity: O(n)**

* step1, compute prefixSum O(n)
* step2, build strictly monotone decreasing stack O(n)
* step3, iterate prefixSum O(n). pop top elements in smdStack O(n)

```
Runtime: 232 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        N = len(hours)
        prefixSum = [0] * (N+1)
        for i in range(1, N+1):
            prefixSum[i] = prefixSum[i-1] + (1 if hours[i-1] > 8 else -1)
        stack = []  ## mono dec stack
        for i in range(N+1):
            if not stack or prefixSum[stack[-1]] > prefixSum[i]:
                # Trick, store index than value.
                stack.append(i)
        res = 0
        for j in range(N, -1, -1):
            while stack and prefixSum[stack[-1]] < prefixSum[j]:
                res = max(res, j - stack[-1])
                stack.pop()
                          
        return res
```

**Solution 2: (Greedy, Hash Table)**

__Intuition__
If working hour > 8 hours, yes it's tiring day.
But I doubt if 996 is a well-performing interval.
Life needs not only 996 but also 669.


__Explanation__
We starts with a score = 0,
If the working hour > 8, we plus 1 point.
Otherwise we minus 1 point.
We want find the maximum interval that have strict positive score.

After one day of work, if we find the total score > 0,
the whole interval has positive score,
so we set res = i + 1.

If the score is a new lowest score, we record the day by seen[cur] = i.
seen[score] means the first time we see the score is seen[score]th day.

We want a positive score, so we want to know the first occurrence of score - 1.
score - x also works, but it comes later than score - 1.
So the maximum interval is i - seen[score - 1]


__Complexity__
Time O(N) for one pass.
Space O(N) in worst case if no tiring day.

```
Runtime: 17 ms
Memory: 23.42 MB
```
```c++
class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int res = 0, score = 0, n = hours.size();
        unordered_map<int, int> seen;
        for (int i = 0; i < n; ++i) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) {
                res = i + 1;
            } else {
                if (seen.find(score) == seen.end())
                    seen[score] = i;
                if (seen.find(score - 1) != seen.end())
                    res = max(res, i - seen[score - 1]);
            }
        }
        return res;
    }
};
```
