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
        MathOperati