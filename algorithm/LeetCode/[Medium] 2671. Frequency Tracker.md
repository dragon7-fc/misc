2671. Frequency Tracker

Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

Implement the `FrequencyTracker` class.

* `FrequencyTracker():` Initializes the `FrequencyTracker` object with an empty array initially.
* `void add(int number)`: Adds `number` to the data structure.
* `void deleteOne(int number)`: Deletes **one** occurence of `number` from the data structure. The data structure **may not contain** `number`, and in this case nothing is deleted.
* `bool hasFrequency(int frequency)`: Returns `true` if there is a number in the data structure that occurs `frequency` number of times, otherwise, it returns `false`.
 

**Example 1:**
```
Input
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
Output
[null, null, null, true]

Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.add(3); // The data structure now contains [3, 3]
frequencyTracker.hasFrequency(2); // Returns true, because 3 occurs twice
```

**Example 2:**
```
Input
["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]
Output
[null, null, null, false]

Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // The data structure now contains [1]
frequencyTracker.deleteOne(1); // The data structure becomes empty []
frequencyTracker.hasFrequency(1); // Returns false, because the data structure is empty
```

**Example 3:**
```
Input
["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
[[], [2], [3], [1]]
Output
[null, false, null, true]

Explanation
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.hasFrequency(2); // Returns false, because the data structure is empty
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.hasFrequency(1); // Returns true, because 3 occurs once
```
 

**Constraints:**

* `1 <= number <= 10^5`
* `1 <= frequency <= 10^5`
* `At most, 2 * 10^5 calls will be made to `add`, `deleteOne`, and `hasFrequency` in total.`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 706 ms
Memory: 72.6 MB
```
```python
class FrequencyTracker:

    def __init__(self):
        self.cnt = collections.Counter()
        self.freq = collections.Counter()

    def add(self, number: int) -> None:
        self.freq[self.cnt[number]] -= 1
        self.freq[self.cnt[number] + 1] += 1
        self.cnt[number] += 1
        

    def deleteOne(self, number: int) -> None:
        if self.cnt[number]:
            self.freq[self.cnt[number]] -= 1
            self.freq[self.cnt[number] - 1] += 1
            self.cnt[number] -= 1
            
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
```

**Solution 2: (Two Arrays)**
```
Runtime: 718 ms
Memory: 339.8 MB
```
```c++
class FrequencyTracker {
    int cnt[100001] = {}, freq[100001] = {};
public:
    FrequencyTracker() {
        
    }
    
    void add(int number) {
        --freq[cnt[number]];
        ++freq[++cnt[number]];
    }
    
    void deleteOne(int number) {
        if (cnt[number]) {
            --freq[cnt[number]];
            ++freq[--cnt[number]];
        }
    }
    
    bool hasFrequency(int frequency) {
        return freq[frequency];
    }
};

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker* obj = new FrequencyTracker();
 * obj->add(number);
 * obj->deleteOne(number);
 * bool param_3 = obj->hasFrequency(frequency);
 */
```
