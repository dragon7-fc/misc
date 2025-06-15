125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note:** For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**
```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**
```
Input: "race a car"
Output: false
```

# Solution
---
## Approach 1: Compare with Reverse
**Intuition**

A palindrome is a word, phrase, or sequence that reads the same backwards as forwards. e.g. `madam`

A palindrome, and its reverse, are identical to each other.

## Algorithm

We'll reverse the given string and compare it with the original. If those are equivalent, it's a palindrome.

Since only alphanumeric characters are considered, we'll filter out all other types of characters before we apply our algorithm.

Additionally, because we're treating letters as case-insensitive, we'll convert the remaining letters to lower case. The digits will be left the same.

**C++**
```c++
class Solution {
 public:
  bool isPalindrome(string s) {
    string filtered_string, reversed_string;

    for (auto ch : s) {
      if (isalnum(ch))
        filtered_string += tolower(ch);
    }

    reversed_string.resize(filtered_string.size());
    reverse_copy(filtered_string.begin(), filtered_string.end(),
                 reversed_string.begin());

    return filtered_string == reversed_string;
  }
};
```

**Python**
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
```

**Complexity Analysis**

* Time complexity : $O(n)$, in length $n$ of the string.

    We need to iterate thrice through the string:
    1. When we filter out non-alphanumeric characters, and convert the remaining characters to lower-case.
    1. When we reverse the string.
    1. When we compare the original and the reversed strings.

    Each iteration runs linear in time (since each character operation completes in constant time). Thus, the effective run-time complexity is linear.

* Space complexity : $O(n)$, in length nn of the string. We need $O(n)$ additional space to stored the filtered string and the reversed string.

## Approach 2: Two Pointers
**Intuition**

If you take any ordinary string, and concatenate its reverse to it, you'll get a palindrome. This leads to an interesting insight about the converse: every palindrome half is reverse of the other half.

Simply speaking, if one were to start in the middle of a palindrome, and traverse outwards, they'd encounter the same characters, in the exact same order, in both halves!

![125_1_1.png](img/125_1_1.png)
![125_1_2.png](img/125_1_2.png)
![125_1_3.png](img/125_1_3.png)
![125_1_4.png](img/125_1_4.png)
![125_1_5.png](img/125_1_5.png)
![125_1_6.png](img/125_1_6.png)

**Algorithm**

Since the input string contains characters that we need to ignore in our palindromic check, it becomes tedious to figure out the real middle point of our palindromic input.

>Instead of going outwards from the middle, we could just go inwards towards the middle!

So, if we start traversing inwards, from both ends of the input string, we can expect to see the same characters, in the same order.

The resulting algorithm is simple:

* Set two pointers, one at each end of the input string
* If the input is palindromic, both the pointers should point to equivalent characters, at all times. [1]
    * If this condition is not met at any point of time, we break and return early. [2]
* We can simply ignore non-alphanumeric characters by continuing to traverse further.
* Continue traversing inwards until the pointers meet in the middle.

**C++**
```c++
class Solution {
 public:
  bool isPalindrome(string s) {
    for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
      while (i < j && !isalnum(s[i]))
        i++;
      while (i < j && !isalnum(s[j]))
        j--;

      if (i < j && tolower(s[i]) != tolower(s[j]))
        return false;
    }

    return true;
  }
};
```

**Python**
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
```

**Complexity Analysis**

* Time complexity : $O(n)$, in length $n$ of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.

* Space complexity : $O(1)$. No extra space required, at all.

# Submissions
---
**Solution 1: (Compare with Reverse)**
```
Runtime: 60 ms
Memory Usage: 19.8 MB
```
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
```

**Solution 2: (Compare with Reverse)**
```
Runtime: 16 ms
Memory Usage: 7.8 MB
```
```c++
class Solution {
public:
    bool isPalindrome(string s) {
        string filtered_string, reversed_string;

        for (auto ch : s) {
          if (isalnum(ch))
            filtered_string += tolower(ch);
        }

        reversed_string.resize(filtered_string.size());
        reverse_copy(filtered_string.begin(), filtered_string.end(),
                     reversed_string.begin());

        return filtered_string == reversed_string;
    }
};
```

**Solution 3: (Two Pointers)**
```
Runtime: 52 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
```

**Solution 4: (Two Pointers)**
```
Runtime: 12 ms
Memory Usage: 7.3 MB
```
```c++
class Solution {
public:
    bool isPalindrome(string s) {
        for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
          while (i < j && !isalnum(s[i]))
            i++;
          while (i < j && !isalnum(s[j]))
            j--;

          if (i < j && tolower(s[i]) != tolower(s[j]))
            return false;
        }

        return true;
    }
};
```

**Solution 5: (String)**
```
Runtime: 52 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_str = [*filter(lambda c:c.isdigit() or c.isalpha(), s.lower())]  # list(filter(lambda c:c.isdigit() or c.isalpha(), s.lower()))
        return filter_str[::-1] == filter_str
```

**Solution 6: (Two Ponters)**
```
Runtime: 3 ms, Beats 31.39%
Memory: 9.84 MB, Beats 79.34%
```
```c++
class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size(), i = 0, j = n-1;
        while (i < j) {
            while (i < n && !isalnum(s[i])) {
                i += 1;
            }
            while (j >= 0 && !isalnum(s[j])) {
                j -= 1;
            }
            if (i >= j) {
                break;
            }
            if (isalpha(s[i]) && isalpha(s[j]) && tolower(s[i]) == tolower(s[j]) 
                    || isdigit(s[i]) && isdigit(s[j]) && s[i] == s[j]) {
                i += 1;
                j -= 1;
                continue;
            } else {
                return false;
            }
        }
        return true;
    }
};
```
