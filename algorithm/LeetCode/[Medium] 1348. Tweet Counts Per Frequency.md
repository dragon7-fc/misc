1348. Tweet Counts Per Frequency

Implement the class `TweetCounts` that supports two methods:

1. recordTweet(string tweetName, int time)

Stores the tweetName at the recorded time (in seconds).
1. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)

* Returns the total number of occurrences for the given `tweetName` per `minute`, `hour`, or `day` (depending on `freq`) starting from the `startTime` (in seconds) and ending at the `endTime` (in seconds).
* `freq` is always `minute`, `hour` or `day`, representing the time interval to get the total number of occurrences for the given tweetName.
* The first time interval always starts from the `startTime`, so the time intervals are `[startTime, startTime + delta*1>`,  `[startTime + delta*1, startTime + delta*2>`, `[startTime + delta*2, startTime + delta*3>`, ... , `[startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)>` for some non-negative number i and delta (which depends on `freq`).  
 

**Example:**
```
Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]. The frequency is per minute (60 seconds), so there is one interval of time: 1) [0, 60> - > 2 tweets.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2, 1]. The frequency is per minute (60 seconds), so there are two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
tweetCounts.recordTweet("tweet3", 120);                            // All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]. The frequency is per hour (3600 seconds), so there is one interval of time: 1) [0, 211> - > 4 tweets.
```

**Constraints:**

* There will be at most `10000` operations considering both `recordTweet` and `getTweetCountsPerFrequency`.
* `0 <= time, startTime, endTime <= 10^9`
* `0 <= endTime - startTime <= 10^4`

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 416 ms
Memory Usage: 20.3 MB
```
```python
class TweetCounts:

    def __init__(self):
        self.tweets = dict()

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.setdefault(tweetName, []).append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute": seconds = 60 
        elif freq == "hour": seconds = 3600
        else: seconds = 86400
        
        ans = [0] * ((endTime - startTime)//seconds + 1)
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime: ans[(t-startTime)//seconds] += 1
        return ans 


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```

**Solution 2: (Binary Search, multiset)**
```
Runtime: 59 ms
Memory: 39.6 MB
```
```c++
class TweetCounts {
    unordered_map<string, multiset<int>> m;
public:
    TweetCounts() {
        
    }
    
    void recordTweet(string tweetName, int time) {
        m[tweetName].insert(time);
    }
    
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        int d = 86400;
        if (freq[0] == 'm') {
            d = 60;
        } else if (freq[0] == 'h') {
            d = 3600;
        }
        vector<int> rst((endTime - startTime) / d + 1);
        const auto s = m.find(tweetName);
        if (s != m.end()) {
            for (auto it = s->second.lower_bound(startTime); it != s->second.end() && *it <= endTime; ++it) {
               ++rst[(*it - startTime) / d];
            }
        }
        return rst;
    }
};

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts* obj = new TweetCounts();
 * obj->recordTweet(tweetName,time);
 * vector<int> param_2 = obj->getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```
