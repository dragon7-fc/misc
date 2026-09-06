1116. Print Zero Even Odd

You have a function `printNumber` that can be called with an integer parameter and prints it to the console.

* For example, calling `printNumber(7)` prints 7 to the console.

You are given an instance of the class `ZeroEvenOdd` that has three functions: `zero`, `even`, and `odd`. The same instance of `ZeroEvenOdd` will be passed to three different threads:

* Thread A: calls `zero()` that should only output `0`'s.
* Thread B: calls `even()` that should only output even numbers.
* Thread C: calls `odd()` that should only output odd numbers.

Modify the given class to output the series `"010203040506..."` where the length of the series must be `2n`.

Implement the `ZeroEvenOdd` class:

* `ZeroEvenOdd(int n)` Initializes the object with the number `n` that represents the numbers that should be printed.
* `void zero(printNumber)` Calls `printNumber` to output one zero.
* `void even(printNumber)` Calls `printNumber` to output one even number.
* `void odd(printNumber)` Calls `printNumber` to output one odd number.
 

**Example 1:**
```
Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously.
One of them calls zero(), the other calls even(), and the last one calls odd().
"0102" is the correct output.
```

**Example 2:**
```
Input: n = 5
Output: "0102030405"
```

**Constraints:**

* `1 <= n <= 1000`

# Submissions
---
**Solution 1: (semaphore)**
```
Runtime: 3 ms, Beats 69.00%
Memory: 11.14 MB, Beats 36.34%
```
```c++
class ZeroEvenOdd {
private:
    int n;
    sem_t sem_z, sem_o, sem_e;

public:
    ZeroEvenOdd(int n) {
        this->n = n;
        sem_init(&sem_z, 0, 1);
        sem_init(&sem_o, 0, 0);
        sem_init(&sem_e, 0, 0);
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        for (int i = 1; i <= n; ++i) {
            sem_wait(&sem_z);
            printNumber(0);
            if (i & 1) sem_post(&sem_o);
            else sem_post(&sem_e);
        }
    }

    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            sem_wait(&sem_e);
            printNumber(i);
            sem_post(&sem_z);
        }
    }

    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            sem_wait(&sem_o);
            printNumber(i);
            sem_post(&sem_z);
        }
    }

    ~ZeroEvenOdd() {
        sem_destroy(&sem_z);
        sem_destroy(&sem_o);
        sem_destroy(&sem_e);
    }
};
```

**Solution 2: (Mutex)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.66 MB, Beats -%
```
```c
typedef struct {
    int n;
    int turn;
    bool is_zero;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} ZeroEvenOdd;

ZeroEvenOdd* zeroEvenOddCreate(int n) {
    ZeroEvenOdd* obj = (ZeroEvenOdd*) malloc(sizeof(ZeroEvenOdd));
    obj->n = n;
    obj->turn = 1;
    obj->is_zero = true;
    pthread_mutex_init(&(obj->lock), NULL);
    pthread_cond_init(&(obj->cond), NULL);
    return obj;
}

void printNumber(int x);

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.

void zero(ZeroEvenOdd* obj) {
    for (int _ = 1; _ <= obj->n; _ ++) {
        pthread_mutex_lock(&(obj->lock));
        while (!obj->is_zero) {
            pthread_cond_wait(&obj->cond, &obj->lock); 
        }
        printNumber(0);
        obj->is_zero = false;
        pthread_mutex_unlock(&obj->lock);
        pthread_cond_broadcast(&obj->cond);        
    }
    pthread_exit(NULL);
}

void even(ZeroEvenOdd* obj) {
    for (int _ = 2; _ <= obj->n; _ += 2) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->is_zero || obj->turn % 2) {
            pthread_cond_wait(&obj->cond, &obj->lock); 
        }
        printNumber(obj->turn);
        obj->turn += 1;
        obj->is_zero = true;
        pthread_mutex_unlock(&obj->lock);
        pthread_cond_broadcast(&obj->cond);   
    }
    pthread_exit(NULL);
}

void odd(ZeroEvenOdd* obj) {
    for (int _ = 1; _ <= obj->n; _ += 2) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->is_zero || (obj->turn % 2 == 0)) {
            pthread_cond_wait(&obj->cond, &obj->lock); 
        }
        printNumber(obj->turn);
        obj->turn += 1;
        obj->is_zero = true;
        pthread_mutex_unlock(&obj->lock);
        pthread_cond_broadcast(&obj->cond);
    }
    pthread_exit(NULL);
}

void zeroEvenOddFree(ZeroEvenOdd* obj) {
    free(obj);
}
```

**Solution 3: (Semaphore)**
```
Runtime: 4 ms, Beats 67.61%
Memory: 9.60 MB, Beats -%
```
```c
typedef struct {
    int n;
    int turn;
    sem_t sem_zero;
    sem_t sem_even;
    sem_t sem_odd;
} ZeroEvenOdd;

ZeroEvenOdd* zeroEvenOddCreate(int n) {
    ZeroEvenOdd* obj = (ZeroEvenOdd*) malloc(sizeof(ZeroEvenOdd));
    obj->n = n;
    obj->turn = 1;
    sem_init(&obj->sem_zero, 0, 1);
    sem_init(&obj->sem_even, 0, 0);
    sem_init(&obj->sem_odd, 0, 0);
    return obj;
}

void printNumber(int x);

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.

void zero(ZeroEvenOdd* obj) {
    for (int _ = 1; _ <= obj->n; _ ++) {
        sem_wait(&obj->sem_zero);
        printNumber(0);
        if (obj->turn & 1) {
            sem_post(&obj->sem_odd);
        } else {
            sem_post(&obj->sem_even);
        }
    }
    sem_post(&obj->sem_even);
    sem_post(&obj->sem_odd);
    pthread_exit(NULL);
}

void even(ZeroEvenOdd* obj) {
    for (int _ = 2; _ <= obj->n; _ += 2) {
        sem_wait(&obj->sem_even);
        printNumber(obj->turn);
        obj->turn += 1;
        sem_post(&obj->sem_zero);
    }
    sem_post(&obj->sem_zero);
    sem_post(&obj->sem_odd);
    pthread_exit(NULL);
}

void odd(ZeroEvenOdd* obj) {
    for (int _ = 1; _ <= obj->n; _ += 2) {
        sem_wait(&obj->sem_odd);
        printNumber(obj->turn);
        obj->turn += 1;
        sem_post(&obj->sem_zero);
    }
    sem_post(&obj->sem_zero);
    sem_post(&obj->sem_even);
    pthread_exit(NULL);
}

void zeroEvenOddFree(ZeroEvenOdd* obj) {
    free(obj);
}
```
