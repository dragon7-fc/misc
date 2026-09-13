Bounded Blocking Queue with Shutdown

Implement a fixed-capacity FIFO queue that supports multiple producer and consumer threads and a clean shutdown path.

C++ API:
```
class BlockingQueue {
public:
    explicit BlockingQueue(size_t capacity); // capacity >= 1
    bool push(int value);                    // waits while full; false after close
    bool pop(int& out);                      // waits while empty; drains after close
    void close();                            // idempotent; wakes all waiters
};
```

For C, implement the equivalent API with `pthread_mutex_t` and `pthread_cond_t` using the supplied struct starter.

Semantics:

* `push` must wait while the queue is full. It must not spin.
* `pop` must wait while the queue is empty and still open.
* `close()` is idempotent and wakes every blocked producer/consumer.
* After close, no new values may be pushed.
* Values already queued when close occurs must still be returned in FIFO order.
* Once the queue is both closed and empty, `pop` returns `false`.
* Condition-variable wakeups are notifications, not proof that the predicate is true; re-check the predicate while holding the mutex.

Example lifecycle:
```
capacity = 2
push(10), push(20)          -> queue full
third producer push(30)     -> blocks
consumer pop                -> 10, producer may proceed
close()
pop                         -> 20
pop                         -> 30
pop                         -> false
push(40)                    -> false
```

The goal is to implement the synchronization protocol, not merely wrap a queue container.

# Solution
---
**Solution 1: (Mutex)**
```c++
#include <condition_variable>
#include <cstddef>
#include <deque>
#include <mutex>

class BlockingQueue {
public:
    explicit BlockingQueue(size_t capacity) : capacity_(capacity) {}

    bool push(int value) {
        // Your code here
        std::unique_lock<std::mutex> lock(mu_);
        notFull_.wait(lock, [&] { return closed_ || queue_.size() < capacity_; });
        if (closed_) return false;
        queue_.push_back(value);
        lock.unlock();
        notEmpty_.notify_one();
        return true;
    }

    bool pop(int& out) {
        // Your code here
        std::unique_lock<std::mutex> lock(mu_);
        notEmpty_.wait(lock, [&] { return closed_ || !queue_.empty(); });
        if (queue_.empty()) return false; // closed and drained
        out = queue_.front();
        queue_.pop_front();
        lock.unlock();
        notFull_.notify_one();
        return true;
    }

    void close() {
        // Your code here
        {
            std::lock_guard<std::mutex> lock(mu_);
            closed_ = true;
        }
        notEmpty_.notify_all();
        notFull_.notify_all();
    }

private:
    const size_t capacity_;
    std::deque<int> queue_;
    bool closed_ = false;
    std::mutex mu_;
    std::condition_variable notEmpty_;
    std::condition_variable notFull_;
};
```
