# Comprehensive OOPS Study Notes - Units 1 & 2

## UNIT I: PARADIGMS & BASIC CONSTRUCTS

### 1. Object-Oriented Programming (OOP) Concepts

#### **Objects**
An object is a real-world entity with **state** and **behavior**. Objects have:
- **State**: Represented by attributes/data
- **Behavior**: Represented by methods/functions
- **Identity**: Unique identification in memory

#### **Classes**
A class is a **blueprint** or **template** for creating objects. It defines the structure and behavior that objects will have.

```java
class Dog {
    // Attributes (State)
    String name;
    int age;
    
    // Method (Behavior)
    void bark() {
        System.out.println(name + " is barking!");
    }
}
```

#### **Key OOP Principles**

**1. Encapsulation**
- Wrapping data and methods together in a single unit (class)
- Data hiding using access modifiers

```java
class Person {
    private String name;  // Private data
    private int age;
    
    // Public methods to access private data
    public void setName(String name) {
        this.name = name;
    }
    
    public String getName() {
        return name;
    }
}
```

**2. Inheritance**
- Acquiring properties and behaviors from parent class
- Promotes code reusability
- Types: Single, Multilevel, Hierarchical

```java
// Parent class
class Animal {
    void eat() {
        System.out.println("Animal is eating");
    }
}

// Child class
class Dog extends Animal {
    void bark() {
        System.out.println("Dog is barking");
    }
}
```

**3. Polymorphism**
- Same method behaving differently in different contexts
- **Method Overloading** (Compile-time)
- **Method Overriding** (Runtime)

```java
// Method Overloading
class Calculator {
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
}

// Method Overriding
class Animal {
    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}
```

**4. Abstraction**
- Hiding implementation details, showing only essential features
- Achieved through abstract classes and interfaces

```java
abstract class Shape {
    abstract void draw();  // Abstract method
    
    void display() {       // Concrete method
        System.out.println("Displaying shape");
    }
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing circle");
    }
}
```

### 2. Java Environment

#### **JVM (Java Virtual Machine)**
- Abstract machine providing runtime environment
- Platform-dependent implementation
- Loads, verifies, and executes bytecode

#### **JRE (Java Runtime Environment)**
- Set of software tools for running Java applications
- Contains JVM + libraries
- Implementation of JVM

#### **JDK (Java Development Kit)**
- Software development environment
- Contains JRE + development tools (javac, java, javadoc)

### 3. Java Programming Structures

#### **Basic Program Structure**
```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

#### **Class Definition**
```java
class Box {
    // Instance variables
    double width, height, depth;
    
    // Method
    double volume() {
        return width * height * depth;
    }
}
```

#### **Creating and Using Objects**
```java
public class BoxDemo {
    public static void main(String[] args) {
        // Creating objects
        Box myBox = new Box();
        
        // Setting values
        myBox.width = 10;
        myBox.height = 20;
        myBox.depth = 15;
        
        // Using methods
        double vol = myBox.volume();
        System.out.println("Volume: " + vol);
    }
}
```

### 4. Methods in Java

#### **Method Structure**
```java
returnType methodName(parameters) {
    // Method body
    return value;  // if returnType is not void
}
```

#### **Method Examples**
```java
class Rectangle {
    double length, width;
    
    // Method with no parameters
    void display() {
        System.out.println("Length: " + length + ", Width: " + width);
    }
    
    // Method with parameters
    void setDimensions(double l, double w) {
        length = l;
        width = w;
    }
    
    // Method returning value
    double calculateArea() {
        return length * width;
    }
}
```

#### **Method Overloading**
```java
class MathOperations {
    int multiply(int a, int b) {
        return a * b;
    }
    
    int multiply(int a, int b, int c) {
        return a * b * c;
    }
    
    double multiply(double a, double b) {
        return a * b;
    }
}
```

### 5. Constructors

#### **Default Constructor**
```java
class Student {
    String name;
    int age;
    
    // Default constructor
    Student() {
        name = "Unknown";
        age = 0;
        System.out.println("Default constructor called");
    }
}
```

#### **Parameterized Constructor**
```java
class Student {
    String name;
    int age;
    
    // Parameterized constructor
    Student(String n, int a) {
        name = n;
        age = a;
    }
}
```

#### **Constructor Overloading**
```java
class Box {
    double width, height, depth;
    
    // Default constructor
    Box() {
        width = height = depth = 0;
    }
    
    // Parameterized constructor
    Box(double w, double h, double d) {
        width = w;
        height = h;
        depth = d;
    }
    
    // Constructor for cube
    Box(double side) {
        width = height = depth = side;
    }
}
```

### 6. Access Modifiers

| Modifier  | Within Class | Within Package | Outside Package (Subclass) | Outside Package |
|-----------|--------------|----------------|----------------------------|-----------------|
| private   | Yes          | No             | No                         | No              |
| default   | Yes          | Yes            | No                         | No              |
| protected | Yes          | Yes            | Yes                        | No              |
| public    | Yes          | Yes            | Yes                        | Yes             |

```java
class AccessExample {
    private int privateVar = 1;      // Only within class
    int defaultVar = 2;              // Within package
    protected int protectedVar = 3;  // Within package + subclasses
    public int publicVar = 4;        // Everywhere
    
    private void privateMethod() {
        System.out.println("Private method");
    }
    
    public void publicMethod() {
        System.out.println("Public method");
    }
}
```

### 7. Static Members

#### **Static Variables**
```java
class Counter {
    static int count = 0;  // Shared by all objects
    int id;
    
    Counter() {
        count++;
        id = count;
    }
    
    static void displayCount() {
        System.out.println("Total objects: " + count);
    }
}
```

#### **Static Methods**
```java
class MathUtils {
    static int add(int a, int b) {
        return a + b;
    }
    
    static double calculateArea(double radius) {
        return 3.14159 * radius * radius;
    }
}

// Usage: MathUtils.add(5, 3);
```

#### **Static Blocks**
```java
class InitializationExample {
    static int value;
    
    static {
        System.out.println("Static block executed");
        value = 100;
    }
    
    public static void main(String[] args) {
        System.out.println("Value: " + value);
    }
}
```

### 8. this Keyword

```java
class Employee {
    String name;
    int salary;
    
    Employee(String name, int salary) {
        this.name = name;      // Refers to instance variable
        this.salary = salary;
    }
    
    void display() {
        this.showDetails();    // Calls method of current object
    }
    
    void showDetails() {
        System.out.println("Name: " + name + ", Salary: " + salary);
    }
}
```

### 9. finalize() Method

```java
class ResourceManager {
    ResourceManager() {
        System.out.println("Resource allocated");
    }
    
    @Override
    protected void finalize() throws Throwable {
        try {
            System.out.println("Resource being cleaned up");
            // Cleanup code here
        } finally {
            super.finalize();
        }
    }
}

// Note: finalize() is deprecated in modern Java
// Use try-with-resources instead
```

---

## UNIT II: EXCEPTION HANDLING & STREAMS

### 1. Arrays

#### **One-Dimensional Arrays**
```java
class ArrayExample {
    public static void main(String[] args) {
        // Declaration and initialization
        int[] numbers = new int[5];
        int[] values = {10, 20, 30, 40, 50};
        
        // Accessing elements
        numbers[0] = 100;
        System.out.println("First element: " + values[0]);
        
        // Array length
        System.out.println("Array length: " + values.length);
        
        // Iterating through array
        for (int i = 0; i < values.length; i++) {
            System.out.println(values[i]);
        }
    }
}
```

#### **Multi-Dimensional Arrays**
```java
class TwoDArrayExample {
    public static void main(String[] args) {
        // 2D array declaration
        int[][] matrix = new int[3][4];
        int[][] values = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        
        // Accessing elements
        matrix[0][0] = 10;
        System.out.println("Element at [1][2]: " + values[1][2]);
        
        // Iterating through 2D array
        for (int i = 0; i < values.length; i++) {
            for (int j = 0; j < values[i].length; j++) {
                System.out.print(values[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

#### **Passing Arrays to Methods**
```java
class ArrayMethods {
    static void printArray(int[] arr) {
        for (int element : arr) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
    
    static int findMin(int[] arr) {
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
    
    public static void main(String[] args) {
        int[] numbers = {64, 34, 25, 12, 22};
        printArray(numbers);
        System.out.println("Minimum: " + findMin(numbers));
    }
}
```

### 2. Strings

#### **String Class**
```java
class StringExample {
    public static void main(String[] args) {
        // String creation
        String str1 = "Hello";           // String literal
        String str2 = new String("World"); // Using new keyword
        
        // String operations
        System.out.println("Length: " + str1.length());
        System.out.println("Uppercase: " + str1.toUpperCase());
        System.out.println("Concatenation: " + str1.concat(" " + str2));
        System.out.println("Character at index 1: " + str1.charAt(1));
        System.out.println("Substring: " + str1.substring(1, 4));
        
        // String comparison
        String str3 = "Hello";
        System.out.println("str1 == str3: " + (str1 == str3));         // true (same reference)
        System.out.println("str1.equals(str2): " + str1.equals("Hello")); // true (content comparison)
    }
}
```

#### **StringBuffer Class**
```java
class StringBufferExample {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Hello");
        
        // StringBuffer operations (mutable)
        sb.append(" World");
        System.out.println("After append: " + sb);
        
        sb.insert(6, "Beautiful ");
        System.out.println("After insert: " + sb);
        
        sb.replace(6, 15, "Amazing");
        System.out.println("After replace: " + sb);
        
        sb.delete(6, 13);
        System.out.println("After delete: " + sb);
        
        sb.reverse();
        System.out.println("After reverse: " + sb);
        
        System.out.println("Capacity: " + sb.capacity());
    }
}
```

#### **String vs StringBuffer**
```java
class StringComparison {
    public static void main(String[] args) {
        // String (Immutable)
        String str = "Hello";
        str = str + " World";  // Creates new string object
        
        // StringBuffer (Mutable)
        StringBuffer sb = new StringBuffer("Hello");
        sb.append(" World");   // Modifies existing object
        
        System.out.println("String: " + str);
        System.out.println("StringBuffer: " + sb);
    }
}
```

### 3. Packages

#### **Creating a Package**
```java
// File: mypackage/Student.java
package mypackage;

public class Student {
    private int rollNo;
    private String name;
    
    public Student(int rollNo, String name) {
        this.rollNo = rollNo;
        this.name = name;
    }
    
    public void displayInfo() {
        System.out.println("Roll No: " + rollNo + ", Name: " + name);
    }
}
```

#### **Using Packages**
```java
// File: TestPackage.java
import mypackage.Student;  // Import specific class
// import mypackage.*;     // Import all classes from package

public class TestPackage {
    public static void main(String[] args) {
        Student student = new Student(101, "John");
        student.displayInfo();
    }
}
```

### 4. Inheritance

#### **Single Inheritance**
```java
class Vehicle {
    protected String brand;
    protected int maxSpeed;
    
    public Vehicle(String brand, int maxSpeed) {
        this.brand = brand;
        this.maxSpeed = maxSpeed;
    }
    
    public void displayInfo() {
        System.out.println("Brand: " + brand + ", Max Speed: " + maxSpeed);
    }
}

class Car extends Vehicle {
    private int doors;
    
    public Car(String brand, int maxSpeed, int doors) {
        super(brand, maxSpeed);  // Call parent constructor
        this.doors = doors;
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();  // Call parent method
        System.out.println("Doors: " + doors);
    }
}
```

#### **Multilevel Inheritance**
```java
class Animal {
    void eat() {
        System.out.println("Animal eats food");
    }
}

class Mammal extends Animal {
    void walk() {
        System.out.println("Mammal walks");
    }
}

class Dog extends Mammal {
    void bark() {
        System.out.println("Dog barks");
    }
}
```

#### **Hierarchical Inheritance**
```java
class Shape {
    protected double area;
    
    void displayArea() {
        System.out.println("Area: " + area);
    }
}

class Rectangle extends Shape {
    void calculateArea(double length, double width) {
        area = length * width;
    }
}

class Circle extends Shape {
    void calculateArea(double radius) {
        area = 3.14159 * radius * radius;
    }
}
```

### 5. super Keyword

```java
class Parent {
    protected int value = 100;
    
    Parent() {
        System.out.println("Parent constructor called");
    }
    
    Parent(int value) {
        this.value = value;
        System.out.println("Parent parameterized constructor");
    }
    
    void display() {
        System.out.println("Parent display method");
    }
}

class Child extends Parent {
    private int value = 200;
    
    Child() {
        super(500);  // Call parent constructor
        System.out.println("Child constructor called");
    }
    
    void display() {
        super.display();  // Call parent method
        System.out.println("Parent value: " + super.value);  // Access parent variable
        System.out.println("Child value: " + this.value);
    }
}
```

### 6. Method Overriding and Dynamic Method Dispatch

```java
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Cat meows");
    }
}

class DynamicMethodDispatch {
    public static void main(String[] args) {
        Animal animal;  // Reference variable
        
        animal = new Dog();
        animal.makeSound();  // Calls Dog's makeSound()
        
        animal = new Cat();
        animal.makeSound();  // Calls Cat's makeSound()
    }
}
```

### 7. Abstract Classes

```java
abstract class Shape {
    protected String color;
    
    public Shape(String color) {
        this.color = color;
    }
    
    // Abstract method (must be implemented by subclasses)
    abstract double calculateArea();
    
    // Concrete method
    public void displayColor() {
        System.out.println("Color: " + color);
    }
}

class Circle extends Shape {
    private double radius;
    
    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    
    @Override
    double calculateArea() {
        return 3.14159 * radius * radius;
    }
}

class Rectangle extends Shape {
    private double length, width;
    
    public Rectangle(String color, double length, double width) {
        super(color);
        this.length = length;
        this.width = width;
    }
    
    @Override
    double calculateArea() {
        return length * width;
    }
}
```

### 8. final Keyword

```java
// final class - cannot be inherited
final class Constants {
    public static final int MAX_VALUE = 100;  // final variable
    
    // final method - cannot be overridden
    public final void display() {
        System.out.println("This method cannot be overridden");
    }
}

class FinalExample {
    final int value = 50;  // final instance variable
    
    void testFinal() {
        final int localVar = 10;  // final local variable
        // localVar = 20;  // Compilation error
        System.out.println("Final local variable: " + localVar);
    }
}
```

### 9. Exception Handling

#### **Basic Exception Handling**
```java
class ExceptionHandlingExample {
    public static void main(String[] args) {
        try {
            int[] numbers = {1, 2, 3, 4, 5};
            int result = numbers[10] / 0;  // This will throw exceptions
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index out of bounds: " + e.getMessage());
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("General exception: " + e.getMessage());
        } finally {
            System.out.println("Finally block always executes");
        }
        
        System.out.println("Program continues...");
    }
}
```

#### **Custom Exception**
```java
class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

class Person {
    private String name;
    private int age;
    
    public void setAge(int age) throws InvalidAgeException {
        if (age < 0 || age > 150) {
            throw new InvalidAgeException("Invalid age: " + age);
        }
        this.age = age;
    }
    
    public static void main(String[] args) {
        Person person = new Person();
        try {
            person.setAge(-5);
        } catch (InvalidAgeException e) {
            System.out.println("Exception caught: " + e.getMessage());
        }
    }
}
```

#### **throws and throw**
```java
class ThrowExample {
    static void validateAge(int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Age must be 18 or above");
        }
        System.out.println("Valid age: " + age);
    }
    
    public static void main(String[] args) {
        try {
            validateAge(15);
        } catch (InvalidAgeException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

### 10. Interfaces

#### **Basic Interface**
```java
interface Drawable {
    int MAX_SIZE = 100;  // public static final by default
    
    void draw();  // public abstract by default
    void resize(int size);
}

interface Colorable {

