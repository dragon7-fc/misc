1405. Longest Happy String

A string is called happy if it does not have any of the strings `'aaa'`, `'bbb'` or `'ccc'` as a substring.

Given three integers `a`, `b` and `c`, return any string `s`, which satisfies following conditions:

* `s` is happy and longest possible.
* `s` contains at most `a` occurrences of the letter `'a'`, at most `b` occurrences of the letter `'b'` and at most `c` occurrences of the letter `'c'`.
* `s` will only contain `'a'`, `'b'` and `'c'` letters.

If there is no such string `s` return the empty string `""`.

 

**Example 1:**
```
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
```

**Example 2:**
```
Input: a = 2, b = 2, c = 1
Output: "aabbc"
```

**Example 3:**
```
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
```

**Constraints:**

* `0 <= a, b, c <= 100`
* `a + b + c > 0`

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 24 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
        if b != 0:
            heappush(max_heap, (-b, 'b'))
        if c != 0:
            heappush(max_heap, (-c, 'c'))
        s = []
        while max_heap:
            first, char1 = heappop(max_heap) # char with most rest numbers
            if len(s) >= 2 and s[-1] == s[-2] == char1: # check whether this char is the same with previous two
                if not max_heap: # if there is no other choice, just return
                    return ''.join(s)
                second, char2 = heappop(max_heap) # char with second most rest numbers
                s.append(char2)
                second += 1 # count minus one, because the second here is negative, thus add 1
                if second != 0: # only if there is rest number count, add it back to heap
                    heappush(max_heap, (second, char2))
                heappush(max_heap, (first, char1)) # also need to put this part back to heap
                continue
                
            #  situation that this char can be directly added to answer
            s.append(char1)
            first += 1
            if first != 0:
                heappush(max_heap, (first, char1))
        return ''.join(s)
```

**Solution 2: (Heap)**
```
Runtime: 0 ms
Memory: 7.77 MB
```
```c++
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int,int>> pq;
        if (a) {
            pq.push({a, 0});
        }
        if (b) {
            pq.push({b, 1});
        }
        if (c) {
            pq.push({c, 2});
        }
        string ans;
        while (pq.size()) {
            auto [cnt, i] = pq.top();
            pq.pop();
            if (ans.size() >= 2 && 'a'+i == ans.back() && *(ans.rbegin()+1) == ans.back()) {
                if (pq.empty()) {
                    break;
                }
                auto [cnt2, j] = pq.top();
                pq.pop();
                ans += 'a'+j;
                if (cnt2-1) {
                    pq.push({cnt2-1, j});
                }
                pq.push({cnt, i});
            } else {
                ans += 'a'+i;
                if (cnt-1) {
                    pq.push({cnt-1, i});
                }
            }
        }
        return ans;
    }
};
```

**Solution 3: (Greedy)**

a b c
1 2 10

ccaccbccbcc

```
Runtime: 3 ms
Memory: 7.59 MB
```
```c++
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        int curra = 0, currb = 0, currc = 0;
        // Maximum total iterations possible is given by the sum of a, b and c.
        int totalIterations = a + b + c;
        string ans = "";

        for (int i = 0; i < totalIterations; i++) {
            if ((a >= b and a >= c and curra != 2) or
                (a > 0 and (currb == 2 or currc == 2))) {
                // If 'a' is maximum and it's streak is less than 2, or if
                // streak of 'b' or 'c' is 2, then 'a' will be the next
                // character.
                ans += 'a';
                a--;
                curra++;
                currb = 0;
                currc = 0;
            } else if ((b >= a and b >= c and currb != 2) or
                       (b > 0 and (currc == 2 or curra == 2))) {
                // If 'b' is maximum and it's streak is less than 2, or if
                // streak of 'a' or 'c' is 2, then 'b' will be the next
                // character.
                ans += 'b';
                b--;
                currb++;
                curra = 0;
                currc = 0;
            } else if ((c >= a and c >= b and currc != 2) or
                       (c > 0 and (curra == 2 or currb == 2))) {
                // If 'c' is maximum and it's streak is less than 2, or if
                // streak of 'a' or 'b' is 2, then 'c' will be the next
                // character.
                ans += 'c';
                c--;
                currc++;
                curra = 0;
                currb = 0;
            }
        }
        return ans;
    }
};
```
