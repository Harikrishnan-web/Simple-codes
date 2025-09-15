Here’s the full content formatted cleanly as a Markdown (.md) file without watermarks or span tags:

# Unit 1: Paradigms & Basic Constructs

## Overview of Object-Oriented Programming (OOP)
OOP is a programming paradigm organized around **objects** rather than actions and data. It can be characterized as data controlling access to code.

***

### Core OOP Concepts
* **Object:** A real-world entity with a **state** (data/value) and **behavior** (functionality). An object is an instance of a class, occupies some space in memory, and has a unique ID. Objects can communicate with each other without knowing the details of their data or code.
* **Class:** A blueprint from which you can create individual objects. It is a logical entity and a collection of objects. A class consists of data members and methods, but it doesn't store any space in memory.
* **Inheritance:** The mechanism of acquiring all the properties and behaviors of one class to another. It provides **code reusability** and establishes relationships between different classes. A class that inherits is a **subclass** (or child class), and the class whose properties are inherited is the **superclass** (or parent class).
* **Polymorphism:** The ability to perform one task in different ways. For example, a `Shape` class with a `draw()` method can have different implementations in subclasses like `Triangle`, `Rectangle`, or `Circle`. This is supported in Java through method overloading and method overriding.
* **Abstraction:** The process of hiding implementation details and showing only the essential functionality to the user. In Java, abstraction is achieved using abstract classes and interfaces.
* **Encapsulation:** The process of wrapping code and data together into a single unit. This concept is also known as **data hiding**, where data is hidden inside a class, typically by being declared as private.

***

### Java Basics: Classes, Methods, and Objects
In Java, a class is at the core of a program and serves as a template for an object.

#### Defining a Class
A class is declared using the `class` keyword. It can contain instance variables (data) and methods (code).

```java
class Box {
  // Instance variables
  double width;
  double height;
  double depth;
  
  // Methods
  double volume() {
    return width * height * depth;
  }
}

> Variables defined within a class are called instance variables because each object (instance) of the class contains its own copy.



Creating and Using Objects

An object is an instance of a class. You create an object using the new operator, which dynamically allocates memory for it at run time.

public class BoxDemo {
  public static void main(String args[]) {
    Box mybox = new Box(); // Creates a Box object
    
    // Accessing instance variables using the dot (.) operator
    mybox.width = 10;
    mybox.height = 20;
    mybox.depth = 15;
    
    // Invoking a method on the object
    double vol = mybox.volume();
    System.out.println("Volume is " + vol); // Output: Volume is 3000.0
  }
}

Constructors

Constructors are special member functions used to initialize the objects of a class. They are invoked when an object is created and have the same name as the class.

Default Constructor (no-arg constructor): A constructor without any parameters. If no constructor is explicitly defined, the Java compiler provides a default one.

Parameterized Constructor: A constructor that accepts a specific number of parameters to initialize objects with different values.


class Box {
  double width, height, depth;
  
  // Parameterized constructor
  Box(double w, double h, double d) {
    width = w;
    height = h;
    depth = d;
  }
}

class BoxDemo7 {
  public static void main(String args[]) {
    Box mybox1 = new Box(10, 20, 15); // Passes values to the constructor
  }
}

The this Keyword

The this keyword refers to the object that invoked a method or constructor. It is used to refer to the current object and can also be used to invoke a current class constructor.

Method Overloading

This is a form of polymorphism where a class has two or more methods with the same name but different parameter declarations.

class OverloadDemo {
  void test() {
    System.out.println("No parameters");
  }

  void test(int a) {
    System.out.println("a: " + a);
  }

  void test(int a, int b) {
    System.out.println("a and b: " + a + " " + b);
  }
}

Access Specifiers

Access modifiers specify the accessibility (scope) of a data member, method, constructor, or class.

Modifier	Within Class	Within Package	Outside Package (by subclass)	Outside Package

Private	Y	N	N	N
Default	Y	Y	N	N
Protected	Y	Y	Y	N
Public	Y	Y	Y	Y


private: Accessible only within the same class.

default: Accessible only within the same package.

protected: Accessible within the same package and also by subclasses in different packages through inheritance.

public: Accessible everywhere.


The static Keyword

static is a non-access modifier that makes a member belong to the class itself, not to a specific object. All instances of the class share the same static variable.

Static variables: Declared at the class level and are shared among all objects.

Static methods: Can be accessed without creating an object. A static method can only call other static methods and access static data, and cannot use the this or super keywords.


class StaticDemo {
  static int a = 42;
  static void callme() {
    System.out.println("a = " + a);
  }
}

class StaticByName {
  public static void main(String args[]) {
    StaticDemo.callme();
  }
}
// Output:
// a = 42

finalize() Method

The finalize() method is called by the garbage collector just before an object is destroyed. Its traditional purpose was for resource cleanup. However, its use is discouraged due to unpredictability and performance issues. Modern alternatives like try-with-resources are recommended.


---

Unit 2: Exception Handling & Streams

Arrays and Strings

Arrays

An array is a collection of similar-type elements with contiguous memory locations. In Java, arrays are objects, and their length can be determined using the .length member. A disadvantage is their fixed size.

One-Dimensional Array: A simple list of elements.

Multidimensional Array: An array of arrays, also known as Jagged Arrays.


class Testarray1 {
  public static void main(String args[]) {
    // Declaration, instantiation, and initialization
    int a[] = {33, 3, 4, 5};
    
    // Prints array elements
    for(int i = 0; i < a.length; i++) {
      System.out.println(a[i]);
    }
  }
}

Strings

A string in Java is an object representing a sequence of characters. Java string objects are immutable.

String Literal: Created using double quotes (e.g., String s = "welcome";).

new Keyword: Creates a new string object in memory (e.g., String s = new String("Welcome");).


StringBuffer Class

The StringBuffer class is used to create mutable (modifiable) string objects.

append(): Concatenates the given argument with the string.

insert(): Inserts a string at a specified position.

replace(): Replaces a portion of the string.

delete(): Deletes a portion of the string.

reverse(): Reverses the current string.


class StringBufferExample {
  public static void main(String args[]) {
    StringBuffer sb = new StringBuffer("Hello ");
    sb.append("Compiler");
    System.out.println(sb); // prints Hello Compiler
  }
}


---

Inheritance and Method Overriding

Inheritance is the mechanism of a subclass acquiring the properties and behaviors of a superclass. It is used for method overriding and code reusability.

Types of Inheritance

Single Inheritance: One class extends one other class.

Multilevel Inheritance: One class inherits from a derived class.

Hierarchical Inheritance: One class is inherited by multiple subclasses.

Multiple Inheritance: One class extends more than one class. It is not directly supported in Java but can be achieved through interfaces.


The super Keyword

The super keyword refers to the superclass.

super(): Invokes the constructor of the parent class.

super.variable: Refers to a variable in the parent class.

super.method(): Refers to a method of the parent class.


class ParentClass {
  void disp() {
    System.out.println("Parent Class method");
  }
}

public class SubClass extends ParentClass {
  void disp() {
    System.out.println("Child Class method");
  }
  
  void show() {
    super.disp(); // Calls the Parent Class disp() method
    disp();       // Calls the Child Class disp() method
  }
  
  public static void main(String args[]) {
    SubClass s = new SubClass();
    s.show();
  }
}
// Output:
// Parent Class method
// Child Class method

Method overriding occurs when a method in a subclass has the same name and type signature as a method in its superclass. When called, the subclass's version is executed.


---

Abstract Classes and Interfaces

Abstract Classes

An abstract class is declared with the abstract keyword and cannot be instantiated. It can have abstract methods (without a body) and non-abstract methods (with a body).

Abstract method: A method declared with the abstract keyword and no implementation. Subclasses must implement all abstract methods.


abstract class Bike {
  abstract void run(); // Abstract method
}

class Honda extends Bike {
  void run() {
    System.out.println("running safely..");
  }
}

class TestAbstraction2 {
  public static void main(String args[]) {
    Bike obj = new Honda();
    obj.run();
  }
}
// Output:
// running safely..

Interfaces

An interface is a blueprint of a class that provides a mechanism to achieve abstraction and multiple inheritance. It is declared using the interface keyword.

All interface methods are public and abstract by default.

All interface variables are public, static, and final by default.

A class uses the implements keyword to use an interface.


interface Drawable {
  void draw();
}

class Circle implements Drawable {
  public void draw() {
    System.out.println("drawing circle");
  }
}

class TestInterface1 {
  public static void main(String args[]) {
    Drawable d = new Circle();
    d.draw(); // Output: drawing circle
  }
}


---

Exception Handling

An exception is a problem that arises during a program's execution, disrupting its normal flow. If an exception is not handled, the program terminates abnormally.

try block: Encloses code that might generate an exception.

catch block: Placed immediately after a try block to catch a specific type of exception.

finally block: Always executes, whether or not an exception occurs, and is typically used for cleanup.


class Exc2 {
  public static void main(String args[]) {
    try {
      int d = 0;
      int a = 42 / d;
    } catch (ArithmeticException e) {
      System.out.println("Division by zero.");
    }
    System.out.println("After catch statement.");
  }
}
// Output:
// Division by zero.
// After catch statement.


---

I/O Streams

A stream is a sequence of data. Java uses streams for input and output operations, and they are divided into two main categories:

Byte Streams: Used for 8-bit byte input and output (e.g., FileInputStream, FileOutputStream).

Character Streams: Used for 16-bit Unicode character input and output (e.g., FileReader, FileWriter).


InputStream and OutputStream

InputStream: Reads data from a source. The InputStream class is an abstract class and defines methods like read(), available(), and close().

OutputStream: Writes data to a destination. The OutputStream class defines methods like write(), close(), and flush().


Do you want me to also **split this into separate `.md` files per unit** (Unit 1 and Unit 2), or keep it as one large file?

