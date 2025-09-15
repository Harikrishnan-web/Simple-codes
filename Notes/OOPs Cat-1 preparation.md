***

# OOP Unit I – Full Notes with Java Code

***

## OOP Concepts Overview

Object-Oriented Programming (OOP) is organized around **objects** rather than actions and data. It enhances code **modularity**, **reusability**, and **data security** through several key principles[1].

- **Object**
- **Class**
- **Inheritance**
- **Polymorphism**
- **Abstraction**
- **Encapsulation**

***

### Objects

An **object** is any real-world entity with a state (data) and behavior (actions). It is an instance of a class.

#### Example: Object Creation in Java

```java
class Dog {
    String name;
    int age;
    void bark() {
        System.out.println(name + " is barking!");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.name = "Buddy";
        myDog.age = 3;
        myDog.bark(); // Output: Buddy is barking!
    }
}
```
- `"Dog"` is the class.
- `myDog` is the object.
- `name` and `age` are attributes.
- `bark()` is a behavior[1].

***

### Classes

A **class** defines the blueprint for objects.

#### Example: Basic Class Structure

```java
class Box {
    double width;
    double height;
    double depth;
}
```
- It doesn't allocate memory until an object is created[1].

#### Creating Objects:

```java
Box mybox = new Box();
mybox.width = 10;
mybox.height = 20;
mybox.depth = 15;
```
- Access members using the `.` operator.

***

### Methods and Messages

**Methods**: Functions inside a class that describe behaviors.

**Messages**: When you call methods on objects.

#### Example

```java
class Cat {
    String name;
    int age;
    void meow() {
        System.out.println(name + " says Meow!");
    }
}

public class Main {
    public static void main(String[] args) {
        Cat myCat = new Cat();
        myCat.name = "Whiskers";
        myCat.age = 2;
        myCat.meow(); // Output: Whiskers says Meow!
    }
}
```
Explanation: The method `meow()` is called as a message to the object[1].

***

## OOP Principles

### Abstraction

**Abstraction** hides complex implementation details and only shows essential features.

#### Example

```java
abstract class Animal {
    abstract void makeSound(); // Abstract method
    void sleep() { // Concrete method
        System.out.println("Sleeping...");
    }
}
class Dog extends Animal {
    void makeSound() {
        System.out.println("Woof!");
    }
}
```
Abstract classes/methods provide a skeleton — implementation is given by subclasses[1].

***

### Encapsulation

Wrapping data and methods into a single class, often restricting access via access specifiers[1].

#### Example

```java
class Person {
    private String name; // Data hidden
    private int age;
    public void setName(String name) { this.name = name; }
    public String getName() { return name; }
    public void setAge(int age) { this.age = age; }
    public int getAge() { return age; }
}
```
Encapsulation ensures data security and prevents unauthorized access.

***

### Inheritance

Acquiring properties/behaviors from another class. It allows reusability[1].

#### Example

```java
class Animal {
    void eat() { System.out.println("Eats food"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat(); // Inherited
        d.bark(); // Own method
    }
}
```
A `Dog` is an `Animal` — inherits `eat()`.

***

### Polymorphism

Enables one action to behave differently based on context.

- **Method Overloading** (compile-time polymorphism): Same method name, different parameters.
- **Method Overriding** (run-time polymorphism): Subclass changes the behavior of superclass method.

#### Example: Method Overloading

```java
class MathOps {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
}
```

#### Example: Method Overriding

```java
class Animal {
    void sound() { System.out.println("Some sound"); }
}
class Dog extends Animal {
    @Override
    void sound() { System.out.println("Woof!"); }
}
```

#### Polymorphism Usage

```java
Animal a = new Dog();
a.sound(); // Woof!
```
- The actual method called depends on the object's runtime type[1].

***

## Java-Specific Constructs

### Access Specifiers

Control visibility of class members:

| Specifier  | Within Class | Within Package | Subclass Outside Package | Everywhere |
|------------|:-------------:|:-------------:|:-----------------------:|:----------:|
| private    | Yes           | No            | No                      | No         |
| default    | Yes           | Yes           | No                      | No         |
| protected  | Yes           | Yes           | Yes                     | No         |
| public     | Yes           | Yes           | Yes                     | Yes        |

#### Example

```java
class Example {
    private int x; // accessible only inside Example
    public int y;  // accessible everywhere
}
```


***

### Static Members

Share a single copy of variables or methods across all objects, belong to the class itself.

#### Example

```java
class Counter {
    static int count = 0;
    Counter() { count++; }
    static void printCount() { System.out.println("Count: " + count); }
}
```
- Can be called without creating an object.

***

### Constructors

Special methods to initialize objects.

#### Example: Default Constructor

```java
class Box {
    double width, height, depth;
    Box() {
        width = 10; height = 10; depth = 10;
    }
}
```
#### Parameterized Constructor

```java
class Box {
    double width, height, depth;
    Box(double w, double h, double d) {
        width = w; height = h; depth = d;
    }
}
```

#### Constructor Overloading

```java
class Box {
    double width, height, depth;
    Box() { width = -1; height = -1; depth = -1; }
    Box(double w, double h, double d) { width = w; height = h; depth = d; }
    Box(double len) { width = height = depth = len; }
}
```


***

### Finalize Method

Called before object is garbage collected; mainly used for resource cleanup but not recommended in modern Java.

#### Example

```java
public class Car {
    public Car() { System.out.println("Car is created"); }
    @Override
    protected void finalize() throws Throwable {
        try { System.out.println("Car is being destroyed"); }
        finally { super.finalize(); }
    }
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar = null;
        System.gc();
    }
}
```
- Prefer try-with-resources or explicit cleanup methods instead of finalize[1].

***

## Practice Problems – With Expected Inputs and Outputs

Practice these to gain fluency in basic Java coding[1].

- Calculate expression: $$((25.5 \times 3.5 - 3.5 \times 3.5) / (40.5 - 4.5))$$
- Compute average of three numbers.
- Print area and perimeter of a circle.
- Swap two variables.

For details and more examples, refer to the full problem set in your attached material.

***

# Key Points Summary

- **Object** and **class**: Real-world entities, blueprints.
- **OOP principles**: Abstraction, Encapsulation, Inheritance, Polymorphism.
- **Java constructs**: Access specifiers, static members, constructors, finalize method.
- **Coding style**: Use comments, correct naming, clear access levels.
- **Exam preparation**: Focus on concept definitions and code writing ability.

These notes are structured to ensure maximum coverage to tackle any question. Focus especially on explanations and the commented code examples[1].

***

# OOP Unit II – Exception Handling & Streams (CS23312)

***

## Arrays

An **array** is a collection of elements of the same type, stored in contiguous memory and indexed starting from 0[1].

### One-Dimensional Array

```java
int[] a = new int; // Declaration and instantiation
a=10; a[1]=20; a=70; a=40; a=50;
for(int i=0; i<a.length; i++)
    System.out.println(a[i]);
```
- Retrieve length using `.length`
- Can be passed to methods

### Multidimensional Array

```java
int[][] twoD = new int; // 2D array
for(int i=0; i<4; i++)
    for(int j=0; j<5; j++)
        twoD[i][j] = i * 5 + j;
```
Arrays of arrays ("jagged arrays") are possible by allocating subarrays separately[1].

***

## Java Comments & JavaDoc

- **Single line**: `// This is a comment`
- **Multi-line**:
  ```java
  /* This is a 
     multi-line comment */
  ```
- **Documentation**:
  ```java
  /** This is a doc comment for API documentation */
  public class Example {
      /** Returns sum of two integers */
      public int add(int a, int b) { return a + b; }
  }
  ```
JavaDoc comments are used for generating HTML documentation[1].

***

## Strings and StringBuffer

### String Class

- Immutable sequence of characters:

```java
String s1 = "Hello";
String s2 = new String("Hello");
System.out.println(s1.equals(s2)); // true
System.out.println(s1.charAt(0));  // 'H'
System.out.println(s1.length());   // 5
```

#### Common String Methods

| Method                         | Description                           |
|------------------------------- |---------------------------------------|
| `charAt(int idx)`              | Gets character at index               |
| `toLowerCase()`, `toUpperCase()` | Case conversion                      |
| `concat(String)`               | Concatenates strings                  |
| `replace(char, char)`          | Replaces character                    |
| `split(String)`                | Splits string                         |
| `substring(int, int)`          | Gets substring                        |
| `equals(Object)`               | Compares for equality                 |
| `isEmpty()`                    | Checks for empty string               |
| `indexOf(String)`              | Finds index                           |
| `trim()`                       | Removes leading/trailing spaces       |

### StringBuffer Class

- Mutable string manipulation:

```java
StringBuffer sb = new StringBuffer("Hello");
sb.append("World");       // HelloWorld
sb.insert(1, "Java");     // HJavaelloWorld
sb.replace(0, 5, "Hi");   // HiWorld
sb.delete(1, 3);          // Hld
sb.reverse();             // dlH
System.out.println(sb);   // Prints final value
```

#### Buffer Capacity Example

```java
StringBuffer sb = new StringBuffer();
System.out.println(sb.capacity()); // Default 16
sb.ensureCapacity(50);
System.out.println(sb.capacity()); // Increased as needed
```
StringBuffer is used for efficient, mutable string operations[1].

***

## Packages

A **package** is a collection of related classes, interfaces, and sub-packages. Use the `package` keyword:

```java
package mypack;

public class Balance {
    String name;
    double bal;
    Balance(String n, double b) { name = n; bal = b; }
    void show() { System.out.println(name + ": " + bal); }
}
```

Compile and run using fully qualified class name. Example: `java mypack.Balance`

Benefits:
- Organizes code
- Prevents namespace collision
- Provides access control[1]

***

## Interfaces

An **interface** declares a set of methods that classes must implement, enabling abstraction and multiple inheritance.

```java
interface Drawable {
    void draw(); // Method is implicitly public and abstract
}

class Rectangle implements Drawable {
    public void draw() { System.out.println("drawing rectangle"); }
}
```

Multiple interfaces can be implemented:

```java
interface Printable { void print(); }
interface Showable { void show(); }

class A implements Printable, Showable {
    public void print() { System.out.println("Hello"); }
    public void show() { System.out.println("Welcome"); }
}
```
Interface methods are always public, abstract, interface variables are public, static, final[1].

***

## Inheritance

Inheritance enables code reuse and hierarchical relationships[1].

### Single Inheritance

```java
class A { public void dispA() { System.out.println("A"); } }
class B extends A { public void dispB() { System.out.println("B"); } }
```

### Multilevel

```java
class C extends B { public void dispC() { System.out.println("C"); } }
```

### Hierarchical

Multiple classes inherit from the same parent:

```java
class D extends A { ... }
class E extends A { ... }
```

### super Keyword

- `super()` calls parent constructor
- `super.variable` accesses parent's variable
- `super.method()` calls parent's method

```java
class Parent { void display() { System.out.println("Parent"); } }
class Child extends Parent {
    void display() { System.out.println("Child"); }
    void show() { display(); super.display(); }
}
```

***

## Abstract Classes

Abstract classes can have abstract and concrete methods.

```java
abstract class Shape { abstract void draw(); }
class Circle extends Shape { void draw() { System.out.println("Circle"); } }
```
Cannot create direct instances; must be subclassed.

***

## Final Keyword

- **Final variable**: cannot be changed.
- **Final method**: cannot be overridden.
- **Final class**: cannot be extended.

```java
final int SPEED = 60;
final class Base { ... }
class Derived extends Base { } // Error
```

***

## Exception Handling

Exceptions are errors occurring during program execution. Java provides these keywords:
- **try**: wrap risky code
- **catch**: handle exception
- **finally**: always runs
- **throw**: manually trigger exception
- **throws**: specify possible exception in method signature[1]

### Example: Basic Exception Handling

```java
try {
    int a = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Division by zero!");
} finally {
    System.out.println("Cleanup.");
}
```

### Exception Hierarchy

All exception classes derive from `Throwable`, mostly via `Exception`.

#### User-Defined Exception Example

```java
class MyException extends Exception {
    MyException(String message) { super(message); }
}

try {
    throw new MyException("Custom error");
} catch (MyException e) {
    System.out.println(e.getMessage());
}
```
***

## Dynamic Method Dispatch

Decides which overridden method to call at runtime:

```java
class A { void m1() { System.out.println("A"); } }
class B extends A { void m1() { System.out.println("B"); } }
A ref;
ref = new B();
ref.m1(); // Calls B's m1() due to runtime type
```

***

## I/O Streams

Java uses **streams** for data input/output. Types:
- **InputStream/OutputStream**: byte streams
- **Reader/Writer**: character streams
- **Buffered Streams**: buffer the read/write for efficiency

### Basic File I/O

```java
import java.io.*;

FileInputStream fin = new FileInputStream("test.txt");
int i;
while((i = fin.read()) != -1)
    System.out.print((char) i);
fin.close();
```

### Buffered Streams Example

```java
FileOutputStream fout = new FileOutputStream("test.txt");
BufferedOutputStream bout = new BufferedOutputStream(fout);
String s = "Hello World";
bout.write(s.getBytes());
bout.flush(); // Ensures writing out all data
bout.close(); fout.close();
```
***

## Summary Table – Topic Mapping

| Topic                      | Covered        |
|----------------------------|:-------------:|
| Arrays                     | Yes           |
| Comments & JavaDoc         | Yes           |
| Strings/StringBuffer       | Yes           |
| Packages & Interfaces      | Yes           |
| Inheritance & super        | Yes           |
| Abstract/Final keyword     | Yes           |
| Exception handling         | Yes           |
| Dynamic dispatch           | Yes           |
| I/O streams                | Yes           |
| Buffered/File Streams      | Yes           |

***


