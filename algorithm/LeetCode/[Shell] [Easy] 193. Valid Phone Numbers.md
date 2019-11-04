193. Valid Phone Numbers

Given a text file `file.txt` that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

**Example:**

```
Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
```

**Solution 1:**

In egrep, +, ?, |, (, and ), treated as meta characters. Where as in grep, they are rather treated as pattern instead of meta characters. By including 'backslash' followed by meta character can let the grep to treat it as meta characters like ?, +, {, |, (, and ).
```
Runtime: 0 ms
Memory Usage: 3.1 MB
```
```sh
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt
```

**Solution 2:**
```
Runtime: 8 ms
Memory Usage: 3.1 MB
```
```sh
# Read from the file file.txt and output all valid phone numbers to stdout.
grep '^\(([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}\|[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}\)$' file.txt
```