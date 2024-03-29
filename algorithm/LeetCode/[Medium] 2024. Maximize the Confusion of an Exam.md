2024. Maximize the Confusion of an Exam

A teacher is writing a test with n true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by **maximizing** the number of **consecutive** questions with the **same** answer (multiple trues or multiple falses in a row).

You are given a string `answerKey`, where `answerKey[i]` is the original answer to the ith question. In addition, you are given an integer `k`, the maximum number of times you may perform the following operation:

* Change the answer key for any question to `'T'` or `'F'` (i.e., set `answerKey[i]` to `'T'` or `'F'`).

Return the maximum number of consecutive `'T'`s or `'F'`s in the answer key after performing the operation at most `k` times.

 

**Example 1:**
```
Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
```

**Example 2:**
```
Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
```

**Example 3:**
```
Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
```

**Constraints:**

* `n == answerKey.length`
* `1 <= n <= 5 * 104`
* `answerKey[i]` is either `'T'` or `'F'`
* ``1 <= k <= n`

# Submissions
---
**Solution 1: (Sliding Windowa, Counter)**
```
Runtime: 404 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxf = res = 0
        count = collections.Counter()
        for i in range(len(answerKey)):
            count[answerKey[i]] += 1
            maxf = max(maxf, count[answerKey[i]])
            if res - maxf < k:
                res += 1
            else:
                count[answerKey[i - res]] -= 1
        return res
```

**Solution 2: (Sliding Window, Counter)**
```
Runtime: 44 ms
Memory Usage: 10.1 MB
```
```c++
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int res = 0, maxf = 0;
        unordered_map<int, int> count;
        for (int i = 0; i < answerKey.length(); ++i) {
            maxf = max(maxf, ++count[answerKey[i]]);
            if (res - maxf < k)
                res++;
            else
                count[answerKey[i - res]]--;
        }
        return res;
    }
};
```

**Solution 3: (Sliding Window)**
```
Runtime: 31 ms
Memory: 10.2 MB
```
```c++
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int i_t = 0, i_f = 0, cnt_t = 0, cnt_f = 0, ans = 0;
        for (int j = 0; j < answerKey.size(); j ++) {
            answerKey[j] == 'T'? cnt_t += 1: cnt_f += 1;
            while (cnt_t > k) {
                cnt_t = answerKey[i_t] == 'T' ? cnt_t - 1: cnt_t;
                i_t += 1;
            }
            while (cnt_f > k) {
                cnt_f = answerKey[i_f] == 'F' ? cnt_f - 1: cnt_f;
                i_f += 1;
            }
            ans = max(ans, j-i_t+1);
            ans = max(ans, j-i_f+1);
        }
        return ans;
    }
};
```
