192. Word Frequency

Write a bash script to calculate the frequency of each word in a text file `words.txt`.

For simplicity sake, you may assume:

* words.txt contains only lowercase characters and space ' ' characters.
* Each word must consist of lowercase characters only.
* Words are separated by one or more whitespace characters.

**Example:**

```
Assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1
```

**Note:**

* Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
* Could you write it in one-line using Unix pipes?

**Solution 1:**
```
Runtime: 4 ms
Memory Usage: 3.3 MB
```
```sh
# Read from the file words.txt and output the word frequency list to stdout.
for word in $(cat words.txt); do echo $word; done | sort | uniq -c | sort -r | awk '{ print $2 " "$1}'
```

**Solution 2:**
```
Runtime: 0 ms
Memory Usage: 3.3 MB
```
```sh
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -cs "[a-z]" "\n" | sort | uniq -c | sort -k1nr -k2 |awk '{print $2,$1}'
```

**Solution 3:**
```
Runtime: 0 ms
Memory Usage: 3.3 MB
```
```sh
# Read from the file words.txt and output the word frequency list to stdout.
awk '{for(i=1;i<=NF;i++) print $i}' words.txt | sort | uniq -c |sort -r|awk '{print $2" "$1}'
```