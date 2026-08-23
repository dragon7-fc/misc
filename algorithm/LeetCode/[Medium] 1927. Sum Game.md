1927. Sum Game

Alice and Bob take turns playing a game, with **Alice starting first**.

You are given a string `num` of **even length** consisting of digits and `'?'` characters. On each turn, a player will do the following if there is still at least one `'?'` in `num`:

* Choose an index `i` where `num[i] == '?'`.
* Replace `num[i]` with any digit between `'0'` and `'9'`.

The game ends when there are no more `'?'` characters in `num`.

For Bob to win, the sum of the digits in the first half of `num` must be **equal** to the sum of the digits in the second half. For Alice to win, the sums must **not be equal**.

* For example, if the game ended with `num = "243801"`, then Bob wins because `2+4+3 = 8+0+1`. If the game ended with `num = "243803"`, then Alice wins because `2+4+3 != 8+0+3`.

Assuming Alice and Bob play **optimally**, return `true` if Alice will win and `false` if Bob will win.

 

**Example 1:**
```
Input: num = "5023"
Output: false
Explanation: There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
```

**Example 2:**
```
Input: num = "25??"
Output: true
Explanation: Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.
```

**Example 3:**
```
Input: num = "?3295???"
Output: false
Explanation: It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first '?' with '9'. num = "93295???".
- Bob replaces one of the '?' in the right half with '9'. num = "932959??".
- Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
- Bob replaces the last '?' in the right half with '7'. num = "93295927".
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.
```

**Constraints:**

* `2 <= num.length <= 10^5`
* `num.length` is even.
* `num` consists of only digits and `'?'`.

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 116 ms
Memory Usage: 15.4 MB
```
```python
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        # number of ?s
        a = b = 0

        # left sums and right sums
        l = r = 0

        # first half: counting ?s and sums
        for c in num[ : n // 2]:
            if c == "?":
                a += 1
            else:
                l += int(c)

        # second half: counting ?s and sums
        for c in num[n // 2 : ]:
            if c == "?":
                b += 1
            else:
                r += int(c)

        # Odd ?s, Alice will always win cuz she has the final say
        if (a + b) % 2 == 1:
            return True

        # The only situation Bob can win
        if l - r == 9 * (b - a) // 2:
            return False
        return True
```

**Solution 2: (Counter, Math, '??' should be 9. When Alice set 1 '?' to be x, Bob can set the other '?' to be 9-x. When the number of '?' is odd, Alice always wins)**
```
Runtime: 4 ms, Beats 47.55%
Memory: 15.37 MB, Beats 5.36%
```
```c++
class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();

        auto get = [](string&& s) -> pair<int, int> {
            int nn = 0, qq = 0;
            for (char ch : s) {
                if (ch == '?') {
                    ++qq;
                } else {
                    nn += (ch - '0');
                }
            }
            return {nn, qq};
        };

        auto [n0, q0] = get(num.substr(0, n / 2));
        auto [n1, q1] = get(num.substr(n / 2, n / 2));

        return ((q0 + q1) % 2 == 1) || (n0 - n1 != (q1 - q0) * 9 / 2);
                //Odd ?s, Alice will always win cuz she has the final say
                                       // The only situation Bob can win
    }
};
```

**Solution 3: (Counter, Math)**

case 1:
        sumL   sumR
         qL     qR
case 2:
        sumL
               sumR
                qR
         qL
case 3:
               sumR
        sumL
         qL
                qR
```
Runtime: 7 ms, Beats 21.45%
Memory: 14.09 MB, Beats 33.57%
```
```c++
class Solution {
public:
    bool sumGame(string num) {
        int n = num.length();
        int sumL = 0, sumR = 0;
        int qL = 0, qR = 0;

        for (int i = 0; i < n / 2; ++i) {
            if (num[i] == '?') qL++;
            else sumL += num[i] - '0';
        }

        for (int i = n / 2; i < n; ++i) {
            if (num[i] == '?') qR++;
            else sumR += num[i] - '0';
        }

        // Total remaining '?' difference must be even for Bob to balance them
        // And the sum difference must be offset by 9 * (delta_q / 2)
        return (2 * (sumL - sumR) != 9 * (qR - qL));
    }
};
```
