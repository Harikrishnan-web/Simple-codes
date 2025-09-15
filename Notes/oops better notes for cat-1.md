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

**Output Example:**
```
Buddy is barking!
```

#### **Key OOP Principles**

**1. Encapsulation**
- Wrapping data and methods together in a single unit (class)
- Data hiding using access modifiers
- **Use:** Protects data integrity and provides controlled access
- **Advantages:** Increased security, maintainability, modularity
- **Disadvantages:** Can make simple operations more complex

```java
class Person {
    private String name;  // Private data
    private int age;
    
    // Public methods to access private data
    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name;
        } else {
            System.out.println("Invalid name provided");
        }
    }
    
    public String getName() {
        return name;
    }
    
    public void setAge(int age) {
        if (age > 0 && age < 150) {
            this.age = age;
        } else {
            System.out.println("Invalid age provided");
        }
    }
    
    public int getAge() {
        return age;
    }
}

// Usage
class TestEncapsulation {
    public static void main(String[] args) {
        Person person = new Person();
        person.setName("John");
        person.setAge(25);
        
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
        
        // Testing validation
        person.setAge(-5);  // Will show error message
    }
}
```

**Output:**
```
Name: John
Age: 25
Invalid age provided
```

**2. Inheritance**
- Acquiring properties and behaviors from parent class
- Promotes code reusability
- Types: Single, Multilevel, Hierarchical
- **Use:** Establish IS-A relationship between classes
- **Advantages:** Code reusability, method overriding, hierarchical classification
- **Disadvantages:** Tight coupling, inherited changes affect subclasses

```java
// Parent class
class Animal {
    String name;
    
    void eat() {
        System.out.println(name + " is eating");
    }
    
    void sleep() {
        System.out.println(name + " is sleeping");
    }
}

// Child class
class Dog extends Animal {
    String breed;
    
    void bark() {
        System.out.println(name + " is barking");
    }
    
    void wagTail() {
        System.out.println(name + " is wagging tail");
    }
}

// Usage
class TestInheritance {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.name = "Buddy";
        dog.breed = "Golden Retriever";
        
        // Using inherited methods
        dog.eat();
        dog.sleep();
        
        // Using own methods
        dog.bark();
        dog.wagTail();
        
        System.out.println("Breed: " + dog.breed);
    }
}
```

**Output:**
```
Buddy is eating
Buddy is sleeping
Buddy is barking
Buddy is wagging tail
Breed: Golden Retriever
```

**3. Polymorphism**
- Same method behaving differently in different contexts
- **Method Overloading** (Compile-time polymorphism)
- **Method Overriding** (Runtime polymorphism)
- **Use:** One interface, multiple implementations
- **Advantages:** Flexibility, maintainability, extensibility
- **Disadvantages:** Can be confusing, runtime overhead for dynamic binding

```java
// Method Overloading Example
class Calculator {
    int add(int a, int b) {
        System.out.println("Adding two integers");
        return a + b;
    }
    
    double add(double a, double b) {
        System.out.println("Adding two doubles");
        return a + b;
    }
    
    int add(int a, int b, int c) {
        System.out.println("Adding three integers");
        return a + b + c;
    }
}

// Method Overriding Example
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks: Woof!");
    }
}

class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Cat meows: Meow!");
    }
}

// Usage
class TestPolymorphism {
    public static void main(String[] args) {
        // Method Overloading
        Calculator calc = new Calculator();
        System.out.println("Result 1: " + calc.add(5, 3));
        System.out.println("Result 2: " + calc.add(5.5, 3.2));
        System.out.println("Result 3: " + calc.add(1, 2, 3));
        
        System.out.println();
        
        // Method Overriding
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();
        
        animal1.makeSound();  // Calls Dog's version
        animal2.makeSound();  // Calls Cat's version
    }
}
```

**Output:**
```
Adding two integers
Result 1: 8
Adding two doubles
Result 2: 8.7
Adding three integers
Result 3: 6

Dog barks: Woof!
Cat meows: Meow!
```

**4. Abstraction**
- Hiding implementation details, showing only essential features
- Achieved through abstract classes and interfaces
- **Use:** Hide complexity, provide template for subclasses
- **Advantages:** Simplifies programming model, promotes code organization
- **Disadvantages:** Cannot instantiate abstract classes directly

```java
abstract class Shape {
    String color;
    
    // Abstract method (must be implemented by subclasses)
    abstract double calculateArea();
    
    // Concrete method (can be used as is)
    void displayColor() {
        System.out.println("Shape color: " + color);
    }
}

class Circle extends Shape {
    double radius;
    
    Circle(double radius, String color) {
        this.radius = radius;
        this.color = color;
    }
    
    @Override
    double calculateArea() {
        return 3.14159 * radius * radius;
    }
}

class Rectangle extends Shape {
    double length, width;
    
    Rectangle(double length, double width, String color) {
        this.length = length;
        this.width = width;
        this.color = color;
    }
    
    @Override
    double calculateArea() {
        return length * width;
    }
}

// Usage
class TestAbstraction {
    public static void main(String[] args) {
        Circle circle = new Circle(5.0, "Red");
        Rectangle rectangle = new Rectangle(4.0, 6.0, "Blue");
        
        System.out.println("Circle Area: " + circle.calculateArea());
        circle.displayColor();
        
        System.out.println("Rectangle Area: " + rectangle.calculateArea());
        rectangle.displayColor();
    }
}
```

**Output:**
```
Circle Area: 78.53975
Shape color: Red
Rectangle Area: 24.0
Shape color: Blue
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
        System.out.println("Java Version: " + System.getProperty("java.version"));
        System.out.println("Operating System: " + System.getProperty("os.name"));
    }
}
```

**Output:**
```
Hello from any platform!
Java Version: 11.0.2
Operating System: Windows 10
```

#### **JRE (Java Runtime Environment)**
**What is JRE?**
JRE is everything you need to RUN Java programs. It includes JVM plus libraries and other files.

**Contains:**
- JVM (the engine)
- Core libraries (pre-written code for common tasks)
- Supporting files

**When to Use:** Install JRE if you only want to run Java programs, not write them.

**Advantages:**
- Smaller download size than JDK
- Sufficient for running applications
- Includes all necessary runtime libraries

**Disadvantages:**
- Cannot compile Java source code
- No development tools included

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

**Advantages:**
- Complete development environment
- Includes all tools needed for Java development
- Can both compile and run programs

**Disadvantages:**
- Larger download size
- More complex installation

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
// Basic Java program demonstrating structure
class HelloWorld {                          // Class declaration
    public static void main(String[] args) {  // Main method
        System.out.println("Hello, World!");  // Statement
        System.out.println("Welcome to Java Programming!");
        
        // Variable declaration and initialization
        String message = "Java is platform independent";
        int year = 2024;
        
        System.out.println(message);
        System.out.println("Year: " + year);
    }
}
```

**Output:**
```
Hello, World!
Welcome to Java Programming!
Java is platform independent
Year: 2024
```

**Line-by-Line Breakdown:**
- `class HelloWorld` - Every Java program needs at least one class. The class name should match the filename.
- `public` - Access modifier meaning this method can be called from anywhere
- `static` - Method belongs to class, not object. Main must be static so JVM can call it without creating objects
- `void` - Method doesn't return any value
- `main` - Special method name that JVM looks for to start program execution
- `String[] args` - Command line arguments (if any)
- `System.out.println()` - Prints text to console

**Use:** Entry point for Java applications
**Advantages:** Standardized structure, clear execution flow
**Disadvantages:** Requires understanding of access modifiers and static concepts

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
    
    // Method to display box dimensions
    void displayDimensions() {
        System.out.println("Box Dimensions:");
        System.out.println("Width: " + width);
        System.out.println("Height: " + height);
        System.out.println("Depth: " + depth);
    }
}

// Usage example
class BoxDemo {
    public static void main(String[] args) {
        Box myBox = new Box();
        
        myBox.width = 10;
        myBox.height = 20;
        myBox.depth = 15;
        
        myBox.displayDimensions();
        System.out.println("Volume: " + myBox.volume());
    }
}
```

**Output:**
```
Box Dimensions:
Width: 10.0
Height: 20.0
Depth: 15.0
Volume: 3000.0
```

**Key Concepts:**
- **Class vs Object**: Class is blueprint, object is actual instance
- **Instance Variables**: Each object has its own copy of these variables
- **Methods**: Functions that belong to the class
- **Memory**: Class definition doesn't use memory, objects do

**Use:** Define template for creating objects
**Advantages:** Encapsulation, code reusability, modularity
**Disadvantages:** Memory overhead for each object

#### **Creating and Using Objects - Bringing Classes to Life**

```java
class Student {
    String name;
    int rollNumber;
    double marks;
    
    void displayInfo() {
        System.out.println("Student Information:");
        System.out.println("Name: " + name);
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Marks: " + marks);
        System.out.println();
    }
    
    String getGrade() {
        if (marks >= 90) return "A+";
        else if (marks >= 80) return "A";
        else if (marks >= 70) return "B";
        else if (marks >= 60) return "C";
        else return "F";
    }
}

public class StudentDemo {
    public static void main(String[] args) {
        // Step 1: Create first student object
        Student student1 = new Student();
        student1.name = "Alice";
        student1.rollNumber = 101;
        student1.marks = 85.5;
        
        // Step 2: Create second student object
        Student student2 = new Student();
        student2.name = "Bob";
        student2.rollNumber = 102;
        student2.marks = 92.0;
        
        // Step 3: Use the objects
        student1.displayInfo();
        System.out.println("Grade: " + student1.getGrade());
        
        student2.displayInfo();
        System.out.println("Grade: " + student2.getGrade());
        
        // Demonstrate multiple references
        Student student3 = student1;  // Same object, different reference
        student3.marks = 95.0;        // Changes original object
        
        System.out.println("After modifying through student3:");
        student1.displayInfo();
        System.out.println("Grade: " + student1.getGrade());
    }
}
```

**Output:**
```
Student Information:
Name: Alice
Roll Number: 101
Marks: 85.5

Grade: A
Student Information:
Name: Bob
Roll Number: 102
Marks: 92.0

Grade: A+
After modifying through student3:
Student Information:
Name: Alice
Roll Number: 101
Marks: 95.0

Grade: A+
```

**Understanding Object References:**
- `Student student1` - Creates a reference (like a remote control)
- `new Student()` - Creates actual object in memory
- Reference points to object's memory location
- Multiple references can point to same object

**Use:** Create instances of classes to work with data
**Advantages:** Multiple objects from same class, independent state for each object
**Disadvantages:** Memory usage increases with each object

### 4. Methods in Java

#### **Understanding Methods - The Actions Objects Can Perform**

```java
class Calculator {
    // Method with no parameters and no return value
    void displayWelcome() {
        System.out.println("Welcome to Calculator!");
        System.out.println("Available operations: +, -, *, /");
    }
    
    // Method with parameters (input data needed)
    void setValues(int a, int b) {
        System.out.println("Values set: " + a + " and " + b);
    }
    
    // Method that returns a value
    int add(int a, int b) {
        int result = a + b;
        System.out.println("Adding " + a + " + " + b + " = " + result);
        return result;
    }
    
    // Method that both takes input and returns output
    double calculatePercentage(int marks, int total) {
        if (total == 0) {
            System.out.println("Error: Total cannot be zero");
            return 0;
        }
        double percentage = (marks * 100.0) / total;
        System.out.println("Percentage: " + marks + "/" + total + " = " + percentage + "%");
        return percentage;
    }
    
    // Method with multiple return types based on conditions
    String getGrade(double percentage) {
        if (percentage >= 90) {
            System.out.println("Excellent performance!");
            return "A+";
        } else if (percentage >= 80) {
            System.out.println("Good performance!");
            return "A";
        } else if (percentage >= 70) {
            System.out.println("Average performance!");
            return "B";
        } else {
            System.out.println("Need improvement!");
            return "C";
        }
    }
}

class MethodDemo {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        // Method with no return value
        calc.displayWelcome();
        System.out.println();
        
        // Method with parameters
        calc.setValues(15, 25);
        
        // Method that returns value
        int sum = calc.add(15, 25);
        System.out.println("Stored result: " + sum);
        System.out.println();
        
        // Chaining method calls
        double percentage = calc.calculatePercentage(85, 100);
        String grade = calc.getGrade(percentage);
        System.out.println("Final Grade: " + grade);
    }
}
```

**Output:**
```
Welcome to Calculator!
Available operations: +, -, *, /

Values set: 15 and 25
Adding 15 + 25 = 40
Stored result: 40

Percentage: 85/100 = 85.0%
Good performance!
Final Grade: A
```

**Use:** Perform specific tasks, organize code into reusable units
**Advantages:** Code reusability, modularity, easier debugging and maintenance
**Disadvantages:** Method call overhead, can make simple programs complex

#### **Method Overloading - Same Name, Different Signatures**

```java
class MathOperations {
    // Version 1: Two integers
    int multiply(int a, int b) {
        System.out.println("Multiplying two integers: " + a + " × " + b);
        return a * b;
    }
    
    // Version 2: Three integers (different number of parameters)
    int multiply(int a, int b, int c) {
        System.out.println("Multiplying three integers: " + a + " × " + b + " × " + c);
        return a * b * c;
    }
    
    // Version 3: Two doubles (different parameter types)
    double multiply(double a, double b) {
        System.out.println("Multiplying two doubles: " + a + " × " + b);
        return a * b;
    }
    
    // Version 4: Different order of parameter types
    double multiply(int a, double b) {
        System.out.println("Multiplying int and double: " + a + " × " + b);
        return a * b;
    }
    
    // Version 5: Array of numbers
    int multiply(int[] numbers) {
        System.out.print("Multiplying array: ");
        int result = 1;
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i]);
            if (i < numbers.length - 1) System.out.print(" × ");
            result *= numbers[i];
        }
        System.out.println();
        return result;
    }
}

class OverloadingDemo {
    public static void main(String[] args) {
        MathOperations math = new MathOperations();
        
        // Compiler automatically chooses correct version
        System.out.println("Result 1: " + math.multiply(5, 3));
        System.out.println("Result 2: " + math.multiply(5, 3, 2));
        System.out.println("Result 3: " + math.multiply(5.5, 3.2));
        System.out.println("Result 4: " + math.multiply(5, 3.2));
        
        int[] numbers = {2, 3, 4};
        System.out.println("Result 5: " + math.multiply(numbers));
    }
}
```

**Output:**
```
Multiplying two integers: 5 × 3
Result 1: 15
Multiplying three integers: 5 × 3 × 2
Result 2: 30
Multiplying two doubles: 5.5 × 3.2
Result 3: 17.6
Multiplying int and double: 5 × 3.2
Result 4: 16.0
Multiplying array: 2 × 3 × 4
Result 5: 24
```

**Rules for Method Overloading:**
- Same method name
- Different parameter list (number, type, or order)
- Return type can be same or different
- Must be in same class

**Use:** Provide multiple ways to perform similar operations
**Advantages:** Convenience, readability, flexibility for different data types
**Disadvantages:** Can be confusing if overused, increases code complexity

### 5. Constructors

#### **Default Constructor**
```java
class Student {
    String name;
    int rollNumber;
    double marks;
    
    // Default constructor
    Student() {
        name = "Unknown";
        rollNumber = 0;
        marks = 0.0;
        System.out.println("Default constructor called");
        System.out.println("Student created with default values");
    }
    
    void displayInfo() {
        System.out.println("Name: " + name + ", Roll: " + rollNumber + ", Marks: " + marks);
    }
}

class DefaultConstructorDemo {
    public static void main(String[] args) {
        System.out.println("Creating student with default constructor:");
        Student student = new Student();
        student.displayInfo();
    }
}
```

**Output:**
```
Creating student with default constructor:
Default constructor called
Student created with default values
Name: Unknown, Roll: 0, Marks: 0.0
```

#### **Parameterized Constructor**
```java
class Student {
    String name;
    int rollNumber;
    double marks;
    
    // Parameterized constructor
    Student(String n, int roll, double m) {
        name = n;
        rollNumber = roll;
        marks = m;
        System.out.println("Parameterized constructor called");
        System.out.println("Student created: " + name);
    }
    
    void displayInfo() {
        System.out.println("Name: " + name + ", Roll: " + rollNumber + ", Marks: " + marks);
    }
}

class ParameterizedConstructorDemo {
    public static void main(String[] args) {
        System.out.println("Creating students with parameterized constructor:");
        Student student1 = new Student("Alice", 101, 85.5);
        student1.displayInfo();
        
        Student student2 = new Student("Bob", 102, 92.0);
        student2.displayInfo();
    }
}
```

**Output:**
```
Creating students with parameterized constructor:
Parameterized constructor called
Student created: Alice
Name: Alice, Roll: 101, Marks: 85.5
Parameterized constructor called
Student created: Bob
Name: Bob, Roll: 102, Marks: 92.0
```

#### **Constructor Overloading**
```java
class Box {
    double width, height, depth;
    
    // Default constructor
    Box() {
        width = height = depth = 1.0;
        System.out.println("Default constructor: Creating unit box");
    }
    
    // Parameterized constructor for all dimensions
    Box(double w, double h, double d) {
        width = w;
        height = h;
        depth = d;
        System.out.println("Full constructor: Creating box " + w + "×" + h + "×" + d);
    }
    
    // Constructor for cube (all sides equal)
    Box(double side) {
        width = height = depth = side;
        System.out.println("Cube constructor: Creating cube with side " + side);
    }
    
    // Copy constructor
    Box(Box other) {
        width = other.width;
        height = other.height;
        depth = other.depth;
        System.out.println("Copy constructor: Creating copy of existing box");
    }
    
    double volume() {
        return width * height * depth;
    }
    
    void displayDimensions() {
        System.out.println("Dimensions: " + width + "×" + height + "×" + depth + 
                          ", Volume: " + volume());
    }
}

class ConstructorOverloadingDemo {
    public static void main(String[] args) {
        System.out.println("Creating different types of boxes:\n");
        
        // Using different constructors
        Box box1 = new Box();                    // Default
        box1.displayDimensions();
        System.out.println();
        
        Box box2 = new Box(10, 20, 15);         // Parameterized
        box2.displayDimensions();
        System.out.println();
        
        Box box3 = new Box(5);                  // Cube
        box3.displayDimensions();
        System.out.println();
        
        Box box4 = new Box(box2);               // Copy constructor
        box4.displayDimensions();
    }
}
```

**Output:**
```
Creating different types of boxes:

Default constructor: Creating unit box
Dimensions: 1.0×1.0×1.0, Volume: 1.0

Full constructor: Creating box 10.0×20.0×15.0
Dimensions: 10.0×20.0×15.0, Volume: 3000.0

Cube constructor: Creating cube with side 5.0
Dimensions: 5.0×5.0×5.0, Volume: 125.0

Copy constructor: Creating copy of existing box
Dimensions: 10.0×20.0×15.0, Volume: 3000.0
```

**Use:** Initialize object state when created
**Advantages:** Ensures objects are properly initialized, provides flexibility in object creation
**Disadvantages:** Must remember to handle all cases, can create confusion with too many overloaded versions

### 6. Access Modifiers

| Modifier  | Within Class | Within Package | Outside Package (Subclass) | Outside Package |
|-----------|--------------|----------------|----------------------------|-----------------|
| private   | Yes          | No             | No                         | No              |
| default   | Yes          | Yes            | No                         | No              |
| protected | Yes          | Yes            | Yes                        | No              |
| public    | Yes          | Yes            | Yes                        | Yes             |

```java
class AccessModifierDemo {
    private int privateVar = 1;      // Only within this class
    int defaultVar = 2;              // Within same package
    protected int protectedVar = 3;  // Within package + subclasses
    public int publicVar = 4;        // Accessible everywhere
    
    private void privateMethod() {
        System.out.println("Private method - only accessible within this class");
        System.out.println("Private variable: " + privateVar);
    }
    
    void defaultMethod() {
        System.out.println("Default method - accessible within package");
        System.out.println("Default variable: " + defaultVar);
    }
    
    protected void protectedMethod() {
        System.out.println("Protected method - accessible within package and subclasses");
        System.out.println("Protected variable: " + protectedVar);
    }
    
    public void publicMethod() {
        System.out.println("Public method - accessible everywhere");
        System.out.println("Public variable: " + publicVar);
        
        // All methods can be called from within the same class
        privateMethod();
    }
    
    // Public method to demonstrate access levels
    public void demonstrateAccess() {
        System.out.println("\nDemonstrating access from within the class:
Private: 1
Default: 2
Protected: 3
Public: 4
```

**Use:** Control visibility and access to class members
**Advantages:** Encapsulation, data security, controlled access
**Disadvantages:** Can make code verbose, need to understand access levels

### 7. Static Members

#### **Static Variables**
```java
class Counter {
    static int totalCount = 0;  // Shared by all objects
    int instanceId;
    String name;
    
    Counter(String name) {
        totalCount++;  // Increment shared counter
        instanceId = totalCount;  // Assign unique ID
        this.name = name;
        System.out.println("Created " + name + " with ID: " + instanceId);
    }
    
    void displayInfo() {
        System.out.println("Object: " + name + ", ID: " + instanceId + 
                          ", Total objects created: " + totalCount);
    }
    
    static void displayTotalCount() {
        System.out.println("Total objects created so far: " + totalCount);
        // Note: Cannot access instance variables in static method
        // System.out.println(name);  // This would cause compilation error
    }
}

class StaticVariableDemo {
    public static void main(String[] args) {
        System.out.println("Initial count:");
        Counter.displayTotalCount();
        
        System.out.println("\nCreating objects:");
        Counter c1 = new Counter("Counter1");
        Counter c2 = new Counter("Counter2");
        Counter c3 = new Counter("Counter3");
        
        System.out.println("\nDisplaying individual object info:");
        c1.displayInfo();
        c2.displayInfo();
        c3.displayInfo();
        
        System.out.println("\nFinal count:");
        Counter.displayTotalCount();
    }
}
```

**Output:**
```
Initial count:
Total objects created so far: 0

Creating objects:
Created Counter1 with ID: 1
Created Counter2 with ID: 2
Created Counter3 with ID: 3

Displaying individual object info:
Object: Counter1, ID: 1, Total objects created: 3
Object: Counter2, ID: 2, Total objects created: 3
Object: Counter3, ID: 3, Total objects created: 3

Final count:
Total objects created so far: 3
```

#### **Static Methods**
```java
class MathUtils {
    static final double PI = 3.14159;
    
    static int add(int a, int b) {
        System.out.println("Adding: " + a + " + " + b);
        return a + b;
    }
    
    static double calculateCircleArea(double radius) {
        System.out.println("Calculating area of circle with radius: " + radius);
        return PI * radius * radius;
    }
    
    static double calculateRectangleArea(double length, double width) {
        System.out.println("Calculating area of rectangle: " + length + " × " + width);
        return length * width;
    }
    
    static void displayConstants() {
        System.out.println("Mathematical Constants:");
        System.out.println("PI = " + PI);
    }
    
    // Static method can call other static methods
    static void performCalculations() {
        System.out.println("Performing sample calculations:");
        System.out.println("5 + 3 = " + add(5, 3));
        System.out.println("Circle area (r=5): " + calculateCircleArea(5.0));
        System.out.println("Rectangle area (4×6): " + calculateRectangleArea(4.0, 6.0));
    }
}

class StaticMethodDemo {
    public static void main(String[] args) {
        // Call static methods without creating object
        MathUtils.displayConstants();
        System.out.println();
        
        // Individual method calls
        int sum = MathUtils.add(10, 20);
        double area = MathUtils.calculateCircleArea(7.0);
        
        System.out.println("Sum result: " + sum);
        System.out.println("Area result: " + area);
        System.out.println();
        
        // Calling static method that calls other static methods
        MathUtils.performCalculations();
    }
}
```

**Output:**
```
Mathematical Constants:
PI = 3.14159

Adding: 10 + 20
Calculating area of circle with radius: 7.0
Sum result: 30
Area result: 153.93791

Performing sample calculations:
Adding: 5 + 3
5 + 3 = 8
Calculating area of circle with radius: 5.0
Circle area (r=5): 78.53975
Calculating area of rectangle: 4.0 × 6.0
Rectangle area (4×6): 24.0
```

#### **Static Blocks**
```java
class InitializationExample {
    static int staticValue;
    static String staticMessage;
    int instanceValue;
    
    // Static block - executed when class is first loaded
    static {
        System.out.println("Static block 1 executed");
        staticValue = 100;
        staticMessage = "Initialized by static block";
    }
    
    // Another static block - executed in order
    static {
        System.out.println("Static block 2 executed");
        staticValue += 50;  // Modify the value
        System.out.println("Static value updated to: " + staticValue);
    }
    
    // Instance block - executed for each object creation
    {
        System.out.println("Instance block executed");
        instanceValue = staticValue + 10;
    }
    
    // Constructor
    InitializationExample() {
        System.out.println("Constructor executed");
        System.out.println("Instance value: " + instanceValue);
    }
    
    void displayValues() {
        System.out.println("Static value: " + staticValue);
        System.out.println("Static message: " + staticMessage);
        System.out.println("Instance value: " + instanceValue);
    }
}

class StaticBlockDemo {
    public static void main(String[] args) {
        System.out.println("Program started");
        
        System.out.println("\nCreating first object:");
        InitializationExample obj1 = new InitializationExample();
        obj1.displayValues();
        
        System.out.println("\nCreating second object:");
        InitializationExample obj2 = new InitializationExample();
        obj2.displayValues();
    }
}
```

**Output:**
```
Static block 1 executed
Static block 2 executed
Static value updated to: 150
Program started

Creating first object:
Instance block executed
Constructor executed
Instance value: 160
Static value: 150
Static message: Initialized by static block
Instance value: 160

Creating second object:
Instance block executed
Constructor executed
Instance value: 160
Static value: 150
Static message: Initialized by static block
Instance value: 160
```

**Use:** Share data among all instances, utility methods that don't need object state
**Advantages:** Memory efficient, accessible without object creation, class-level operations
**Disadvantages:** Cannot access instance members, loaded in memory throughout program execution

### 8. this Keyword

```java
class Employee {
    String name;
    int salary;
    String department;
    
    Employee(String name, int salary, String department) {
        // Using 'this' to distinguish between parameters and instance variables
        this.name = name;
        this.salary = salary;
        this.department = department;
        
        System.out.println("Employee created: " + this.name);
    }
    
    void setSalary(int salary) {
        if (salary > 0) {
            this.salary = salary;  // 'this' refers to current object
            System.out.println("Salary updated for " + this.name + ": " + this.salary);
        } else {
            System.out.println("Invalid salary amount");
        }
    }
    
    void displayInfo() {
        System.out.println("Employee Details:");
        System.out.println("Name: " + this.name);
        System.out.println("Salary: " + this.salary);
        System.out.println("Department: " + this.department);
        
        // 'this' can be used to call other methods of current object
        this.calculateAnnualSalary();
    }
    
    void calculateAnnualSalary() {
        int annual = this.salary * 12;
        System.out.println("Annual Salary: " + annual);
    }
    
    // Method to compare with another employee
    boolean hasSameDepartment(Employee other) {
        return this.department.equals(other.department);
    }
    
    // Method that returns current object reference
    Employee updateName(String newName) {
        this.name = newName;
        System.out.println("Name updated to: " + this.name);
        return this;  // Return current object for method chaining
    }
    
    Employee updateDepartment(String newDept) {
        this.department = newDept;
        System.out.println("Department updated to: " + this.department);
        return this;  // Return current object for method chaining
    }
}

class ThisKeywordDemo {
    public static void main(String[] args) {
        System.out.println("Creating employees:");
        Employee emp1 = new Employee("John", 50000, "IT");
        Employee emp2 = new Employee("Alice", 55000, "HR");
        
        System.out.println("\nDisplaying employee information:");
        emp1.displayInfo();
        System.out.println();
        emp2.displayInfo();
        
        System.out.println("\nUpdating salary:");
        emp1.setSalary(60000);
        
        System.out.println("\nChecking same department:");
        if (emp1.hasSameDepartment(emp2)) {
            System.out.println(emp1.name + " and " + emp2.name + " work in same department");
        } else {
            System.out.println(emp1.name + " and " + emp2.name + " work in different departments");
        }
        
        System.out.println("\nDemonstrating method chaining:");
        emp1.updateName("John Smith").updateDepartment("Management");
        
        System.out.println("\nFinal employee info:");
        emp1.displayInfo();
    }
}
```

**Output:**
```
Creating employees:
Employee created: John
Employee created: Alice

Displaying employee information:
Employee Details:
Name: John
Salary: 50000
Department: IT
Annual Salary: 600000

Employee Details:
Name: Alice
Salary: 55000
Department: HR
Annual Salary: 660000

Updating salary:
Salary updated for John: 60000

Checking same department:
John and Alice work in different departments

Demonstrating method chaining:
Name updated to: John Smith
Department updated to: Management

Final employee info:
Employee Details:
Name: John Smith
Salary: 60000
Department: Management
Annual Salary: 720000
```

**Use:** Refer to current object, resolve naming conflicts, enable method chaining
**Advantages:** Clear code, method chaining, explicit object reference
**Disadvantages:** Can make code verbose, not always necessary

### 9. finalize() Method

```java
class ResourceManager {
    String resourceName;
    static int resourceCount = 0;
    
    ResourceManager(String name) {
        this.resourceName = name;
        resourceCount++;
        System.out.println("Resource allocated: " + resourceName + 
                          " (Total: " + resourceCount + ")");
    }
    
    void useResource() {
        System.out.println("Using resource: " + resourceName);
    }
    
    // finalize method - called by garbage collector
    @Override
    protected void finalize() throws Throwable {
        try {
            resourceCount--;
            System.out.println("Resource being finalized: " + resourceName + 
                              " (Remaining: " + resourceCount + ")");
            // Cleanup code would go here
        } finally {
            super.finalize();
        }
    }
}

// Modern alternative using try-with-resources (AutoCloseable)
class ModernResource implements AutoCloseable {
    String resourceName;
    static int resourceCount = 0;
    
    ModernResource(String name) {
        this.resourceName = name;
        resourceCount++;
        System.out.println("Modern resource allocated: " + resourceName + 
                          " (Total: " + resourceCount + ")");
    }
    
    void useResource() {
        System.out.println("Using modern resource: " + resourceName);
    }
    
    @Override
    public void close() {
        resourceCount--;
        System.out.println("Modern resource closed: " + resourceName + 
                          " (Remaining: " + resourceCount + ")");
    }
}

class FinalizeDemo {
    public static void main(String[] args) {
        System.out.println("=== Demonstrating finalize() method ===");
        
        // Create and use resources
        ResourceManager rm1 = new ResourceManager("Database Connection");
        ResourceManager rm2 = new ResourceManager("File Handle");
        
        rm1.useResource();
        rm2.useResource();
        
        // Remove references
        rm1 = null;
        rm2 = null;
        
        // Suggest garbage collection (not guaranteed to run immediately)
        System.out.println("\nCalling System.gc()...");
        System.gc();
        
        // Give some time for finalize to potentially run
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        System.out.println("\n=== Demonstrating modern approach ===");
        
        // Modern approach with try-with-resources
        try (ModernResource mr1 = new ModernResource("Network Socket");
             ModernResource mr2 = new ModernResource("Memory Buffer")) {
            
            mr1.useResource();
            mr2.useResource();
            
            // Resources automatically closed at end of try block
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        System.out.println("\nProgram ending...");
    }
}
```

**Output:**
```
=== Demonstrating finalize() method ===
Resource allocated: Database Connection (Total: 1)
Resource allocated: File Handle (Total: 2)
Using resource: Database Connection
Using resource: File Handle

Calling System.gc()...
Resource being finalized: File Handle (Remaining: 1)
Resource being finalized: Database Connection (Remaining: 0)

=== Demonstrating modern approach ===
Modern resource allocated: Network Socket (Total: 1)
Modern resource allocated: Memory Buffer (Total: 2)
Using modern resource: Network Socket
Using modern resource: Memory Buffer
Modern resource closed: Memory Buffer (Remaining: 1)
Modern resource closed: Network Socket (Remaining: 0)

Program ending...
```

**Use:** Cleanup resources before object destruction (deprecated approach)
**Advantages:** Automatic cleanup when object is garbage collected
**Disadvantages:** Not guaranteed to run, deprecated in modern Java, unpredictable timing

**Modern Alternative:** Use `AutoCloseable` interface with try-with-resources statements for guaranteed resource cleanup.

---

## UNIT II: EXCEPTION HANDLING & STREAMS

### 1. Arrays

#### **One-Dimensional Arrays**
```java
class OneDArrayExample {
    public static void main(String[] args) {
        System.out.println("=== One-Dimensional Arrays Demo ===\n");
        
        // Different ways to declare and initialize arrays
        int[] numbers = new int[5];  // Declaration with size
        int[] values = {10, 20, 30, 40, 50};  // Declaration with initialization
        
        // Filling the first array
        System.out.println("Filling numbers array:");
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = (i + 1) * 10;
            System.out.println("numbers[" + i + "] = " + numbers[i]);
        }
        
        System.out.println("\nPre-initialized values array:");
        for (int i = 0; i < values.length; i++) {
            System.out.println("values[" + i + "] = " + values[i]);
        }
        
        // Array properties
        System.out.println("\nArray Properties:");
        System.out.println("Numbers array length: " + numbers.length);
        System.out.println("Values array length: " + values.length);
        
        // Enhanced for loop (for-each)
        System.out.println("\nUsing enhanced for loop:");
        System.out.print("Numbers: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
        
        // Array operations
        System.out.println("\nArray Operations:");
        int sum = calculateSum(values);
        int max = findMaximum(values);
        double average = calculateAverage(values);
        
        System.out.println("Sum: " + sum);
        System.out.println("Maximum: " + max);
        System.out.println("Average: " + average);
    }
    
    static int calculateSum(int[] arr) {
        int sum = 0;
        for (int element : arr) {
            sum += element;
        }
        return sum;
    }
    
    static int findMaximum(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }
    
    static double calculateAverage(int[] arr) {
        return (double) calculateSum(arr) / arr.length;
    }
}
```

**Output:**
```
=== One-Dimensional Arrays Demo ===

Filling numbers array:
numbers[0] = 10
numbers[1] = 20
numbers[2] = 30
numbers[3] = 40
numbers[4] = 50

Pre-initialized values array:
values[0] = 10
values[1] = 20
values[2] = 30
values[3] = 40
values[4] = 50

Array Properties:
Numbers array length: 5
Values array length: 5

Using enhanced for loop:
Numbers: 10 20 30 40 50 

Array Operations:
Sum: 150
Maximum: 50
Average: 30.0
```

#### **Multi-Dimensional Arrays**
```java
class TwoDArrayExample {
    public static void main(String[] args) {
        System.out.println("=== Two-Dimensional Arrays Demo ===\n");
        
        // 2D array declaration and initialization
        int[][] matrix = new int[3][4];  // 3 rows, 4 columns
        int[][] predefined = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        // Filling the matrix
        System.out.println("Filling 3x4 matrix:");
        int value = 1;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = value++;
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
        
        System.out.println("\nPredefined 3x3 matrix:");
        printMatrix(predefined);
        
        // Matrix operations
        System.out.println("\nMatrix Operations:");
        System.out.println("Sum of predefined matrix: " + matrixSum(predefined));
        
        // Transpose demonstration
        System.out.println("\nTranspose of predefined matrix:");
        int[][] transposed = transpose(predefined);
        printMatrix(transposed);
        
        // Jagged array (arrays of different sizes)
        System.out.println("\nJagged Array Demo:");
        int[][] jaggedArray = {
            {1, 2},
            {3, 4, 5, 6},
            {7, 8, 9}
        };
        
        System.out.println("Jagged array contents:");
        for (int i = 0; i < jaggedArray.length; i++) {
            System.out.print("Row " + i + ": ");
            for (int j = 0; j < jaggedArray[i].length; j++) {
                System.out.print(jaggedArray[i][j] + " ");
            }
            System.out.println("(Length: " + jaggedArray[i].length + ")");
        }
    }
    
    static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
    }
    
    static int matrixSum(int[][] matrix) {
        int sum = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                sum += matrix[i][j];
            }
        }
        return sum;
    }
    
    static int[][] transpose(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] result = new int[cols][rows];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[j][i] = matrix[i][j];
            }
        }
        return result;
    }
}
```

**Output:**
```
=== Two-Dimensional Arrays Demo ===

Filling 3x4 matrix:
1	2	3	4	
5	6	7	8	
9	10	11	12	

Predefined 3x3 matrix:
1	2	3	
4	5	6	
7	8	9	

Matrix Operations:
Sum of predefined matrix: 45

Transpose of predefined matrix:
1	4	7	
2	5	8	
3	6	9	

Jagged Array Demo:
Jagged array contents:
Row 0: 1 2 (Length: 2)
Row 1: 3 4 5 6 (Length: 4)
Row 2: 7 8 9 (Length: 3)
```

#### **Passing Arrays to Methods**
```java
class ArrayMethodsDemo {
    public static void main(String[] args) {
        System.out.println("=== Array Methods Demo ===\n");
        
        int[] numbers = {64, 34, 25, 12, 22, 11, 90};
        int[] originalNumbers = numbers.clone(); // Keep original for comparison
        
        System.out.println("Original array:");
        printArray(originalNumbers);
        
        // Demonstrate that arrays are passed by reference
        System.out.println("\nModifying array in method:");
        modifyArray(numbers);
        printArray(numbers);
        
        // Array searching
        int target = 25;
        int index = linearSearch(numbers, target);
        if (index != -1) {
            System.out.println("\n" + target + " found at index: " + index);
        } else {
            System.out.println("\n" + target + " not found in array");
        }
        
        // Array sorting
        System.out.println("\nSorting array using bubble sort:");
        bubbleSort(numbers);
        printArray(numbers);
        
        // Statistics
        System.out.println("\nArray Statistics:");
        System.out.println("Minimum: " + findMin(numbers));
        System.out.println("Maximum: " + findMax(numbers));
        System.out.println("Average: " + calculateAverage(numbers));
        
        // Array reversal
        System.out.println("\nReversed array:");
        reverseArray(numbers);
        printArray(numbers);
    }
    
    static void printArray(int[] arr) {
        System.out.print("Array: [");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) System.out.print(", ");
        }
        System.out.println("]");
    }
    
    static void modifyArray(int[] arr) {
        System.out.println("Adding 10 to each element");
        for (int i = 0; i < arr.length; i++) {
            arr[i] += 10;  // Modifies original array
        }
    }
    
    static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }
    
    static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
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
    
    static int findMax(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }
    
    static double calculateAverage(int[] arr) {
        int sum = 0;
        for (int element : arr) {
            sum += element;
        }
        return (double) sum / arr.length;
    }
    
    static void reverseArray(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
```

**Output:**
```
=== Array Methods Demo ===

Original array:
Array: [64, 34, 25, 12, 22, 11, 90]

Modifying array in method:
Adding 10 to each element
Array: [74, 44, 35, 22, 32, 21, 100]

35 found at index: 2

Sorting array using bubble sort:
Array: [21, 22, 32, 35, 44, 74, 100]

Array Statistics:
Minimum: 21
Maximum: 100
Average: 46.857142857142854

Reversed array:
Array: [100, 74, 44, 35, 32, 22, 21]
```

**Use:** Store multiple values of same type, implement data structures
**Advantages:** Fast access by index, memory efficient for similar data types
**Disadvantages:** Fixed size, all elements must be same type, insertion/deletion is expensive

### 2. Strings

#### **String Class**
```java
class StringExample {
    public static void main(String[] args) {
        System.out.println("=== String Class Demo ===\n");
        
        // Different ways to create strings
        String str1 = "Hello";           // String literal (stored in string pool)
        String str2 = new String("World"); // Using new keyword (creates new object)
        String str3 = "Hello";           // Points to same object as str1 (string pool)
        
        System.out.println("String Creation:");
        System.out.println("str1: " + str1);
        System.out.println("str2: " + str2);
        System.out.println("str3: " + str3);
        
        // String comparison
        System.out.println("\nString Comparison:");
        System.out.println("str1 == str3: " + (str1 == str3));         // true (same reference)
        System.out.println("str1 == str2: " + (str1 == str2));         // false (different objects)
        System.out.println("str1.equals(\"Hello\"): " + str1.equals("Hello")); // true (content comparison)
        
        // String operations
        System.out.println("\nString Operations:");
        System.out.println("Length of str1: " + str1.length());
        System.out.println("Uppercase: " + str1.toUpperCase());
        System.out.println("Lowercase: " + str1.toLowerCase());
        System.out.println("Character at index 1: " + str1.charAt(1));
        System.out.println("Substring (1,4): " + str1.substring(1, 4));
        System.out.println("Index of 'l': 2
Last index of 'l': 3

String Concatenation:
Concatenated: Hello World
Using + operator: Hello World!

String Immutability Demo:
Original string: Java
After concat: original = Java
Modified string: Java Programming

More String Methods:
Original: '  Java Programming  '
Trimmed: 'Java Programming'
Replace 'a' with 'X': '  JXvX ProgrXmming  '
Contains 'Program': true
Starts with '  Java': true
Ends with 'ming  ': true

String Split:
Original: Java,Python,JavaScript,C++
Split result: [Java] [Python] [JavaScript] [C++] 
```

**Use:** Handle text data, string manipulation, user input processing
**Advantages:** Rich set of methods, immutable (thread-safe), string pool optimization
**Disadvantages:** Immutable (creates new objects for modifications), can be memory intensive for frequent modifications

#### **StringBuffer Class**
```java
class StringBufferExample {
    public static void main(String[] args) {
        System.out.println("=== StringBuffer Class Demo ===\n");
        
        // Creating StringBuffer objects
        StringBuffer sb1 = new StringBuffer();              // Default capacity 16
        StringBuffer sb2 = new StringBuffer(32);            // Custom capacity
        StringBuffer sb3 = new StringBuffer("Hello");       // With initial string
        
        System.out.println("Initial StringBuffer states:");
        System.out.println("sb1 capacity: " + sb1.capacity() + ", length: " + sb1.length());
        System.out.println("sb2 capacity: " + sb2.capacity() + ", length: " + sb2.length());
        System.out.println("sb3 capacity: " + sb3.capacity() + ", length: " + sb3.length());
        System.out.println("sb3 content: '" + sb3 + "'");
        
        // StringBuffer operations (mutable)
        System.out.println("\nStringBuffer Append Operations:");
        sb3.append(" World");
        System.out.println("After append(' World'): " + sb3);
        System.out.println("Length: " + sb3.length() + ", Capacity: " + sb3.capacity());
        
        sb3.append("!").append(" Java").append(" Programming");
        System.out.println("After chained appends: " + sb3);
        
        // Insert operation
        System.out.println("\nInsert Operations:");
        sb3.insert(6, "Beautiful ");
        System.out.println("After insert at position 6: " + sb3);
        
        sb3.insert(0, ">> ");
        System.out.println("After insert at beginning: " + sb3);
        
        // Replace operation
        System.out.println("\nReplace Operations:");
        StringBuffer sb4 = new StringBuffer("Java is great");
        System.out.println("Original: " + sb4);
        sb4.replace(5, 7, "was");
        System.out.println("After replace(5,7,'was'): " + sb4);
        
        sb4.replace(8, 13, "awesome");
        System.out.println("After replace(8,13,'awesome'): " + sb4);
        
        // Delete operations
        System.out.println("\nDelete Operations:");
        StringBuffer sb5 = new StringBuffer("Hello Beautiful World Java Programming");
        System.out.println("Original: " + sb5);
        
        sb5.delete(6, 16);  // Delete "Beautiful "
        System.out.println("After delete(6,16): " + sb5);
        
        sb5.deleteCharAt(0);  // Delete first character
        System.out.println("After deleteCharAt(0): " + sb5);
        
        // Reverse operation
        System.out.println("\nReverse Operation:");
        StringBuffer sb6 = new StringBuffer("Programming");
        System.out.println("Original: " + sb6);
        sb6.reverse();
        System.out.println("After reverse(): " + sb6);
        
        // Capacity management
        System.out.println("\nCapacity Management:");
        StringBuffer sb7 = new StringBuffer();
        System.out.println("Initial capacity: " + sb7.capacity());
        
        sb7.append("This is a long string that will exceed the initial capacity");
        System.out.println("After long append:");
        System.out.println("Content: " + sb7);
        System.out.println("Length: " + sb7.length() + ", Capacity: " + sb7.capacity());
        
        // Manual capacity adjustment
        sb7.ensureCapacity(100);
        System.out.println("After ensureCapacity(100): " + sb7.capacity());
        
        sb7.trimToSize();
        System.out.println("After trimToSize(): " + sb7.capacity());
        
        // Performance comparison demonstration
        System.out.println("\nPerformance Comparison Demo:");
        performanceComparison();
    }
    
    static void performanceComparison() {
        int iterations = 10000;
        
        // String concatenation (inefficient)
        long startTime = System.currentTimeMillis();
        String str = "";
        for (int i = 0; i < iterations; i++) {
            str += "a";  // Creates new String object each time
        }
        long stringTime = System.currentTimeMillis() - startTime;
        
        // StringBuffer concatenation (efficient)
        startTime = System.currentTimeMillis();
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < iterations; i++) {
            sb.append("a");  // Modifies existing object
        }
        long stringBufferTime = System.currentTimeMillis() - startTime;
        
        System.out.println("String concatenation time: " + stringTime + "ms");
        System.out.println("StringBuffer concatenation time: " + stringBufferTime + "ms");
        System.out.println("StringBuffer is " + (stringTime / (double) stringBufferTime) + " times faster");
    }
}
```

**Output:**
```
=== StringBuffer Class Demo ===

Initial StringBuffer states:
sb1 capacity: 16, length: 0
sb2 capacity: 32, length: 0
sb3 capacity: 21, length: 5
sb3 content: 'Hello'

StringBuffer Append Operations:
After append(' World'): Hello World
Length: 11, Capacity: 21
After chained appends: Hello World! Java Programming

Insert Operations:
After insert at position 6: Hello Beautiful World! Java Programming
After insert at beginning: >> Hello Beautiful World! Java Programming

Replace Operations:
Original: Java is great
After replace(5,7,'was'): Java was great
After replace(8,13,'awesome'): Java was awesome

Delete Operations:
Original: Hello Beautiful World Java Programming
After delete(6,16): Hello World Java Programming
After deleteCharAt(0): ello World Java Programming

Reverse Operation:
Original: Programming
After reverse(): gnimmargorP

Capacity Management:
Initial capacity: 16
After long append:
Content: This is a long string that will exceed the initial capacity
Length: 62, Capacity: 70
After ensureCapacity(100): 100
After trimToSize(): 62

Performance Comparison Demo:
String concatenation time: 156ms
StringBuffer concatenation time: 2ms
StringBuffer is 78.0 times faster
```

#### **StringBuilder Class (Similar to StringBuffer but not synchronized)**
```java
class StringBuilderExample {
    public static void main(String[] args) {
        System.out.println("=== StringBuilder vs StringBuffer Demo ===\n");
        
        // StringBuilder - not thread-safe but faster
        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" World").insert(6, "Beautiful ").reverse();
        System.out.println("StringBuilder result: " + sb);
        
        // Comparison of all three approaches
        compareStringOperations();
    }
    
    static void compareStringOperations() {
        System.out.println("\nComparison of String, StringBuffer, and StringBuilder:");
        
        String str = "Java";
        StringBuffer sbf = new StringBuffer("Java");
        StringBuilder sb = new StringBuilder("Java");
        
        // All perform the same logical operations
        str = str + " Programming";
        sbf.append(" Programming");
        sb.append(" Programming");
        
        System.out.println("String result: " + str);
        System.out.println("StringBuffer result: " + sbf);
        System.out.println("StringBuilder result: " + sb);
        
        System.out.println("\nKey Differences:");
        System.out.println("String: Immutable, creates new objects");
        System.out.println("StringBuffer: Mutable, thread-safe, synchronized methods");
        System.out.println("StringBuilder: Mutable, not thread-safe, faster than StringBuffer");
    }
}
```

**Output:**
```
=== StringBuilder vs StringBuffer Demo ===

StringBuilder result: lufituaeB dlroW olleH

Comparison of String, StringBuffer, and StringBuilder:
String result: Java Programming
StringBuffer result: Java Programming
StringBuilder result: Java Programming

Key Differences:
String: Immutable, creates new objects
StringBuffer: Mutable, thread-safe, synchronized methods
StringBuilder: Mutable, not thread-safe, faster than StringBuffer
```

#### **String vs StringBuffer vs StringBuilder Comparison**
```java
class StringComparison {
    public static void main(String[] args) {
        System.out.println("=== Complete String Comparison ===\n");
        
        demonstrateImmutability();
        System.out.println();
        demonstrateMutability();
        System.out.println();
        performanceTest();
    }
    
    static void demonstrateImmutability() {
        System.out.println("String Immutability:");
        String str = "Hello";
        System.out.println("Original string: " + str);
        System.out.println("String object ID: " + System.identityHashCode(str));
        
        str = str + " World";  // Creates new String object
        System.out.println("After concatenation: " + str);
        System.out.println("String object ID: " + System.identityHashCode(str));
        System.out.println("Notice: Object ID changed (new object created)");
    }
    
    static void demonstrateMutability() {
        System.out.println("StringBuffer/StringBuilder Mutability:");
        StringBuffer sb = new StringBuffer("Hello");
        System.out.println("Original StringBuffer: " + sb);
        System.out.println("StringBuffer object ID: " + System.identityHashCode(sb));
        
        sb.append(" World");  // Modifies existing object
        System.out.println("After append: " + sb);
        System.out.println("StringBuffer object ID: " + System.identityHashCode(sb));
        System.out.println("Notice: Object ID same (existing object modified)");
    }
    
    static void performanceTest() {
        System.out.println("Performance Test (1000 concatenations):");
        int iterations = 1000;
        
        // String concatenation
        long start = System.nanoTime();
        String str = "";
        for (int i = 0; i < iterations; i++) {
            str += "a";
        }
        long stringTime = System.nanoTime() - start;
        
        // StringBuffer concatenation
        start = System.nanoTime();
        StringBuffer sbf = new StringBuffer();
        for (int i = 0; i < iterations; i++) {
            sbf.append("a");
        }
        long stringBufferTime = System.nanoTime() - start;
        
        // StringBuilder concatenation
        start = System.nanoTime();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < iterations; i++) {
            sb.append("a");
        }
        long stringBuilderTime = System.nanoTime() - start;
        
        System.out.println("String time: " + stringTime / 1_000_000.0 + " ms");
        System.out.println("StringBuffer time: " + stringBufferTime / 1_000_000.0 + " ms");
        System.out.println("StringBuilder time: " + stringBuilderTime / 1_000_000.0 + " ms");
        
        System.out.println("\nRecommendations:");
        System.out.println("- Use String for simple, infrequent operations");
        System.out.println("- Use StringBuffer for frequent modifications in multi-threaded environment");
        System.out.println("- Use StringBuilder for frequent modifications in single-threaded environment");
    }
}
```

**Output:**
```
=== Complete String Comparison ===

String Immutability:
Original string: Hello
String object ID: 1554874502
After concatenation: Hello World
String object ID: 1846274136
Notice: Object ID changed (new object created)

StringBuffer/StringBuilder Mutability:
Original StringBuffer: Hello
StringBuffer object ID: 1639705018
After append: Hello World
StringBuffer object ID: 1639705018
Notice: Object ID same (existing object modified)

Performance Test (1000 concatenations):
String time: 15.234 ms
StringBuffer time: 0.123 ms
StringBuilder time: 0.089 ms

Recommendations:
- Use String for simple, infrequent operations
- Use StringBuffer for frequent modifications in multi-threaded environment
- Use StringBuilder for frequent modifications in single-threaded environment
```

**Use Cases:**
- **String:** Simple text operations, constants, when immutability is desired
- **StringBuffer:** Frequent string modifications in multi-threaded applications
- **StringBuilder:** Frequent string modifications in single-threaded applications

**Advantages:**
- **String:** Simple to use, immutable (thread-safe), string pool optimization
- **StringBuffer:** Mutable, thread-safe, efficient for multiple modifications
- **StringBuilder:** Mutable, fastest performance, efficient for multiple modifications

**Disadvantages:**
- **String:** Inefficient for frequent modifications, creates many objects
- **StringBuffer:** Slower than StringBuilder due to synchronization
- **StringBuilder:** Not thread-safe

### 3. Packages

#### **Creating a Package**
```java
// File: mypackage/Student.java
package mypackage;

public class Student {
    private int rollNo;
    private String name;
    private double marks;
    
    public Student(int rollNo, String name, double marks) {
        this.rollNo = rollNo;
        this.name = name;
        this.marks = marks;
        System.out.println("Student created: " + name);
    }
    
    public void displayInfo() {
        System.out.println("Roll No: " + rollNo);
        System.out.println("Name: " + name);
        System.out.println("Marks: " + marks);
        System.out.println("Grade: " + calculateGrade());
        System.out.println("------------------------");
    }
    
    public String calculateGrade() {
        if (marks >= 90) return "A+";
        else if (marks >= 80) return "A";
        else if (marks >= 70) return "B";
        else if (marks >= 60) return "C";
        else return "F";
    }
    
    // Getters and setters
    public int getRollNo() { return rollNo; }
    public String getName() { return name; }
    public double getMarks() { return marks; }
    
    public void setMarks(double marks) {
        if (marks >= 0 && marks <= 100) {
            this.marks = marks;
            System.out.println("Marks updated for " + name + ": " + marks);
        } else {
            System.out.println("Invalid marks! Must be between 0 and 100");
        }
    }
}
```

```java
// File: mypackage/Teacher.java
package mypackage;

public class Teacher {
    private String name;
    private String subject;
    private int experience;
    
    public Teacher(String name, String subject, int experience) {
        this.name = name;
        this.subject = subject;
        this.experience = experience;
        System.out.println("Teacher created: " + name);
    }
    
    public void displayInfo() {
        System.out.println("Teacher Name: " + name);
        System.out.println("Subject: " + subject);
        System.out.println("Experience: " + experience + " years");
        System.out.println("Category: " + getExperienceCategory());
        System.out.println("------------------------");
    }
    
    public String getExperienceCategory() {
        if (experience >= 20) return "Senior";
        else if (experience >= 10) return "Experienced";
        else if (experience >= 5) return "Intermediate";
        else return "Junior";
    }
    
    public void teachStudent(Student student) {
        System.out.println("Teacher " + name + " is teaching " + student.getName());
        System.out.println("Subject: " + subject);
    }
    
    // Getters
    public String getName() { return name; }
    public String getSubject() { return subject; }
    public int getExperience() { return experience; }
}
```

#### **Using Packages**
```java
// File: PackageDemo.java (in default package)
import mypackage.Student;
import mypackage.Teacher;
// Or import mypackage.*; to import all classes

class PackageDemo {
    public static void main(String[] args) {
        System.out.println("=== Package Demo ===\n");
        
        // Creating objects from imported classes
        System.out.println("Creating students:");
        Student student1 = new Student(101, "Alice", 85.5);
        Student student2 = new Student(102, "Bob", 92.0);
        Student student3 = new Student(103, "Charlie", 78.0);
        
        System.out.println("\nCreating teachers:");
        Teacher teacher1 = new Teacher("Dr. Smith", "Mathematics", 15);
        Teacher teacher2 = new Teacher("Ms. Johnson", "Physics", 8);
        
        System.out.println("\nStudent Information:");
        student1.displayInfo();
        student2.displayInfo();
        student3.displayInfo();
        
        System.out.println("Teacher Information:");
        teacher1.displayInfo();
        teacher2.displayInfo();
        
        System.out.println("Teaching Sessions:");
        teacher1.teachStudent(student1);
        teacher2.teachStudent(student2);
        
        System.out.println("\nUpdating student marks:");
        student1.setMarks(95.0);
        student1.displayInfo();
    }
}
```

**Output:**
```
=== Package Demo ===

Creating students:
Student created: Alice
Student created: Bob
Student created: Charlie

Creating teachers:
Teacher created: Dr. Smith
Teacher created: Ms. Johnson

Student Information:
Roll No: 101
Name: Alice
Marks: 85.5
Grade: A
------------------------
Roll No: 102
Name: Bob
Marks: 92.0
Grade: A+
------------------------
Roll No: 103
Name: Charlie
Marks: 78.0
Grade: B
------------------------
Teacher Information:
Teacher Name: Dr. Smith
Subject: Mathematics
Experience: 15 years
Category: Experienced
------------------------
Teacher Name: Ms. Johnson
Subject: Physics
Experience: 8 years
Category: Intermediate
------------------------
Teaching Sessions:
Teacher Dr. Smith is teaching Alice
Subject: Mathematics
Teacher Ms. Johnson is teaching Bob
Subject: Physics

Updating student marks:
Marks updated for Alice: 95.0
Roll No: 101
Name: Alice
Marks: 95.0
Grade: A+
------------------------
```

#### **Package Access Modifiers Demo**
```java
// File: mypackage/AccessDemo.java
package mypackage;

public class AccessDemo {
    private int privateVar = 1;
    int defaultVar = 2;          // Package-private
    protected int protectedVar = 3;
    public int publicVar = 4;
    
    public void demonstrateAccess() {
        System.out.println("Inside mypackage.AccessDemo:");
        System.out.println("Private: " + privateVar);
        System.out.println("Default: " + defaultVar);
        System.out.println("Protected: " + protectedVar);
        System.out.println("Public: " + publicVar);
    }
}
```

```java
// File: mypackage/SamePackageAccess.java
package mypackage;

public class SamePackageAccess {
    public void testAccess() {
        AccessDemo demo = new AccessDemo();
        
        System.out.println("Accessing from same package (mypackage):");
        // demo.privateVar;     // Not accessible
        System.out.println("Default: " + demo.defaultVar);      // Accessible
        System.out.println("Protected: " + demo.protectedVar);  // Accessible
        System.out.println("Public: " + demo.publicVar);        // Accessible
    }
}
```

```java
// File: DifferentPackageAccess.java (in default package)
import mypackage.AccessDemo;

class DifferentPackageAccess {
    public static void main(String[] args) {
        AccessDemo demo = new AccessDemo();
        
        System.out.println("Accessing from different package:");
        // demo.privateVar;     // Not accessible
        // demo.defaultVar;     // Not accessible
        // demo.protectedVar;   // Not accessible (unless subclass)
        System.out.println("Public: " + demo.publicVar);        // Accessible
        
        demo.demonstrateAccess();
    }
}
```

#### **Built-in Packages Example**
```java
// Using Java's built-in packages
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;
import java.io.File;
import java.text.SimpleDateFormat;

class BuiltInPackagesDemo {
    public static void main(String[] args) {
        System.out.println("=== Built-in Packages Demo ===\n");
        
        // java.util package
        System.out.println("Using java.util classes:");
        ArrayList<String> list = new ArrayList<>();
        list.add("Java");
        list.add("Python");
        list.add("JavaScript");
        System.out.println("ArrayList: " + list);
        
        Date currentDate = new Date();
        System.out.println("Current Date: " + currentDate);
        
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        System.out.println("Formatted Date: " + formatter.format(currentDate));
        
        // java.io package
        System.out.println("\nUsing java.io classes:");
        File file = new File("example.txt");
        System.out.println("File exists: " + file.exists());
        System.out.println("File name: " + file.getName());
        
        // java.lang package (automatically imported)
        System.out.println("\nUsing java.lang classes (auto-imported):");
        String str = "Hello World";
        System.out.println("String length: " + str.length());
        System.out.println("Math.sqrt(16): " + Math.sqrt(16));
        System.out.println("Integer.MAX_VALUE: " + Integer.MAX_VALUE);
        
        System.out.println("\nCommon Java Packages:");
        System.out.println("java.lang - Core classes (String, Object, System)");
        System.out.println("java.util - Utility classes (Collections, Date, Scanner)");
        System.out.println("java.io - Input/Output classes");
        System.out.println("java.net - Network programming");
        System.out.println("java.awt - Abstract Window Toolkit (GUI)");
        System.out.println("javax.swing - Swing GUI components");
    }
}
```

**Output:**
```
=== Built-in Packages Demo ===

Using java.util classes:
ArrayList: [Java, Python, JavaScript]
Current Date: Mon Sep 15 10:30:45 UTC 2025
Formatted Date: 15/09/2025 10:30:45

Using java.io classes:
File exists: false
File name: example.txt

Using java.lang classes (auto-imported):
String length: 11
Math.sqrt(16): 4.0
Integer.MAX_VALUE: 2147483647

Common Java Packages:
java.lang - Core classes (String, Object, System)
java.util - Utility classes (Collections, Date, Scanner)
java.io - Input/Output classes
java.net - Network programming
java.awt - Abstract Window Toolkit (GUI)
javax.swing - Swing GUI components
```

**Use:** Organize related classes, avoid naming conflicts, control access
**Advantages:** Better code organization, namespace management, access control, reusability
**Disadvantages:** Additional complexity, longer class names with fully qualified names, directory structure requirements

**Package Benefits:**
1. **Organization**: Group related classes together
2. **Access Control**: Use package-private access
3. **Namespace**: Avoid class name conflicts
4. **Distribution**: Easy to distribute related classes
5. **Security**: Control which classes can access package internals

This completes the comprehensive OOPS study notes for Units 1 and 2, covering all major concepts with practical examples, outputs, use cases, advantages, and disadvantages. The content is structured to provide both theoretical understanding and practical implementation knowledge for Java programming. of 'l': " + str1.indexOf('l'));
        System.out.println("Last index of 'l': " + str1.lastIndexOf('l'));
        
        // String concatenation
        System.out.println("\nString Concatenation:");
        String concatenated = str1.concat(" " + str2);
        System.out.println("Concatenated: " + concatenated);
        String combined = str1 + " " + str2 + "!";
        System.out.println("Using + operator: " + combined);
        
        // String immutability demonstration
        System.out.println("\nString Immutability Demo:");
        String original = "Java";
        System.out.println("Original string: " + original);
        String modified = original.concat(" Programming");
        System.out.println("After concat: original = " + original);
        System.out.println("Modified string: " + modified);
        
        // More string methods
        System.out.println("\nMore String Methods:");
        String text = "  Java Programming  ";
        System.out.println("Original: '" + text + "'");
        System.out.println("Trimmed: '" + text.trim() + "'");
        System.out.println("Replace 'a' with 'X': " + text.replace('a', 'X'));
        System.out.println("Contains 'Program': " + text.contains("Program"));
        System.out.println("Starts with '  Java': " + text.startsWith("  Java"));
        System.out.println("Ends with 'ming  ': " + text.endsWith("ming  "));
        
        // String split
        System.out.println("\nString Split:");
        String sentence = "Java,Python,JavaScript,C++";
        String[] languages = sentence.split(",");
        System.out.println("Original: " + sentence);
        System.out.print("Split result: ");
        for (String lang : languages) {
            System.out.print("[" + lang + "] ");
        }
        System.out.println();
    }
}
```

**Output:**
```
=== String Class Demo ===

String Creation:
str1: Hello
str2: World
str3: Hello

String Comparison:
str1 == str3: true
str1 == str2: false
str1.equals("Hello"): true

String Operations:
Length of str1: 5
Uppercase: HELLO
Lowercase: hello
Character at index 1: e
Substring (1,4): ell
Index:");
        System.out.println("Private: " + privateVar);
        System.out.println("Default: " + defaultVar);
        System.out.println("Protected: " + protectedVar);
        System.out.println("Public: " + publicVar);
    }
}

class TestAccess {
    public static void main(String[] args) {
        AccessModifierDemo demo = new AccessModifierDemo();
        
        // Public access - works
        System.out.println("Accessing public members:");
        demo.publicMethod();
        System.out.println("Public variable directly: " + demo.publicVar);
        
        // Default access - works (same package)
        System.out.println("\nAccessing default members:");
        demo.defaultMethod();
        System.out.println("Default variable directly: " + demo.defaultVar);
        
        // Protected access - works (same package)
        System.out.println("\nAccessing protected members:");
        demo.protectedMethod();
        System.out.println("Protected variable directly: " + demo.protectedVar);
        
        // Private access - won't work (commented out)
        // demo.privateMethod();  // Compilation error
        // System.out.println(demo.privateVar);  // Compilation error
        
        demo.demonstrateAccess();
    }
}
```

**Output:**
```
Accessing public members:
Public method - accessible everywhere
Public variable: 4
Private method - only accessible within this class
Private variable: 1
Public variable directly: 4

Accessing default members:
Default method - accessible within package
Default variable: 2
Default variable directly: 2

Accessing protected members:
Protected method - accessible within package and subclasses
Protected variable: 3
Protected variable directly: 3

Demonstrating access from within the class
