3649. Number of Perfect Pairs

You are given an integer array `nums`.

A pair of indices `(i, j)` is called **perfect** if the following conditions are satisfied:

* `i < j`
* Let `a = nums[i], b = nums[j]`. Then:
    * `min(|a - b|, |a + b|) <= min(|a|, |b|)`
    * `max(|a - b|, |a + b|) >= max(|a|, |b|)`

Return the number of **distinct** perfect pairs.

**Note**: The absolute value `|x|` refers to the non-negative value of `x`.

 

**Example 1:**
```
Input: nums = [0,1,2,3]

Output: 2

Explanation:

There are 2 perfect pairs:

(i, j)	(a, b)	min(|a − b|, |a + b|)	min(|a|, |b|)	max(|a − b|, |a + b|)	max(|a|, |b|)
(1, 2)	(1, 2)	min(|1 − 2|, |1 + 2|) = 1	1	max(|1 − 2|, |1 + 2|) = 3	2
(2, 3)	(2, 3)	min(|2 − 3|, |2 + 3|) = 1	2	max(|2 − 3|, |2 + 3|) = 5	3
```

**Example 2:**
```
Input: nums = [-3,2,-1,4]

Output: 4

Explanation:

There are 4 perfect pairs:

(i, j)	(a, b)	min(|a − b|, |a + b|)	min(|a|, |b|)	max(|a − b|, |a + b|)	max(|a|, |b|)
(0, 1)	(-3, 2)	min(|-3 - 2|, |-3 + 2|) = 1	2	max(|-3 - 2|, |-3 + 2|) = 5	3
(0, 3)	(-3, 4)	min(|-3 - 4|, |-3 + 4|) = 1	3	max(|-3 - 4|, |-3 + 4|) = 7	4
(1, 2)	(2, -1)	min(|2 - (-1)|, |2 + (-1)|) = 1	1	max(|2 - (-1)|, |2 + (-1)|) = 3	2
(1, 3)	(2, 4)	min(|2 - 4|, |2 + 4|) = 2	2	max(|2 - 4|, |2 + 4|) = 6	4
```

**Example 3:**
```
Input: nums = [1,10,100,1000]

Output: 0

Explanation:

There are no perfect pairs. Thus, the answer is 0.
```
 

**Constraints:**

* `2 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Math, Sort)**

How We Got Here
The brute force solution checks each pair, but that is too slow. To optimize, we analyze the condition carefully:

min(|a - b|, |a + b|) <= min(|a|, |b|)
AND
max(|a - b|, |a + b|) >= max(|a|, |b|)
Take absolute values of all numbers (because the conditions are symmetric for positive/negative).
After simplification, this condition essentially boils down to:
For two values x = |a| and y = |b|:
   x/2 <= y <= 2x
with the help of properties

min(∣a−b∣,∣a+b∣)= ∣ ∣a∣−∣b∣ |
 

min(∣a∣,∣b∣)= 1/2 (∣∣a+b∣−∣a−b∣∣)

This means: one number must lie within half to double the other.

Steps
Convert all numbers to their absolute values.

Sort the array.

For each number arr[i], we need to count how many arr[j] (j > i) satisfy arr[j] <= 2*arr[i].

Since the array is sorted, we can use a two-pointer approach.
Maintain a right pointer r that moves as long as arr[r] <= 2*arr[i].
For each i, add (r - i) to the count.
This ensures we don’t re-check pairs unnecessarily.

Complexity
Time: O(n log n) (sorting + linear two-pointer scan).
Space: O(n).

```
Runtime: 51 ms, Beats 88.89%
Memory: 157.30 MB, Beats 33.33%
```
```c++
typedef long long ll;

class Solution {
public:
    long long perfectPairs(vector<int>& nums) {
        int n = nums.size();
        vector<ll> arr;
        for (auto it : nums) arr.push_back(llabs(it));
        sort(arr.begin(), arr.end());

        ll cnt = 0;
        int r = 0;
        for (int i = 0; i < n; i++) {
            if (r < i) r = i;
            while (r + 1 < n && arr[r + 1] <= 2 * arr[i]) r++;
            cnt += (r - i);
        }
        return cnt;
    }
};
```
