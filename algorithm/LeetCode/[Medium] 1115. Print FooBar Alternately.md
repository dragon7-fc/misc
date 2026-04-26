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
