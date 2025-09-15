 # Unit 1: Paradigms & Basic Constructs

## Overview of Object-Oriented Programming (OOP)
OOP is a programming paradigm organized around **objects** rather than actions and data. [span_0](start_span)[span_1](start_span)It can be characterized as data controlling access to code[span_0](end_span)[span_1](end_span).

***

### Core OOP Concepts
* **[span_2](start_span)[span_3](start_span)Object:** A real-world entity with a **state** (data/value) and **behavior** (functionality)[span_2](end_span)[span_3](end_span). [span_4](start_span)[span_5](start_span)An object is an instance of a class, occupies some space in memory, and has a unique ID[span_4](end_span)[span_5](end_span). [span_6](start_span)Objects can communicate with each other without knowing the details of their data or code[span_6](end_span).
* **[span_7](start_span)Class:** A blueprint from which you can create individual objects[span_7](end_span). [span_8](start_span)It is a logical entity and a collection of objects[span_8](end_span). [span_9](start_span)A class consists of data members and methods, but it doesn't store any space in memory[span_9](end_span).
* **[span_10](start_span)Inheritance:** The mechanism of acquiring all the properties and behaviors of one class to another[span_10](end_span). [span_11](start_span)It provides **code reusability** and establishes relationships between different classes[span_11](end_span). [span_12](start_span)A class that inherits is a **subclass** (or child class), and the class whose properties are inherited is the **superclass** (or parent class)[span_12](end_span).
* **[span_13](start_span)Polymorphism:** The ability to perform one task in different ways[span_13](end_span). [span_14](start_span)For example, a `Shape` class with a `draw()` method can have different implementations in subclasses like `Triangle`, `Rectangle`, or `Circle`[span_14](end_span). [span_15](start_span)[span_16](start_span)[span_17](start_span)This is supported in Java through method overloading and method overriding[span_15](end_span)[span_16](end_span)[span_17](end_span).
* **[span_18](start_span)[span_19](start_span)Abstraction:** The process of hiding implementation details and showing only the essential functionality to the user[span_18](end_span)[span_19](end_span). [span_20](start_span)In Java, abstraction is achieved using abstract classes and interfaces[span_20](end_span).
* **[span_21](start_span)[span_22](start_span)Encapsulation:** The process of wrapping code and data together into a single unit[span_21](end_span)[span_22](end_span). [span_23](start_span)[span_24](start_span)This concept is also known as **data hiding**, where data is hidden inside a class, typically by being declared as private[span_23](end_span)[span_24](end_span).

***

### Java Basics: Classes, Methods, and Objects
[span_25](start_span)In Java, a class is at the core of a program and serves as a template for an object[span_25](end_span).

#### Defining a Class
[span_26](start_span)A class is declared using the `class` keyword[span_26](end_span). [span_27](start_span)It can contain instance variables (data) and methods (code)[span_27](end_span).

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

[cite_start]Variables defined within a class are called instance variables because each object (instance) of the class contains its own copy[cite: 245].
Creating and Using Objects
[cite_start]An object is an instance of a class[cite: 134]. [cite_start]You create an object using the new operator, which dynamically allocates memory for it at run time[cite: 267, 268].
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
[cite_start]Constructors are special member functions used to initialize the objects of a class[cite: 281]. [cite_start]They are invoked when an object is created and have the same name as the class[cite: 282, 283].
 * [cite_start]Default Constructor (no-arg constructor): A constructor without any parameters[cite: 287]. [cite_start]If no constructor is explicitly defined, the Java compiler provides a default one[cite: 284, 295].
 * [cite_start]Parameterized Constructor: A constructor that accepts a specific number of parameters to initialize objects with different values[cite: 297].
<!-- end list -->
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
[cite_start]The this keyword refers to the object that invoked a method or constructor[cite: 352]. [cite_start]It is used to refer to the current object and can also be used to invoke a current class constructor[cite: 353, 354].
Method Overloading
[cite_start]This is a form of polymorphism where a class has two or more methods with the same name but different parameter declarations[cite: 359, 360].
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
[cite_start]Access modifiers specify the accessibility (scope) of a data member, method, constructor, or class[cite: 369].
| Modifier | Within Class | Within Package | Outside Package (by subclass) | Outside Package |
|---|---|---|---|---|
| Private | Y | N | N | N |
| Default | Y | Y | N | N |
| Protected | Y | Y | Y | N |
| Public | Y | Y | Y | Y |
 * [cite_start]private: Accessible only within the same class[cite: 371].
 * [cite_start]default: Accessible only within the same package[cite: 377].
 * [cite_start]protected: Accessible within the same package and also by subclasses in different packages through inheritance[cite: 381].
 * [cite_start]public: Accessible everywhere[cite: 387].
The static Keyword
[cite_start]static is a non-access modifier that makes a member belong to the class itself, not to a specific object[cite: 405]. [cite_start]All instances of the class share the same static variable[cite: 399].
 * [cite_start]Static variables: Declared at the class level and are shared among all objects[cite: 398, 400].
 * [cite_start]Static methods: Can be accessed without creating an object[cite: 405]. [cite_start]A static method can only call other static methods and access static data, and cannot use the this or super keywords[cite: 408, 409].
<!-- end list -->
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
[cite_start]The finalize() method is called by the garbage collector just before an object is destroyed[cite: 415, 434]. [cite_start]Its traditional purpose was for resource cleanup[cite: 437]. [cite_start]However, its use is discouraged due to unpredictability and performance issues[cite: 435, 440]. [cite_start]Modern alternatives like try-with-resources are recommended[cite: 443, 452].
Unit 2: Exception Handling & Streams
Arrays and Strings
Arrays
[cite_start]An array is a collection of similar-type elements with contiguous memory locations[cite: 475]. [cite_start]In Java, arrays are objects, and their length can be determined using the .length member[cite: 476]. [cite_start]A disadvantage is their fixed size[cite: 483].
 * One-Dimensional Array: A simple list of elements.
 * [cite_start]Multidimensional Array: An array of arrays, also known as Jagged Arrays[cite: 496].
<!-- end list -->
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
[cite_start]A string in Java is an object representing a sequence of characters[cite: 518]. [cite_start]Java string objects are immutable[cite: 521].
 * [cite_start]String Literal: Created using double quotes (e.g., String s = "welcome";)[cite: 522].
 * [cite_start]new Keyword: Creates a new string object in memory (e.g., String s = new String("Welcome");)[cite: 523].
StringBuffer Class
[cite_start]The StringBuffer class is used to create mutable (modifiable) string objects[cite: 536].
 * [cite_start]append(): Concatenates the given argument with the string[cite: 536].
 * [cite_start]insert(): Inserts a string at a specified position[cite: 538].
 * [cite_start]replace(): Replaces a portion of the string[cite: 539].
 * [cite_start]delete(): Deletes a portion of the string[cite: 540].
 * [cite_start]reverse(): Reverses the current string[cite: 541].
<!-- end list -->
class StringBufferExample {
  public static void main(String args[]) {
    StringBuffer sb = new StringBuffer("Hello ");
    sb.append("Compiler");
    System.out.println(sb); // prints Hello Compiler
  }
}

Inheritance and Method Overriding
[cite_start]Inheritance is the mechanism of a subclass acquiring the properties and behaviors of a superclass[cite: 640]. [cite_start]It is used for method overriding and code reusability[cite: 643].
Types of Inheritance
 * [cite_start]Single Inheritance: One class extends one other class[cite: 652].
 * [cite_start]Multilevel Inheritance: One class inherits from a derived class[cite: 654].
 * [cite_start]Hierarchical Inheritance: One class is inherited by multiple subclasses[cite: 658].
 * Multiple Inheritance: One class extends more than one class. [cite_start]It is not directly supported in Java but can be achieved through interfaces[cite: 665].
The super Keyword
[cite_start]The super keyword refers to the superclass[cite: 666].
 * [cite_start]super(): Invokes the constructor of the parent class[cite: 666, 668].
 * [cite_start]super.variable: Refers to a variable in the parent class[cite: 667].
 * [cite_start]super.method(): Refers to a method of the parent class[cite: 667, 683].
<!-- end list -->
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

[cite_start]Method overriding occurs when a method in a subclass has the same name and type signature as a method in its superclass[cite: 690, 691]. [cite_start]When called, the subclass's version is executed[cite: 692].
Abstract Classes and Interfaces
Abstract Classes
[cite_start]An abstract class is declared with the abstract keyword and cannot be instantiated[cite: 725, 729]. [cite_start]It can have abstract methods (without a body) and non-abstract methods (with a body)[cite: 726].
 * [cite_start]Abstract method: A method declared with the abstract keyword and no implementation[cite: 730]. [cite_start]Subclasses must implement all abstract methods[cite: 856].
<!-- end list -->
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
[cite_start]An interface is a blueprint of a class that provides a mechanism to achieve abstraction and multiple inheritance[cite: 839]. [cite_start]It is declared using the interface keyword[cite: 840].
 * [cite_start]All interface methods are public and abstract by default[cite: 857].
 * [cite_start]All interface variables are public, static, and final by default[cite: 858].
 * [cite_start]A class uses the implements keyword to use an interface[cite: 854].
<!-- end list -->
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

Exception Handling
[cite_start]An exception is a problem that arises during a program's execution, disrupting its normal flow[cite: 760]. [cite_start]If an exception is not handled, the program terminates abnormally[cite: 761].
 * [cite_start]try block: Encloses code that might generate an exception[cite: 769].
 * [cite_start]catch block: Placed immediately after a try block to catch a specific type of exception[cite: 771].
 * [cite_start]finally block: Always executes, whether or not an exception occurs, and is typically used for cleanup[cite: 772].
<!-- end list -->
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

I/O Streams
[cite_start]A stream is a sequence of data[cite: 879]. [cite_start]Java uses streams for input and output operations, and they are divided into two main categories[cite: 876, 878]:
 * [cite_start]Byte Streams: Used for 8-bit byte input and output (e.g., FileInputStream, FileOutputStream)[cite: 882].
 * [cite_start]Character Streams: Used for 16-bit Unicode character input and output (e.g., FileReader, FileWriter)[cite: 883].
InputStream and OutputStream
 * [cite_start]InputStream: Reads data from a source[cite: 880]. [cite_start]The InputStream class is an abstract class and defines methods like read(), available(), and close()[cite: 890, 893].
 * [cite_start]OutputStream: Writes data to a destination[cite: 881]. [cite_start]The OutputStream class defines methods like write(), close(), and flush()[cite: 895, 897].
<!-- end list -->

