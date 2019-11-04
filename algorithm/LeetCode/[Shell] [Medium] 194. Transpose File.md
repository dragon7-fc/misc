194. Transpose File

Given a text file `file.txt`, transpose its content.

You may assume that each row has the same number of columns and each field is separated by the ' ' character.

**Example:**

```
If file.txt has the following content:

name age
alice 21
ryan 30
Output the following:

name alice ryan
age 21 30
```

# Submissions
---
**Solution 1:**
```
Runtime: 4 ms
Memory Usage: 3.5 MB
```
```sh
# Read from the file file.txt and print its transposed content to stdout.
col="$(head -1 file.txt | wc -w)"

for i in $(seq 1 $col);do awk '{ print $'$i' }' file.txt | paste -s -d" ";done
```

**Solution 2:**
```
Runtime: 8 ms
Memory Usage: 3.5 MB
```
```sh
# Read from the file file.txt and print its transposed content to stdout.
awk ' { for (i = 1; i <= NF; ++i)  if (NR == 1) cols[i] = $i;  else  cols[i] =  cols[i] " " $i } END { for (i in cols) print cols[i]}' file.txt 
```