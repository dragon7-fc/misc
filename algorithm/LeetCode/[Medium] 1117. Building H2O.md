1117. Building H2O

There are two kinds of threads: `oxygen` and `hydrogen`. Your goal is to group these threads to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given `releaseHydrogen` and `releaseOxygen` methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

* If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads.
* If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.

We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up with. The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

 

**Example 1:**
```
Input: water = "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
```

**Example 2:**
```
Input: water = "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
```

**Constraints:**

* `3 * n == water.length`
* `1 <= n <= 20`
* water[i] is either `'H'` or `'O'`.
* There will be exactly `2 * n` `'H'` in water.
* There will be exactly `n` `'O'` in water.

# Submissions
---
**Solution 1: (condition_variable and Mutex)**
```
Runtime: 8 ms, Beats 32.45%
Memory: 12.17 MB, Beats 22.02%
```
```c++
class H2O {
    mutex mtx;
    condition_variable cv;
    int hydrogen_count = 0;
public:
    H2O() {
        
    }

    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lock(mtx);

        // Wait until there are less than 2 hydrogens
        while (hydrogen_count >= 2) 
        {
            // Mutex unlocked & thread enters waiting state
            cv.wait(lock);
        }

        hydrogen_count++;
        
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();

        // If two hydrogen atoms are ready, wake up oxygen
        cv.notify_one();
    }

    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lock(mtx);

        // Wait until exactly 2 hydrogens are available
        while (hydrogen_count < 2) {
            cv.wait(lock);
        }

        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();

        // Reset for the next water molecule
        hydrogen_count = 0;
        // Notify waiting hydrogen threads
        cv.notify_all(); 
    }
};
```

**Solution 2: (Mutex)**
```
Runtime: 18 ms, Beats 38.28%
Memory: 12.29 MB, Beats 85.94%
```
```c
typedef struct {
    // User defined data may be declared here.
    int turn;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} H2O;

void releaseHydrogen();

void releaseOxygen();

H2O* h2oCreate() {
    H2O* obj = (H2O*) malloc(sizeof(H2O));
    
    // Initialize user defined data here.
    obj->turn = 1;
    pthread_mutex_init(&obj->lock, NULL);
    pthread_cond_init(&obj->cond, NULL);
    return obj;
}

void hydrogen(H2O* obj) {
    pthread_mutex_lock(&(obj->lock));
    while (obj->turn % 3 == 0) {
        pthread_cond_wait(&obj->cond, &obj->lock); 
    }

    // releaseHydrogen() outputs "H". Do not change or remove this line.
    releaseHydrogen();

    obj->turn += 1;
    pthread_mutex_unlock(&(obj->lock));
    pthread_cond_broadcast(&(obj->cond));
}

void oxygen(H2O* obj) {
    pthread_mutex_lock(&(obj->lock));
    while (obj->turn % 3) {
        pthread_cond_wait(&obj->cond, &obj->lock); 
    }

    // releaseOxygen() outputs "O". Do not change or remove this line.
    releaseOxygen();

    obj->turn += 1;
    pthread_mutex_unlock(&(obj->lock));
    pthread_cond_broadcast(&(obj->cond));
}

void h2oFree(H2O* obj) {
    // User defined data may be cleaned up here.
    
}
```

**Solution 3: (Semaphore)**
```
Runtime: 12 ms, Beats 53.91%
Memory: 11.90 MB, Beats 99.22%
```
```c
typedef struct {
    // User defined data may be declared here.
    int turn;
    sem_t sem_hydrogen;
    sem_t sem_oxygen;
} H2O;

void releaseHydrogen();

void releaseOxygen();

H2O* h2oCreate() {
    H2O* obj = (H2O*) malloc(sizeof(H2O));
    
    // Initialize user defined data here.
    obj->turn = 1;
    sem_init(&obj->sem_hydrogen, 0, 1);
    sem_init(&obj->sem_oxygen, 0, 0);
    return obj;
}

void hydrogen(H2O* obj) {
    sem_wait(&obj->sem_hydrogen);

    // releaseHydrogen() outputs "H". Do not change or remove this line.
    releaseHydrogen();

    obj->turn += 1;
    if (obj->turn % 3) {
        sem_post(&obj->sem_hydrogen);
    } else {
        sem_post(&obj->sem_oxygen);
    }
}

void oxygen(H2O* obj) {
    sem_wait(&obj->sem_oxygen);

    // releaseOxygen() outputs "O". Do not change or remove this line.
    releaseOxygen();

    obj->turn += 1;
    if (obj->turn % 3) {
        sem_post(&obj->sem_hydrogen);
    } else {
        sem_post(&obj->sem_oxygen);
    }
}

void h2oFree(H2O* obj) {
    // User defined data may be cleaned up here.
    
}
```
