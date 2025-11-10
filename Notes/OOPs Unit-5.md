### Unit-5
---
# 1)Introduction to Swing (from your PDF, with all details, code, and expected output)

**Definition and Overview:**
- **Swing** is a *Java Foundation Classes (JFC)* library and an extension of the Abstract Window Toolkit (AWT).
- It provides many more user interface components than AWT, offers improved functionality, new component types, drag-and-drop support, and better event handling.
- Swing is part of the standard Java distribution and is entirely written in Java, making its components platform-independent and lightweight.
- Swing supports standalone GUI applications, Servlets, and Applets and employs the *Model-View-Controller (MVC)* design architecture.
- Swing has a "pluggable look and feel," allowing GUI appearance customization.
- Swing offers powerful components like tables, lists, scroll panes, color chooser, tabbed pane, etc.
- It is built on top of AWT and is considered more portable, flexible, and resource-friendly than AWT.

***

**Swing vs. AWT:**

| Java AWT                                | Java Swing                            |
|------------------------------------------|---------------------------------------|
| Components are platform-dependent        | Components are platform-independent   |
| Components are heavyweight               | Components are lightweight            |
| Doesn’t support pluggable look and feel  | Supports pluggable look and feel      |
| Less components                         | Many powerful components              |
| Requires java.awt package                | Requires javax.swing package          |

***

**Commonly Used Swing Methods (Component Class):**
- `add(Component c)` – Add a component to another component.
- `setSize(int width, int height)` – Set size of the component.
- `setLayout(LayoutManager m)` – Set the layout manager for the component.
- `setVisible(boolean b)` – Set visibility (default is false).

***

**Hierarchy:**  
The hierarchy starts from `Component` class, goes up through Swing API classes like `JFrame`, `JButton`, etc.

***

#### **Swing Example 1**  
**Code:**
```java
import javax.swing.*;
public class FirstSwingExample {
    public static void main(String args[]) {
        JFrame f = new JFrame(); // creating instance of JFrame
        JButton b = new JButton("click"); // creating instance of JButton
        b.setBounds(130, 100, 100, 40); // x axis, y axis, width, height
        f.add(b); // adding button in JFrame
        f.setSize(400, 500); // 400 width and 500 height
        f.setLayout(null); // using no layout managers
        f.setVisible(true); // making the frame visible
    }
}
```
**Expected Output:**  
A window (`JFrame`) of size 400x500 pixels. It contains a button labeled "click" placed at coordinates (130, 100) with width 100 and height 40.

***

#### **Swing Example 2**  
**Code:**
```java
import javax.swing.*;
public class Simple extends JFrame {
    Simple() {
        JFrame f = new JFrame(); // creating instance of JFrame
        JButton b = new JButton("click"); // creating instance of JButton
        b.setBounds(130, 100, 100, 40);
        f.add(b); // adding button in JFrame
        f.setSize(400, 500);
        f.setLayout(null);
        f.setVisible(true);
    }
    public static void main(String args[]) {
        new Simple();
    }
}
```
**Expected Output:**  
Identical to the first example: a frame of size 400x500 pixels with a "click" button at specified coordinates.

***

**Summary of Details from PDF:**
- Swing offers a rich set of lightweight, platform-independent UI components.
- It improves upon AWT with custom look-and-feel, advanced components, better resource management, and MVC-based architecture.
- Swing GUIs can be created using simple class and method calls, demonstrated above with `JFrame` and `JButton`.
- GUI windows display as specified, with frame size and button placement matching code.

---
# 2) Model-View-Controller (MVC)  
The Model-View-Controller (MVC) is a well-known design pattern in the web development field. It is way to organize our code. It specifies that a program or application shall consist of data model, presentation information and control information. The MVC pattern needs all these components to be separated as different objects. In this section, we will discuss the MVC Architecture in Java, along with its advantages and disadvantages and examples to understand the implementation of MVC in Java.  
What is MVC architecture in Java?  
The model designs based on the MVC architecture follow MVC design pattern. The application logic is separated from the user interface while designing the software using model designs. The MVC pattern architecture consists of three layers  
- Model  
It represents the business layer of application. It is an object to carry the data that can also contain the logic to update controller if data is changed.  
- View  
It represents the presentation layer of application. It is used to visualize the data that the model contains.  
- Controller  
It works on both the model and view. It is used to manage the flow of application, i.e. data flow in the model object and to update the view whenever data is changed.  
In Java Programming, the Model contains the simple Java classes, the View used to display the data and the Controller contains the servlets. Due to this separation the user requests are processed as follows  
1. A client browser sends a request to the controller on the server side, for a page  
2. The controller then calls the model. It gathers the requested data.  
3. Then the controller transfers the data retrieved to the view layer.  
4. Now the result is sent back to the browser client by the view.  
Advantages of MVC Architecture  
The advantages of MVC architecture are as follows,  
- MVC has the feature of scalability that in turn helps the growth of application.  
- The components are easy to maintain because there is less dependency.  
- A model can be reused by multiple views that provides reusability of code.  
- The developers can work with the three layers Model, View, and Controller simultaneously.  
- Using MVC, the application becomes more understandable.  
- Using MVC, each layer is maintained separately therefore we do not require to deal with massive code.  
- The extending and testing of application is easier.  

Implementation of MVC using Java  
To implement MVC pattern in Java, we are required to create the following three classes.  
- Employee Class, will act as model layer.  
- EmployeeView Class, will act as a view layer.  
- EmployeeController Class, will act a controller layer.  

MVC Architecture Layers  

Model Layer  
The Model in the MVC design pattern acts as a data layer for the application. It represents the business logic for application and also the state of application. The model object fetches and store the model state in the database. Using the model layer, rules are applied to the data that represents the concepts of application. Lets consider the following code snippet that creates a class that represents model  
```java
public class Employee {
    private String EmployeeName;
    private String EmployeeId;
    private String EmployeeDepartment;
    public String getId() { return EmployeeId; }
    public void setId(String id) { this.EmployeeId=id; }
    public String getName() { return EmployeeName; }
    public void setName(String name) { this.EmployeeName = name; }
    public String getDepartment() { return EmployeeDepartment; }
    public void setDepartment(String Department) { this.EmployeeDepartment = Department; }
}
```

View Layer  
As the name depicts, view represents the visualization of data received from the model. The view layer consists of output of application or user interface. It sends the requested data to the client, that is fetched from model layer by controller. Lets take an example where we create a view using the EmployeeView class.  
```java
public class EmployeeView {
    public void printEmployeeDetails(String EmployeeName, String EmployeeId, String EmployeeDepartment){
        System.out.println("Employee Details");
        System.out.println("Name: " + EmployeeName);
        System.out.println("Employee ID: " + EmployeeId);
        System.out.println("Employee Department: " + EmployeeDepartment);
    }
}
```

Controller Layer  
The controller layer gets the user requests from the view layer and processes them, with the necessary validations. It acts as an interface between Model and View. The requests are then sent to model for data processing. Once they are processed, the data is sent back to the controller and then displayed on the view. Lets consider the following code snippet that creates the controller using the EmployeeController class.  
```java
public class EmployeeController {
    private Employee model;
    private EmployeeView view;
    public EmployeeController(Employee model, EmployeeView view) {
        this.model = model;
        this.view = view;
    }
    public void setEmployeeName(String name) { model.setName(name); }
    public String getEmployeeName() { return model.getName(); }
    public void setEmployeeId(String id) { model.setId(id); }
    public String getEmployeeId() { return model.getId(); }
    public void setEmployeeDepartment(String Department) { model.setDepartment(Department); }
    public String getEmployeeDepartment() { return model.getDepartment(); }
    public void updateView() {
        view.printEmployeeDetails(model.getName(), model.getId(), model.getDepartment());
    }
}
```

Main Class Java file  
The following example displays the main file to implement the MVC architecture. Here, we are using the MVC Main class.  
```java
public class MVCMain {
    public static void main(String args[]) {
        Employee model = retriveEmployeeFromDatabase();
        EmployeeView view = new EmployeeView();
        EmployeeController controller = new EmployeeController(model, view);
        controller.updateView();
        controller.setEmployeeName("Nirnay");
        System.out.println("Employee Details after updating");
        controller.updateView();
    }
    private static Employee retriveEmployeeFromDatabase() {
        Employee Employee = new Employee();
        Employee.setName("Anu");
        Employee.setId("11");
        Employee.setDepartment("Salesforce");
        return Employee;
    }
}
```

Output  
Employee Details  
Name: Anu  
Employee ID: 11  
Employee Department: Salesforce  

Employee Details after updating  
Name: Nirnay  
Employee ID: 11  
Employee Department: Salesforce
---
# 3) Java Layout Management  
The Layout Managers are used to arrange components in a particular manner. The Java Layout Managers facilitates us to control the positioning and size of the components in GUI forms. Layout Manager is an interface that is implemented by all the classes of layout managers.  

Java BorderLayout  
The BorderLayout is used to arrange the components in five regions north, south, east, west, and center. Each region area may contain one component only. It is the default layout of a frame or window. The BorderLayout provides five constants for each region  
1. public static final int NORTH  
2. public static final int SOUTH  
3. public static final int EAST  
4. public static final int WEST  
5. public static final int CENTER  

Constructors of BorderLayout class  
o BorderLayout creates a border layout but with no gaps between the components.  
o BorderLayout(int hgap, int vgap) creates a border layout with the given horizontal and vertical gaps between the components.  

Example 1  
```java
import java.awt.*;
import javax.swing.*;
public class Border {
    JFrame f;
    Border() {
        f = new JFrame();
        JButton b1 = new JButton("NORTH");
        JButton b2 = new JButton("SOUTH");
        JButton b3 = new JButton("EAST");
        JButton b4 = new JButton("WEST");
        JButton b5 = new JButton("CENTER");
        f.add(b1, BorderLayout.NORTH);
        f.add(b2, BorderLayout.SOUTH);
        f.add(b3, BorderLayout.EAST);
        f.add(b4, BorderLayout.WEST);
        f.add(b5, BorderLayout.CENTER);
        f.setSize(300, 300);
        f.setVisible(true);
    }
    public static void main(String args[]) {
        new Border();
    }
}
```
Expected Output:  
A window of size 300x300, with five buttons labeled as NORTH, SOUTH, EAST, WEST, CENTER, each placed in their respective region.

Example 2  
```java
import java.awt.*;
import javax.swing.*;
public class BorderLayoutExample {
    JFrame jframe;
    BorderLayoutExample() {
        jframe = new JFrame();
        JButton btn1 = new JButton("NORTH");
        JButton btn2 = new JButton("SOUTH");
        JButton btn3 = new JButton("EAST");
        JButton btn4 = new JButton("WEST");
        JButton btn5 = new JButton("CENTER");
        jframe.setLayout(new BorderLayout(20, 15)); // horizontal gap 20, vertical gap 15
        jframe.add(btn1, BorderLayout.NORTH);
        jframe.add(btn2, BorderLayout.SOUTH);
        jframe.add(btn3, BorderLayout.EAST);
        jframe.add(btn4, BorderLayout.WEST);
        jframe.add(btn5, BorderLayout.CENTER);
        jframe.setSize(300, 300);
        jframe.setVisible(true);
    }
    public static void main(String args[]) {
        new BorderLayoutExample();
    }
}
```
Expected Output:  
A 300x300 window, five buttons in respective BorderLayout regions with visible gaps between them.

Java BorderLayout - Without Specifying Region  
If we do not specify the region, only the latest component added is shown in the frame, and all the previously added components get discarded. The latest component covers the whole area.

Example  
```java
import java.awt.*;
import javax.swing.*;
public class BorderLayoutWithoutRegionExample {
    JFrame jframe;
    BorderLayoutWithoutRegionExample() {
        jframe = new JFrame();
        JButton btn1 = new JButton("NORTH");
        JButton btn2 = new JButton("SOUTH");
        JButton btn3 = new JButton("EAST");
        JButton btn4 = new JButton("WEST");
        JButton btn5 = new JButton("CENTER");
        jframe.setLayout(new BorderLayout(7, 7));
        jframe.add(btn1);
        jframe.add(btn2);
        jframe.add(btn3);
        jframe.add(btn4);
        jframe.add(btn5); // Only this button is visible, occupies whole frame
        jframe.setSize(300, 300);
        jframe.setVisible(true);
    }
    public static void main(String args[]) {
        new BorderLayoutWithoutRegionExample();
    }
}
```
Expected Output:  
A window of 300x300 with only the last added button ("CENTER") visible and covering the entire window.
---
# 4) Introduction to JavaFX  
JavaFX is a Java library used to develop desktop applications as well as Rich Internet Applications (RIA). The applications built in JavaFX can run on multiple platforms including Web, Mobile, and Desktop. JavaFX is intended to replace Swing in Java as a GUI framework and provides more functionalities than Swing. Like Swing, JavaFX supplies its own components and does not depend upon the operating system. It is lightweight and hardware accelerated. JavaFX supports various operating systems including Windows, Linux, and Mac OS.

Features of JavaFX  
- Java Library: JavaFX consists of many classes and interfaces written in Java.  
- FXML: FXML is an XML based declarative markup language. GUI coding can be done in FXML for enhanced user interfaces.  
- Scene Builder: Scene builder generates FXML markup which can be imported into an IDE.  
- Web View: JavaFX applications can embed web pages using WebKit HTML technology.  
- Built-in UI Controls: Built-in components are not dependent on the operating system.  
- CSS-like Styling: JavaFX code can be styled using embedded CSS for improved viewing.  
- Swing Interoperability: JavaFX applications can embed Swing code through the Swing Node class.  
- Canvas API: Provides methods for direct drawing in an area of a JavaFX scene.  
- Rich Set of APIs: Wide collection of APIs for GUI development.  
- Integrated Graphics Library: Classes for 2D and 3D graphics handling.  
- Graphics Pipeline: Graphics rendered pipeline (prism), hardware accelerated.  
- High Performance Media Engine: Media pipeline supports low-latency web media playback using Gstreamer.  
- Self-contained Deployment Model: Packages have all application resources and private copy of Java and JavaFX Runtime.

Architecture of JavaFX  
- JavaFX API: Implements the required classes for JavaFX application development.  
  - javafx.animation: Transition-based animations for nodes.  
  - javafx.css: CSS-like styling for GUI applications.  
  - javafx.geometry: Methods and classes for 2D geometric figures.  
  - javafx.scene: Scene graph and sub-packages (canvas, chart, control, effect, image, input, layout, media, paint, shape, text, transform, web, etc.)  
  - javafx.application: Life cycle management classes.  
  - javafx.event: Event handling classes and interfaces.  
  - javafx.stage: Top-level container classes.
- Scene Graph:  
  - Root Node: Node with no parent.  
  - Leaf Node: Node with no children.  
  - Branch Node: Node with both parent and children.  
- Quantum Toolkit: Connects Prism and Glass windowing toolkits.  
- Prism: Hardware-accelerated graphics rendering pipeline.  
- Glass Windowing Toolkit: Platform-dependent layer for OS integration.  
- WebView: Uses WebKit HTML engine for embedding web pages.  
- Media Engine: High-performance media playback based on Gstreamer framework.

Life Cycle of JavaFX Application  
- start: Entry point for application graphics code.  
- init: Empty override-able method; cannot create stage or scene.  
- stop: Empty override-able method; code to halt application.  
- launch (static): Used to launch the JavaFX application.  
  - Sequence: Instance of application → init() → start() → stop()  
- Application terminated when the last window closes or by Platform.exit/System.exit().

Example  
```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Label;

public class HelloJavaFX extends Application {
    @Override
    public void start(Stage primaryStage) {
        Label label = new Label("Hello JavaFX!");
        Scene scene = new Scene(label, 400, 200);
        primaryStage.setScene(scene);
        primaryStage.setTitle("JavaFX Example");
        primaryStage.show();
    }
    public static void main(String[] args) {
        launch(args);
    }
}
```
Expected Output:  
A window titled "JavaFX Example" of size 400x200 pixels displaying the label "Hello JavaFX!" in the center of the window.
--
