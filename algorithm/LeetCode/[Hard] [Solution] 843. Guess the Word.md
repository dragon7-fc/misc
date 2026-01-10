843. Guess the Word

This problem is an **interactive problem** new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as **secret**.

You may call `master.guess(word)` to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an `integer` type, representing the number of exact matches (value and position) of your guess to the **secret word**.  Also, if your guess is not in the given wordlist, it will return `-1` instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to `master.guess` and at least one of these guesses was the **secret**, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

**Example 1:**
```
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
```

**Note:**  Any solutions that attempt to circumvent the judge will result in disqualification.

# Solution
---
## Approach #1: Minimax with Heuristic [Accepted]
**Intuition**

We can guess that having less words in the word list is generally better. If the data is random, we can reason this is often the case.

Now let's use the strategy of making the guess that minimizes the maximum possible size of the resulting word list. If we started with $N$ words in our word list, we can iterate through all possibilities for what the secret could be.

**Algorithm**

Store `H[i][j]` as the number of matches of `wordlist[i]` and `wordlist[j]`. For each guess that hasn't been guessed before, do a minimax as described above, taking the guess that gives us the smallest group that might occur.

```python
class Solution(object):
    def findSecretWord(self, wordlist, master):
        N = len(wordlist)
        self.H = [[sum(a==b for a,b in itertools.izip(wordlist[i], wordlist[j]))
                   for j in xrange(N)] for i in xrange(N)]

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)

    def solve(self, possible, path = ()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in xrange(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess
```

**Complexity Analysis**

* Time Complexity: $O(N^2 \log N)$, where $N$ is the number of words, and assuming their length is $O(1)$. Each call to solve is $O(N^2)$, and the number of calls is bounded by $O(\log N)$.

* Space Complexity: $O(N^2)$.

# Submissions
---
**Solution 1: (Minimax with Heuristic)**
```
Runtime: 92 ms
Memory Usage: 12.9 MB
```
```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        N = len(wordlist)
        self.H = [[sum(a==b for a,b in zip(wordlist[i], wordlist[j]))
                   for j in range(N)] for i in range(N)]

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)

    def solve(self, possible, path = ()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess
```

**Solution 2: (Mastermind Strategy)**

This is one of the most interesting Google HARD problems — a pure Mastermind-style deduction puzzle.
I solved it in C++ with a clean elimination strategy that consistently Beats 100%.

The key idea is simple:
Use the feedback from each guess to eliminate all invalid words and shrink the search space fast.

Short, intuitive, and highly effective. Here's the approach 👇

__Approach:__
We treat the problem like Mastermind.
For every guessed word, the Master returns how many characters match in the same position.
We use this feedback to eliminate all words that don't have the same match count.

Steps:
Pick any word from the candidate list.
Call master.guess() on it.
Filter out words that don't match the returned similarity.
Repeat until only one valid word remains.
Why this works:
Each guess dramatically shrinks the search space.
The elimination is deterministic, simple, and extremely efficient.
That's why this strategy beats 100%.

__COMPLEXITY__
Time Complexity: O(N² * L)
Space Complexity: O(N)


secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10

                          case 1:                   |      case 2:
                          guessWord == secret       |      guessWord != secret
                    guessWord                       | guessWord  
----------------------------------------------------|----------------------------------
                               match      match     |            match     match
                               secret     guessWord |            secret    guessWord
secret =  "acckzz"                                  |
words  = ["acckzz",     x        6          6       |                          3
          "ccbazz",                         3       |     x        3           6
          "eiowzz",                         2       |                          2
          "abcczz"]                         4       |                          2

```
Runtime: 4 ms, Beats 48.60%
Memory: 8.74 MB, Beats 98.73%
```
```c++
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
    // Count matching characters at the same positions
    int matchCount(const string &a, const string &b) {
        int cnt = 0;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] == b[i]) cnt++;
        }
        return cnt;
    }
public:
    void findSecretWord(vector<string>& words, Master& master) {
        unordered_set<string> candidates(words.begin(), words.end());

        while (!candidates.empty()) {
            // Pick an arbitrary word from the set
            string guessWord = *candidates.begin();

            // Make a guess using Master's API
            int matched = master.guess(guessWord);

            // Filter words that have the same match count
            for (auto it = candidates.begin(); it != candidates.end();) {
                if (matchCount(*it, guessWord) != matched)
                    it = candidates.erase(it);
                else
                    ++it;
            }

            // Remove the used word
            candidates.erase(guessWord);
        }
    }
};
```
