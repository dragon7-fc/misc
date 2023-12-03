2034. Stock Price Fluctuation

You are given a stream of **records** about a particular stock. Each record contains a **timestamp** and the corresponding **price** of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream **correcting** the price of the previous wrong record.

Design an algorithm that:

* **Updates** the price of the stock at a particular timestamp, **correcting** the price from any previous records at the timestamp.
* Finds the **latest price** of the stock based on the current records. The **latest price** is the price at the latest timestamp recorded.
* Finds the **maximum price** the stock has been based on the current records.
* Finds the **minimum price** the stock has been based on the current records.

Implement the StockPrice class:

* `StockPrice()` Initializes the object with no price records.
* `void update(int timestamp, int price)` Updates the `price` of the stock at the given `timestamp`.
* `int current()` Returns the **latest price** of the stock.
* `int maximum()` Returns the **maximum price** of the stock.
* `int minimum()` Returns the **minimum price** of the stock.
 

**Example 1:**

```
Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.
```

**Constraints:**

* `1 <= timestamp, price <= 10^9`
* At most 10^5 calls will be made in total to `update`, `current`, `maximum`, and `minimum`.
* `current`, `maximum`, and `minimum` will be called only after `update` has been called at least once.

# Submissions
---
**Solution 1: (Hash Table, Heap)**
```
Runtime: 860 ms
Memory Usage: 60.4 MB
```
```python
class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.highestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []
    def update(self, timestamp: int, price: int) -> None:
        #Keep track of current prices
        self.timestamps[timestamp] = price
        self.highestTimestamp = max(self.highestTimestamp, timestamp)
        
		#For maximum/minimum
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        #Just return the highest timestamp in O(1)
        return self.timestamps[self.highestTimestamp]

    def maximum(self) -> int:
        currPrice, timestamp = heappop(self.maxHeap)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while -currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.maxHeap)
            
        heappush(self.maxHeap, (currPrice, timestamp))
        return -currPrice

    def minimum(self) -> int:
        currPrice, timestamp = heappop(self.minHeap)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.minHeap)
            
        heappush(self.minHeap, (currPrice, timestamp))
        return currPrice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
```

**Solution 2: (multiset)**
```
Runtime: 484 ms
Memory Usage: 168.7 MB
```
```c++
class StockPrice {
public:
    map<int, int> rec;
    multiset<int> count;
    
    StockPrice() {
        
    }
    
    void update(int timestamp, int price) {
        if (rec.find(timestamp) != rec.end())
            count.erase(count.find(rec[timestamp]));
        rec[timestamp] = price;
        count.insert(price);
    }
    
    int current() {
        return rec.rbegin()->second;
    }
    
    int maximum() {
        return *count.rbegin();
    }
    
    int minimum() {
        return *count.begin();
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */
```
