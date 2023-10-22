2355. Maximum Number of Books You Can Take

You are given a **0-indexed** integer array `books` of length `n` where `books[i]` denotes the number of books on the `i`th shelf of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from `l` to `r` where `0 <= l <= r < n`. For each index `i` in the range `l <= i < r`, you must take **strictly fewer** books from shelf `i` than shelf `i + 1`.

Return the **maximum** number of books you can take from the bookshelf.

 

**Example 1:**
```
Input: books = [8,5,2,7,9]
Output: 19
Explanation:
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.
```

**Example 2:**
```
Input: books = [7,0,3,4,5]
Output: 12
Explanation:
- Take 3 books from shelf 2.
- Take 4 books from shelf 3.
- Take 5 books from shelf 4.
You have taken 12 books so return 12.
It can be proven that 12 is the maximum number of books you can take.
```

**Example 3:**
```
Input: books = [8,2,3,7,3,4,0,1,4,3]
Output: 13
Explanation:
- Take 1 book from shelf 0.
- Take 2 books from shelf 1.
- Take 3 books from shelf 2.
- Take 7 books from shelf 3.
You have taken 13 books so return 13.
It can be proven that 13 is the maximum number of books you can take.
```

**Constraints:**

* `1 <= books.length <= 10^5`
* `0 <= books[i] <= 10^5`

# Submission
---
**Solution 1: (Monostack and Sequence Sum, greedy maintain an optimized sequence sum from value diff and index diff)**
```
Runtime: 97 ms
Memory: 67.6 MB
```
```c++
class Solution {
    long long ssum(long long l, int cnt) {
        return (l * (l + 1) - (l > cnt ? (l - cnt) * (l - cnt + 1) : 0)) / 2;
    }
public:
    long long maximumBooks(vector<int>& books) {
        vector<int> ms;
        long long cur = 0, res = 0;
        for (int i = 0; i < books.size(); ++i) {
            while (!ms.empty() && books[i] - books[ms.back()] < i - ms.back()) {
                int j = ms.back(); ms.pop_back();
                cur -= ssum(books[j], ms.empty() ? j + 1: j - ms.back());
            }
            cur += ssum(books[i], ms.empty() ? i + 1 : i - ms.back());
            ms.push_back(i);
            res = max(cur, res);
        }
        return res;
    }
};
```
