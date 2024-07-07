728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, `128` is a self-dividing number because `128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0`.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

**Example 1:**
```
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
```

**Note:**

* The boundaries of each input argument are `1 <= left <= right <= 10000`.

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition and Algorithm**

For each number in the given range, we will directly test if that number is self-dividing.

By definition, we want to test each whether each digit is non-zero and divides the number. For example, with `128`, we want to test `d != 0` && `128 % d == 0` for `d = 1, 2, 8`. To do that, we need to iterate over each digit of the number.

A straightforward approach to that problem would be to convert the number into a character array (string in Python), and then convert back to integer to perform the modulo operation when checking `n % d == 0`.

We could also continually divide the number by 10 and peek at the last digit. That is shown as a variation in a comment.

```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        """
        Alternate implementation of self_dividing:
        def self_dividing(n):
            x = n
            while x > 0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True
        """
        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans #Equals filter(self_dividing, range(left, right+1))
```

**Complexity Analysis**

* Time Complexity: $O(D)$, where $D$ is the number of integers in the range $[L, R]$, and assuming $\log(R)$ is bounded. (In general, the complexity would be $O(D\log R)$.)

* Space Complexity: $O(D)$, the length of the answer.

# Submissions
---
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        """
        Alternate implementation of self_dividing:
        def self_dividing(n):
            x = n
            while x > 0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True
        """
        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans #Equals filter(self_dividing, range(left, right+1))
```

**Solution 2: (Brute Force)**
```
Runtime: 0 ms
Memory: 7.59 MB
```
```c++
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        int d, ca;
        for (int a = left; a <= right; a++) {
            ca = a;
            while (ca) {
                d = ca%10;
                if (d == 0 || a%d) {
                    break;
                }
                ca /= 10;
            }
            if (ca == 0) {
                ans.push_back(a);
            }
        }
        return ans;
    }
};
```
