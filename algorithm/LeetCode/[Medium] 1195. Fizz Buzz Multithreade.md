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
