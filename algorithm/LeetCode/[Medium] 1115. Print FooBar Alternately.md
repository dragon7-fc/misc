1115. Print FooBar Alternately

Suppose you are given the following code:

```
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
```

The same instance of `FooBar` will be passed to two different threads:

* thread `A` will call `foo()`, while
* thread `B` will call `bar()`.

Modify the given program to output `"foobar"` `n` times.

 

**Example 1:**
```
Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
```

**Example 2:**
```
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
```

**Constraints:**

* `1 <= n <= 1000`

# Submissions
---
**Solution 1: (mutex)**
```
Runtime: 9 ms, Beats 49.97%
Memory: 11.28 MB, Beats 77.23%
```
```c++
class FooBar {
private:
    int n;
    mutex m1, m2;
public:
    FooBar(int n) {
        this->n = n;
        m2.lock();
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            m1.lock();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            m2.unlock();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            m2.lock();
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            m1.unlock();
        }
    }
};
```

**Solution 2: (semaphore)**
```
Runtime: 3 ms, Beats 90.24%
Memory: 11.14 MB, Beats 92.82%
```
```c++
class FooBar {
private:
    int n;
    binary_semaphore foos{1}, bars{0};
public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            foos.acquire();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            bars.release();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            bars.acquire();
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            foos.release();
        }
    }
};
```

**Solution 3: (Mutex)**
```
Runtime: 9 ms, Beats 55.71%
Memory: 10.81 MB, Beats 6.43%
```
```c
typedef struct {
    int n;
    int turn;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} FooBar;

// Function declarations. Do not change or remove this line
void printFoo();
void printBar();

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    pthread_mutex_init(&(obj->lock), NULL);
    pthread_cond_init(&(obj->cond), NULL);
    obj->turn = 0;

    return obj;
}

void foo(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&(obj->lock));
        // while not my turn
        while(obj->turn != 0)
        {
            // wait and unlock
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }

        // printFoo() outputs "foo". Do not change or remove this line.
        printFoo();

        obj->turn = 1;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }
}

void bar(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&(obj->lock));
        // while not my turn
        while(obj->turn != 1)
        {
            // wait and unlock
            pthread_cond_wait(&(obj->cond), &(obj->lock)); 
        }
        // printBar() outputs "bar". Do not change or remove this line.
        printBar();

        obj->turn = 0;
        pthread_mutex_unlock(&(obj->lock));
        pthread_cond_broadcast(&(obj->cond));
    }
}

void fooBarFree(FooBar* obj) {
    free(obj);
}
```

**Solution 4: (Semaphore)**
```
Runtime: 11 ms, Beats 42.14%
Memory: 10.64 MB, Beats 73.57%
```
```c
typedef struct {
    int n;
    sem_t sem_foo;
    sem_t sem_bar;

} FooBar;

// Function declarations. Do not change or remove this line
void printFoo();
void printBar();

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    
    sem_init(&obj->sem_foo, 0, 1);
    sem_init(&obj->sem_bar, 0, 0);

    return obj;
}

void foo(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->sem_foo);

        // printFoo() outputs "foo". Do not change or remove this line.
        printFoo();

        sem_post(&obj->sem_bar);
    }
}

void bar(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->sem_bar);

        // printBar() outputs "bar". Do not change or remove this line.
        printBar();

        sem_post(&obj->sem_foo);
    }
}

void fooBarFree(FooBar* obj) {
    free(obj);
}
```

**Solution 4: (Mutex)**
```
Runtime: 4 ms, Beats 83.93%
Memory: 11.40 MB, Beats 44.03%
```
```c++
class FooBar {
private:
    int n;
    int turn;
    mutex mtx;
    condition_variable cv;

public:
    FooBar(int n) {
        this->n = n;
        turn = 0;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&]{ return turn == 0; });
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            turn = 1;
            cv.notify_one();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&]{ return turn == 1; });
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            turn = 0;
            cv.notify_one();
        }
    }
};
```
