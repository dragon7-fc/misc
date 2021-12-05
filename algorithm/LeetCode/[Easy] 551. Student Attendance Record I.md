551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:

* 'A' : Absent.
* 'L' : Late.
* 'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

**Example 1:**
```
Input: "PPALLP"
Output: True
```

**Example 2:**
```
Input: "PPALLL"
Output: False
```

# Submissions
---
**Solution 1: (String)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s   
```

**Solution 2: (String)**
```
Runtime: 0 ms
Memory Usage: 5.5 MB
```
```c


bool checkRecord(char * s){
    int absent, late;

	absent = late = 0;
	for (;;)
		switch (*s++) {
			case '\0':
				return true;
			case 'L':
				if (++late > 2)
					return false;
				break;
			case 'A':
				if (++absent > 1)
					return false;
			default:
				late = 0;
		}
}
```
