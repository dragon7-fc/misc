195. Tenth Line

Given a text file `file.txt`, print just the 10th line of the file.

**Example:**

```
Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:

Line 10
```

**Note:**

1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.

# Submissions
---
**Solution 1:**
```
Runtime: 4 ms
Memory Usage: 3.8 MB
```
```sh
# Read from the file file.txt and output the tenth line to stdout.
cat file.txt | sed -n '10p'
```

**Solution 2:**
```
Runtime: 4 ms
Memory Usage: 3.7 MB
```
```sh
# Read from the file file.txt and output the tenth line to stdout.
cat file.txt | awk 'NR==10{print}'
```

**Solution 3:**
```
Runtime: 0 ms
Memory Usage: 3.6 MB
```
```sh
# Read from the file file.txt and output the tenth line to stdout.
cat file.txt | awk '{if(NR==10) print}'
```
