401. Binary Watch

A binary watch has 4 LEDs on the top which represent the **hours (0-11)**, and the 6 LEDs on the bottom represent the **minutes (0-59)**.

Each LED represents a zero or one, with the least significant bit on the right.

![401_Binary_clock_samui_moon.jpg](img/401_Binary_clock_samui_moon.jpg)

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

**Example:**
```
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
```

**Note:**

* The order of output does not matter.
* The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
* The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return ["{:d}:{:02d}".format(h, m)
               for h in range(12) for m in range(60)
               if (bin(h) + bin(m)).count('1') == num]
```

**Solution 2: (Enumerating Hours and Minutes)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.57 MB, Beats 85.28%
```
```c++
class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> ans;
        for (int h = 0; h < 12; ++h) {
            for (int m = 0; m < 60; ++m) {
                if (__builtin_popcount(h) + __builtin_popcount(m) == turnedOn) {
                    ans.push_back(to_string(h) + ":" + (m < 10 ? "0" : "") +
                                  to_string(m));
                }
            }
        }
        return ans;
    }
};
```

**Solution 3: (Binary Enumeration)**

           9 8 7 6 5 4 3 2 1 0
    1023 = 1 1 1 1 1 1 1 1 1 1
           ^^^^^^^ ^^^^^^^^^^^
              h         m

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.76 MB, Beats 41.32%
```
```c++
class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> ans;
        for (int i = 0; i < 1024; ++i) {
            int h = i >> 6, m = i & 63;  // Extract the high 4 bits and low 6
                                         // bits using bitwise operations
            if (h < 12 && m < 60 && __builtin_popcount(i) == turnedOn) {
                ans.push_back(to_string(h) + ":" + (m < 10 ? "0" : "") +
                              to_string(m));
            }
        }
        return ans;
    }
};
```
