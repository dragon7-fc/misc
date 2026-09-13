Counting Semaphore with Multiple-Permit Acquire

Implement a bounded counting semaphore that supports acquiring or releasing more than one permit at a time.

C++ API:
```
class CountingSemaphore {
public:
    CountingSemaphore(size_t initial, size_t maximum); // initial <= maximum
    bool acquire(size_t permits = 1);                  // blocks until possible
    bool tryAcquire(size_t permits = 1);               // never blocks
    bool release(size_t permits = 1);                  // false on overflow
    size_t available() const;
};
```

For C, implement equivalent functions using the supplied pthread-based starter.

Contract:

* `acquire(0)` and `tryAcquire(0)` succeed immediately.
* A request larger than `maximum` can never be satisfied and returns false.
* `acquire(n)` waits until at least `n` permits are available, then subtracts exactly `n` atomically with respect to other operations.
* `tryAcquire(n)` returns `false` immediately when insufficient permits exist.
* `release(n)` fails without changing state if it would exceed the configured maximum.
* The count must never underflow or exceed maximum.
* Waiting must use a blocking primitive, not busy polling.

Why multiple permits? It prevents this from collapsing into a three-line textbook semaphore and forces you to think about waiter predicates and wakeup policy. If one waiter needs 3 permits while another needs 1, waking an arbitrary single waiter may not be sufficient to make progress.

# Submissions
---
**Solution 1: (Mutex)**
```c
#include <stdbool.h>
#include <stddef.h>
#include <pthread.h>

typedef struct {
    size_t count;
    size_t maximum;
    pthread_mutex_t mu;
    pthread_cond_t cv;
} CountingSemaphore;

bool semaphore_init(CountingSemaphore *s, size_t initial, size_t maximum) {
    // Your code here
    s->count = initial;
    s->maximum = maximum;
    pthread_mutex_init(&s->mu, NULL);
    pthread_cond_init(&s->cv, NULL);
    return true;
}

bool semaphore_acquire(CountingSemaphore *s, size_t permits) {
    // Your code here
    if (permits > s->maximum) {
        return false;
    }
    if (permits == 0) {
        return true;
    }
    pthread_mutex_lock(&s->mu);
    while (s->count < permits) {
        pthread_cond_wait(&s->cv, &s->mu);
    }
    s->count -= permits;
    pthread_mutex_unlock(&s->mu);
    return true;
}

bool semaphore_try_acquire(CountingSemaphore *s, size_t permits) {
    // Your code here
    if (permits > s->maximum) {
        return false;
    }
    pthread_mutex_lock(&s->mu);
    if (s->count < permits) {
        pthread_mutex_unlock(&s->mu);
        return false;
    }
    s->count -= permits;
    pthread_mutex_unlock(&s->mu);
    return true;
}

bool semaphore_release(CountingSemaphore *s, size_t permits) {
    // Your code here
    pthread_mutex_lock(&s->mu);
    if (permits > s->maximum - s->count) {
        pthread_mutex_unlock(&s->mu);
        return false;
    }
    s->count += permits;
    pthread_mutex_unlock(&s->mu);
    pthread_cond_broadcast(&s->cv);
    return true;
}

size_t semaphore_available(CountingSemaphore *s) {
    // Your code here
    pthread_mutex_lock(&s->mu);
    size_t rst = s->count;
    pthread_mutex_unlock(&s->mu);
    return rst;
}
```

**Solution 2: (Mutex)**
```c++
#include <condition_variable>
#include <cstddef>
#include <mutex>

class CountingSemaphore {
public:
    CountingSemaphore(size_t initial, size_t maximum)
        : count_(initial), maximum_(maximum) {}

    bool acquire(size_t permits = 1) {
        // Your code here
        if (permits > maximum_) {
            return false;
        }
        if (permits == 0) {
            return true;
        }
        unique_lock<mutex> lock(mu_);
        cv_.wait(lock, [&] { 
            return count_ >= permits; 
        });
        count_ -= permits;
        return true;
    }

    bool tryAcquire(size_t permits = 1) {
        // Your code here
        if (permits > maximum_) return false;
        lock_guard<mutex> lock(mu_);
        if (count_ < permits) {
            return false;
        }
        count_ -= permits;
        return true;
    }

    bool release(size_t permits = 1) {
        // Your code here
        unique_lock<mutex> lock(mu_);
        if (permits > maximum_ - count_) {
            return false;
        }
        count_ += permits;
        lock.unlock();
        cv_.notify_all();
        return true;
    }

    size_t available() const {
        // Your code here
        std::lock_guard<std::mutex> lock(mu_);
        return count_;
    }

private:
    mutable std::mutex mu_;
    std::condition_variable cv_;
    size_t count_;
    const size_t maximum_;
};
```

