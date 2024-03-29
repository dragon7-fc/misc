1396. Design Underground System

Implement the class UndergroundSystem that supports three methods:

1. `checkIn(int id, string stationName, int t)`

    * A customer with id card equal to `id`, gets in the station `stationName` at time `t`.
    * A customer can only be checked into one place at a time.
1. `checkOut(int id, string stationName, int t)`

    * A customer with `id` card equal to `id`, gets out from the station `stationName` at time `t`.
1. `getAverageTime(string startStation, string endStation)`

    * Returns the average time to travel between the `startStation` and the `endStation`.
    * The average time is computed from all the previous traveling from `startStation` to `endStation` that happened **directly**.
    * Call to `getAverageTime` is always valid.

You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time **t1** at some station, then it gets out at time **t2** with **t2 > t1**. All events happen in chronological order.

 

**Example 1:**
```
Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.0,11.0,null,11.0,null,12.0]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.0
```

**Constraints:**

* There will be at most `20000` operations.
* `1 <= id, t <= 10^6`
* All strings consist of uppercase, lowercase English letters and digits.
* `1 <= stationName.length <= 10`
* Answers within `10^-5` of the actual value will be accepted as correct.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 484 ms
Memory Usage: 25 MB
```
```python
class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevstation, prevt = self.check[id]
        time = t-prevt
        if (prevstation, stationName) in self.time:
            totaltime, stationN = self.time[(prevstation, stationName)]
            self.time[(prevstation,stationName)] = (totaltime+time, stationN+1)
        else:
            self.time[(prevstation,stationName)] = (time,1)
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totaltime, stationN = self.time[(startStation,endStation)]
        return totaltime/stationN


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```

**Solution 2: (Hash Table)**
```
Runtime: 178 ms
Memory: 58.9 MB
```
```c++
class UndergroundSystem {
    // id -> {station name,time}
    unordered_map<int,pair<string,int>>checkInStation; 

    // Route -> {total time,count}
    unordered_map<string,pair<int,int>> checkOutStation;
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        checkInStation[id] = {stationName,t};
    }
    
    void checkOut(int id, string stationName, int t) {
        auto cIn = checkInStation[id];
        checkInStation.erase(id);
        string route = cIn.first + "_" + stationName;
        checkOutStation[route].first += t - cIn.second;
        checkOutStation[route].second += 1; 
    }
    
    double getAverageTime(string startStation, string endStation) {
        string route  = startStation + "_" + endStation;
        auto time = checkOutStation[route];
        return (double)time.first/time.second;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
```
