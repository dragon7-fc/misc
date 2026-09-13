Fixed-Priority RTOS Scheduler with Round-Robin Peers

Implement a small fixed-priority RTOS scheduler model for at most 16 tasks. This is a stateful scheduling problem, not a one-line "return max priority" exercise.

```
class FixedPriorityScheduler {
public:
    static constexpr size_t kMaxTasks = 16;
    static constexpr unsigned kMaxPriority = 7;

    bool addTask(int id, unsigned priority); // starts BLOCKED
    bool makeReady(int id);
    bool block(int id);
    int pickNext();                          // -1 if none READY
};
```

Rules:

* Task IDs are unique; priorities are 0..7, larger number means higher priority.
* A registered task starts BLOCKED.
* `pickNext()` chooses the highest-priority READY task.
* READY tasks with equal priority must run round-robin. Each successful `pickNext()` rotates the selected task behind its equal-priority peers.
* A higher-priority READY task always wins over lower-priority tasks, even if those lower tasks have waited longer.
* Calling `makeReady()` for an already READY task is a no-op; it must not duplicate the task or reset its round-robin position.
* `block()` removes the task from the ready set until it is made ready again.
* Use fixed task storage; no dynamic allocation is needed.

Example:
```
add A(p3), B(p3), C(p5)
makeReady(A), makeReady(B)
pickNext -> A
pickNext -> B
pickNext -> A
makeReady(C)
pickNext -> C
pickNext -> C
block(C)
pickNext -> B
```

You may use a fixed task table plus monotonically increasing ready-order/ticket values, or per-priority ready queues. Preserve the required scheduling semantics rather than matching one representation.

# Submissions
---
**Solution 1: (Greedy, smallest ticket as candidate)**
                           A.ticket B.ticket C.ticket
add A(p3), B(p3), C(p5)           1        2        3
makeReady(A),                     4
makeReady(B)                               5
pickNext -> A                     6
pickNext -> B                              7
pickNext -> A                     8
makeReady(C)                                        9
pickNext -> C                                      10
pickNext -> C                                      11
block(C)
pickNext -> B                             12

```c++
#include <array>
#include <cstddef>
#include <cstdint>

class FixedPriorityScheduler {
public:
    static constexpr size_t kMaxTasks = 16;
    static constexpr unsigned kMaxPriority = 7;

    bool addTask(int id, unsigned priority) {
        // Your code here
        if (priority > kMaxPriority || find(id) != nullptr) return false;
        for (auto& t : tasks_) {
            if (!t.used) {
                t = Task{true, id, priority, false, 0};
                return true;
            }
        }
        return false;
    }
    bool makeReady(int id) {
        // Your code here
        Task* t = find(id);
        if (!t) return false;
        if (!t->ready) {
            t->ready = true;
            t->ticket = nextTicket_++;
        }
        return true;
    }
    bool block(int id) {
        // Your code here
        Task* t = find(id);
        if (!t) return false;
        t->ready = false;
        return true;
    }
    int pickNext() {
        // Your code here
        Task* best = nullptr;
        for (auto& t : tasks_) {
            if (!t.used || !t.ready) continue;
            if (!best || t.priority > best->priority ||
                (t.priority == best->priority && t.ticket < best->ticket)) {
                best = &t;
            }
        }
        if (!best) return -1;
        best->ticket = nextTicket_++;
        return best->id;
    }

private:
    struct Task {
        bool used = false;
        int id = 0;
        unsigned priority = 0;
        bool ready = false;
        uint64_t ticket = 0;
    };
    std::array<Task, kMaxTasks> tasks_{};
    uint64_t nextTicket_ = 1;
    
    Task* find(int id) {
        for (auto& t : tasks_) if (t.used && t.id == id) return &t;
        return nullptr;
    }
};
```
