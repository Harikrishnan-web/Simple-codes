Object-Oriented Programming (OOP) Concepts
1. Objects and Classes
Object: Real-world entity with state (data), behavior (methods), and identity.

Class: Blueprint/template for creating objects. Contains data (attributes) and methods (functions).

2. Methods and Messages
Methods: Functions inside a class that define object behavior.

Messages: Calls to invoke methods on objects.

3. Abstraction and Encapsulation
Abstraction: Hiding complex details, showing only necessary features.

Encapsulation: Wrapping data and methods into a single unit (class), restricting direct access using access specifiers.

4. Inheritance
Mechanism where one class (child/subclass) acquires properties and methods of another (parent/superclass).

Supports code reuse and hierarchy.

5. Abstract Classes
Classes that cannot be instantiated.

Can contain abstract methods (without implementation) and concrete methods (with implementation).

Subclass must provide implementation for abstract methods.

6. Polymorphism
Ability to take many forms.

Compile-time polymorphism: Method overloading (same method name, different parameters).

Run-time polymorphism: Method overriding (subclass provides specific method implementation).

Java OOP Basics with Code Examples
Defining a Class and Creating Objects
java
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
        myDog.bark();
    }
}
Output:

text
Buddy is barking!
Encapsulation with Access Specifiers and Getters/Setters
java
class Person {
    private String name;
    private int age;

    public void setName(String name) { this.name = name; }
    public String getName() { return name; }
    public void setAge(int age) { this.age = age; }
    public int getAge() { return age; }
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person();
        p.setName("Alice");
        p.setAge(30);
        System.out.println(p.getName() + " is " + p.getAge() + " years old.");
    }
}
Output:

text
Alice is 30 years old.
Inheritance Example
java
class Animal {
    void eat() {
        System.out.println("This animal eats food.");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("The dog barks.");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.eat();  // Inherited method
        myDog.bark(); // Own method
    }
}
Output:

text
This animal eats food.
The dog barks.
Abstract Class Example
java
abstract class Animal {
    abstract void sound();  // Abstract method

    void sleep() {
        System.out.println("This animal is sleeping.");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("The dog barks.");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.sound();
        myDog.sleep();
    }
}
Output:

text
The dog barks.
This animal is sleeping.
Polymorphism: Method Overloading and Overriding
Method Overloading:

java
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

public class Main {
    public static void main(String[] args) {
        OverloadDemo obj = new OverloadDemo();
        obj.test();
        obj.test(10);
        obj.test(10, 20);
    }
}
Output:

text
No parameters
a: 10
a and b: 10 20
Method Overriding:

java
class A {
    void show() {
        System.out.println("Parent class method");
    }
}

class B extends A {
    @Override
    void show() {
        System.out.println("Child class method");
    }
}

public class Main {
    public static void main(String[] args) {
        B obj = new B();
        obj.show();  // Calls child class version
    }
}
Output:

text
Child class method
Static Members and Methods
java
class StaticDemo {
    static int a = 10;
    static void display() {
        System.out.println("a = " + a);
    }
}

public class Main {
    public static void main(String[] args) {
        StaticDemo.display();
    }
}
Output:

text
a = 10
Constructors and Overloading
java
class Box {
    double width, height, depth;

    Box() {  // Default constructor
        width = height = depth = 1.0;
    }

    Box(double w, double h, double d) {  // Parameterized constructor
        width = w;
        height = h;
        depth = d;
    }

    double volume() {
        return width * height * depth;
    }
}

public class Main {
    public static void main(String[] args) {
        Box b1 = new Box();  // Default constructor
        Box b2 = new Box(10, 20, 15);  // Parameterized constructor

        System.out.println("Volume b1: " + b1.volume());
        System.out.println("Volume b2: " + b2.volume());
    }
}
Output:

text
Volume b1: 1.0
Volume b2: 3000.0
Finalize Method (Garbage Collection Notification)
java
public class Car {
    public Car() {
        System.out.println("Car is created");
    }

    @Override
    protected void finalize() throws Throwable {
        System.out.println("Car is being destroyed");
        super.finalize();
    }

    public static void main(String[] args) {
        Car myCar = new Car();
        myCar = null;  // Make eligible for GC
        System.gc();   // Suggest garbage collector to run
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("End of main method");
    }
}
Possible Output:

text
Car is created
Car is being destroyed
End of main method
(Note: finalize() output depends on JVM GC timing and may not always appear.)