1717. Maximum Score From Removing Substrings

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

* Remove substring "ab" and gain x points.
    * For example, when removing `"ab"` from `"cabxbae"` it becomes `"cxbae"`.
* Remove substring "ba" and gain y points.
    * For example, when removing `"ba"` from `"cabxbae"` it becomes `"cabxe"`.

Return the maximum points you can gain after applying the above operations on `s`.

 

**Example 1:**
```
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
```

**Example 2:**
```
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
```

**Constraints:**

* `1 <= s.length <= 105`
* `1 <= x, y <= 104`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Greedy, Focus on some pattern)**
```
Runtime: 1140 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a = 'a'
        b = 'b'
        if x < y:
            x, y = y, x
            a, b = b, a
        seen = Counter()
        ans = 0
        for c in s + 'x':
            if c in 'ab':
                if c == b and 0 < seen[a]:
                    ans += x
                    seen[a] -= 1
                else:
                    seen[c] += 1
            else:
                ans += y * min(seen[a], seen[b])
                seen = Counter()

        return ans
```

**Solution 1: (Greedy, Stack)**
```
Runtime: 97 ms
Memory: 29.3 MB
```
```c++
class Solution {
    string greedy(string s, char a, char b) {
        string st;
        for (auto ch : s) {
            if (!st.empty() && st.back() == a && ch == b) {
                st.pop_back();
            } else
                st.push_back(ch);
        }
        return st;
    }
public:
    int maximumGain(string s, int x, int y, char a = 'a', char b = 'b') {
        if (y > x) {
            swap(x, y);
            swap(a, b);
        }
        auto s1 = greedy(s, a, b), s2 = greedy(s1, b, a);
        return (s.size() - s1.size()) / 2 * x + (s1.size() - s2.size()) /2 * y;
    }
};
```

**Solution 3: (Greedy)**
```
Runtime: 95 ms
Memory: 25.63 MB
```
```c++
class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int ans = 0;
        vector<pair<int,string>> dp = {{x, "ab"},{y, "ba"}};
        sort(dp.begin(), dp.end(), [](auto pa, auto pb){return pa.first > pb.first;});
        string pre = s, cur;
        for (int i = 0; i < dp.size(); i ++) {
            cur = pre[0];
            for (int j = 1; j < pre.size(); j ++) {
                if (cur != "" && cur.back() == dp[i].second[0] && pre[j] == dp[i].second[1]) {
                    cur.pop_back();
                    ans += dp[i].first;
                } else {
                    cur += pre[j];
                }
            }
            pre = cur;
        }
        return ans;
    }
```

**Solution 4: (Greedy Way (Stack))**
```
Runtime: 112 ms
Memory: 30.47 MB
```
```c++
class Solution {
    string removeSubstring(const string& input, const string& targetPair) {
        stack<char> charStack;

        // Iterate through each character in the input string
        for (char currentChar : input) {
            // Check if current character forms the target pair with the top of
            // the stack
            if (currentChar == targetPair[1] && !charStack.empty() &&
                charStack.top() == targetPair[0]) {
                charStack
                    .pop();  // Remove the matching character from the stack
            } else {
                charStack.push(currentChar);
            }
        }

        // Reconstruct the remaining string after removing target pairs
        string remainingChars;
        while (!charStack.empty()) {
            remainingChars += charStack.top();
            charStack.pop();
        }
        reverse(remainingChars.begin(), remainingChars.end());
        return remainingChars;
    }
public:
    int maximumGain(string s, int x, int y) {
        int totalScore = 0;
        string highPriorityPair = x > y ? "ab" : "ba";
        string lowPriorityPair = highPriorityPair == "ab" ? "ba" : "ab";

        // First pass: remove high priority pair
        string stringAfterFirstPass = removeSubstring(s, highPriorityPair);
        int removedPairsCount =
            (s.length() - stringAfterFirstPass.length()) / 2;

        // Calculate score from first pass
        totalScore += removedPairsCount * max(x, y);

        // Second pass: remove low priority pair
        string stringAfterSecondPass =
            removeSubstring(stringAfterFirstPass, lowPriorityPair);
        removedPairsCount =
            (stringAfterFirstPass.length() - stringAfterSecondPass.length()) /
            2;

        // Calculate score from second pass
        totalScore += removedPairsCount * min(x, y);

        return totalScore;
    }
};
```

**Solution 5: (Greedy Way (Without Stack))**
```
Runtime: 70 ms
Memory: 18.29 MB
```
```c++
class Solution {
    int removeSubstring(string& inputString, string targetSubstring,
                        int pointsPerRemoval) {
        int totalPoints = 0;
        int writeIndex = 0;

        // Iterate through the string
        for (int readIndex = 0; readIndex < inputString.size(); readIndex++) {
            // Add the current character
            inputString[writeIndex++] = inputString[readIndex];

            // Check if we've written at least two characters and
            // they match the target substring
            if (writeIndex > 1 &&
                inputString[writeIndex - 2] == targetSubstring[0] &&
                inputString[writeIndex - 1] == targetSubstring[1]) {
                writeIndex -= 2;  // Move write index back to remove the match
                totalPoints += pointsPerRemoval;
            }
        }

        // Trim the string to remove any leftover characters
        inputString.erase(inputString.begin() + writeIndex, inputString.end());

        return totalPoints;
    }
public:
    int maximumGain(string s, int x, int y) {
        int totalPoints = 0;

        if (x > y) {
            // Remove "ab" first (higher points), then "ba"
            totalPoints += removeSubstring(s, "ab", x);
            totalPoints += removeSubstring(s, "ba", y);
        } else {
            // Remove "ba" first (higher or equal points), then "ab"
            totalPoints += removeSubstring(s, "ba", y);
            totalPoints += removeSubstring(s, "ab", x);
        }

        return totalPoints;
    }
};
```

**Solution 6: (Greedy Way (Counting))**
```
Runtime: 52 ms
Memory: 18.28 MB
```
```c++
class Solution {
public:
    int maximumGain(string s, int x, int y) {
        // Ensure "ab" always has more points than "ba"
        if (x < y) {
            // Swap points
            int temp = x;
            x = y;
            y = temp;
            // Reverse the string to maintain logic
            reverse(s.begin(), s.end());
        }

        int aCount = 0, bCount = 0, totalPoints = 0;

        for (int i = 0; i < s.size(); ++i) {
            char currentChar = s[i];

            if (currentChar == 'a') {
                ++aCount;
            } else if (currentChar == 'b') {
                if (aCount > 0) {
                    // Can form "ab", remove it and add points
                    --aCount;
                    totalPoints += x;
                } else {
                    // Can't form "ab", keep 'b' for potential future "ba"
                    ++bCount;
                }
            } else {
                // Non 'a' or 'b' character encountered
                // Calculate points for any remaining "ba" pairs
                totalPoints += min(bCount, aCount) * y;
                // Reset counters for next segment
                aCount = bCount = 0;
            }
        }
        // Calculate points for any remaining "ba" pairs at the end
        totalPoints += min(bCount, aCount) * y;

        return totalPoints;
    }
};
```
