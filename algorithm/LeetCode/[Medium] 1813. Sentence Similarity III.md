1813. Sentence Similarity III

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, `"Hello World"`, `"HELLO"`, `"hello world hello world"` are all sentences. Words consist of only uppercase and lowercase English letters.

Two sentences `sentence1` and `sentence2` are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, `sentence1 = "Hello my name is Jane"` and `sentence2 = "Hello Jane"` can be made equal by inserting `"my name is"` between `"Hello"` and `"Jane"` in `sentence2`.

Given two sentences `sentence1` and `sentence2`, return `true` if `sentence1` and `sentence2` are similar. Otherwise, return `false`.

 

**Example 1:**
```
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
```

**Example 2:**
```
Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
```

**Example 3:**
```
Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
```

**Example 4:**
```
Input: sentence1 = "Luky", sentence2 = "Lucccky"
Output: false
```

**Constraints:**

* `1 <= sentence1.length, sentence2.length <= 100`
* `sentence1` and `sentence2` consist of lowercase and uppercase English letters and spaces.
* The words in `sentence1` and `sentence2` are separated by a single space.

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 20 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        n1, n2 = map(len, (words1, words2))
        if n1 > n2:
            return self.areSentencesSimilar(sentence2, sentence1)
        i = 0
        while i < n1 and words1[i] == words2[i]:
            i += 1
        while i < n1 and words1[i] == words2[n2 - n1 + i]:
            i += 1
        return i == n1
```

**Solution 2: (String, dequeue)**
```
Runtime: 0 ms
Memory: 7.1 MB
```
```c++
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        string temp = "";
        deque<string>a,b;
        for(char c: sentence1){
            if(c == ' ') a.push_back(temp),temp = "";
            else temp += c;
        }
        a.push_back(temp),temp = "";
        for(char c: sentence2){
            if(c == ' ') b.push_back(temp),temp = "";
            else temp += c;
        }
        b.push_back(temp),temp = "";
		// removing common from front
        while(a.size() != 0 && b.size() != 0 && (a.front() == b.front())) a.pop_front(),b.pop_front();
        //removing common from back
		while(a.size() != 0 && b.size() != 0 && (a.back() == b.back())) a.pop_back(),b.pop_back();
		if(a.size() == 0 || b.size() == 0) return true;
        return false;
    }
};
```

**Solution 3: (Deque)**
```
Runtime: 4 ms
Memory: 8.91 MB
```
```c++
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        istringstream iss1(sentence1);
        vector<string> vec1((istream_iterator<string>{iss1}),
                            istream_iterator<string>());
        istringstream iss2(sentence2);
        vector<string> vec2((istream_iterator<string>{iss2}),
                            istream_iterator<string>());
        // Compare the prefixes or beginning of the strings.
        while (!vec1.empty() && !vec2.empty() && vec1.front() == vec2.front()) {
            vec1.erase(vec1.begin());
            vec2.erase(vec2.begin());
        }
        // Compare the suffixes or ending of the strings.
        while (!vec1.empty() && !vec2.empty() && vec1.back() == vec2.back()) {
            vec1.pop_back();
            vec2.pop_back();
        }
        return vec1.empty() || vec2.empty();
    }
};
```

**Solution 4: (Two Pointers)**
```
Runtime: 2 ms
Memory: 9.11 MB
```
```c++
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        // Convert sentences to lists of words
        stringstream ss1(sentence1), ss2(sentence2);
        string word;
        vector<string> s1Words, s2Words;
        while (ss1 >> word) s1Words.push_back(word);
        while (ss2 >> word) s2Words.push_back(word);

        int start = 0, ends1 = s1Words.size() - 1, ends2 = s2Words.size() - 1;

        // If words in s1 are more than s2, swap them and return the answer.
        if (s1Words.size() > s2Words.size()) return areSentencesSimilar(sentence2, sentence1);

        // Find the maximum words matching from the beginning.
        while (start < s1Words.size() && s1Words[start] == s2Words[start])
            ++start;

        // Find the maximum words matching in the end.
        while (ends1 >= 0 && s1Words[ends1] == s2Words[ends2]) {
            --ends1;
            --ends2;
        }

        // If ends1 index is less than start, then sentence is similar.
        return ends1 < start;
    }
};
```

**Solution 5: (Two Pointers)**
```
Runtime: 3 ms
Memory: 7.75 MB
```
```c++
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        if (sentence1.size() > sentence2.size()) {
            swap(sentence1, sentence2);
        }
        int m = sentence1.size(), n = sentence2.size(), i = 0, j = m-1, j2 = n-1, k;
        while (i <= j && sentence1[i] == sentence2[i]) {
            k = 0;
            while (i+k <= j && sentence1[i+k] != ' ' && sentence1[i+k] == sentence2[i+k]) {
                k += 1; 
            }
            if (i+k > j && (i+k > j2 || sentence2[i+k] == ' ')) {
                return true;
            }
            if (i+k <= j && sentence1[i+k] != ' ' || sentence2[i+k] != ' ') {
                break;
            }
            i += k+1;
        }
        while (i <= j && sentence1[j] == sentence2[j2]) {
            k = 0;
            while (i <= j-k && sentence1[j-k] != ' ' && sentence1[j-k] == sentence2[j2-k]) {
                k += 1;
            }
            if (i > j-k && i < j2-k && sentence2[j2-k] == ' ') {
                return true;
            }
            if (i <= j-k && sentence1[j-k] != ' ' || sentence2[j2-k] != ' ') {
                break;
            }
            j -= k+1;
            j2 -= k+1;
        }
        return i > j;
    }
};
```
