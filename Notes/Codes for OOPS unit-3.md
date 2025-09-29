# Object Oriented Programming - Unit III Code Examples
## Generics & Multi-Threading - All Code Implementations

---

## **GENERICS - CODE EXAMPLES**

### **1. Generic Class with Two Type Parameters**

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

**Explanation**:
- Creates a generic class that can hold two different types of objects (T and V)
- Constructor initializes both objects
- `showTypes()` displays the actual class types at runtime
- Getter methods return the stored objects
- In main, creates instance with Integer and String types

**Output**:
```
Type of T is java.lang.Integer
Type of V is java.lang.String
value: 88
value: Generics
```

---

### **2. Bounded Type Generic Class**

```java
class Stats<T extends Number> {
    T[] nums;
    
    Stats(T[] o) {
        nums = o;
    }
    
    double average() {
        double sum = 0.0;
        for(int i=0; i < nums.length; i++) 
            sum += nums[i].doubleValue();
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

**Explanation**:
- Generic class bounded by Number class (T extends Number)
- Can only accept Number subclasses (Integer, Double, Float, etc.)
- `average()` method uses `doubleValue()` available in Number class
- Calculates and returns average of array elements
- Works with both Integer and Double arrays

**Output**:
```
iob average is 3.0
dob average is 3.3
```

---

## **MULTITHREADING - CODE EXAMPLES**

### **3. Main Thread Example**

```java
class MainThread {
    public static void main(String[] args) {
        Thread t1 = Thread.currentThread();
        t1.setName("MainThread");
        System.out.println("Name of thread is " + t1); 
    }
}
```

**Explanation**:
- Gets reference to currently executing thread using `currentThread()`
- Changes thread name to "MainThread" using `setName()`
- Prints thread information including name, priority (5), and group (main)

**Output**:
```
Name of thread is Thread[MainThread,5,main]
```

---

### **4. Creating Thread by Implementing Runnable Interface**

```java
public class ThreadSample implements Runnable {
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
        Thread s = new Thread(d);
        s.start();
        
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
- `ThreadSample` implements Runnable interface
- Overrides `run()` method with thread execution logic
- Child thread prints countdown from 5 to 1 with 1-second delay
- Main thread creates Thread object, passing Runnable instance
- Calls `start()` to begin child thread execution
- Main thread also runs its own countdown with 5-second delay
- Both threads run concurrently

**Output** (approximate - order may vary):
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

---

### **5. Creating Thread by Extending Thread Class**

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
- `ThreadSample` extends Thread class
- Overrides `run()` method directly
- Creates ThreadSample object and calls `start()` directly
- No need to create separate Thread object
- Both threads run concurrently similar to previous example

**Output** (similar to previous example - order may vary)

---

### **6. Thread Priority Example**

```java
public class MyThread1 extends Thread {
    MyThread1(String s) {
        super(s);
        start(); 
    }
    
    public void run() { 
        for(int i=0; i<5; i++) {
            Thread cur = Thread.currentThread();
            cur.setPriority(Thread.MAX_PRIORITY);
            int p = cur.getPriority();
            System.out.println("Thread Name: " + Thread.currentThread().getName());
            System.out.println("Thread Priority: " + cur); 
        }
    }
}

class MyThread2 extends Thread {
    MyThread2(String s) {
        super(s);
        start(); 
    }
    
    public void run() {
        for(int i=0; i<5; i++) {
            Thread cur = Thread.currentThread();
            cur.setPriority(Thread.MIN_PRIORITY);
            System.out.println(cur.getPriority());
            int p = cur.getPriority(); 
            System.out.println("Thread Name: " + Thread.currentThread().getName());
            System.out.println("Thread Priority: " + cur);
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

**Explanation**:
- Creates two thread classes with different priorities
- `MyThread1` sets priority to MAX_PRIORITY (10)
- `MyThread2` sets priority to MIN_PRIORITY (1)
- Constructor automatically starts thread execution
- Both threads print their name and priority 5 times
- Higher priority thread may execute more frequently (depends on JVM)

**Output** (order may vary based on thread scheduling):
```
Thread Name: MyThread1
Thread Priority: Thread[MyThread1,10,main]
1
Thread Name: MyThread2
Thread Priority: Thread[MyThread2,1,main]
Thread Name: MyThread1
Thread Priority: Thread[MyThread1,10,main]
...
```

---

### **7. Synchronized Method Example**

```java
package Thread;

public class SynThread {
    public static void main(String args[]) {
        share s = new share();
        MyThread m1 = new MyThread(s, "Thread1");
        MyThread m2 = new MyThread(s, "Thread2");
        MyThread m3 = new MyThread(s, "Thread3"); 
    }
}

class MyThread extends Thread {
    share s;
    
    MyThread(share s, String str) {
        super(str);
        this.s = s;
        start();
    }
    
    public void run() {
        s.doword(Thread.currentThread().getName()); 
    }
}

class share {
    public synchronized void doword(String str) {
        for (int i = 0; i < 5; i++) {
            System.out.println("Started: " + str);
            try {
                Thread.sleep(1000); 
            } catch (Exception e) {
            }
        }
    }
}
```

**Explanation**:
- Three threads share the same `share` object
- `doword()` method is synchronized - only one thread can execute it at a time
- Each thread attempts to print 5 messages
- Lock ensures threads execute `doword()` sequentially, not concurrently
- One thread completes all 5 iterations before next thread starts

**Output**:
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

---

### **8. Synchronized Block Example**

```java
class Table {
    void printTable(int n) {
        synchronized(this) { //synchronized block
            for(int i=1; i<=5; i++) {
                System.out.println(n*i);
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
        this.t=t; 
    }
    public void run() { 
        t.printTable(5);
    }
}

class MyThread2 extends Thread {
    Table t;
    MyThread2(Table t) { 
        this.t=t; 
    }
    public void run() { 
        t.printTable(100); 
    }
}

public class TestSynchronizedBlock1 {
    public static void main(String args[]) {
        Table obj = new Table(); //only one object
        MyThread1 t1 = new MyThread1(obj);
        MyThread2 t2 = new MyThread2(obj);
        t1.start();
        t2.start(); 
    }
}
```

**Explanation**:
- Only the for-loop inside `printTable()` is synchronized, not entire method
- Two threads share same Table object
- Thread1 prints multiplication table of 5
- Thread2 prints multiplication table of 100
- Synchronized block ensures tables don't mix during printing
- More efficient than synchronizing entire method if other code exists outside block

**Output**:
```
5
10
15
20
25
100
200
300
400
500
```

---

### **9. Static Synchronization Example**

```java
class Table {
    synchronized static void printTable(int n) {
        for(int i=1; i<=10; i++) {
            System.out.println(n*i);
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

class MyThread3 extends Thread { 
    public void run() { 
        Table.printTable(100); 
    }
}

class MyThread4 extends Thread { 
    public void run() { 
        Table.printTable(1000); 
    }
}

public class TestSynchronization4 {
    public static void main(String t[]) {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();
        MyThread3 t3 = new MyThread3();
        MyThread4 t4 = new MyThread4();
        t1.start();
        t2.start();
        t3.start();
        t4.start(); 
    }
}
```

**Explanation**:
- `printTable()` is static synchronized method
- Lock is on Table class, not on object instances
- Four threads call the static method
- Each thread prints multiplication table of different number (1, 10, 100, 1000)
- All threads synchronized at class level
- Tables print sequentially without mixing

**Output**:
```
1
2
3
...
10
10
20
30
...
100
100
200
300
...
1000
1000
2000
3000
...
10000
```

---

### **10. Inter-thread Communication Example (wait and notify)**

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
        System.out.println("deposit completed... ");
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

**Explanation**:
- Customer has initial balance of 10000
- First thread attempts to withdraw 15000
- Insufficient balance causes thread to call `wait()` and release lock
- Second thread deposits 10000
- After deposit, calls `notify()` to wake waiting thread
- First thread resumes and completes withdrawal
- Demonstrates inter-thread communication and synchronization

**Output**:
```
going to withdraw...
Less balance; waiting for deposit...
going to deposit...
deposit completed... 
withdraw completed...
```

---

### **11. Daemon Thread Example**

```java
public class TestDaemonThread1 extends Thread {
    public void run() {
        if(Thread.currentThread().isDaemon()) { //checking for daemon thread
            System.out.println("daemon thread work");
        } else {
            System.out.println("user thread work");
        }
    }
    
    public static void main(String[] args) {
        TestDaemonThread1 t1 = new TestDaemonThread1(); //creating thread
        TestDaemonThread1 t2 = new TestDaemonThread1();
        TestDaemonThread1 t3 = new TestDaemonThread1();
        
        t1.setDaemon(true); //now t1 is daemon thread
        
        t1.start(); //starting threads
        t2.start();
        t3.start();
    }
}
```

**Explanation**:
- Creates three threads
- `t1` is set as daemon thread using `setDaemon(true)`
- `t2` and `t3` are user threads (default)
- `run()` method checks if current thread is daemon
- Daemon thread prints "daemon thread work"
- User threads print "user thread work"
- Daemon thread terminates when all user threads finish

**Output**:
```
daemon thread work
user thread work
user thread work
```

---

### **12. Thread Group Example**

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

**Explanation**:
- Creates ThreadGroup named "Parent ThreadGroup"
- Three threads (one, two, three) are added to this group
- All threads execute `run()` method that prints thread name
- `getName()` returns thread group name
- `list()` prints detailed information about group and its threads
- Shows thread names, priorities (5), and parent group

**Output**:
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

---

### **13. Complete Multithreading Example with Multiple Methods**

```java
package multithreading;

class ThreadCount extends Thread {
    ThreadCount() {
        super("Overriding Thread Class");
        System.out.println("New thread created" + this);
        start();
    }
    
    public void run() { //Run Method
        try {
            for (int i=0; i<10; i++) {
                System.out.println("New thread created" + this);
                Thread.sleep(1500);
            }
        } catch(InterruptedException e) {
            System.out.println("Currently executing thread is interrupted");
        }
        System.out.println("Currently executing thread run is terminated");
    }
}

public class MultiThreading {
    public static void main(String args[]) {
        ThreadCount C = new ThreadCount();
        try {
            while(C.isAlive()) {
                System.out.println("Main Method Thread will be alive, until it's Child Thread stays alive");
                Thread.sleep(2500); //Sleep method
            }
        } catch(InterruptedException e) {
            System.out.println("Main Method thread is interrupted");
        }
        System.out.println("Main Method's thread run is terminated");
    }
}
```

**Explanation**:
- Constructor creates and starts child thread automatically
- Child thread prints message 10 times with 1.5 second delay
- Main thread checks if child is alive using `isAlive()`
- Main thread sleeps for 2.5 seconds between checks
- Main thread continues until child thread completes
- Demonstrates thread lifecycle and coordination

**Output**:
```
New thread createdThread[Overriding Thread Class,5,main]
Main Method Thread will be alive, until it's Child Thread stays alive 
New thread createdThread[Overriding Thread Class,5,main]
New thread createdThread[Overriding Thread Class,5,main]
Main Method Thread will be alive, until it's Child Thread stays alive 
New thread createdThread[Overriding Thread Class,5,main]
New thread createdThread[Overriding Thread Class,5,main]
Main Method Thread will be alive, until it's Child Thread stays alive 
New thread createdThread[Overriding Thread Class,5,main]
Main Method Thread will be alive, until it's Child Thread stays alive 
New thread createdThread[Overriding Thread Class,5,main]
New thread createdThread[Overriding Thread Class,5,main]
Main Method Thread will be alive, until it's Child Thread stays alive 
New thread createdThread[Overriding Thread Class,5,main]
New thread createdThread[Overriding Thread Class,5,main]
Main Method Thread will be alive, until it's Child Thread stays alive 
New thread createdThread[Overriding Thread Class,5,main]
Main Method Thread will be alive, until it's Child Thread stays alive 
Currently executing thread run is terminated
Main Method's thread run is terminated
```

---

## **Summary of All Code Examples Covered**

1. ✅ Generic class with two type parameters (TwoGen)
2. ✅ Bounded type generic class (Stats with Number bound)
3. ✅ Main thread identification and naming
4. ✅ Thread creation using Runnable interface
5. ✅ Thread creation by extending Thread class
6. ✅ Thread priority demonstration
7. ✅ Synchronized method example
8. ✅ Synchronized block example
9. ✅ Static synchronization example
10. ✅ Inter-thread communication (wait/notify)
11. ✅ Daemon thread example
12. ✅ Thread group example
13. ✅ Complete multithreading with isAlive() and sleep()

**All code examples from the document have been covered with detailed explanations and expected outputs!**