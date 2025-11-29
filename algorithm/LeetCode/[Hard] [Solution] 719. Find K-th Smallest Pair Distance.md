719. Find K-th Smallest Pair Distance

Given an integer array, return the `k`-th smallest **distance** among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

**Example 1:**
```
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
```

**Note:**

* `2 <= len(nums) <= 10000`.
* `0 <= nums[i] < 1000000`.
* `1 <= k <= len(nums) * (len(nums) - 1) / 2`.

# Solution
---
## Approach #1: Heap [Time Limit Exceeded]
**Intuition and Algorithm**

Sort the points. For every point with index `i`, the pairs with indexes `(i, j)` [by order of distance] are `(i, i+1), (i, i+2), ..., (i, N-1)`.

Let's keep a heap of pairs, initially `heap = [(i, i+1) for all i]`, and ordered by distance (the distance of `(i, j)` is `nums[j] - nums[i]`.) Whenever we use a pair `(i, x)` from our heap, we will add `(i, x+1)` to our heap when appropriate.

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i+1)
                for i in xrange(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in xrange(k):
            d, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush((nums[nei + 1] - nums[root], root, nei + 1))

        return d
```

**Complexity Analysis**

* Time Complexity: $O((k+N) \log{N})$ where $N$ is the length of `nums`. As $k = O(N^2)$, this is $O(N^2 \log {N})$ in the worst case. The complexity added by our heap operations is either $O((k+N) \log N)$ in the Java solution, or $O(k \log{N} + N)$ in the Python solution because the `heapq.heapify` operation is linear time. Additionally, we add $O(N \log N)$ complexity due to sorting.

* Space Complexity: $O(N)$, the space used to store our heap of at most `N-1` elements.

## Approach #2: Binary Search + Prefix Sum [Accepted]
**Intuition**

Let's binary search for the answer. It's definitely in the range `[0, W]`, where `W = max(nums) - min(nums)]`.

Let `possible(guess)` be `true` if and only if there are `k` or more pairs with distance less than or equal to `guess`. We will focus on evaluating our `possible` function quickly.

**Algorithm**

Let `prefix[v]` be the number of points in `nums` less than or equal to `v`. Also, let `multiplicity[j]` be the number of points `i` with `i < j` and `nums[i] == nums[j]`. We can record both of these with a simple linear scan.

Now, for every point `i`, the number of points `j` with `i < j` and `nums[j] - nums[i] <= guess` is `prefix[x+guess] - prefix[x] + (count[i] - multiplicity[i])`, where `count[i]` is the number of ocurrences of `nums[i]` in `nums`. The sum of this over all `i` is the number of pairs with distance `<= guess`.

Finally, because the sum of `count[i] - multiplicity[i]` is the same as the sum of `multiplicity[i]`, we could just replace that term with `multiplicity[i]` without affecting the answer. (Actually, the sum of multiplicities in total will be a constant used in the answer, so we could precalculate it if we wanted.)

In our Java solution, we computed `possible = count >= k` directly in the binary search instead of using a helper function.

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            return sum(prefix[min(x + guess, W)] - prefix[x] + multiplicity[i]
                       for i, x in enumerate(nums)) >= k

        nums.sort()
        W = nums[-1]

        #multiplicity[i] = number of nums[j] == nums[i] (j < i)
        multiplicity = [0] * len(nums)
        for i, x in enumerate(nums):
            if i and x == nums[i-1]:
                multiplicity[i] = 1 + multiplicity[i - 1]

        #prefix[v] = number of values <= v
        prefix = [0] * (W + 1)
        left = 0
        for i in xrange(len(prefix)):
            while left < len(nums) and nums[left] == i:
                left += 1
            prefix[i] = left

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
```

**Complexity Analysis**

* Time Complexity: $O(W + N \log{W} + N \log{N})$, where $N$ is the length of `nums`, and $W$ is equal to `nums[nums.length - 1] - nums[0]`. We do $O(W)$ work to calculate prefix initially. The $\log W$ factor comes from our binary search, and we do $O(N)$ work inside our call to possible (or to calculate count in Java). The final $O(N\log N)$ factor comes from sorting.

* Space Complexity: $O(N+W)$, the space used to store multiplicity and prefix.


## Approach #3: Binary Search + Sliding Window [Accepted]
**Intuition**

As in Approach #2, let's binary search for the answer, and we will focus on evaluating our `possible` function quickly.

**Algorithm**

We will use a sliding window approach to count the number of pairs with distance `<= guess`.

For every possible `right`, we maintain the loop invariant: `left` is the smallest value such that `nums[right] - nums[left] <= guess`. Then, the number of pairs with `right` as it's right-most endpoint is `right - left`, and we add all of these up.

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
```

**Complexity Analysis**

* Time Complexity: $O(N \log{W} + N \log{N})$, where $N$ is the length of nums, and $W$ is equal to `nums[nums.length - 1] - nums[0]`. The $\log W$ factor comes from our binary search, and we do $O(N)$ work inside our call to possible (or to calculate count in Java). The final $O(N\log N)$ factor comes from sorting.

* Space Complexity: $O(1)$. No additional space is used except for integer variables.

# Submissions
---
**Solution 1: (Binary Search + Sliding Window)**
```
Runtime: 112 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
```

**Solution 2: (Binary Search + Sliding Window)**
```
Runtime: 5 ms
Memory: 12.88 MB
```
```c++
class Solution {
    // Count number of pairs with distance <= maxDistance using a moving window
    int countPairsWithMaxDistance(vector<int>& nums, int maxDistance) {
        int count = 0;
        int arraySize = nums.size();
        int left = 0;

        for (int right = 0; right < arraySize; ++right) {
            // Adjust the left pointer to maintain the window with distances <=
            // maxDistance
            while (nums[right] - nums[left] > maxDistance) {
                ++left;
            }
            // Add the number of valid pairs ending at the current right index
            count += right - left;
        }
        return count;
    }
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int arraySize = nums.size();

        // Initialize binary search range
        int low = 0;
        int high = nums[arraySize - 1] - nums[0];

        while (low < high) {
            int mid = (low + high) / 2;

            // Count pairs with distance <= mid
            int count = countPairsWithMaxDistance(nums, mid);

            // Adjust binary search bounds based on count
            if (count < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
};
```

**Solution 3: (Binary Search + Sliding Window)**
```
Runtime: 6 ms, Beats 35.32%
Memory: 14.04 MB, Beats 33.30%
```
```c++
class Solution {
    bool check(int mid, int k, vector<int> &nums) {
        int n = nums.size(), i = 0, j, ck = 0;
        for (j = 1; j < n; j ++) {
            while (nums[j] - nums[i] > mid) {
                i += 1;
            }
            ck += j - i;
        }
        return ck >= k;
    }
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.back() - nums[0], mid, ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (!check(mid, k, nums)) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
