3339. Find the Number of K-Even Arrays

You are given three integers `n`, `m`, and `k`.

An array arr is called **k-even** if there are exactly `k` indices such that, for each of these indices `i` (`0 <= i < n - 1`):

* `(arr[i] * arr[i + 1]) - arr[i] - arr[i + 1]` is even.

Return the number of possible **k-even** arrays of size n where all elements are in the range [1, m].

Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: n = 3, m = 4, k = 2

Output: 8

Explanation:

The 8 possible 2-even arrays are:

[2, 2, 2]
[2, 2, 4]
[2, 4, 2]
[2, 4, 4]
[4, 2, 2]
[4, 2, 4]
[4, 4, 2]
[4, 4, 4]
```

**Example 2:**
```
Input: n = 5, m = 1, k = 0

Output: 1

Explanation:

The only 0-even array is [1, 1, 1, 1, 1].
```

**Example 3:**
```
Input: n = 7, m = 7, k = 5

Output: 5832
```
 

**Constraints:**

* `1 <= n <= 750`
* `0 <= k <= n - 1`
* `1 <= m <= 1000`

# Submissions
---
**Solution 1: (DP Bottom-Up)**

    o * o - o - o = o
    o * e - o - e = o
    e * o - e - o = o
    e * e - e - e = e

    o o -> o
    e o -> o
    o e -> o
 >  e e -> e

```
Runtime: 15 ms, Beats 83.33%
Memory: 10.42, MB Beats 66.67%
```
```c++
class Solution {
public:
    int countOfArrays(int n, int m, int k) {
        int modulo = 1000000007;
        // total odd number count is (m+1)/2 ; total even number count is (m/2)
        int odd_count = (m+1)/2, even_count = (m/2);
        // dp_odd[j] -> j-even array which ends with odd number
        // dp_even[j] -> j-even array which ends with even number
        vector<long> dp_odd(k+1), dp_even(k+1);
        // the number of 0-even array ends with odd number is odd_count
        dp_odd[0] = odd_count;
        // the number of 0-even array ends with even number is even_count
        dp_even[0] = even_count;
        for (int i = 1 ; i < n; i++){
            for (int j = k; j >= 0; j--){
                long tmp = dp_odd[j];
                dp_odd[j] = ((dp_even[j] + dp_odd[j]) * odd_count) % modulo;
                if (j > 0)
                    dp_even[j] = ((dp_even[j-1] + tmp )* even_count) % modulo;
                else
                    dp_even[j] = ( tmp * even_count) % modulo;
            }
        }
        return (dp_odd[k] + dp_even[k]) % modulo;
    }
};
```
