816. Ambiguous Coordinates

We had some 2-dimensional coordinates, like `"(1, 3)"` or `"(2, 0.5)"`.  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

**Example 1:**
```
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
```

**Example 2:**
```
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation: 
0.0, 00, 0001 or 00.01 are not allowed.
```

**Example 3:**
```
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
```

**Example 4:**
```
Input: "(100)"
Output: [(10, 0)]
Explanation: 
1.0 is not allowed.
```

**Note:**

* `4 <= S.length <= 12`.
* `S[0] = "("`, `S[S.length - 1] = ")"`, and the other elements in `S` are digits.

# Solution
---
## Approach #1: Cartesian Product [Accepted]
**Intuition and Algorithm**

For each place to put the comma, we separate the string into two fragments. For example, with a string like `"1234"`, we could separate it into fragments `"1"` and `"234"`, `"12"` and `"34"`, or `"123"` and `"4"`.

Then, for each fragment, we have a choice of where to put the period, to create a list `make(...)` of choices. For example, `"123"` could be made into `"1.23"`, `"12.3"`, or `"123"`.

Because of extranneous zeroes, we should ignore possibilities where the part of the fragment to the `left` of the decimal starts with `"0"` (unless it is exactly `"0"`), and ignore possibilities where the part of the fragment to the `right` of the decimal ends with `"0"`, as these are not allowed.

Note that this process could result in an empty answer, such as for the case `S = "(000)"`.

```python
class Solution(object):
    def ambiguousCoordinates(self, S):
        def make(frag):
            N = len(frag)
            for d in xrange(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in xrange(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$, where $N$ is the length `S`. We evaluate the sum $O(\sum_k k(N-k))$.

* Space Complexity: $O(N^3)$, to store the answer.

# Submissions
---
**Solution: (Cartesian Product)**
```
Runtime: 44 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def make(frag):
            N = len(frag)
            for d in range(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in range(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]
```

**Solution 1: (String)**
```
Runtime: 18 ms
Memory Usage: 9.8 MB
```
```c++
class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
        vector<string> res;
        string s2 = s.substr(1, s.size()-2);
        int n = s2.size();
        
        for (int i = 1; i < n; i++) {
            vector<string> first = getNumbers(s2.substr(0, i));
            vector<string> second = getNumbers(s2.substr(i));
            
            for (int j = 0; j < first.size(); j++) {
                for (int k = 0; k < second.size(); k++) {
                    res.push_back("(" + first[j] + ", " + second[k] + ")");
                }
            }
        }
        return res;
    }
    
    vector<string> getNumbers(string num) {
        vector<string> res;
        int n = num.size();
        
        if (n == 1) 
            return {num};
        
        if (num[0] != '0') 
            res.push_back(num);
        
        if (num[0] == '0') {
            if (num.back() == '0') return {};
            return {"0." + num.substr(1)};
        }
        
        for (int i = 1; i < n; i++) {
            if (num.substr(i).back() == '0') continue;
            res.push_back(num.substr(0, i) + "." + num.substr(i));
        }
        
        return res;
    }
};
```
