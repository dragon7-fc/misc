855. Exam Room

In an exam room, there are `N` seats in a single row, numbered `0, 1, 2, ..., N-1`.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class `ExamRoom(int N)` that exposes two functions: `ExamRoom.seat()` returning an int representing what seat the student sat in, and `ExamRoom.leave(int p)` representing that the student in seat number `p` now leaves the room.  It is guaranteed that any calls to `ExamRoom.leave(p)` have a student sitting in seat `p`.

 

**Example 1:**
```
Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
```

**Note:**

* `1 <= N <= 10^9`
* `ExamRoom.seat()` and `ExamRoom.leave()` will be called at most `10^4` times across all test cases.
* Calls to `ExamRoom.leave(p)` are guaranteed to have a student currently sitting in seat number `p`.

# Solution
---
## Approach 1: Maintain Sorted Positions
**Intuition**

We'll maintain `ExamRoom.students`, a sorted list (or `TreeSet` in Java) of positions the students are currently seated in.

**Algorithm**

The `ExamRoom.leave(p)` operation is clear - we will just `list.remove` (or `TreeSet.remove`) the student from `ExamRoom.students`.

Let's focus on the `ExamRoom.seat() : int` operation. For each pair of adjacent students `i` and `j`, the maximum distance to the closest student is `d = (j - i) / 2`, achieved in the left-most seat `i + d`. Otherwise, we could also sit in the left-most seat, or the right-most seat.

Finally, we should handle the case when there are no students separately.

For more details, please review the comments made in the implementations.

```python
class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) / 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)
```

**Complexity Analysis**

* Time Complexity: Each seat operation is $O(P)$, (where $P$ is the number of students sitting), as we iterate through every student. Each `leave` operation is $O(P)$ ($\log P$ in Java).

* Space Complexity: $O(P)$, the space used to store the positions of each student sitting.

# Submissions
---
**Solution 1: (Maintain Sorted Positions)**
```
Runtime: 324 ms
Memory Usage: 12.9 MB
```
```python
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student
    
    def leave(self, p: int) -> None:
        self.students.remove(p)
        

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
```

**Solution 2: (Straight Forward)**
```
Runtime: 143 ms
Memory: 22.89 MB
```
```c++
class ExamRoom {
    int N;
    vector<int> arr;
public:
    ExamRoom(int n) {
        N = n;
    }
    
    int seat() {
        if (arr.size() == 0) {
            arr.push_back(0);
            return 0;
        }
        int d = max(arr[0], N - 1 - arr.back());
        for (int i = 0; i < arr.size() - 1; ++i) {
            d = max(d, (arr[i + 1] - arr[i]) / 2);
        }
        if (arr[0] == d) {
            arr.insert(arr.begin(), 0);
            return 0;
        }
        for (int i = 0; i < arr.size() - 1; ++i)
            if ((arr[i + 1] - arr[i]) / 2 == d) {
                arr.insert(arr.begin() + i + 1, (arr[i + 1] + arr[i]) / 2);
                return arr[i + 1];
            }
        arr.push_back(N - 1);
        return N - 1;
    }
    
    void leave(int p) {
        for (int i = 0; i < arr.size(); ++i) {
            if (arr[i] == p) {
                arr.erase(arr.begin() + i);
            }
        }
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom* obj = new ExamRoom(n);
 * int param_1 = obj->seat();
 * obj->leave(p);
 */
```
