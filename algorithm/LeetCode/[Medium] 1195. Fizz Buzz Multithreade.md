1195. Fizz Buzz Multithreaded

You have the four functions:

* `printFizz` that prints the word `"fizz"` to the console,
* `printBuzz` that prints the word `"buzz"` to the console,
* `printFizzBuzz` that prints the word `"fizzbuzz"` to the console, and
* `printNumber` that prints a given integer to the console.

You are given an instance of the class `FizzBuzz` that has four functions: `fizz`, `buzz`, `fizzbuzz` and `number`. The same instance of FizzBuzz will be passed to four different threads:

* Thread A: calls `fizz()` that should output the word `"fizz"`.
* Thread B: calls `buzz()` that should output the word `"buzz"`.
* Thread C: calls `fizzbuzz()` that should output the word `"fizzbuzz"`.
* Thread D: calls `number()` that should only output the integers.

Modify the given class to output the series `[1, 2, "fizz", 4, "buzz", ...]` where the `i`th token (**1-indexed**) of the series is:

* "fizzbuzz" if i is divisible by `3` and `5`,
* "fizz" if i is divisible by `3` and not `5`,
* "buzz" if i is divisible by `5` and not `3`, or
* `i` if `i` is not divisible by `3` or `5`.

Implement the `FizzBuzz` class:

`FizzBuzz(int n)` Initializes the object with the number n that represents the length of the sequence that should be printed.
`void fizz(printFizz)` Calls `printFizz` to output `"fizz"`.
`void buzz(printBuzz)` Calls `printBuzz` to output `"buzz"`.
`void fizzbuzz(printFizzBuzz)` Calls `printFizzBuzz` to output `"fizzbuzz"`.
`void number(printNumber)` Calls `printnumber` to output the numbers.
 

**Example 1:**
```
Input: n = 15
Output: [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
Example 2:

Input: n = 5
Output: [1,2,"fizz",4,"buzz"]
```

**Constraints:**

* `1 <= n <= 50`

# Submissions
---
**Solution 1: (mutex + condition_variable)**

Intuition
The goal is to synchronize four threads — each responsible for printing fizz, buzz, fizzbuzz, or the number — so that their combined output matches the normal FizzBuzz sequence from 1 to n.
Since all threads share a common counter (curr), we must ensure only one thread acts for a given value and all others wait safely.

Approach
We use a mutex + condition variable to coordinate execution among threads.

Each thread continuously checks the current number curr.

Using a condition variable, a thread waits until its specific condition is true:

fizz: divisible by 3 but not 5

buzz: divisible by 5 but not 3

fizzbuzz: divisible by 15

number: not divisible by 3 or 5

Once the condition is met:

The thread prints the appropriate output.

Increments curr.

Calls notify_all() to wake the other waiting threads.

When curr > n, all threads exit gracefully.

This ensures that only the correct thread proceeds for each number, maintaining order and avoiding deadlocks or race conditions.

Complexity
Time complexity:
O(n) — each number from 1 to n is processed exactly once.

Space complexity:
O(1) — only a few synchronization variables are used.

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.36 MB, Beats 88.96%
```
```c++
class FizzBuzz {
private:
    int n;
    int curr = 1;
    mutex mtx;
    condition_variable cv;

public:
    FizzBuzz(int n) {
        this->n = n;
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        while (true) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock , [this] { return curr > n || (curr % 3 == 0 && curr % 5 != 0); });
            if(curr > n) break;
            printFizz();
            ++curr;
            lock.unlock();
            cv.notify_all();
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        while (true) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock , [this] { return curr > n || (curr % 3 != 0 && curr % 5 == 0); });
            if(curr > n) break;
            printBuzz();
            ++curr;
            lock.unlock();
            cv.notify_all();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        while (true) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock , [this] { return curr > n || curr % 15 == 0; });
            if(curr > n) break;
            printFizzBuzz();
            ++curr;
            lock.unlock();
            cv.notify_all();
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        while(true) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock , [this] { return curr > n || (curr % 3 != 0 && curr % 5 != 0); });
            if(curr > n) break;
            printNumber(curr);
            ++curr;
            lock.unlock();
            cv.notify_all();
        }
    }
};
```

**Solution 2: (Mutex)**
```
Runtime: 5 ms, Beats 33.93%
Memory: 9.18 MB, Beats 41.07%
```
```c++
typedef struct {
    int n;
    int turn;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*) malloc(sizeof(FizzBuzz));
    obj->n = n;
    pthread_mutex_init(&(obj->lock), NULL);
    pthread_cond_init(&(obj->cond), NULL);
    obj->turn = 1;
    return obj;
}

// Don't change the following declarations
void printNumber(int a);
void printFizz();
void printBuzz();
void printFizzBuzz();

// printFizz() outputs "fizz".
void fizz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && !(obj->turn % 3 == 0 && obj->turn % 5)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printFizz();

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }
    
}

// printBuzz() outputs "buzz".
void buzz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && !(obj->turn % 5 == 0 && obj->turn % 3)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printBuzz();

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }
    
}

// printFizzBuzz() outputs "fizzbuzz".
void fizzbuzz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && !(obj->turn % 3 == 0 && obj->turn % 5 == 0)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printFizzBuzz();

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }

}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.
void number(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && (obj->turn % 3 == 0 || obj->turn % 5 == 0)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printNumber(obj->turn);

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));        
    }
}

void fizzBuzzFree(FizzBuzz* obj) {
    free(obj);
}
```
**Solution 3: (Mutex)**
```
Runtime: 5 ms, Beats 33.93%
Memory: 9.18 MB, Beats 41.07%
```
```c
typedef struct {
    int n;
    int turn;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*) malloc(sizeof(FizzBuzz));
    obj->n = n;
    pthread_mutex_init(&(obj->lock), NULL);
    pthread_cond_init(&(obj->cond), NULL);
    obj->turn = 1;
    return obj;
}

// Don't change the following declarations
void printNumber(int a);
void printFizz();
void printBuzz();
void printFizzBuzz();

// printFizz() outputs "fizz".
void fizz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && !(obj->turn % 3 == 0 && obj->turn % 5)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printFizz();

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }
    
}

// printBuzz() outputs "buzz".
void buzz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && !(obj->turn % 5 == 0 && obj->turn % 3)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printBuzz();

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }
    
}

// printFizzBuzz() outputs "fizzbuzz".
void fizzbuzz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && !(obj->turn % 3 == 0 && obj->turn % 5 == 0)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printFizzBuzz();

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }

}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.
void number(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&(obj->lock));
        while (obj->turn <= obj->n && (obj->turn % 3 == 0 || obj->turn % 5 == 0)) {
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        if (obj->turn > obj->n) {
            pthread_mutex_unlock(&obj->lock);
            pthread_exit(NULL);
        }

        printNumber(obj->turn);

        obj->turn += 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));        
    }
}

void fizzBuzzFree(FizzBuzz* obj) {
    free(obj);
}
```

**Solution 4: (Semaphore)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.28 MB, Beats 16.07%
```
```c
typedef struct {
    int n;
    int turn;
    sem_t sem_fizz;
    sem_t sem_buzz;
    sem_t sem_fizzbuzz;
    sem_t sem_number;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*) malloc(sizeof(FizzBuzz));
    obj->n = n;
    obj->turn = 1;
    sem_init(&obj->sem_fizz, 0, 0);
    sem_init(&obj->sem_buzz, 0, 0);
    sem_init(&obj->sem_fizzbuzz, 0, 0);
    sem_init(&obj->sem_number, 0, 1);
    return obj;
}

// Don't change the following declarations
void printNumber(int a);
void printFizz();
void printBuzz();
void printFizzBuzz();

void do_post(FizzBuzz* obj) {
    if (obj->turn % 3 == 0 && obj->turn % 5) {
        sem_post(&obj->sem_fizz);
    } else if (obj->turn % 3 && obj->turn % 5 == 0) {
        sem_post(&obj->sem_buzz);
    } else if (obj->turn % 3 == 0 && obj->turn % 5 == 0) {
        sem_post(&obj->sem_fizzbuzz);
    } else {
        sem_post(&obj->sem_number);
    }
}

// printFizz() outputs "fizz".
void fizz(FizzBuzz* obj) {
    while (1) {
        sem_wait(&obj->sem_fizz);
        if (obj->turn > obj->n) {
            break;
        }

        printFizz();

        obj->turn += 1;

        do_post(obj);
    }
    sem_post(&obj->sem_buzz);
    sem_post(&obj->sem_fizzbuzz);
    sem_post(&obj->sem_number);
    pthread_exit(NULL);
}

// printBuzz() outputs "buzz".
void buzz(FizzBuzz* obj) {
    while (1) {
        sem_wait(&obj->sem_buzz);
        if (obj->turn > obj->n) {
            break;
        }

        printBuzz();

        obj->turn += 1;

        do_post(obj);
    }
    sem_post(&obj->sem_fizz);
    sem_post(&obj->sem_fizzbuzz);
    sem_post(&obj->sem_number);
    pthread_exit(NULL);
}

// printFizzBuzz() outputs "fizzbuzz".
void fizzbuzz(FizzBuzz* obj) {
    while (1) {
        sem_wait(&obj->sem_fizzbuzz);
        if (obj->turn > obj->n) {
            break;
        }

        printFizzBuzz();

        obj->turn += 1;

        do_post(obj);
    }
    sem_post(&obj->sem_fizz);
    sem_post(&obj->sem_buzz);
    sem_post(&obj->sem_number);
    pthread_exit(NULL);
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.
void number(FizzBuzz* obj) {
    while (1) {
        sem_wait(&obj->sem_number);
        if (obj->turn > obj->n) {
            break;
        }

        printNumber(obj->turn);

        obj->turn += 1;

        do_post(obj);
    }
    sem_post(&obj->sem_fizz);
    sem_post(&obj->sem_buzz);
    sem_post(&obj->sem_fizzbuzz);
    pthread_exit(NULL);
}

void fizzBuzzFree(FizzBuzz* obj) {
    free(obj);
}
```
