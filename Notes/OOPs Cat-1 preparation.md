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

Citations:
[1] OOP-unit-1.pdf https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/68867823/489c5df9-ecf9-46c9-934c-4a856b5137b9/OOP-unit-1.pdf
