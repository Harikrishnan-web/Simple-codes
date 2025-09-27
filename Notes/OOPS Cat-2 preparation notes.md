# Unit III: Generics & Multithreading - Complete Exam Notes

## Topics Covered:
1. **Generics**
   - Motivation for generic programming
   - Generic classes and methods
   - Bounded types
   - Generic code and virtual machine
   - Inheritance and generics
   - Reflection and generics
   - Restrictions on generics

2. **Multithreaded Programming**
   - Thread concept and lifecycle
   - Creating threads (Runnable interface & Thread class)
   - Thread states and properties
   - Thread priorities
   - Thread synchronization (synchronized methods, blocks, static synchronization)
   - Inter-thread communication (wait, notify, notifyAll)
   - Daemon threads
   - Thread groups
   - Executors and synchronizers

---

# GENERICS

## What are Generics?
Generic programming enables creating classes, interfaces, and methods that automatically work with all types of data (Integer, String, Float, etc.). It expands the ability to reuse code safely and easily.

## Advantages of Java Generics
1. **Type-safety**: Can hold only a single type of objects
2. **No Type casting required**: No need to typecast objects
3. **Compile-Time Checking**: Problems caught at compile time, not runtime

## Generic Classes

### Basic Generic Class Example:
```java
class TwoGen<T, V> {
    T ob1;
    V ob2;
    
    TwoGen(T o1, V o2) {
        ob1 = o1; 
        ob2 = o2;
    }
    
    void showTypes() {
        System.out.println("Type of T is " + ob1.getClass().getName()); 
        System.out.println("Type of V is " + ob2.getClass().getName());
    }
    
    T getob1() { 
        return ob1; 
    }
    
    V getob2() { 
        return ob2; 
    }
}

public class MainClass {
    public static void main(String args[]) {
        TwoGen<Integer, String> tgObj = new TwoGen<Integer, String>(88, "Generics");
        
        tgObj.showTypes();
        
        int v = tgObj.getob1(); 
        System.out.println("value: " + v);
        
        String str = tgObj.getob2(); 
        System.out.println("value: " + str);
    }
}
```

**Output:**
```
Type of T is java.lang.Integer
Type of V is java.lang.String
value: 88
value: Generics
```

**Explanation**: 
- `T` and `V` are type parameters that can be replaced with any reference type
- When creating object, we specify actual types: `TwoGen<Integer, String>`
- Type safety ensures we can't assign wrong types

## Bounded Types
Limits the types that can be passed to a type parameter using `extends` keyword.

### Syntax:
```java
<T extends superclass>
```

### Bounded Type Example:
```java
class Stats<T extends Number> {
    T[] nums;
    
    Stats(T[] o) {
        nums = o;
    }
    
    double average() {
        double sum = 0.0;
        for(int i = 0; i < nums.length; i++) {
            sum += nums[i].doubleValue();
        }
        return sum / nums.length;
    }
}

public class MainClass {
    public static void main(String args[]) {
        Integer inums[] = { 1, 2, 3, 4, 5 };
        Stats<Integer> iob = new Stats<Integer>(inums); 
        double v = iob.average();
        System.out.println("iob average is " + v);
        
        Double dnums[] = { 1.1, 2.2, 3.3, 4.4, 5.5 };
        Stats<Double> dob = new Stats<Double>(dnums);
        double w = dob.average(); 
        System.out.println("dob average is " + w);
    }
}
```

**Output:**
```
iob average is 3.0
dob average is 3.3
```

**Explanation**: 
- `T extends Number` restricts T to Number and its subclasses only
- This allows using Number methods like `doubleValue()`
- Provides type safety while allowing numeric operations

## Restrictions on Generics
1. Cannot instantiate generic types with primitive types
2. Cannot create instances of type parameters
3. Cannot declare static fields whose types are type parameters
4. Cannot use casts or instanceof with parameterized types
5. Cannot create arrays of parameterized types
6. Cannot create, catch, or throw objects of parameterized types
7. Cannot overload methods where formal parameter types erase to same raw type

---

# MULTITHREADED PROGRAMMING

## Basic Concepts

### Thread
A single sequential flow of control within a program. Also called execution context or lightweight process.

### Multithreading
A programming concept where a program is divided into two or more subprograms that can be executed simultaneously.

### Multitasking Types:
1. **Process-based multitasking**: Different programs running simultaneously
2. **Thread-based multitasking**: Different parts of same program running simultaneously

## Thread Lifecycle

### Thread States:
1. **Newborn State**: Thread object created but not started
2. **Runnable State**: Ready for execution, waiting for processor
3. **Running State**: Currently executing
4. **Blocked State**: Prevented from running (waiting, sleeping, suspended)
5. **Dead State**: Thread completed execution

## Main Thread

### Main Thread Example:
```java
class MainThread {
    public static void main(String[] args) {
        Thread t1 = Thread.currentThread();
        t1.setName("MainThread");
        System.out.println("Name of thread is " + t1);
    }
}
```

**Output:**
```
Name of thread is Thread[MainThread,5,main]
```

**Explanation**: Every Java program starts with main thread. It's automatically created and must be the last thread to finish execution.

## Creating Threads

### Method 1: Implementing Runnable Interface

```java
public class ThreadSample implements Runnable {
    public void run() {
        try {
            for (int i = 5; i > 0; i--) {
                System.out.println("Child Thread " + i);
                Thread.sleep(1000);
            }
        }
        catch (InterruptedException e) {
            System.out.println("Child interrupted");
        }
        System.out.println("Exiting Child Thread");
    }
}

public class MainThread {
    public static void main(String[] arg) {
        ThreadSample d = new ThreadSample();
        Thread s = new Thread(d);
        s.start();
        
        try {
            for (int i = 5; i > 0; i--) {
                System.out.println("Main Thread " + i);
                Thread.sleep(5000);
            }
        }
        catch (InterruptedException e) {
            System.out.println("Main interrupted");
        }
        System.out.println("Exiting Main Thread");
    }
}
```

**Output:**
```
Child Thread 5
Main Thread 5
Child Thread 4
Child Thread 3
Child Thread 2
Child Thread 1
Exiting Child Thread
Main Thread 4
Main Thread 3
Main Thread 2
Main Thread 1
Exiting Main Thread
```

### Method 2: Extending Thread Class

```java
public class ThreadSample extends Thread {
    public void run() {
        try {
            for (int i = 5; i > 0; i--) {
                System.out.println("Child Thread " + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Child interrupted");
        }
        System.out.println("Exiting Child Thread");
    }
}

public class MainThread {
    public static void main(String[] arg) {
        ThreadSample d = new ThreadSample(); 
        d.start();
        
        try {
            for (int i = 5; i > 0; i--) {
                System.out.println("Main Thread " + i);
                Thread.sleep(5000);
            }
        } catch (InterruptedException e) {
            System.out.println("Main interrupted");
        }
        System.out.println("Exiting Main Thread");
    }
}
```

**Explanation**: 
- **Runnable Interface**: More flexible, allows class to extend another class
- **Thread Class**: Direct inheritance, simpler but limits inheritance options

## Thread Priority

### Priority Constants:
- `Thread.MIN_PRIORITY` = 1
- `Thread.NORM_PRIORITY` = 5 (default)
- `Thread.MAX_PRIORITY` = 10

### Thread Priority Example:
```java
public class MyThread1 extends Thread {
    MyThread1(String s) {
        super(s);
        start();
    }
    
    public void run() {
        for(int i = 0; i < 5; i++) {
            Thread cur = Thread.currentThread();
            cur.setPriority(Thread.MAX_PRIORITY);
            int p = cur.getPriority();
            System.out.println("Thread Name: " + Thread.currentThread().getName());
            System.out.println("Thread Priority: " + p);
        }
    }
}

class MyThread2 extends Thread {
    MyThread2(String s) {
        super(s);
        start();
    }
    
    public void run() {
        for(int i = 0; i < 5; i++) {
            Thread cur = Thread.currentThread();
            cur.setPriority(Thread.MIN_PRIORITY);
            System.out.println("Thread Name: " + Thread.currentThread().getName());
            System.out.println("Thread Priority: " + cur.getPriority());
        }
    }
}

public class ThreadPriority {
    public static void main(String[] args) {
        MyThread1 m1 = new MyThread1("MyThread1");
        MyThread2 m2 = new MyThread2("MyThread2");
    }
}
```

## Thread Synchronization

### Why Synchronization?
- Prevents thread interference
- Prevents consistency problems
- Controls access to shared resources

### Types of Synchronization:
1. **Mutual Exclusive**
   - Synchronized method
   - Synchronized block
   - Static synchronization

2. **Inter-thread Communication**
   - wait(), notify(), notifyAll()

### Synchronized Method Example:
```java
class Share {
    public synchronized void doWork(String str) {
        for (int i = 0; i < 5; i++) {
            System.out.println("Started: " + str);
            try {
                Thread.sleep(1000);
            }
            catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}

class MyThread extends Thread {
    Share s;
    
    MyThread(Share s, String str) {
        super(str);
        this.s = s;
        start();
    }
    
    public void run() {
        s.doWork(Thread.currentThread().getName());
    }
}

public class SynThread {
    public static void main(String args[]) {
        Share s = new Share();
        MyThread m1 = new MyThread(s, "Thread1");
        MyThread m2 = new MyThread(s, "Thread2");
        MyThread m3 = new MyThread(s, "Thread3");
    }
}
```

**Output:**
```
Started: Thread1
Started: Thread1
Started: Thread1
Started: Thread1
Started: Thread1
Started: Thread2
Started: Thread2
Started: Thread2
Started: Thread2
Started: Thread2
Started: Thread3
Started: Thread3
Started: Thread3
Started: Thread3
Started: Thread3
```

### Synchronized Block Example:
```java
class Table {
    void printTable(int n) {
        synchronized(this) { // synchronized block
            for(int i = 1; i <= 5; i++) {
                System.out.println(n * i);
                try {
                    Thread.sleep(400);
                } catch(Exception e) {
                    System.out.println(e);
                }
            }
        }
    }
}

class MyThread1 extends Thread {
    Table t;
    MyThread1(Table t) { 
        this.t = t; 
    }
    public void run() { 
        t.printTable(5); 
    }
}

class MyThread2 extends Thread {
    Table t;
    MyThread2(Table t) { 
        this.t = t; 
    }
    public void run() { 
        t.printTable(100); 
    }
}

public class TestSynchronizedBlock1 {
    public static void main(String args[]) {
        Table obj = new Table();
        MyThread1 t1 = new MyThread1(obj);
        MyThread2 t2 = new MyThread2(obj);
        t1.start();
        t2.start();
    }
}
```

### Static Synchronization Example:
```java
class Table {
    synchronized static void printTable(int n) {
        for(int i = 1; i <= 10; i++) {
            System.out.println(n * i);
            try {
                Thread.sleep(400);
            } catch(Exception e) {}
        }
    }
}

class MyThread1 extends Thread {
    public void run() { 
        Table.printTable(1); 
    }
}

class MyThread2 extends Thread {
    public void run() { 
        Table.printTable(10); 
    }
}

public class TestSynchronization4 {
    public static void main(String t[]) {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();
        t1.start();
        t2.start();
    }
}
```

**Explanation**:
- **Synchronized Method**: Entire method is synchronized
- **Synchronized Block**: Only specific code block is synchronized
- **Static Synchronization**: Lock is on class, not object instance

## Inter-thread Communication

### Methods:
- `wait()`: Releases lock and waits for notification
- `notify()`: Wakes up one waiting thread
- `notifyAll()`: Wakes up all waiting threads

### wait() vs sleep():
| wait() | sleep() |
|--------|---------|
| Releases the lock | Doesn't release lock |
| Method of Object class | Method of Thread class |
| Non-static method | Static method |
| Must be notified | Completes after specified time |

### Inter-thread Communication Example:
```java
class Customer {
    int amount = 10000;
    
    synchronized void withdraw(int amount) {
        System.out.println("going to withdraw...");
        if(this.amount < amount) {
            System.out.println("Less balance; waiting for deposit...");
            try {
                wait();
            } catch(Exception e) {}
        }
        this.amount -= amount;
        System.out.println("withdraw completed...");
    }
    
    synchronized void deposit(int amount) {
        System.out.println("going to deposit...");
        this.amount += amount;
        System.out.println("deposit completed...");
        notify();
    }
}

class Test {
    public static void main(String args[]) {
        final Customer c = new Customer();
        
        new Thread() {
            public void run() {
                c.withdraw(15000);
            }
        }.start();
        
        new Thread() {
            public void run() {
                c.deposit(10000);
            }
        }.start();
    }
}
```

**Output:**
```
going to withdraw...
Less balance; waiting for deposit...
going to deposit...
deposit completed...
withdraw completed...
```

## Daemon Thread

Daemon threads are service provider threads that provide services to user threads. They automatically terminate when all user threads die.

### Daemon Thread Example:
```java
public class TestDaemonThread1 extends Thread {
    public void run() {
        if(Thread.currentThread().isDaemon()) {
            System.out.println("daemon thread work");
        }
        else {
            System.out.println("user thread work");
        }
    }
    
    public static void main(String[] args) {
        TestDaemonThread1 t1 = new TestDaemonThread1();
        TestDaemonThread1 t2 = new TestDaemonThread1();
        TestDaemonThread1 t3 = new TestDaemonThread1();
        
        t1.setDaemon(true); // now t1 is daemon thread
        
        t1.start();
        t2.start();
        t3.start();
    }
}
```

## Thread Group

Provides a way to group multiple threads in a single object for collective operations.

### Thread Group Example:
```java
public class ThreadGroupDemo implements Runnable {
    public void run() {
        System.out.println(Thread.currentThread().getName());
    }
    
    public static void main(String[] args) {
        ThreadGroupDemo runnable = new ThreadGroupDemo();
        ThreadGroup tg1 = new ThreadGroup("Parent ThreadGroup");
        
        Thread t1 = new Thread(tg1, runnable, "one");
        t1.start();
        Thread t2 = new Thread(tg1, runnable, "two");
        t2.start();
        Thread t3 = new Thread(tg1, runnable, "three");
        t3.start();
        
        System.out.println("Thread Group Name: " + tg1.getName());
        tg1.list();
    }
}
```

**Output:**
```
one
two
three
Thread Group Name: Parent ThreadGroup
java.lang.ThreadGroup[name=Parent ThreadGroup,maxpri=10]
    Thread[one,5,Parent ThreadGroup]
    Thread[two,5,Parent ThreadGroup]
    Thread[three,5,Parent ThreadGroup]
```

## Important Thread Methods

| Method | Description |
|--------|-------------|
| start() | Initiates thread execution |
| currentThread() | Returns reference to currently executing thread |
| run() | Contains the code to be executed by thread |
| isAlive() | Checks if thread is alive or dead |
| sleep() | Suspends thread temporarily |
| yield() | Sends current thread to standby mode |
| interrupt() | Interrupts the currently executing thread |
| join() | Waits for thread to complete |
| setPriority() | Sets thread priority |
| getPriority() | Gets thread priority |

---

# 15-MARK EXAM QUESTIONS & ANSWER HINTS

## 1. Explain Generics in Java with advantages and bounded types. Provide complete examples. (15 marks)

**Answer Hints:**
- Define generics and motivation (3 marks)
- List and explain 3 advantages with examples (4 marks)
- Explain bounded types with syntax and complete example (5 marks)
- Discuss restrictions on generics (3 marks)

## 2. Describe thread lifecycle and methods of creating threads in Java. Compare both methods with complete programs. (15 marks)

**Answer Hints:**
- Draw and explain thread lifecycle with 5 states (5 marks)
- Explain Runnable interface method with complete code (5 marks)
- Explain Thread class extension method with complete code (4 marks)
- Compare both methods with advantages/disadvantages (1 mark)

## 3. What is thread synchronization? Explain different types with complete examples and outputs. (15 marks)

**Answer Hints:**
- Define synchronization and need (2 marks)
- Synchronized method with complete example and output (4 marks)
- Synchronized block with complete example and output (4 marks)
- Static synchronization with complete example and output (4 marks)
- Compare all three methods (1 mark)

## 4. Explain inter-thread communication in Java. Differentiate wait() and sleep() methods with complete example. (15 marks)

**Answer Hints:**
- Define inter-thread communication (2 marks)
- Explain wait(), notify(), notifyAll() methods (4 marks)
- Complete producer-consumer or bank example with output (6 marks)
- Tabular comparison of wait() vs sleep() (3 marks)

## 5. Write a complete Java program demonstrating multithreading with thread priorities, synchronization, and inter-thread communication. (15 marks)

**Answer Hints:**
- Design a real-world scenario (bank, producer-consumer, etc.) (2 marks)
- Implement multiple threads with different priorities (4 marks)
- Use appropriate synchronization mechanism (4 marks)
- Implement inter-thread communication (4 marks)
- Provide complete output and explanation (1 mark)

## 6. Explain generic classes and methods with inheritance. Discuss generic code and virtual machine relationship. (15 marks)

**Answer Hints:**
- Generic class definition with complete example (4 marks)
- Generic methods with examples (3 marks)
- Inheritance with generics and wildcards (4 marks)
- Type erasure and virtual machine relationship (3 marks)
- Reflection and generics (1 mark)

## 7. Describe daemon threads and thread groups in Java. Provide complete implementations with examples. (15 marks)

**Answer Hints:**
- Define daemon threads with characteristics (3 marks)
- Complete daemon thread example with output (4 marks)
- Explain thread groups with constructors and methods (4 marks)
- Complete thread group example with output (3 marks)
- Practical applications and benefits (1 mark)

## 8. Create a comprehensive multithreaded application demonstrating all thread states, priorities, and synchronization mechanisms. (15 marks)

**Answer Hints:**
- Design application architecture (2 marks)
- Implement threads showing all 5 states (5 marks)
- Use different priority levels (2 marks)
- Implement all three synchronization types (4 marks)
- Complete working code with detailed output (2 marks)

## Quick Revision Tips:
- Remember all 5 thread states
- Know difference between Runnable and Thread class
- Understand synchronized method vs block vs static
- Master wait(), notify(), notifyAll() usage
- Practice generic class and bounded type syntax
- Understand type erasure concept
- Know thread priority constants (1, 5, 10)
- Remember daemon thread characteristics

**Good luck with your exam! 🎯**