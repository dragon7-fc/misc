2222. Number of Ways to Select Buildings

You are given a **0-indexed** binary string s which represents the types of buildings along a street where:

* `s[i] = '0'` denotes that the `i`th building is an office and
* `s[i] = '1'` denotes that the `i`th building is a restaurant.

As a city official, you would like to **select** 3 buildings for random inspection. However, to ensure variety, **no two consecutive** buildings out of the **selected** buildings can be of the same type.

* For example, given `s = "001101"`, we cannot select the `1`st, `3`rd, and `5`th buildings as that would form `"011"` which is not allowed due to having two consecutive buildings of the same type.

Return the **number of valid ways** to select 3 buildings.

 

**Example 1:**
```
Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
``

**Example 2:**
```
Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
```

**Constraints:**

* `3 <= s.length <= 10^5`
* `s[i]` is either `'0'` or `'1'`.

# Submissions
```
**Solution 1: (DP Bottom-Up)**
```
Runtime: 1520 ms
Memory Usage: 15.2 MB
```
```c++
class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}
        for i in range(len(s)):
            if s[i] == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            if s[i] == "1":
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]
                
        return dp["010"] + dp["101"]
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 98 ms
Memory Usage: 24.4 MB
```
```c++
class Solution {
public:
    long long numberOfWays(string s) {
        long one = 0, zero = 0, oneZero = 0, zeroOne = 0, ways = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '0') {
                ++zero;
                oneZero += one; // Count in '10'.
                ways += zeroOne; // Count in '010'.
            }else {
                ++one;
                zeroOne += zero; // Count in '01'.
                ways += oneZero; // Count in '101'.
            }
        }
        return ways;
    }
};
```

**Solution 3: (prefix sum)**
```
Runtime: 83 ms
Memory: 24.6 MB
```
```c++
class Solution {
public:
    long long numberOfWays(string s) {
        int n = s.size(), zero = 0;
        for (int c: s) {
            zero += c == '0' ? 1 : 0;
        }
        int one = n - zero, zero_left = 0, one_left = 0;
        long long ans = 0;
        for (auto c: s) {
            if (c == '0') {
                zero -= 1;
                zero_left += 1;
                ans += one_left * one;
            } else {
                one -= 1;
                one_left += 1;
                ans += zero_left * zero;
            }
        }
        return ans;
    }
};
```
