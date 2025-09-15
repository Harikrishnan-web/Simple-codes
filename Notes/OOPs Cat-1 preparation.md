Sure! Here are detailed notes covering the key concepts from Unit 1 and Unit 2 of your Object-Oriented Programming course. These notes are structured to help you understand the topics thoroughly and prepare for your exams.
Unit 1: Paradigms & Basic Constructs
Overview of Object-Oriented Programming (OOP)
[cite_start]OOP is a programming paradigm that organizes code around objects rather than actions or data alone. [cite_start]It focuses on "who is being affected" rather than "what is happening".
Core OOP Concepts
 * [cite_start]Object: A real-world entity with a state (data/attributes) and behavior (functionality). [cite_start]Objects are instances of a class, occupy memory, and have a unique identity. [cite_start]They communicate by sending messages to each other.
 * [cite_start]Class: A blueprint or template for creating objects. [cite_start]It's a logical entity that groups similar objects and defines their common data members and methods. [cite_start]A class itself doesn't take up memory; memory is allocated when an object is created from it.
 * [cite_start]Inheritance: A mechanism where one class (a subclass or child class) acquires the properties and behaviors of another class (a superclass or parent class). [cite_start]It's a key principle for code reusability and establishing an "is-a" relationship.
 * [cite_start]Polymorphism: The ability of an object or method to take on many forms. It allows a single name to be used for different but related actions. [cite_start]In Java, this is achieved through method overloading (at compile time) and method overriding (at runtime).
 * [cite_start]Abstraction: The process of hiding complex implementation details and showing only the essential functionality to the user. [cite_start]For instance, when you make a phone call, you don't know the internal processes involved. [cite_start]In Java, this is achieved using abstract classes and interfaces.
 * [cite_start]Encapsulation: The practice of wrapping data and the code that operates on that data into a single unit, like a capsule. [cite_start]This is done by bundling a class's data members and methods together, and often restricting direct access to the data using access modifiers. [cite_start]This concept is a form of data hiding.
Java Basics: Classes, Methods, and Objects
In Java, a program's structure revolves around classes and objects.
Defining a Class
[cite_start]A class is defined using the class keyword.
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

The variables (width, height, depth) are called instance variables, and the code within the class is contained in methods (volume()). [cite_start]Both are considered members of the class.
Creating and Using Objects
[cite_start]To use a class, you must create an object, or an instance of that class, using the new keyword. [cite_start]The dot (.) operator is used to access the object's instance variables and methods.
public class BoxDemo {
  public static void main(String args[]) {
    Box mybox = new Box(); // Declares and allocates a Box object
    
    // Assigns values to the instance variables
    mybox.width = 10;
    mybox.height = 20;
    mybox.depth = 15;
    
    // Calls the method and prints the result
    double vol = mybox.volume();
    System.out.println("Volume is " + vol); // Output: Volume is 3000.0
  }
}

Constructors
[cite_start]A constructor is a special method used to initialize objects when they're created. [cite_start]It has the same name as the class and no return type. [cite_start]If you don't define a constructor, Java provides a default one.
 * [cite_start]Default Constructor: A constructor with no parameters.
   class Box {
  double width;
  // Default constructor
  Box() {
    System.out.println("Constructing Box");
    width = 10;
  }
}

 * [cite_start]Parameterized Constructor: A constructor with parameters, used to initialize objects with different values.
   class Box {
  double width;
  // Parameterized constructor
  Box(double w, double h, double d) {
    this.width = w;
    this.height = h;
    this.depth = d;
  }
}

The this Keyword
[cite_start]The this keyword refers to the current object inside a method or constructor. It's often used to distinguish between instance variables and local method parameters with the same name, as shown in the parameterized constructor example above.
Method Overloading
[cite_start]This is a form of polymorphism where a class has two or more methods with the same name but different parameter declarations (number, type, or order of arguments).
class OverloadDemo {
  void test() { // No parameters
    System.out.println("No parameters");
  }

  void test(int a) { // One integer parameter
    System.out.println("a: " + a);
  }

  double test(double a) { // One double parameter
    System.out.println("double a: " + a);
    return a * a;
  }
}

Access Specifiers
[cite_start]Access modifiers, also known as access specifiers, control the visibility and scope of a class, method, or variable.
| Modifier | Within Class | Within Package | Outside Package (by subclass) | Outside Package |
|---|---|---|---|---|
| private | Yes | No | No | No |
| default | Yes | Yes | No | No |
| protected | Yes | Yes | Yes | No |
| public | Yes | Yes | Yes | Yes |
| [cite_start] |  |  |  |  |
 * [cite_start]private: Accessible only within the same class.
 * [cite_start]default: Accessible only within the same package.
 * [cite_start]protected: Accessible within the same package and also by subclasses in different packages. [cite_start]It cannot be applied to a class.
 * [cite_start]public: Accessible from everywhere.
The static Keyword
The static keyword can be applied to variables, methods, blocks, and nested classes. [cite_start]A static member belongs to the class itself, not to a specific object. [cite_start]This means only a single copy exists and is shared by all objects of that class.
 * [cite_start]Static Variables: Shared among all objects of a class. They are essentially global variables.
 * [cite_start]Static Methods: Can be called without creating an object of the class. [cite_start]The most common example is main(). [cite_start]A static method can only call other static methods and access static data; it cannot use this or super.
<!-- end list -->
class StaticDemo {
  static int a = 42;
  static int b = 99;
  
  static void callme() {
    System.out.println("a = " + a);
  }
}

class StaticByName {
  public static void main(String args[]) {
    StaticDemo.callme(); // Calling a static method without an object
    System.out.println("b = " + StaticDemo.b); // Accessing a static variable
  }
}
// Output:
// a = 42
// b = 99

finalize() Method
[cite_start]The finalize() method is called by the garbage collector on an object when it determines there are no more references to the object. [cite_start]Its traditional use was for cleanup, like releasing resources not managed by the garbage collector. [cite_start]However, it is unpredictable and its use is now discouraged in modern Java in favor of better alternatives like try-with-resources.
Unit 2: Exception Handling & Streams
Arrays and Strings
Arrays
[cite_start]An array is a collection of elements of a similar data type stored in contiguous memory locations. [cite_start]In Java, arrays are objects and are dynamically allocated. [cite_start]Their length can be found using the .length member. [cite_start]The first element's index is 0. [cite_start]A disadvantage of arrays is their fixed size, which cannot be changed at runtime.
 * [cite_start]One-Dimensional Arrays: A simple list of elements.
   // Declaration and instantiation
int a[] = new int[5];

// Initialization
a[0] = 10;

// Declaration, instantiation, and initialization
int b[] = {33, 3, 4, 5};

 * [cite_start]Multidimensional Arrays: Arrays of arrays, also known as Jagged Arrays.
   // 2D array declaration
int twoD[][] = new int[4][5];

// Jagged array (rows have different column sizes)
int jagged[][] = new int[4][];
jagged[0] = new int[1];
jagged[1] = new int[2];

Strings
[cite_start]In Java, a String is an object that represents a sequence of character values. [cite_start]Strings are immutable, meaning their value cannot be changed after creation.
There are two ways to create a String object:
 * By string literal: Using double quotes. [cite_start]Java uses a "string constant pool" to reuse identical string literals.
   String s = "welcome";

 * [cite_start]By new keyword: Creates a new string object in heap memory.
   String s = new String("Welcome");

StringBuffer Class
[cite_start]The StringBuffer class is used to create mutable (modifiable) string objects. Its methods allow you to modify the string without creating a new object.
 * append(): Concatenates a string to the end.
   StringBuffer sb = new StringBuffer("Hello ");
sb.append("Compiler"); // sb is now "Hello Compiler"

 * [cite_start]insert(): Inserts a string at a specified position.
   sb.insert(1, "Java"); // sb is now "HJavaello Compiler"

 * [cite_start]replace(): Replaces a portion of the string.
 * [cite_start]delete(): Deletes a portion of the string.
 * [cite_start]reverse(): Reverses the string.
Inheritance and Method Overriding
[cite_start]Inheritance is the mechanism by which one class acquires the properties and behaviors of another. [cite_start]It allows for code reusability and establishing an "is-a" relationship.
Types of Inheritance
Java supports three main types of inheritance:
 * [cite_start]Single Inheritance: One class extends one other class.
 * [cite_start]Multilevel Inheritance: A class inherits from a derived class, forming a chain.
 * [cite_start]Hierarchical Inheritance: One class is inherited by multiple subclasses.
(Multiple and hybrid inheritance are only supported through interfaces in Java) [cite_start].
The super Keyword
[cite_start]The super keyword is used to refer to the superclass. It has three main uses:
 * super(): Invokes the parent class's constructor. [cite_start]It must be the first statement in the subclass constructor.
 * [cite_start]super.variable: Refers to a variable in the parent class when it's hidden by a variable with the same name in the subclass.
 * [cite_start]super.method(): Refers to a method in the parent class, especially when it has been overridden in the subclass.
Method Overriding
[cite_start]When a method in a subclass has the same name and type signature as a method in its superclass, it is said to override the superclass method. [cite_start]The subclass's version of the method is used when called on a subclass object.
class A {
  void show() {
    System.out.println("i and j: ");
  }
}

class B extends A {
  // This overrides show() in A
  void show() {
    System.out.println("k: ");
  }
}

class Override {
  public static void main(String args[]) {
    B subOb = new B();
    subOb.show(); // This calls show() in B
  }
}

Abstract Classes and Interfaces
Abstract Classes
[cite_start]An abstract class is a class declared with the abstract keyword that cannot be instantiated (you can't create an object of it directly). [cite_start]It can have a mix of abstract methods (without implementation) and non-abstract methods (with a body).
 * [cite_start]Abstract Method: A method with the abstract keyword and no body. [cite_start]Subclasses that extend an abstract class must provide an implementation for all its abstract methods, or they must also be declared abstract.
<!-- end list -->
abstract class Shape {
  abstract void draw(); // Abstract method
}

class Circle extends Shape {
  void draw() {
    System.out.println("drawing circle");
  }
}

public class TestAbstraction {
  public static void main(String args[]) {
    Shape s = new Circle(); // You can't do `new Shape()`
    s.draw(); // Output: drawing circle
  }
}

Interfaces
[cite_start]An interface is a blueprint of a class that can contain only static constants and abstract methods. [cite_start]It provides a mechanism for achieving total abstraction and simulating multiple inheritance.
 * [cite_start]All methods in an interface are implicitly public and abstract.
 * [cite_start]All variables in an interface are implicitly public, static, and final.
 * [cite_start]A class uses the implements keyword to use an interface and must provide an implementation for all its methods.
<!-- end list -->
interface Drawable {
  void draw();
}

class Circle implements Drawable {
  public void draw() {
    System.out.println("drawing circle");
  }
}

Exception Handling
[cite_start]An exception is a problem that occurs during program execution, disrupting the normal flow.
 * [cite_start]Errors vs. Exceptions: Errors indicate serious, abnormal conditions that a program shouldn't try to handle (e.g., memory errors). [cite_start]Exceptions are conditions within the code that a developer can handle.
 * Keywords:
   * [cite_start]try: Encloses the "protected code" that might throw an exception.
   * [cite_start]catch: Catches and handles the exception thrown by the try block.
   * finally: A block of code that always executes, regardless of whether an exception occurred or was handled. [cite_start]It's used for cleanup (e.g., closing a connection).
   * [cite_start]throw: Used to explicitly throw an exception.
   * [cite_start]throws: Declares that a method might throw an exception, postponing the handling to the calling method.
<!-- end list -->
public class ExceptionDemo {
  public static void main(String args[]) {
    try {
      int d = 0;
      int a = 42 / d; // This line throws an ArithmeticException
      System.out.println("This won't be printed.");
    } catch (ArithmeticException e) {
      System.out.println("Division by zero.");
    } finally {
      System.out.println("This always executes.");
    }
  }
}
// Output:
// Division by zero.
// This always executes.

I/O Streams
[cite_start]Java uses streams for input and output operations, which are a sequence of data. [cite_start]The java.io package contains all the necessary classes.
 * [cite_start]Byte Streams: Used for reading and writing 8-bit bytes (e.g., FileInputStream, FileOutputStream).
 * [cite_start]Character Streams: Used for reading and writing 16-bit Unicode characters (e.g., FileReader, FileWriter).
InputStream and OutputStream
 * [cite_start]InputStream: Reads data from a source. [cite_start]It's an abstract class and defines methods like read(), available(), and close().
 * [cite_start]OutputStream: Writes data to a destination. [cite_start]It's an abstract class and defines methods like write(), flush(), and close().
Buffered Streams
[cite_start]Buffered streams, like BufferedInputStream and BufferedOutputStream, use an internal buffer to make I/O operations more efficient by reducing the number of times data is accessed from the underlying source.
import java.io.*;

public class BufferedOutputStreamExample {
  public static void main(String args[]) throws Exception {
    FileOutputStream fout = new FileOutputStream("D:\\testout.txt");
    BufferedOutputStream bout = new BufferedOutputStream(fout);
    String s = "Welcome to cse department";
    byte b[] = s.getBytes();
    bout.write(b);
    bout.flush();
    bout.close();
    fout.close();
    System.out.println("Success...");
  }
}

These notes cover the fundamental concepts and code examples for both units. Remember to study the differences between related concepts, like method overloading vs. overriding, and classes vs. interfaces, as these are common exam questions. Good luck! ✍️
