1344. Angle Between Hands of a Clock

Given two numbers, `hour` and `minutes`. Return the smaller angle (in sexagesimal units) formed between the `hour` and the `minute` hand.

 

**Example 1:**

![1344_sample_1_1673.png](img/1344_sample_1_1673.png)
```
Input: hour = 12, minutes = 30
Output: 165
```

**Example 2:**

![1344_sample_2_1673.png](img/1344_sample_2_1673.png)
```
Input: hour = 3, minutes = 30
Output: 75
```

**Example 3:**

![1344_sample_3_1673.png](img/1344_sample_3_1673.png)
```
Input: hour = 3, minutes = 15
Output: 7.5
```

**Example 4:**
```
Input: hour = 4, minutes = 50
Output: 155
```

**Example 5:**
```
Input: hour = 12, minutes = 0
Output: 0
```

**Constraints:**

* `1 <= hour <= 12`
* `0 <= minutes <= 59`
* Answers within `10^-5` of the actual value will be accepted as correct.

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Degree covered by hour hand (hour area + minutes area)
        h = (hour%12 * 30) + (minutes/60 * 30)
        
        # Degree covered by minute hand (Each minute = 6 degree)
        m = minutes * 6
        
        # Absolute angle between them
        angle = abs(m - h)
        
        # If the angle is obtuse (>180), convert it to acute (0<=x<=180)
        if angle > 180:
            angle = 360.0 - angle
        
        return (angle)
```

**Solution 2: (Math)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    double angleClock(int hour, int minutes) {
        double min_angle = ((double)minutes/(double)60)*360; //finding angle of minute hand
        double hour_angle = (double)((hour - 0)%12)*30 + ((double)1/(double)12)*min_angle; // finding angle of hour hand
        double answer = abs(min_angle - hour_angle); // finding the difference
        return min(answer, 360.0 - answer); // returning the min difference
    }
};
```