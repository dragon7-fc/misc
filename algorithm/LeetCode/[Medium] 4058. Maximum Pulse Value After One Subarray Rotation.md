4058. Maximum Pulse Value After One Subarray Rotation

You are given an integer array `nums` of length `n`.

Define the **pulse value** of an integer array `arr` as the **alternating sum** starting at index 0: `pulse(arr) = arr[0] - arr[1] + arr[2] - arr[3] + ....`

You may perform **at most** one operation on `nums`:

* Choose two indices `l` and `r` such that `0 <= l < r < n`.
* Left-rotate the **subarray** `nums[l..r]` by exactly one position. For example, `[a, b, c, d]` becomes `[b, c, d, a]`.
Return the **maximum pulse value** that can be obtained after performing **at most** one such operation.

 

**Example 1:**
```
Input: nums = [1,5,2]

Output: 6

Explanation:

The original pulse value is 1 - 5 + 2 = -2.
Rotate the subarray nums[0..1] from [1, 5] to [5, 1].
The resulting array is [5, 1, 2] and its pulse value is 5 - 1 + 2 = 6, which is the maximum possible.
```

**Example 2:**
```
Input: nums = [6,4,3]

Output: 7

Explanation:

The original pulse value is 6 - 4 + 3 = 5.
Rotate the subarray nums[1..2] from [4, 3] to [3, 4].
The resulting array is [6, 3, 4] and its pulse value is 6 - 3 + 4 = 7, which is the maximum possible.
```

**Example 3:**
```
Input: nums = [9,7]

Output: 2

Explanation:

The original pulse value is 9 - 7 = 2, which is already maximum. Thus, no rotation is required.
```
 

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 4 ms, Beats 71.51%
Memory: 143.81 MB, Beats 62.04%
```
```c++
class Solution {
public:
    long long maxValue(vector<int>& nums) {
        int n = nums.size();
        long long diff = 1e18;
        long long pref = 0;
        long long e = 0;
        long long o = -1e18;
        for (int i = 0; i < n; i++) {
            // Alternating prefix sum
            pref += (i % 2 == 0 ? nums[i] : -nums[i]);
            if ((i + 1) % 2 == 0) {
                diff = min(pref - e, diff);
                e = max(e, pref);
            } else {
                diff = min(pref - o, diff);
                o = max(o, pref);
            }
        }
        // Apply the best possible improvement
        pref -= (2 * min(0LL, diff));

        return pref;
    }
};
```

**Solution 2: (Prefix Sum Parity & Subarray Flipping)**

__Intuition__
To find the maximum possible pulse value after at most one left-rotation, we need to understand exactly how a left-rotation alters the alternating sum (the "pulse").

Consider what happens when we left-rotate a subarray [l…r]:

If the subarray has an even length, every element shifts to an index with a different parity (e.g., an element at an even index moves to an odd index). Consequently, the sign of every single element in this subarray flips!
If the subarray has an odd length, the first element moves to the end (which shares the same parity as its original position), so its sign remains unchanged. The rest of the elements shift left, flipping their signs. Mathematically, the net change in the pulse is identical to simply left-rotating the even-length subarray [l+1…r].
Because odd-length rotations offer no unique advantage over even-length rotations, we only need to evaluate even-length subarrays.

Flipping the signs of all elements in a subarray changes its total contribution from S to −S. The net change to the entire array's pulse is exactly −2S. To maximize the final pulse, we must find an even-length subarray with the most negative possible pulse sum, which will yield the largest +2S boost.

__Approach__
Prefix Pulse Tracking: Let P[i] be the prefix pulse sum up to index i.
Evaluating Subarray Gain: The pulse of a subarray [l…r] is P[r]−P[l−1].
Flipping this subarray gives a net change of −2×(P[r]−P[l−1])=2×(P[l−1]−P[r]).
Since we only care about even-length subarrays, r and l must have different parities. This means r and l−1 must have the same parity.
Max-Min Optimization: To maximize P[l−1]−P[r], we should keep track of the highest P[l−1] seen so far, strictly separated by parity (even or odd).
Single Pass Algorithm:
Iterate through the array while maintaining the running prefix pulse ans.
Maintain maxe (maximum prefix pulse at even indices) and maxo (maximum prefix pulse at odd indices). Note: maxo is initialized to 0 because an empty prefix before index 0 conceptually acts as an "odd" index value P[−1]=0.
At each step, calculate the potential gain by subtracting the current prefix pulse ans from the maximum previous prefix pulse of the same parity.
Keep track of the largest possible gain maxi.
Final Result: The maximum pulse value is the original total pulse (ans at the end of the loop) plus 2×maximum gain (maxi).

__Complexity__
Time Complexity: O(N).
Space Complexity: O(1).

```
Runtime: 0 ms, Beats 100.00%
Memory: 143.61 MB, Beats 93.52%
```
```c++
class Solution {
public:
    long long maxValue(vector<int>& nums) {
        int n = nums.size();

        // ans: Running prefix pulse (alternating sum)
        // maxi: Maximum achievable gain (P[l-1] - P[r])
        // maxo: Maximum prefix pulse seen at odd indices (or -1 for the empty prefix)
        // maxe: Maximum prefix pulse seen at even indices
        long long ans = 0, maxi = 0, maxo = 0, maxe = -1e15;
        
        for(int i = 0; i < n; ++i) {
            if(i & 1) { // Current index is odd
                ans -= nums[i];
                // Max gain ending at this odd index relies on a previous odd index
                maxi = max(maxi, maxo - ans);
                // Update the maximum prefix pulse for odd indices
                maxo = max(maxo, ans);
            } else { // Current index is even
                ans += nums[i];
                // Max gain ending at this even index relies on a previous even index
                maxi = max(maxi, maxe - ans);
                // Update the maximum prefix pulse for even indices
                maxe = max(maxe, ans);
            }
        }
        
        // Return original total pulse + (2 * optimal subarray change)
        return ans + 2 * maxi;
    }
};
```
