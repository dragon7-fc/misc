1702. Maximum Binary String After Change

You are given a binary string binary consisting of only `0`'s or `1`'s. You can apply each of the following operations any number of times:

* Operation 1: If the number contains the substring `"00"`, you can replace it with `"10"`.
    * For example, `"00010" -> "10010"`
* Operation 2: If the number contains the substring `"10"`, you can replace it with `"01"`.
    * For example, `"00010" -> "00001"`

Return the maximum binary string you can obtain after any number of operations. Binary string `x` is greater than binary string `y` if `x`'s decimal representation is greater than `y`'s decimal representation.

 

**Example 1:**
```
Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
```

**Example 2:**
```
Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.
```

**Constraints:**

* `1 <= binary.length <= 10^5`
* `binary` consist of `'0'` and `'1'`.

# Submissions
---
**Solution 1: (Bit Manipulations)**

**Explanation**
We don't need touch the starting 1s, they are already good.

For the rest part,
we continuely take operation 2,
making the string like `00...00011...11`

Then we continuely take operation 1,
making the string like `11...11011...11`.


**Complexity**

* Time O(n)
* Space O(n)

```
Runtime: 64 ms
Memory Usage: 15.6 MB
```
```python
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if '0' not in binary: return binary
        k, n = binary.count('1', binary.find('0')), len(binary)
        return '1' * (n - k - 1) + '0' + '1' * k
```

```
Runtime: 156 ms
Memory: 40.8 MB
```

```c++
class Solution {
public:
    string maximumBinaryString(string binary) {
        int ones = 0, zeros = 0, n = binary.length();
        for (auto& c : binary) {
            if (c == '0')
                zeros++;
            else if (zeros == 0)
                ones++;
            c = '1';
        }
        if (ones < n)
            binary[ones + zeros - 1] = '0';
        return binary;
    }
};
```
