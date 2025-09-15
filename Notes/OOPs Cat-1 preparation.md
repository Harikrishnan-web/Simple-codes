# Comprehensive OOPS Study Notes - Units 1 & 2

## UNIT I: PARADIGMS & BASIC CONSTRUCTS

### 1. Object-Oriented Programming (OOP) Concepts

#### **Objects**
**What is an Object?**
An object is a real-world entity that exists in your program. Think of it like a physical item - a car, a book, or a person. In programming, objects represent these entities with specific characteristics and abilities.

**Key Components of Objects:**
- **State**: What the object knows (its data/attributes). For a car: color, model, speed
- **Behavior**: What the object can do (its methods/functions). For a car: start(), stop(), accelerate()
- **Identity**: Each object has a unique memory location, even if two objects have identical data

**Why Objects Matter:**
Objects make code more organized and closer to how we think about real-world problems. Instead of having scattered functions and variables, everything related to a "car" is bundled together.

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

#### **Understanding Java's Architecture**
**The Problem Java Solves:**
Before Java, programs written for Windows couldn't run on Mac or Linux. Java solved this with "Write Once, Run Anywhere" (WORA) principle.

**How Java Works:**
1. **Source Code (.java)** → Written by programmer
2. **Compiler (javac)** → Converts to bytecode
3. **Bytecode (.class)** → Platform-independent intermediate code
4. **JVM** → Converts bytecode to machine code for specific platform

#### **JVM (Java Virtual Machine)**
**What is JVM?**
JVM is like a translator that understands both Java bytecode and your computer's language. It sits between your Java program and your operating system.

**Key Functions:**
- **Loads** bytecode files (.class)
- **Verifies** code for security issues
- **Executes** bytecode by converting to machine code
- **Memory Management** through garbage collection

**Important:** JVM is platform-dependent (different for Windows, Mac, Linux), but Java code is platform-independent.

```java
// This same code runs on any platform with JVM
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from any platform!");
    }
}
```

#### **JRE (Java Runtime Environment)**
**What is JRE?**
JRE is everything you need to RUN Java programs. It includes JVM plus libraries and other files.

**Contains:**
- JVM (the engine)
- Core libraries (pre-written code for common tasks)
- Supporting files

**When to Use:** Install JRE if you only want to run Java programs, not write them.

#### **JDK (Java Development Kit)**
**What is JDK?**
JDK is everything you need to DEVELOP Java programs. It includes JRE plus development tools.

**Contains:**
- JRE (so you can run programs)
- Compiler (javac - converts .java to .class)
- Debugger (finds errors in code)
- Documentation tools (javadoc)
- Archive tool (jar)

**When to Use:** Install JDK if you want to write Java programs.

**Memory Diagram:**
```
JDK = JRE + Development Tools
JRE = JVM + Libraries  
JVM = Core execution engine
```

### 3. Java Programming Structures

#### **Basic Program Structure**
**Understanding the Anatomy of a Java Program:**

```java
class HelloWorld {                          // Class declaration
    public static void main(String[] args) {  // Main method
        System.out.println("Hello, World!");  // Statement
    }
}
```

**Line-by-Line Breakdown:**
- `class HelloWorld` - Every Java program needs at least one class. The class name should match the filename.
- `public` - Access modifier meaning this method can be called from anywhere
- `static` - Method belongs to class, not object. Main must be static so JVM can call it without creating objects
- `void` - Method doesn't return any value
- `main` - Special method name that JVM looks for to start program execution
- `String[] args` - Command line arguments (if any)
- `System.out.println()` - Prints text to console

**Compilation and Execution Process:**
```bash
# Compile: Creates HelloWorld.class file
javac HelloWorld.java

# Execute: JVM looks for main method and starts execution
java HelloWorld
```

#### **Class Definition - The Blueprint**
**What Makes a Class:**

```java
class Box {
    // Instance variables (attributes) - each object gets its own copy
    double width, height, depth;
    
    // Method - defines what objects can do
    double volume() {
        return width * height * depth;
    }
}
```

**Key Concepts:**
- **Class vs Object**: Class is blueprint, object is actual instance
- **Instance Variables**: Each object has its own copy of these variables
- **Methods**: Functions that belong to the class
- **Memory**: Class definition doesn't use memory, objects do

#### **Creating and Using Objects - Bringing Classes to Life**
**The Object Creation Process:**

```java
public class BoxDemo {
    public static void main(String[] args) {
        // Step 1: Declare reference variable
        Box myBox;
        
        // Step 2: Create object and assign reference
        myBox = new Box();
        
        // Or combine both steps:
        Box myBox2 = new Box();
        
        // Step 3: Use the object
        myBox.width = 10;   // Set attribute
        myBox.height = 20;
        myBox.depth = 15;
        
        // Step 4: Call methods
        double vol = myBox.volume();
        System.out.println("Volume: " + vol);
    }
}
```

**Understanding Object References:**
- `Box myBox` - Creates a reference (like a remote control)
- `new Box()` - Creates actual object in memory
- Reference points to object's memory location
- Multiple references can point to same object

**Memory Visualization:**
```
Stack (Local Variables)    Heap (Objects)
┌──────────────┐          ┌─────────────────┐
│ myBox ────────┼─────────→│ Box Object      │
└──────────────┘          │ width: 10       │
                          │ height: 20      │
                          │ depth: 15       │
                          └─────────────────┘
```

### 4. Methods in Java

#### **Understanding Methods - The Actions Objects Can Perform**
**What is a Method?**
A method is a block of code that performs a specific task. Think of it as a mini-program within your class that can be called whenever needed.

**Method Structure Breakdown:**
```java
returnType methodName(parameters) {
    // Method body - the actual code
    return value;  // if returnType is not void
}
```

**Components Explained:**
- **Return Type**: What kind of data the method gives back (int, String, void for nothing)
- **Method Name**: What you call the method (use descriptive names)
- **Parameters**: Input data the method needs (like ingredients for a recipe)
- **Method Body**: The actual instructions
- **Return Statement**: Sends result back to caller (if not void)

#### **Method Examples with Explanations**
```java
class Rectangle {
    double length, width;
    
    // Method with no parameters and no return value
    void display() {
        System.out.println("Rectangle: " + length + " x " + width);
    }
    
    // Method with parameters (input data needed)
    void setDimensions(double l, double w) {
        // 'l' and 'w' are local variables that receive input values
        length = l;  // Store input in instance variable
        width = w;
    }
    
    // Method that returns a value (calculates and gives back result)
    double calculateArea() {
        double area = length * width;  // Local calculation
        return area;  // Send result back to caller
    }
    
    // Method that both takes input and returns output
    double calculatePerimeter(double extraLength) {
        return 2 * (length + width + extraLength);
    }
}
```

**How Methods Work:**
1. **Method Call**: `rectangle.calculateArea()` - program jumps to method
2. **Execution**: Method code runs with access to object's data
3. **Return**: Method finishes, program returns to where it was called
4. **Result**: If method returns value, caller receives it

#### **Method Overloading - Same Name, Different Signatures**
**What is Method Overloading?**
Having multiple methods with the same name but different parameters. It's like having different versions of the same action.

**Rules for Overloading:**
- Same method name
- Different parameter list (number, type, or order)
- Return type can be same or different
- Must be in same class

```java
class MathOperations {
    // Version 1: Two integers
    int multiply(int a, int b) {
        System.out.println("Multiplying two integers");
        return a * b;
    }
    
    // Version 2: Three integers (different number of parameters)
    int multiply(int a, int b, int c) {
        System.out.println("Multiplying three integers");
        return a * b * c;
    }
    
    // Version 3: Two doubles (different parameter types)
    double multiply(double a, double b) {
        System.out.println("Multiplying two doubles");
        return a * b;
    }
    
    // Version 4: Different order of parameter types
    double multiply(int a, double b) {
        System.out.println("Multiplying int and double");
        return a * b;
    }
}

// Usage - compiler automatically chooses correct version
MathOperations math = new MathOperations();
math.multiply(5, 3);        // Calls version 1
math.multiply(5, 3, 2);     // Calls version 2
math.multiply(5.5, 3.2);    // Calls version 3
math.multiply(5, 3.2);      // Calls version 4
```

**Why Use Method Overloading?**
- **Convenience**: Same logical operation, different input types
- **Readability**: Don't need different names like addInt, addDouble
- **Flexibility**: Users can call with different data types

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
import mypackage.Student;  /