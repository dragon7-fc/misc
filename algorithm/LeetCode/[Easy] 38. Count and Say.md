38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:
```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

* `1` is read off as `"one 1"` or `11`.
* `11` is read off as `"two 1s"` or `21`.
* `21` is read off as `"one 2, then one 1"`or `1211`.

Given an integer `n` where `1 ≤ n ≤ 30`, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

**Note:** Each term of the sequence of integers will be represented as a string.

 

**Example 1:**
```
Input: 1
Output: "1"
Explanation: This is the base case.
```

**Example 2:**
```
Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
```

# Submissions
---
**Solution 1: (String)**
```
Runtime: 36 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        def get(s):
            res = []
            i = 0
            cnt = 1
            while i < len(s):
                if (i+1) == len(s):
                    res.append(str(cnt))
                    res.append(s[i])
                    i += 1
                elif s[i+1] == s[i]:
                    cnt += 1
                    i += 1
                else:
                    res.append(str(cnt))
                    res.append(s[i])
                    cnt = 1
                    i += 1
            return "".join(res)
        
        store = ["1"]
        for i in range(1, n):
            store.append(get(store[i-1]))
        return store[n-1]
```

**Solution 2: (String)**
```
Runtime: 14 ms
Memory Usage: 6.5 MB
```
```c++
class Solution {
    string countAndSayHelper(const string& str) {
        string res;
        for (int i = 0; i < str.size(); ++i) {
            int count = 1;
            while (i < str.size() -1 && str[i] == str[i+1]) {
                count++;
                i++;
            }
            res += to_string(count) + str[i];
        }
        return res;
    }
public:
    string countAndSay(int n) {
        string res {"1"};
        for (int i = 2; i <= n; ++i) {
            res = countAndSayHelper(res);
        }
        return res;
    }
};
```
