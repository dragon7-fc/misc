520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
1. All letters in this word are not capitals, like "leetcode".
1. Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.
 

**Example 1:**
```
Input: "USA"
Output: True
```

**Example 2:**
```
Input: "FlaG"
Output: False
``` 

**Note:** The input will be a non-empty word consisting of uppercase and lowercase latin letters.

# Solution
---
## Overview
It's a fairly easy problem because it does not require you to use any special trick, and all you need to do is to implement the solution step by step.

However, it would take some time if you want to make your code easily readable, beautiful, and short. Below two approaches are introduced, they are "Character by Character" method and "Regex" method.

## Approach 1: Character by Character

**Intuition**

Recall (part of) the description of the problem:

>We define the usage of capitals in a word to be right when one of the following cases holds:
1. All letters in this word are capitals, like "USA".
1. All letters in this word are not capitals, like "leetcode".
1. Only the first letter in this word is capital, like "Google".

The problem gives us three patterns, and ask if the given `word` matches any of them. It would be easy to think of checking the cases one by one. In each case, we can just use the most simple method to check if word matches the pattern -- check the char one by one.

**Algorithm**

We need three bool variables to store if the pattern matches or not. We set the variables to be true at the beginning, and when the pattern doesn't match, we turn the variables into false. You can also do it otherwise, but the code would be a little longer.

The code is a little long... Don't be afraid! It's fairly easy to understand, and we will shorten it later.

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
            
        match1, match2, match3 = True, True, True

        # case 1: All capital
        for i in range(n):
            if not word[i].isupper():
                match1 = False
                break
        if match1:
            return True

        # case 2: All not capital
        for i in range(n):
            if word[i].isupper():
                match2 = False
                break
        if match2:
            return True

        # case 3: All not capital except first
        if not word[0].isupper():
            match3 = False
        if match3:
            for i in range(1, n):
                if word[i].isupper():
                    match3 = False
        if match3:
            return True

        # if not matching
        return False
```

There are a few points you should notice from the code above:

* We use the built-in function `isUpperCase` (in Java) and `isupper` (in Python) to check whether a char is upper case. You can also use the ASCII to do that. Just use something like `word.charAt(i) >= 'A' && word.charAt(i) <= 'Z'`.

* We use `break` after we find matching failed because there is no need to check whether the further char is valid.

* You can combine the three `match` variables into one by reusing it after each case, but I prefer to separate it into three for better readability.

OK! Now we have solved this problem. The time complexity is O(n)O(n) (where nn is word length) because we need to check each char at most three times. This time complexity is great, and there is no too much we can do to improve it.

However, we can make the code looks better and shorter, without reducing the readability.

**Improvement**

Where to start? The biggest problem of the code above is that there are too many cases. What if we can combine them? Notice that the biggest difference between case 2 and case 3 is the condition of the first char.

By combining case 2 and case 3, we get a new pattern: No matter what first char is, the rest should be lowercase.

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        if len(word) == 1:
            return True

        # case 1: All capital
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
        # case 2 and case 3
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False

        # if pass one of the cases
        return True
```

Still, there are a few points you should notice from the code above:

1. We check the length of the word firstly because we need to use the first two char to check if the word matches case1. Fortunately, a word with 1 length would always match either case2 or case3.

1. You can count the number of uppercase/lowercase letters in the word instead of checking it one by one and return immediately. That can also work.

1. Some programming languages have built-in methods to check if the word matches certain case, such as `istitle()` in Python and `word.toUpperCase().equals(word)` in Java. Those methods are doing the same things as our code above. It would be great if you can know both these APIs and how they implemented.

**Complexity Analysis**

* Time complexity: $O(n)$, where n is the length of the word. We only need to check each char at most constant times.

* Space complexity : $O(1)$. We only need constant spaces to store our variables.

## Approach 2: Regex
**Intuition**

Hey, if we want to do pattern matching, why don't we use Regular Expression (Regex)? Regex is a great way to match a given pattern to a string.

**Algorithm**

The pattern of case 1 in regex is $[A-Z]*$, where $[A-Z]$ matches one char from 'A' to 'Z', *∗ represents repeat the pattern before it at least 0 times. Therefore, this pattern represents "All capital".

The pattern of case 2 in regex is $[a-z]*$, where similarly, $[a-z]$ matches one char from 'a' to 'z'. Therefore, this pattern represents "All not capital".

Similarly, the pattern of case 3 in regex is $[A-Z][a-z]*$.

Take these three pattern together, we have $[A-Z]*|[a-z]*|[A-Z][a-z]*$, where "|" represents "or".

Still, we can combine case 2 and case 3, and we get $.[a-z]*$, where "." can matches any char.

Therefore, the final pattern is $[A-Z]*|.[a-z]*$.

```python
import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
```

However, it is worth pointing out that the speed of regex is highly dependent on its pattern and its implementation, and the time complexity can vary from $O(1)$ to $O(2^n)$. If you want to control the speed yourself, using Approach 1 would be better.

**Complexity Analysis**

* Time complexity: Basically $O(n)$, but depends on implementation.

* Space complexity : $O(1)$. We only need constant spaces to store our pattern.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()  
```

**Solution 2: (Character by Character)**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        if len(word) == 1:
            return True

        # case 1: All capital
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
        # case 2 and case 3
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False

        # if pass one of the cases
        return True
```

**Solution 3: (Regex)**
```
Runtime: 44 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
```