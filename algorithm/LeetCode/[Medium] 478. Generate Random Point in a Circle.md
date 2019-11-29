478. Generate Random Point in a Circle

Given the radius and x-y positions of the center of a circle, write a function `randPoint` which generates a uniform random point in the circle.

**Note:**

1. input and output values are in floating-point.
2. radius and x-y position of the center of the circle is passed into the class constructor.
3. a point on the circumference of the circle is considered to be in the circle.
4. `randPoint` returns a size 2 array containing x-position and y-position of the random point, in that order.

**Example 1:**
```
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
```

**Example 2:**
```
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
```

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. `randPoint` has no arguments. Arguments are always wrapped with a list, even if there aren't

# Submissions
---
**Solution 1:**

**what goes on?**

there are more points on a larger circle
any larger circle should "occur" more

**how many points (total) are choosable?**

the area of the disk thats centered at (x,y)
```
pi r ^ 2
```

**choose a random disk area between 0 and max**

choose a random value v between 0 and pi r ^ 2
```
0 <= v <= pi R ^ 2
```

**whats the radius of that disk?**

let the radius be r
```
v = pi * r ** 2
r = (v/pi) ** 0.5
```
then
```
x = xc + rcos(theta)
x = yx + ysin(theta)
```
where theta is a random angle in radius (at most 2 pi = 360 deg)

```
Runtime: 160 ms
Memory Usage: 23.1 MB
```
```python
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        r = (self.randomize(0, math.pi * self.r ** 2) / math.pi) ** 0.5
        theta = self.randomize(0, 2 * math.pi)
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]
        

    def randomize(self,a,b):
        return random.uniform(a, b)


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```