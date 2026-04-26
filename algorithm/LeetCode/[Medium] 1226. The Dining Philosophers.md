1226. The Dining Philosophers

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right forks. Each fork can be held by only one philosopher and so a philosopher can use the fork only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both forks so that the forks become available to others. A philosopher can take the fork on their right or the one on their left as they become available, but cannot start eating before getting both forks.

Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite supply and an infinite demand are assumed.

Design a discipline of behaviour (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.

![1226_an_illustration_of_the_dining_philosophers_problem.png](img/1226_an_illustration_of_the_dining_philosophers_problem.png)

The problem statement and the image above are taken from wikipedia.org

 

The philosophers' ids are numbered from 0 to 4 in a clockwise order. Implement the function `void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)` where:

* `philosopher` is the id of the philosopher who wants to eat.
* `pickLeftFork` and `pickRightFork` are functions you can call to pick the corresponding forks of that philosopher.
* `eat` is a function you can call to let the philosopher eat once he has picked both forks.
* `putLeftFork` and putRightFork are functions you can call to put down the corresponding forks of that philosopher.
* The philosophers are assumed to be thinking as long as they are not asking to eat (the function is not being called with their number).

Five threads, each representing a philosopher, will simultaneously use one object of your class to simulate the process. The function may be called for the same philosopher more than once, even before the last call ends.

 

**Example 1:**
```
Input: n = 1
Output: [[3,2,1],[3,1,1],[3,0,3],[3,1,2],[3,2,2],[4,2,1],[4,1,1],[2,2,1],[2,1,1],[1,2,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[4,2,2],[1,1,1],[1,0,3],[1,1,2],[1,2,2],[0,1,1],[0,2,1],[0,0,3],[0,1,2],[0,2,2]]
Explanation:
n is the number of times each philosopher will call the function.
The output array describes the calls you made to the functions controlling the forks and the eat function, its format is:
output[i] = [a, b, c] (three integers)
- a is the id of a philosopher.
- b specifies the fork: {1 : left, 2 : right}.
- c specifies the operation: {1 : pick, 2 : put, 3 : eat}.
```

**Constraints:**

* `1 <= n <= 60`

# Submissions
---
**Solution 1: (lock the table then pick up both forks together)**
```
Runtime: 20 ms, Beats 90.73%
Memory: 18.55 MB, Beats 51.19%
```
```c++
lass DiningPhilosophers {
    mutex mtxFork[5];
    mutex mtxTable;
public:
    DiningPhilosophers() {
        
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
		int left = philosopher;
        int right = (philosopher + 1) % 5;
		
        unique_lock<mutex> lckTable(mtxTable);
        unique_lock<mutex> lckForkLeft(mtxFork[left]);
        unique_lock<mutex> lckForkRight(mtxFork[right]);
        lckTable.unlock(); // after locking both forks, we can safely unlock table
        
        pickLeftFork(); pickRightFork(); eat(); putRightFork(); putLeftFork();
        // locks will be automatically released due to unique_lock RAII design
    }
};
```

**Solution 2: (change forks picking order)**
```
Runtime: 48 ms, Beats 11.98%
Memory: 18.79 MB, Beats 19.93%
```
```c++
class DiningPhilosophers {
    mutex mtx[5];
public:
    DiningPhilosophers() {
        
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
		int left = philosopher;
        int right = (philosopher + 1) % 5;
        
        if(philosopher % 2 == 0){
            mtx[right].lock(); // lock right before left
            mtx[left].lock();
            pickLeftFork(); pickRightFork();
        }
		else{
            mtx[left].lock(); // lock left before right
            mtx[right].lock();
            pickLeftFork(); pickRightFork();
        }
        
        eat(); putRightFork(); putLeftFork();
        mtx[left].unlock();
        mtx[right].unlock();
    }
};
```

**Solution 3: (limit 4 philosophers to eat at same time)**
```
Runtime: 38 ms, Beats 32.90%
Memory: 18.49 MB, Beats 66.53%
```
```c++
class Semaphore {
private:
	int count;
    mutex mtx;
    condition_variable cv;
	
public:
    Semaphore(int n = 0) : count(n) { }
    void Set(int n) { count = n; }
    void Signal() {
        unique_lock<mutex> lck(mtx);
        ++count;
        cv.notify_one();
    }
    void Wait() {
        unique_lock<mutex> lck(mtx);
        cv.wait(lck, [&](){ return count > 0; }); // standard format of wait() lambda expression
        --count;
    }
};

class DiningPhilosophers {
    mutex mtx[5];
    Semaphore sem;
public:
    DiningPhilosophers() {
        sem.Set(4);
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
		int left = philosopher;
        int right = (philosopher + 1) % 5;
        
        sem.Wait(); // if there are 4 philosophers eating, thread will wait here

        unique_lock<mutex> lckLeft(mtx[left]);
        unique_lock<mutex> lckRight(mtx[right]);
        
        pickLeftFork(); pickRightFork(); eat(); putRightFork(); putLeftFork();
        
        lckLeft.unlock();
        lckRight.unlock();

        sem.Signal(); // finish eating, release 1 spot for other philosophers
    }
};
```
