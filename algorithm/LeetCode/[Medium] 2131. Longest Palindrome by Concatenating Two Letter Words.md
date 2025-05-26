2131. Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings `words`. Each element of `words` consists of two lowercase English letters.

Create the **longest possible** palindrome by selecting some elements from words and concatenating them in **any order**. Each element can be selected **at most once**.

Return the **length** of the longest palindrome that you can create. If it is impossible to create any palindrome, return `0`.

A **palindrome** is a string that reads the same forward and backward.

 

**Example 1:**
```
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
```

**Example 2:**
```
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
```

**Example 3:**
```
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
``` 

**Constraints:**

* `1 <= words.length <= 10^5`
* `words[i].length == 2`
* `words[i]` consists of lowercase English letters.

# Submissions
---
**Solution 1: (A Hash Map Approach)**
```
Runtime: 1301 ms
Memory: 38.4 MB
```
```python
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # a count variable contains the number of occurrences of each word
        count = Counter(words)
        answer = 0
        central = False
        for word, count_of_the_word in count.items():
            # if the word is a palindrome
            if word[0] == word[1]:
                if count_of_the_word % 2 == 0:
                    answer += count_of_the_word
                else:
                    answer += count_of_the_word - 1
                    central = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # word[1] + word[0] is the reversed word
            elif word[0] < word[1]:
                answer += 2 * min(count_of_the_word, count[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer
```

**Solution 2: (A Hash Map Approach)**
```
Runtime: 612 ms
Memory: 168 MB
```
```c++
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> count;
        for (const string& word : words) {
            count[word]++;
        }

        int answer = 0;
        bool central = false;

        for (const auto& [word, countOfTheWord] : count) {
            // if the word is a palindrome
            if (word[0] == word[1]) {
                if (countOfTheWord % 2 == 0) {
                    answer += countOfTheWord;
                } else {
                    answer += countOfTheWord - 1;
                    central = true;
                }
                // consider a pair of non-palindrome words such that one is the
                // reverse of another ({word[1], word[0]} is the reversed word)
            } else if (word[0] < word[1] && count.count({word[1], word[0]})) {
                answer += 2 * min(countOfTheWord, count[{word[1], word[0]}]);
            }
        }

        if (central) {
            answer++;
        }
        return 2 * answer;
    }
};
```

**Solution 3: (A Two-Dimensional Array Approach)**
```
Runtime: 3203 ms
Memory: 37.3 MB
```
```python
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        alphabet_size = 26
        count = [[0 for j in range(alphabet_size)] for i in range(alphabet_size)]
        for word in words:
            count[ord(word[0]) - ord('a')][ord(word[1]) - ord('a')] += 1
        answer = 0
        central = False
        for i in range(alphabet_size):
            if count[i][i] % 2 == 0:
                answer += count[i][i]
            else:
                answer += count[i][i] - 1
                central = True
            for j in range(i + 1, alphabet_size):
                answer += 2 * min(count[i][j], count[j][i])
        if central:
            answer += 1
        return 2 * newAnswer
```

**Solution 4: (A Two-Dimensional Array Approach)**
```
Runtime: 677 ms
Memory: 168.2 MB
```
```c++
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        constexpr int alphabetSize = 26;
        vector count(alphabetSize, vector<int>(alphabetSize));
        for (const string& word : words) {
            count[word[0] - 'a'][word[1] - 'a']++;
        }
        int answer = 0;
        bool central = false;
        for (int i = 0; i < alphabetSize; i++) {
            if (count[i][i] % 2 == 0) {
                answer += count[i][i];
            } else {
                answer += count[i][i] - 1;
                central = true;
            }
            for (int j = i + 1; j < alphabetSize; j++) {
                answer += 2 * min(count[i][j], count[j][i]);
            }
        }
        if (central) {
            answer++;
        }
        return 2 * answer;
    }
};
```

**Solution 5: (Hash Table)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 171.95 MB, Beats 44.24%
```
```c++
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        int cnt[26][26] = {0}, ans = 0;
        for (int i = 0; i < words.size(); i++) {
            int a = words[i][0] - 'a';
            int b = words[i][1] - 'a';
            if (cnt[b][a] > 0) {
                ans += 4;
                cnt[b][a]--;
            }
            else
                cnt[a][b]++;
        }
        
        for (int i = 0; i < 26; i++) {
            if (cnt[i][i] >= 1) {
                ans += 2;
                break;
            }
        }
        return ans;
    }
};
```
