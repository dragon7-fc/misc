3369. Design an Array Statistics Tracker

Design a data structure that keeps track of the values in it and answers some queries regarding their mean, median, and mode.

Implement the `StatisticsTracker` class.

`StatisticsTracker()`: Initialize the StatisticsTracker object with an empty array.
`void addNumber(int number)`: Add `number` to the data structure.
`void removeFirstAddedNumber()`: Remove the earliest added number from the data structure.
`int getMean()`: Return the floored **mean** of the numbers in the data structure.
`int getMedian()`: Return the **median** of the numbers in the data structure.
`int getMode()`: Return the **mode** of the numbers in the data structure. If there are multiple modes, return the smallest one.
Note:

* The **mean** of an array is the sum of all the values divided by the number of values in the array.
* The **median** of an array is the middle element of the array when it is sorted in non-decreasing order. If there are two choices for a median, the larger of the two values is taken.
* The **mode** of an array is the element that appears most often in the array.
 

**Example 1:**
```
Input:
["StatisticsTracker", "addNumber", "addNumber", "addNumber", "addNumber", "getMean", "getMedian", "getMode", "removeFirstAddedNumber", "getMode"]
[[], [4], [4], [2], [3], [], [], [], [], []]

Output:
[null, null, null, null, null, 3, 4, 4, null, 2]

Explanation

StatisticsTracker statisticsTracker = new StatisticsTracker();
statisticsTracker.addNumber(4); // The data structure now contains [4]
statisticsTracker.addNumber(4); // The data structure now contains [4, 4]
statisticsTracker.addNumber(2); // The data structure now contains [4, 4, 2]
statisticsTracker.addNumber(3); // The data structure now contains [4, 4, 2, 3]
statisticsTracker.getMean(); // return 3
statisticsTracker.getMedian(); // return 4
statisticsTracker.getMode(); // return 4
statisticsTracker.removeFirstAddedNumber(); // The data structure now contains [4, 2, 3]
statisticsTracker.getMode(); // return 2
```

**Example 2:**
```
Input:
["StatisticsTracker", "addNumber", "addNumber", "getMean", "removeFirstAddedNumber", "addNumber", "addNumber", "removeFirstAddedNumber", "getMedian", "addNumber", "getMode"]
[[], [9], [5], [], [], [5], [6], [], [], [8], []]

Output:
[null, null, null, 7, null, null, null, null, 6, null, 5]

Explanation

StatisticsTracker statisticsTracker = new StatisticsTracker();
statisticsTracker.addNumber(9); // The data structure now contains [9]
statisticsTracker.addNumber(5); // The data structure now contains [9, 5]
statisticsTracker.getMean(); // return 7
statisticsTracker.removeFirstAddedNumber(); // The data structure now contains [5]
statisticsTracker.addNumber(5); // The data structure now contains [5, 5]
statisticsTracker.addNumber(6); // The data structure now contains [5, 5, 6]
statisticsTracker.removeFirstAddedNumber(); // The data structure now contains [5, 6]
statisticsTracker.getMedian(); // return 6
statisticsTracker.addNumber(8); // The data structure now contains [5, 6, 8]
statisticsTracker.getMode(); // return 5
```

**Constraints:**

* `1 <= number <= 10^9`
* At most, `10^5` calls will be made to `addNumber`, `removeFirstAddedNumber`, `getMean`, `getMedian`, and `getMode` in total.
* `removeFirstAddedNumber`, `getMean`, `getMedian`, and `getMode` will be called only if there is at least one element in the data structure.

# Submissions
---
**Solution 1: (Maintain separate data structures for each statistic)**

StatisticsTracker statisticsTracker = new StatisticsTracker();
statisticsTracker.addNumber(4); // The data structure now contains [4]
sum     | 4
nums    | 4
numFreq | (4,1)
freqNum | (1,4)
upper   | 4
lower   |  
statisticsTracker.addNumber(4); // The data structure now contains [4, 4]
sum     | 4     | 8
nums    | 4     | 4,4
numFreq | (4,1) | (4,2)
freqNum | (1,4) | (2,4)
upper   | 4     | 4
lower   |       | 4
statisticsTracker.addNumber(2); // The data structure now contains [4, 4, 2]
sum     | 4     | 8     | 10
nums    | 4     | 4,4   | 4,4,2
numFreq | (4,1) | (4,2) | (4,2) (2,1)
freqNum | (1,4) | (2,4) | (2,4) (1,2)
upper   | 4     | 4     | 4,4
lower   |       | 4     | 2
statisticsTracker.addNumber(3); // The data structure now contains [4, 4, 2, 3]
sum     | 4     | 8     | 10          | 13
nums    | 4     | 4,4   | 4,4,2       | 4,4,2,3
numFreq | (4,1) | (4,2) | (4,2) (2,1) | (4,2) (2,1) (3,1)
freqNum | (1,4) | (2,4) | (2,4) (1,2) | (1,3) (1,2) (2,4)
upper   | 4     | 4     | 4,4         | 4,4< median     ^
lower   |       | 4     | 2           | 2,3             mode
statisticsTracker.getMean(); // return 3
13 / 4
statisticsTracker.getMedian(); // return 4
statisticsTracker.getMode(); // return 4
statisticsTracker.removeFirstAddedNumber(); // The data structure now contains [4, 2, 3]
sum     | 4     | 8     | 10          | 13                | 9
nums    | 4     | 4,4   | 4,4,2       | 4,4,2,3           | 4,2,3
numFreq | (4,1) | (4,2) | (4,2) (2,1) | (4,2) (2,1) (3,1) | (4,1) (2,1) (3,1)
freqNum | (1,4) | (2,4) | (2,4) (1,2) | (1,3) (1,2) (2,4) | (1,4) (1,3) (1,2)
upper   | 4     | 4     | 4,4         | 4,4               | 4,3            ^
lower   |       | 4     | 2           | 2,3               | 2              mode
statisticsTracker.getMode(); // return 2

```
Runtime: 617 ms, Beats 31.58%
Memory: 364.73 MB, Beats 26.32%
```
```c++
class cmp {
public:
    bool operator() (const pair<int, int>& a, const pair<int, int>& b) const {
        if (a.first != b.first) {
            return a.first < b.first;
        } else {
            return a.second > b.second;
        }
    }
};

class StatisticsTracker {
    long long sum;
    deque<int> nums;
    multiset<int, greater<>> upper;             // min heap (for bigger nums)
    multiset<int> lower;                        // max heap (for smaller nums)
    unordered_map<int, int> numFreq;            // {num, freq}
    set<pair<int, int>, cmp> freqNum;           // {freq, num}

    void balanceTwoHeaps() {
        if (upper.size() == lower.size() - 1) { // if upper over erase
            upper.insert(*prev(lower.end()));
            lower.erase(prev(lower.end()));
        }
        if (lower.size() == upper.size() - 2) { // if lower over erase
            lower.insert(*prev(upper.end()));
            upper.erase(prev(upper.end()));
        }
    }
public:
    StatisticsTracker() {
        sum = 0;
    }
    
    void addNumber(int number) {
        // maintain sum and deque
        sum += number;
        nums.push_back(number);

        // maintain freq
        int prevFreq = numFreq[number]++;
        int currFreq = prevFreq + 1;
        if (prevFreq != 0) {
            freqNum.erase({prevFreq, number});
        }
        freqNum.insert({currFreq, number});

        // maintain two heap
        upper.insert(number);
        lower.insert(*prev(upper.end()));
        upper.erase(prev(upper.end()));
        if (upper.size() < lower.size()) {
            upper.insert(*prev(lower.end()));
            lower.erase(prev(lower.end()));
        }
    }
    
    void removeFirstAddedNumber() {
        // maintain sum and deque
        int number = nums.front(); // the number to remove
        nums.pop_front();
        sum -= number;
        
        // maintain freq
        int prevFreq = numFreq[number]--;
        int currFreq = prevFreq - 1;
        freqNum.erase({prevFreq, number});
        if (currFreq != 0) {
            freqNum.insert({currFreq, number});
        } else {
            numFreq.erase(number);
        }

        // maintain two heap
        if (number >= *prev(upper.end())) {
            upper.erase(upper.find(number));
        } else {
            lower.erase(lower.find(number));
        }
        balanceTwoHeaps();
    }
    
    int getMean() {
        return sum / nums.size();
    }
    
    int getMedian() {
        return *prev(upper.end());
    }
    
    int getMode() {
        return prev(freqNum.end())->second;
    }
};

/**
 * Your StatisticsTracker object will be instantiated and called as such:
 * StatisticsTracker* obj = new StatisticsTracker();
 * obj->addNumber(number);
 * obj->removeFirstAddedNumber();
 * int param_3 = obj->getMean();
 * int param_4 = obj->getMedian();
 * int param_5 = obj->getMode();
 */
```
