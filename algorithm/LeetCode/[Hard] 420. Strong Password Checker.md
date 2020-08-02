420. Strong Password Checker

A password is considered strong if below conditions are all met:

1. It has at least 6 characters and at most 20 characters.
1. It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
1. It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input, and return the **MINIMUM** change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    int strongPasswordChecker(string s) {
        // For diversity requirement.
        bool lower_case(false), upper_case(false), digit(false);
        
        // For repeats.
        std::vector<int> run_lengths;

        char curr;
        int run_length(0);
        for (int i = 0; i < s.size(); ++i) {
            // Do we need new characters.
            if (s[i] >= 'a' && s[i] <= 'z') {
                lower_case = true;
            } else if (s[i] >= 'A' && s[i] <= 'Z') {
                upper_case = true;
            } else if (s[i] > '0' && s[i] <= '9') {
                digit = true;
            }
            
            // Repeats.
            if (i == 0) {
                curr = s[0];
                run_length = 1;
                continue;
            }
            if (s[i] == curr) {
                ++run_length;
            } else {
                if (run_length >= 3) {
                    run_lengths.push_back(run_length);
                }
                curr = s[i];
                run_length = 1;
            }
        }
        if (run_length >= 3) {
            run_lengths.push_back(run_length);
        }

        // Number of new characters needed.
        int num_new(0);
        if (!lower_case) {
            ++num_new;
        }
        if (!upper_case) {
            ++num_new;
        }
        if (!digit) {
            ++num_new;
        }
        
        // We can resolve some repeats if we need to insert or delete characters.
        int num_edits(0);
        if (s.size() < 6) {
            int num_inserts = 6 - s.size();
            // Some of the inserts can also satisfy num_new.
            num_new -= min(num_new, num_inserts);
            // Some of the inserts can break run lengths.
            for (int i = 0; i < run_lengths.size(); ++i) {
                int rl = run_lengths[i];
                while (num_inserts > 0 && rl >= 3) {
                    --num_inserts;
                    ++num_edits;
                    rl -= 2;
                }
                while (num_new > 0 && rl >= 3) {
                    --num_new;
                    ++num_edits;
                    rl -= 2;
                }
                run_lengths[i] = rl;
            }
            num_edits += num_inserts;
        } else if (s.size() > 20) {
            int num_deletes = s.size() - 20;
            // Some of the deletes can break run lengths at the same priority as substitutions.
            for (int i = 0; i < run_lengths.size(); ++i) {
                int rl = run_lengths[i];
                while (num_new > 0 && rl >= 3) {
                    --num_new;
                    ++num_edits;
                    rl -= 3;
                }
                if (rl >= 3 && num_deletes > 0 && rl % 3 == 0) {
                    --num_deletes;
                    ++num_edits;
                    rl -= 1;
                }
                run_lengths[i] = rl;
            }
            // Use the remainder of our deletion budget by priority.
            // This is given by number of deletes needed to break a repeat.
            for (int i = 0; i < run_lengths.size(); ++i) {
                int rl = run_lengths[i];
                if (rl >= 3 && num_deletes >= 2 && rl % 3 == 1) {
                    num_deletes -= 2;
                    num_edits += 2;
                    rl -= 2;
                }
                run_lengths[i] = rl;
            }
            for (int i = 0; i < run_lengths.size(); ++i) {
                int rl = run_lengths[i];
                while (rl >= 3 && num_deletes >= 3 && rl % 3 == 2) {
                    num_deletes -= 3;
                    num_edits += 3;
                    rl -= 3;
                }
                run_lengths[i] = rl;
            }
            num_edits += num_deletes;
        }
        
        // All remaining repeats will now be broken by substitutions.
        int num_replace(0);
        for (int rl : run_lengths) {
            num_replace += rl / 3;
        }
        num_edits += num_replace;
        
        // Some num_new can be satisfied by above substitutions.
        num_new -= min(num_new, num_replace);
        num_edits += num_new;

        return num_edits;
    }
};
```

**Solution 2: (String)**
```
Runtime: 44 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        has_lower, has_upper, has_digit = 0, 0, 0
        rep = 0
        repeat = []
        rep_1, rep_2 = 0, 0
        
        def check(s):
            nonlocal has_upper, has_lower, has_digit, repeat, rep, rep_1, rep_2
            cnt = 0;
            c = '@';
            for i in range(len(s)):
                if s[i].isupper():
                    has_upper = 1
                if s[i].islower():
                    has_lower = 1
                if s[i].isdigit():
                    has_digit = 1
                if s[i] == c:
                    cnt += 1
                else:
                    if cnt >= 3:
                        repeat += [cnt]
                    c = s[i]
                    cnt = 1
            if cnt >= 3:
                repeat += [cnt]
            for x in repeat:
                if x%3 == 0: 
                    rep_1 += 1
                if x%3 == 1:
                    rep_2 += 1
                rep += x // 3
        
        if len(s) == 0:
            return 6
        check(s)
        letter = 3 - has_upper - has_lower - has_digit
        if len(s) < 6:
            return max(6 - len(s), letter)
        if len(s) <= 20 and len(s) >= 6:
            return max(rep, letter)
        if len(s) > 20:
            remain = len(s) - 20
            if remain <= rep_1:
                rep -= remain
            elif remain - rep_1 <= 2 * rep_2:
                rep -= rep_1 + (remain - rep_1) // 2
            else:
                rep -= rep_1 + rep_2 + (remain - rep_1 - 2 * rep_2) // 3
            return remain + max(rep, letter)
        return 0
```