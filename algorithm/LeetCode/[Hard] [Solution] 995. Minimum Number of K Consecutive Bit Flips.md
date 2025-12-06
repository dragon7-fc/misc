995. Minimum Number of K Consecutive Bit Flips

In an array A containing only 0s and 1s, a `K`-bit flip consists of choosing a (contiguous) subarray of length `K` and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of `K`-bit flips required so that there is no 0 in the array.  If it is not possible, return `-1`.

 

**Example 1:**
```
Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
```

**Example 2:**
```
Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
```

**Example 3:**
```
Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
``` 

**Note:**

* `1 <= A.length <= 30000`
* `1 <= K <= A.length`

# Solution
---
## Approach 1: Greedy + Events
**Intuition**

If the leftmost element is a 0, we must flip the subarray starting at index 0. Similarly, if the leftmost element is a 1, we should not flip the subarray starting at index 0. This proves we can proceed in a greedy manner: after finding out whether we have to flip the first subarray (positions 0 to K-1) or not, we can consider the array with the first element (value 1) removed, and repeat this process.

We can do better. Every time we flip a subarray `A[i], A[i+1], ..., A[i+K-1]`, we can consider this as two "events", one 'opening event' at position i that marks the start of the subarray, and one 'closing event' at position `i+K` that marks the end of the subarray. Using these events, we always know how many overlapping flipped subarrays there are: its simply the number of opening events minus the number of closing events.

**Algorithm**

When we flip a subarray, let's call the set of indices we flipped an interval. We'll keep track of `flip`, the number of overlapping intervals in our current position. We only care about the value of `flip` modulo 2.

When we flip an interval starting at `i`, we create a `hint` for a closing event at `i+K` telling us to flip our writing state back.

Please see the inline comments for more details.

```python
class Solution(object):
    def minKBitFlips(self, A, K):
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
        # we can instead flip our current writing state, and put a hint at
        # position i+K to flip back our writing state.
        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:  # If we must flip the subarray starting here...
                ans += 1  # We're flipping the subarray from A[i] to A[i+K-1]
                if i+K > N: return -1  # If we can't flip the entire subarray, its impossible
                flip ^= 1  
                if i+K < N: hint[i + K] ^= 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Greedy + Events, Sliding Window)**
```
Runtime: 876 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
        # we can instead flip our current writing state, and put a hint at
        # position i+K to flip back our writing state.
        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:  # If we must flip the subarray starting here...
                ans += 1  # We're flipping the subarray from A[i] to A[i+K-1]
                if i+K > N: return -1  # If we can't flip the entire subarray, its impossible
                flip ^= 1  
                if i+K < N: hint[i + K] ^= 1

        return ans
```

**Solution 2: (Using an Auxiliary Array)**
```
Runtime: 81 ms
Memory: 108.61 MB
```
```c++
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        // Keeps track of flipped states
        vector<bool> flipped(nums.size(), false);
        // Tracks valid flips within the past window
        int validFlipsFromPastWindow = 0;
        // Counts total flips needed
        int flipCount = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (i >= k) {
                // Decrease count of valid flips from the past window if needed
                if (flipped[i - k]) {
                    validFlipsFromPastWindow--;
                }
            }

            // Check if current bit needs to be flipped
            if (validFlipsFromPastWindow % 2 == nums[i]) {
                // If flipping the window extends beyond the array length,
                // return -1
                if (i + k > nums.size()) {
                    return -1;
                }
                // Increment the count of valid flips and mark current as
                // flipped
                validFlipsFromPastWindow++;
                flipped[i] = true;
                flipCount++;
            }
        }

        return flipCount;
    }
};
```

**Solution 3: (Using a Deque)**
```
Runtime: 104 ms
Memory: 111.99 MB
```
```c++
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        // Queue to keep track of flips
        deque<int> flipQueue;
        // Current flip state
        int flipped = 0;
        // Total number of flips
        int result = 0;

        for (int i = 0; i < n; ++i) {
            // Remove the effect of the oldest flip if it's out of the current
            // window
            if (i >= k) {
                flipped ^= flipQueue.front();
                flipQueue.pop_front();
            }

            // If the current bit is 0 it needs to be flipped
            if (flipped == nums[i]) {
                // If we cannot flip a subarray starting at index i
                if (i + k > n) {
                    return -1;
                }
                // Add a flip at this position
                flipQueue.push_back(1);
                // Toggle the flipped state
                flipped ^= 1;
                // Increment the flip count
                result += 1;
            } else {
                flipQueue.push_back(0);
            }
        }

        return result;
    }
};
```

**Solution 4: (In Constant Space)**
```
Runtime: 88 ms
Memory: 108.57 MB
```
```c++
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        // Tracks the current number of flips
        int currentFlips = 0;
        // Tracks the total number of flips
        int totalFlips = 0;

        for (int i = 0; i < nums.size(); ++i) {
            // If the window slides out of the range and the leftmost element
            // is marked as flipped (2), decrement currentFlips
            if (i >= k && nums[i - k] == 2) {
                currentFlips--;
            }

            // Check if the current bit needs to be flipped
            if ((currentFlips % 2) == nums[i]) {
                // If flipping would exceed array bounds, return -1
                if (i + k > nums.size()) {
                    return -1;
                }
                // Mark the current bit as flipped
                nums[i] = 2;
                currentFlips++;
                totalFlips++;
            }
        }

        return totalFlips;
    }
};
```

**Solution 5: (Greedy, prefix sum, greedy min index element = 0)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 114.76 MB, Beats 40.30%
```
```c++
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size(), i, a = 0, ans = 0;
        vector<int> dp(n + 1);
        for (i = 0; i <= n - k; i ++) {
            a += dp[i];
            if ((a + nums[i]) % 2 == 0) {
                ans += 1;
                a += 1;
                dp[i] += 1;
                dp[i + k] -= 1;
            }
        }
        for (i = n - k + 1; i < n; i ++) {
            a += dp[i];
            if ((a + nums[i]) % 2 == 0) {
                return -1;
            }
        }
        return ans;
    }
};
```
