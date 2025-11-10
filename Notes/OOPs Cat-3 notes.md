# Unit 4 
---
# 1) What is Socket Programming?

**Socket programming** is a way of connecting two nodes (computers) on a network to communicate with each other. Think of it like a telephone connection:
- One socket (node) **listens** on a particular port at an IP address
- The other socket **reaches out** to form a connection

### Key Points:
- Used for communication between applications running on **different JREs** (Java Runtime Environments)
- Applications can be on the same machine or different machines
- Enables real-time data exchange over networks

---

## 2. Types of Socket Programming

### A) Connection-Oriented (TCP)
- **Classes Used:** `Socket` and `ServerSocket`
- **Protocol:** TCP (Transmission Control Protocol)
- **Characteristics:**
  - Reliable communication
  - Guarantees data delivery
  - Data arrives in order
  - Connection established before data transfer (handshake)
  - Slower but more reliable

### B) Connection-Less (UDP)
- **Classes Used:** `DatagramSocket` and `DatagramPacket`
- **Protocol:** UDP (User Datagram Protocol)
- **Characteristics:**
  - Fast but unreliable
  - No guarantee of data delivery
  - Data may arrive out of order
  - No connection establishment needed
  - Known as "fire-and-forget" protocol

---

## 3. Understanding TCP vs UDP

### TCP (Transmission Control Protocol)

**Features:**
- **Data Delivery:** Ensures data is received correctly, nothing missing, in proper order
- **Connection-Oriented:** Computers establish connection first using **three-way handshake**
- **Reliability:** If data isn't received, TCP resends it automatically

**Three-Way Handshake Process:**
```
Client                          Server
  |                               |
  |-------- SYN ----------------->|  (1. Client sends SYN)
  |                               |
  |<------- SYN-ACK --------------|  (2. Server responds with SYN-ACK)
  |                               |
  |-------- ACK ----------------->|  (3. Client sends ACK)
  |                               |
  |===== Connection Established ==|
```

**Use Cases:**
- Web browsing (viewing complete web pages)
- File downloads (getting complete files)
- Email transmission
- Any scenario where data integrity is critical

### UDP (User Datagram Protocol)

**Features:**
- **Connectionless:** No connection establishment needed
- **No Guarantee:** Doesn't guarantee delivery or order
- **Fast:** Faster than TCP because no reliability checks
- **Fire-and-Forget:** Sends data and doesn't care if received

**Use Cases:**
- Video streaming
- Online gaming
- Voice over IP (VoIP)
- DNS queries
- Situations where speed matters more than reliability

---

## 4. Socket Class - Deep Dive

The **Socket class** represents one endpoint of a two-way communication link.

### Creating a Socket:
```java
Socket socket = new Socket("127.0.0.1", 5000);
```

**Parameters Explained:**
- **First Parameter (IP Address):**
  - `"127.0.0.1"` = localhost (your own computer)
  - Can be actual IP like `"192.168.1.100"`
  - Can be hostname like `"www.example.com"`

- **Second Parameter (Port Number):**
  - Range: 0 to 65535
  - Well-known ports (0-1023): HTTP=80, HTTPS=443, FTP=21
  - Registered ports (1024-49151): Used by applications
  - Dynamic ports (49152-65535): Temporary connections
  - In examples: 5000, 6666, 9000 (can choose any available port)

### Important Socket Methods:

| Method | Description |
|--------|-------------|
| `getInputStream()` | Returns InputStream to read data from socket |
| `getOutputStream()` | Returns OutputStream to write data to socket |
| `getPort()` | Returns remote port number |
| `getLocalPort()` | Returns local port number |
| `getInetAddress()` | Returns address to which socket is connected |
| `close()` | Closes the socket connection |
| `isConnected()` | Checks if socket is connected |
| `isClosed()` | Checks if socket is closed |

---

## 5. ServerSocket Class - Deep Dive

The **ServerSocket class** is used to create server applications that wait for client connections.

### Creating a ServerSocket:
```java
ServerSocket serverSocket = new ServerSocket(6666);
```

**What happens:**
- Server starts listening on port 6666
- Waits for incoming client connections
- Can accept multiple clients (one at a time or using threads)

### Important ServerSocket Methods:

| Method | Description | Details |
|--------|-------------|---------|
| `accept()` | Waits for client connection | **Blocking method** - freezes program until client connects; Returns Socket object when client connects |
| `bind(SocketAddress endpoint)` | Binds socket to specific address | Associates server with IP and port |
| `getLocalPort()` | Returns port number | The port server is listening on |
| `getInetAddress()` | Returns local IP address | Server's IP address |
| `close()` | Closes server socket | Releases port for other applications |
| `isClosed()` | Checks if closed | Returns true/false |
| `isBound()` | Checks if bound to address | Returns true/false |

---

## 6. Step-by-Step: How Socket Communication Works

### Client-Side Steps:

**Step 1: Establish Socket Connection**
```java
Socket socket = new Socket("127.0.0.1", 5000);
```
- Creates socket
- Connects to server at IP 127.0.0.1 on port 5000

**Step 2: Get Output Stream (to send data)**
```java
DataOutputStream dout = new DataOutputStream(socket.getOutputStream());
```
- Gets output stream from socket
- Wraps it in DataOutputStream for easy writing

**Step 3: Send Data**
```java
dout.writeUTF("Hello Server");
dout.flush(); // Forces data to be sent immediately
```
- Writes message to stream
- `flush()` ensures data is sent, not buffered

**Step 4: Close Connection**
```java
dout.close();
socket.close();
```
- Closes streams and socket
- Releases resources

### Server-Side Steps:

**Step 1: Create ServerSocket**
```java
ServerSocket ss = new ServerSocket(6666);
```
- Server starts listening on port 6666

**Step 2: Wait for Client (Blocking Call)**
```java
Socket s = ss.accept();
```
- **Blocks here** until client connects
- Returns Socket object when client connects
- Now server can communicate with this client

**Step 3: Get Input Stream (to receive data)**
```java
DataInputStream dis = new DataInputStream(s.getInputStream());
```
- Gets input stream from socket
- Wraps it in DataInputStream for easy reading

**Step 4: Read Data**
```java
String str = (String)dis.readUTF();
System.out.println("message= " + str);
```
- Reads message from client
- Prints it to console

**Step 5: Close Connection**
```java
ss.close();
```
- Closes server socket
- In real applications, server usually keeps running

---

## 7. Complete Working Example with Detailed Comments

### Server Code (MyServer.java):

```java
import java.io.*;
import java.net.*;

public class MyServer {
    public static void main(String[] args) {
        try {
            // STEP 1: Create ServerSocket on port 6666
            // Server will listen for connections on this port
            ServerSocket ss = new ServerSocket(6666);
            System.out.println("Server started. Waiting for client...");
            
            // STEP 2: Wait for client connection (BLOCKING CALL)
            // Program stops here until a client connects
            Socket s = ss.accept();
            System.out.println("Client connected!");
            
            // STEP 3: Create input stream to read data from client
            // getInputStream() returns raw bytes
            // DataInputStream wraps it for easier reading
            DataInputStream dis = new DataInputStream(s.getInputStream());
            
            // STEP 4: Read the message sent by client
            // readUTF() reads a string in UTF-8 format
            String str = (String)dis.readUTF();
            
            // STEP 5: Display the message
            System.out.println("Message received from client: " + str);
            
            // STEP 6: Close the server socket
            // This releases the port 6666
            ss.close();
            System.out.println("Server closed.");
            
        } catch(Exception e) {
            // Handle any errors (connection issues, IO errors, etc.)
            System.out.println("Error: " + e);
        }
    }
}
```

### Client Code (MyClient.java):

```java
import java.io.*;
import java.net.*;

public class MyClient {
    public static void main(String[] args) {
        try {
            // STEP 1: Create socket and connect to server
            // "localhost" means same computer (could be IP address)
            // 6666 is the port number (must match server's port)
            Socket s = new Socket("localhost", 6666);
            System.out.println("Connected to server!");
            
            // STEP 2: Create output stream to send data to server
            // getOutputStream() returns raw bytes
            // DataOutputStream wraps it for easier writing
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            
            // STEP 3: Write message to server
            // writeUTF() writes string in UTF-8 format
            dout.writeUTF("Hello Server");
            System.out.println("Message sent to server: Hello Server");
            
            // STEP 4: Flush the stream
            // Ensures data is sent immediately, not buffered
            dout.flush();
            
            // STEP 5: Close output stream
            dout.close();
            
            // STEP 6: Close socket connection
            s.close();
            System.out.println("Connection closed.");
            
        } catch(Exception e) {
            // Handle any errors (connection refused, server not running, etc.)
            System.out.println("Error: " + e);
        }
    }
}
```

---

## 8. Running the Example

### Step-by-Step Execution:

**1. Compile Both Files:**
```bash
javac MyServer.java
javac MyClient.java
```

**2. Start Server First (in Terminal/Command Prompt 1):**
```bash
java MyServer
```
**Output:**
```
Server started. Waiting for client...
[Program waits here - BLOCKED at accept()]
```

**3. Start Client (in Terminal/Command Prompt 2):**
```bash
java MyClient
```
**Client Output:**
```
Connected to server!
Message sent to server: Hello Server
Connection closed.
```

**Server Output (updates):**
```
Server started. Waiting for client...
Client connected!
Message received from client: Hello Server
Server closed.
```

---

## 9. Important Concepts

### What is "localhost" and "127.0.0.1"?
- **localhost:** Hostname referring to current computer
- **127.0.0.1:** IP address of localhost (loopback address)
- Both refer to the same machine where code is running
- Used for testing when client and server are on same computer

### What is a Port Number?
- Think of IP address as building address
- Port number is like apartment number in that building
- Helps direct traffic to specific application
- **Example:** 
  - Web server on port 80
  - Database on port 3306
  - Your application on port 6666

### Blocking vs Non-Blocking:
- **Blocking Call:** Program stops and waits (like `accept()`)
- **Non-Blocking:** Program continues execution
- `accept()` is blocking - server waits until client connects

### Data Streams:
- **InputStream:** For reading data (coming IN to program)
- **OutputStream:** For writing data (going OUT from program)
- **DataInputStream/DataOutputStream:** Convenience wrappers for reading/writing primitive types and strings

---

## 10. Real-World Analogy

Think of socket programming like a **phone call**:

**ServerSocket = Phone at Office:**
- Sits there waiting for calls (listening)
- When phone rings, you `accept()` the call
- Now you can talk through the connection

**Socket (Client) = Your Phone:**
- You dial the number (IP address and port)
- Connection establishes
- You can talk and listen

**Streams = Telephone Line:**
- **OutputStream:** Your voice going out
- **InputStream:** Their voice coming in
- Both can happen simultaneously (full duplex)

---

## 11. Common Issues and Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| "Connection refused" | Server not running | Start server before client |
| "Address already in use" | Port occupied by another program | Change port number or kill other process |
| "Connection reset" | Server closed unexpectedly | Add proper error handling |
| Client hangs | Server not calling `accept()` | Ensure server is running and listening |

---

This detailed explanation covers the fundamentals of socket programming in Java. The key is understanding that sockets provide a communication channel between two programs, with one acting as server (listener) and the other as client (connector).

---
Here’s a comprehensive explanation covering **all details mentioned in the PDF** about the topic: **InetAddress and URL classes** in Java.

***

# 2) InetAddress and URL Classes

### **Java InetAddress Class**

- **Purpose:** Represents an IP address; used to get IP addresses from hostnames (like converting `www.google.com` to its IP number).
- **Class:** `java.net.InetAddress`
- **Key Points:**
  - Contains methods to fetch IP addresses of hosts like `www.javatpoint.com`, `www.google.com`, etc.
  - IP addresses can be **32-bit** (IPv4) or **128-bit** (IPv6).
  - Each `InetAddress` instance holds an IP along with its corresponding hostname.
  - **Types of addresses:**
    - *Unicast*: Identifier for a single network interface (most common).
    - *Multicast*: Identifier for a set of network interfaces.

- **Cache Mechanism:** Stores both successful and unsuccessful hostname resolutions for efficiency.

#### **IPAddress Concepts**
- An IP address numerically identifies a network resource.
- Often paired with TCP (Transmission Control Protocol) to form a connection between the source and destination machines.

#### **Versions of IP Address**
- **IPv4:**
  - First and widely used version.
  - Deployed with ARPANET (1983).
  - Uses 32 bits (can handle just over 4 million unique addresses).
  - *Features:*
    - Connectionless protocol (data can be sent without guaranteeing delivery).
    - Minimal memory use, easy-to-remember class-based addressing.
    - Supports functionalities like video conferencing.
- **IPv6:**
  - Newer protocol designed to overcome IPv4 limitations.
  - 128-bit address space, offering 340 undecillion unique addresses.
  - Also called "IPng" (Internet Protocol Next Generation).
  - *Features:*
    - Supports both stateful and stateless configurations.
    - Includes hierarchical addressing and routing.
    - Offers Quality of Service (QoS).
  
#### **TCP/IP Protocol Overview**
- TCP/IP is the main protocol model for communication over the internet.
- **TCP:** Creates a communication channel (connection, data transmission, ensures delivery).
- **IP:** Provides unique addresses to devices on the internetwork; uses gateways to verify correct message delivery.

#### **InetAddress Methods and Example**

- **Example Code:**
```java
import java.io.*;
import java.net.*;
public class InetDemo {
    public static void main(String[] args) {
        try {
            InetAddress ip = InetAddress.getByName("www.javatpoint.com");
            System.out.println("Host Name: " + ip.getHostName());
            System.out.println("IP Address: " + ip.getHostAddress());
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```
- **Output:**
  - Host Name: www.javatpoint.com
  - IP Address: 172.67.196.82

***

### **Java URL Class**

- **Purpose:** Represents a Uniform Resource Locator (URL), which points to resources on the World Wide Web.
- **Class:** `java.net.URL`

#### **Information in a URL**
1. **Protocol:** (e.g., http, https)
2. **Server Name/IP Address:** (e.g., www.javatpoint.com)
3. **Port Number:** Optional (e.g., `:80`)
   - If not specified, Java returns -1.
4. **File/Directory Name:** (e.g., `/java-tutorial` or `index.jsp`)

#### **Constructors:**
- `URL(String spec)`
- `URL(String protocol, String host, int port, String file)`
- `URL(String protocol, String host, int port, String file, URLStreamHandler handler)`
- `URL(String protocol, String host, String file)`
- `URL(URL context, String spec)`
- `URL(URL context, String spec, URLStreamHandler handler)`

#### **Commonly Used Methods:**
Some key methods not all shown in code but typically include:
- `getProtocol()` — returns the protocol
- `getHost()` — returns host/server name
- `getPort()` — returns port number (or -1 if not specified)
- `getDefaultPort()` — returns default port for the protocol
- `getFile()` — returns file/directory path
- `getQuery()` — returns query section of the URL after `?`
- `getPath()` — returns path really, typically after the host

#### **URL Example Code 1**
```java
import java.net.*;
public class URLDemo {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://www.javatpoint.com/java-tutorial");
            System.out.println("Protocol: " + url.getProtocol());
            System.out.println("Host Name: " + url.getHost());
            System.out.println("Port Number: " + url.getPort());
            System.out.println("File Name: " + url.getFile());
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```
**Output:**
- Protocol: http
- Host Name: www.javatpoint.com
- Port Number: -1
- File Name: /java-tutorial

#### **URL Example Code 2**
```java
import java.net.*;
public class URLDemo {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://www.google.com/search?q=javatpoint&oq=javatpoint&sourceid=chrome&ie=UTF-8");
            System.out.println("Protocol: " + url.getProtocol());
            System.out.println("Host Name: " + url.getHost());
            System.out.println("Port Number: " + url.getPort());
            System.out.println("Default Port Number: " + url.getDefaultPort());
            System.out.println("Query String: " + url.getQuery());
            System.out.println("Path: " + url.getPath());
            System.out.println("File: " + url.getFile());
        } catch(Exception e){System.out.println(e);}
    }
}
```
**Output:**
- Protocol: https
- Host Name: www.google.com
- Port Number: -1
- Default Port Number: 443
- Query String: q=javatpoint&oq=javatpoint&sourceid=chrome&ie=UTF-8
- Path: /search
- File: /search?q=javatpoint&oq=javatpoint&sourceid=chrome&ie=UTF-8

***
---

# 3) TCP and UDP Protocols in Java

### **Overview**

- **TCP (Transmission Control Protocol)** is **connection-oriented**, reliable, and ensures ordered, complete data transfer. Used for things like web pages, file downloads.
- **UDP (User Datagram Protocol)** is **connectionless**, does NOT guarantee delivery, or data order, but is faster. Used for streaming, gaming, VoIP, etc.

***

### **TCP Example: Client-Server Communication (Socket & ServerSocket)**

#### **Server Side (MyServer.java)**
```java
import java.io.*;
import java.net.*;

public class MyServer {
    public static void main(String args[]) {
        try {
            ServerSocket ss = new ServerSocket(6666);
            Socket s = ss.accept(); // establishes connection
            DataInputStream dis = new DataInputStream(s.getInputStream());
            String str = (String)dis.readUTF();
            System.out.println("message = " + str);
            ss.close();
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```

#### **Client Side (MyClient.java)**
```java
import java.io.*;
import java.net.*;

public class MyClient {
    public static void main(String args[]) {
        try {
            Socket s = new Socket("localhost", 6666);
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            dout.writeUTF("Hello Server");
            dout.flush();
            dout.close();
            s.close();
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```
**How to run:**
- Compile: `javac MyServer.java MyClient.java`
- Run server in one terminal: `java MyServer`
- Run client in another: `java MyClient`

***

#### **TCP Protocol Features (from PDF)**
- **Ensures data delivery:** Order, completeness.
- **Connection-oriented:** 3-way handshake (SYN → SYN-ACK → ACK)
- **Will resend missing data**

***

### **Another TCP Example: Complete Steps and Code**

**Client Side (Client.java):**
```java
import java.io.*;
import java.net.*;
public class Client {
    public static void main(String args[]) {
        try {
            System.out.println("Client program started");
            int PORT = 9000;
            String IP = "127.0.0.1";
            Socket conn = new Socket(IP, PORT);
            DataOutputStream dos = new DataOutputStream(conn.getOutputStream());
            String mssge = "Hello Ninja";
            dos.writeUTF(mssge);
            System.out.println("Client sent the message " + mssge);
            dos.flush();
            dos.close();
            conn.close();
            System.out.println("Client program closed");
        } catch (Exception exp) {
            System.out.println(exp);
        }
    }
}
```

**Server Side (Server.java):**
```java
import java.io.*;
import java.net.*;
public class Server {
    public static void main(String args[]) {
        try {
            System.out.println("Starting the server");
            int PORT = 9000;
            ServerSocket sock = new ServerSocket(PORT);
            Socket conn = sock.accept();
            System.out.println("Client Server Connection established");
            DataInputStream dis = new DataInputStream(conn.getInputStream());
            System.out.println("Waiting for the client's message");
            String msg = (String)dis.readUTF();
            System.out.println("Message from client: " + msg);
            conn.close();
            sock.close();
            System.out.println("Closing the server");
        } catch (Exception exp) {
            System.out.println(exp);
        }
    }
}
```

***

### **UDP Programming (DatagramSocket & DatagramPacket)**

#### **Notes**
- **Classes:** `DatagramSocket`, `DatagramPacket`
- **No connection setup.**
- **No delivery/order guarantee.**

#### **Code Structure (not explicitly included in the PDF, but outlined):**
```java
// Server Side (receiving)
DatagramSocket ds = new DatagramSocket(3000);
byte[] receive = new byte[65535];
DatagramPacket DpReceive = new DatagramPacket(receive, receive.length);
ds.receive(DpReceive);
System.out.println("Received: " + new String(DpReceive.getData(), 0, DpReceive.getLength()));
ds.close();
```
```java
// Client Side (sending)
DatagramSocket ds = new DatagramSocket();
InetAddress ip = InetAddress.getLocalHost();
byte[] buf = "Hello".getBytes();
DatagramPacket DpSend = new DatagramPacket(buf, buf.length, ip, 3000);
ds.send(DpSend);
ds.close();
```
**(The PDF emphasizes these classes and their use for UDP, but does not give full code for UDP as it does for TCP.)**

***

### **Comparison Table (TCP vs UDP)**

| Aspect            | TCP                        | UDP                                  |
|-------------------|----------------------------|--------------------------------------|
| Connection        | Connection-oriented        | Connectionless                       |
| Reliability       | Reliable (guaranteed)      | Unreliable (no guarantee)            |
| Speed             | Slower                     | Faster                               |
| Java Classes      | Socket, ServerSocket       | DatagramSocket, DatagramPacket       |
| Use Cases         | Web, file transfer         | Streaming, gaming, VoIP              |
| Order of packets  | Maintained                 | Not maintained                       |

***

### **All Important Topics Included**
- Concepts, definitions, and comparisons of TCP and UDP
- How to use Java's main TCP and UDP classes
- Detailed code for TCP client-server, partial outline for UDP (as shown in the PDF)
- Real-world, step-by-step instructions and output expectations
- Features, advantages, and reasons for protocol choice

---
# 4) Multi-threaded Servers in Java

**Definition:**  
A server having more than one thread is called a **multi-threaded server**.  
When a client sends a request, the server generates a thread for that client, allowing simultaneous processing of multiple client requests.

***

### **Why Do We Need Multi-threaded Servers?**

- Accept **multiple requests** from different clients at the same time.
- Respond **quickly and efficiently** as each client connection is handled by a separate thread.
- **Waiting time decreases**; in single-threaded, clients have to wait for previous client response.
- **Threads are independent;** an error in one doesn’t affect others.

***

### **Advantages**
- **Quick, efficient response** to growing client queries.
- **Decreased waiting time** for users.
- **Thread independence.**
- **Issues in one thread** don’t affect others.

### **Disadvantages**
- **More complicated code.**
- **Difficult to debug** and analyze cause of errors in a thread-filled environment.

***

### **How Java Creates Threads**

- **Thread**: A light-weight process within a process. Allows parallel execution of code.
- **Creation Methods:**
  - **Extending Thread class**
  - **Implementing Runnable Interface**

#### **Thread By Extending Thread Class**
```java
class MultithreadingDemo extends Thread {
    public void run() {
        try {
            System.out.println("Thread " + Thread.currentThread().getId() + " is running");
        } catch(Exception e) {
            System.out.println("Exception is caught");
        }
    }
}

public class Multithread {
    public static void main(String[] args) {
        int n = 8; // Number of threads
        for (int i = 0; i < n; i++) {
            MultithreadingDemo object = new MultithreadingDemo();
            object.start();
        }
    }
}
```
**Output:**
```
Thread 15 is running
Thread 14 is running
Thread 16 is running
Thread 12 is running
Thread 11 is running
Thread 13 is running
Thread 18 is running
Thread 17 is running
```

***

## **Handling Multiple Client Connections**

**Concept:**  
To handle multiple clients, server must start a separate thread for each client connection. This allows the main server thread to keep accepting new connections.

**Typical Structure:**

1. **Main Server:** Waits for clients.
2. **ClientHandler:** Handles communication in a dedicated thread.
3. **Each client** gets its own thread.

***

### **Multi-threaded Server Example (from PDF):**

**Server Side Code**
```java
import java.net.*;
import java.io.*;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = null;
        boolean listening = true;
        try {
            serverSocket = new ServerSocket(4444);
        } catch (IOException e) {
            System.err.println("Could not listen on port 4444.");
            System.exit(-1);
        }
        while (listening) {
            new Thread(new ClientHandler(serverSocket.accept())).start();
        }
        serverSocket.close();
    }
}
```
**Details:**
- The `while (listening)` loop lets the server keep accepting client connections.
- For each accepted client, `new Thread(new ClientHandler(...)).start()` launches a new thread with the `ClientHandler` runnable.

***

**ClientHandler class (outline from PDF):**
```java
class ClientHandler implements Runnable {
    private Socket clientSocket;

    public ClientHandler(Socket socket) {
        this.clientSocket = socket;
    }

    public void run() {
        // Handle communication with this client
        // E.g., read/write data using clientSocket streams
    }
}
```
- Implement the logic for what the server does per client inside `run`.

***

### **Process Summary Table**

| Step     | Description                        | Java Element                    |
|----------|------------------------------------|---------------------------------|
| Accept   | Wait for new client connections    | `ServerSocket.accept()`         |
| Thread   | Start new thread for each client   | `new Thread(new ClientHandler())` |
| Handle   | Do client-specific work            | `ClientHandler.run()`           |

***

### **Key Points from the PDF**

- **Every connected client gets a thread;** issues in one don't affect others.
- **Server and Client Programs:** Client file – single class; Server file – server class and `ClientHandler` for multithreading.
- **Java supports concurrent execution (multithreading) for maximum CPU usage.**
- **Debugging and maintenance are harder, but performance and responsiveness improve greatly.**

  ---
# 5) Introduction to RMI (Remote Method Invocation) in Java

- **RMI** is a Java API that enables the creation of distributed applications—allowing methods to be called on objects located in different JVMs, possibly on different machines.
- **Remote Communication:** Achieved using *stub* (client-side proxy) and *skeleton* (server-side proxy, removed in newer Java versions).

***

### **Stub & Skeleton**

**Stub** (Client Side):
- Acts as a gateway for outgoing requests.
- Represents the remote object at the client side.
- Handles: connection, parameter marshaling (serializing), waits for the result, returns value to the caller.

**Skeleton** (Server Side, pre-Java 2):
- Receives incoming requests, unmarshals parameters, invokes actual remote method, marshals and returns the result.
- *Note:* Java 2 and newer use dynamic proxies so skeleton is no longer needed.

***

## **Steps for Creating RMI Application**

### **1. Create the Remote Interface**

- Extend `java.rmi.Remote`.
- All methods must declare `throws RemoteException`.

```java
import java.rmi.*;
public interface Adder extends Remote {
    public int add(int x, int y) throws RemoteException;
}
```

***

### **2. Provide Implementation of Remote Interface**

- Extend `UnicastRemoteObject` (or use exportObject).
- Define a constructor that throws `RemoteException`.

```java
import java.rmi.*;
import java.rmi.server.*;

public class AdderRemote extends UnicastRemoteObject implements Adder {
    AdderRemote() throws RemoteException {
        super();
    }
    public int add(int x, int y) { return x + y; }
}
```

***

### **3. Compile Implementation and Create Stub (and Skeleton) with rmic Tool**

- *Generate stub (and skeleton, if needed) with:*
```
rmic AdderRemote
```

***

### **4. Start the RMI Registry**

- Use the `rmiregistry` tool.
- Example (on port 5000):
```
rmiregistry 5000
```

***

### **5. Create and Run the Server Application**

- Bind your remote object to the registry using `Naming.rebind`.

```java
import java.rmi.*;
public class MyServer {
    public static void main(String args[]) {
        try {
            Adder stub = new AdderRemote();
            Naming.rebind("rmi://localhost:5000/sonoo", stub);
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```

***

### **6. Create and Run the Client Application**

- Lookup the remote object by name and call its method.

```java
import java.rmi.*;
public class MyClient {
    public static void main(String args[]) {
        try {
            Adder stub = (Adder)Naming.lookup("rmi://localhost:5000/sonoo");
            System.out.println(stub.add(34, 4));
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```

***

### **How to Run the RMI Example**

1. **Compile all Java files:**
    ```
    javac *.java
    ```
2. **Create stub (and skeleton if necessary):**
    ```
    rmic AdderRemote
    ```
3. **Start the RMI registry in a terminal:**
    ```
    rmiregistry 5000
    ```
4. **Start the server in another terminal:**
    ```
    java MyServer
    ```
5. **Start the client in another terminal:**
    ```
    java MyClient
    ```
**Output Example:**  
Client prints:  
```
38
```

***

### **Important PDF Details Included**

- **RMI enables distributed computing—method calls across JVM/machines.**
- **Stub acts as client proxy, skeleton as server proxy (not used in new Java).**
- **Six steps detailed: interface, implementation, stub, registry, server, client.**
- **Complete Java code for each file.**
- **All required commands for rmic, rmiregistry, compiling, and running given.**
Here is a **full, stepwise guide to creating and running an RMI server and client in Java**, including all details and correct outputs from your PDF:

***

## **1. Create the Remote Interface**

Extend `java.rmi.Remote` and declare methods that throw `RemoteException`.

```java
// Adder.java
import java.rmi.*;
public interface Adder extends Remote {
    public int add(int x, int y) throws RemoteException;
}
```

***

## **2. Implement the Remote Interface**

Extend `UnicastRemoteObject` or use exportObject; make a constructor throwing `RemoteException`.

```java
// AdderRemote.java
import java.rmi.*;
import java.rmi.server.*;

public class AdderRemote extends UnicastRemoteObject implements Adder {
    AdderRemote() throws RemoteException {
        super();
    }
    public int add(int x, int y) { return x + y; }
}
```

***

## **3. Compile Implementation and Create Stub**

Use the `rmic` tool to generate stub (for older Java skeleton also).

```bash
javac Adder.java AdderRemote.java
rmic AdderRemote
```

***

## **4. Start the RMI Registry**

Use the `rmiregistry` tool (use port 5000, as in the PDF).

```bash
rmiregistry 5000
```

***

## **5. Create and Run the Server Application**

The server binds the remote object to the registry.

```java
// MyServer.java
import java.rmi.*;
public class MyServer {
    public static void main(String args[]) {
        try {
            Adder stub = new AdderRemote();
            Naming.rebind("rmi://localhost:5000/sonoo", stub);
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```
**How to run:**  
```bash
javac MyServer.java
java MyServer
```

***

## **6. Create and Run the Client Application**

The client looks up the remote object and invokes its methods.

```java
// MyClient.java
import java.rmi.*;
public class MyClient {
    public static void main(String args[]) {
        try {
            Adder stub = (Adder)Naming.lookup("rmi://localhost:5000/sonoo");
            System.out.println(stub.add(34, 4));
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```
**How to run:**  
```bash
javac MyClient.java
java MyClient
```

***

## **Expected Outputs for Each Program**

### **When Running Server:**  
- If the binding succeeds, it will be silent or may just show exceptions if any.  
- For example, if successful:  
  *(No output; ready to serve requests)*

### **When Running Client:**  
- The client will output the result of the remote method call.  
- **Output:**  
```
38
```
_This output is from the statement: `System.out.println(stub.add(34, 4));` when `34 + 4` is computed on the server and returned._

***

## **Summary Table – RMI Application Lifecycle**

| Step          | Command/File/Action                         | Output/Result          |
|---------------|---------------------------------------------|------------------------|
| 1. Interface  | Adder.java                                  | (No console output)    |
| 2. Impl.      | AdderRemote.java                            | (No console output)    |
| 3. Compile    | javac Adder.java AdderRemote.java           | (Generates .class)     |
|               | rmic AdderRemote                            | (Generates stub)       |
| 4. Registry   | rmiregistry 5000                            | (No output)            |
| 5. Server     | MyServer.java / java MyServer               | (No output)            |
| 6. Client     | MyClient.java / java MyClient               | **38**                 |

***

## **All PDF Details Included**
- RMI intro, distributed computing, stub/skeleton concepts
- Full stepwise setup and explanations
- Remote interface and implementation code  
- Stub generation and registry details
- Server and client complete code

---
# 6) Java RMI and Object Serialization

### **What is Serialization in Java?**

- **Serialization:** The process of converting an object into a byte stream, so it can be transported over a network (to another JVM using RMI) or persisted to disk.
- **Deserialization:** The process of reconstructing the object from its byte stream.

**Serialization is key for RMI:**  
- When you need to transfer objects between JVMs via remote method calls, those objects must be _serializable_.
- Any object (including user-defined objects, lists, etc.) sent as a parameter or a return value in a remote method must implement the `Serializable` interface.

***

### **Serializable Interface and Example**

- **Interface:** `java.io.Serializable` (marker interface, no methods)
- **Fields marked `transient`:** Are _not_ serialized.

```java
// FSFile.java
import java.io.*;
public class FSFile implements Serializable {
    public static final int READ = 0;
    public static final int WRITE = 1;
    private int flag;
    private String filename;
    private transient BufferedWriter writer;
    private transient BufferedReader reader;

    // Custom serialization methods
    private void writeObject(ObjectOutputStream stream) throws IOException {
        stream.defaultWriteObject();
        stream.writeObject(writer);
        stream.writeObject(reader);
    }

    private void readObject(ObjectInputStream stream) throws IOException, ClassNotFoundException {
        stream.defaultReadObject();
        writer = (BufferedWriter) stream.readObject();
        reader = (BufferedReader) stream.readObject();
    }
}
```

- **Key Points:**  
  - You can control serialization of non-serializable fields (like streams) by providing custom `writeObject` and `readObject` methods.
  - The `transient` keyword is used to prevent serialization of fields that cannot or should not be serialized.

***

### **Object Serialization in RMI**

**How it works in RMI:**
- All objects sent as arguments OR returned as results in remote methods MUST be serializable.
- Example: Suppose you have a file service, and you want to transfer a file object (like `FSFile` above) between server and client via RMI.

***

### **Step-by-step Use Case of Serializable Object with RMI (based on PDF)**

#### **1. Define a Serializable Class (see FSFile above)**

#### **2. Use as Parameter or Return Type in Remote Interface**

```java
// FileService.java
import java.rmi.*;
public interface FileService extends Remote {
    public FSFile getFile(String filename) throws RemoteException;
}
```

#### **3. Server Implementation Sends Serializable Object**

```java
// FileServiceImpl.java
import java.rmi.server.*;
import java.rmi.*;
public class FileServiceImpl extends UnicastRemoteObject implements FileService {
    public FileServiceImpl() throws RemoteException { super(); }
    public FSFile getFile(String filename) throws RemoteException {
        // return a new FSFile object which is serializable
        return new FSFile(filename, FSFile.READ);
    }
}
```

#### **4. Client Receives Serializable Object**

```java
// FileClient.java
import java.rmi.*;
public class FileClient {
    public static void main(String[] args) {
        try {
            FileService service = (FileService)Naming.lookup("rmi://localhost:5000/fileservice");
            FSFile file = service.getFile("example.txt");
            System.out.println("Filename: " + file.getFilename());
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```

***

### **Expected Output**

- **On the client terminal**, you see something like:
```
Filename: example.txt
```
(The actual output may include more details if you print other FSFile fields.)

***

### **Summary Table – Serialization in RMI**

| Aspect                     | Implementation                      | Output                                       |
|----------------------------|--------------------------------------|----------------------------------------------|
| Serializable Interface     | `implements Serializable`            | (No output, marker interface)                |
| Custom Serialization       | `writeObject` and `readObject`       | (No output, except possible exceptions)      |
| RMI Transfer (Client Side) | Received object usable as normal     | `Filename: example.txt`                      |

***

### **Key PDF Points Covered**

- **Definition and importance of serialization for RMI**
- **How to make classes serializable, and control serialization with transient, writeObject/readObject**
- **How RMI uses serialized objects for method parameters and return values across JVMs**
- **Full code sample for a serializable class, and use in a real RMI scenario**
- **Output expectation when client receives and uses the serializable object**
---

# 7) Connecting to Databases with JDBC – 5 Steps**

JDBC (Java Database Connectivity) is a Java API for interacting with databases from Java applications.

### **The Five Steps**:

### **1. Register the Driver Class**

Most commonly, you load the database driver class dynamically.  
*Note: From JDBC 4.0, this step is optional if you have the vendor JAR in classpath.*

```java
Class.forName("oracle.jdbc.driver.OracleDriver");
```

**For MySQL**:  
```java
Class.forName("com.mysql.cj.jdbc.Driver");
```
If successful, this loads and registers the driver with the JDBC DriverManager.  
(If the class is missing, you'll get `ClassNotFoundException`.)

***

### **2. Create the Connection Object**

Use `DriverManager.getConnection()` to establish a connection.

```java
Connection con = DriverManager.getConnection(
    "jdbc:oracle:thin:@localhost:1521:xe", "system", "password");
```
or (for MySQL):

```java
Connection con = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/books", "root", "password");
```
- Returns a `Connection` object if successful.
- If the DB is down, wrong username/password, or JDBC URL is wrong, you'll get a `SQLException`.

***

### **3. Create the Statement Object**

Use the `createStatement()` method to create a `Statement`.

```java
Statement stmt = con.createStatement();
```
- This `Statement` object will be used to execute SQL queries.

***

### **4. Execute Queries**

Use the `executeQuery()` method for reading data (`SELECT`), and `executeUpdate()` for updates (`INSERT`, `UPDATE`, `DELETE`).

**Example – Selecting Data**:

```java
ResultSet rs = stmt.executeQuery("select * from emp");
while (rs.next()) {
    System.out.println(rs.getInt(1) + " " + rs.getString(2));
}
```
- This prints each row from the "emp" table, displaying the first two columns.

***

### **5. Close the Connection**

It's important to release database resources by closing the connection.

```java
con.close();
```
By closing the connection object, statement and ResultSet will be closed automatically.

***

## **Complete Example (from PDF): Retrieve Data from MySQL**

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class RetrieveDataExample {
    public static void main(String[] args) {
        try {
            // 1. Load the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2. Establish connection with the database
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/books", "root", "password"
            );

            if (con != null) {
                // 3. SQL query to retrieve data from the 'book' table
                String selectQuery = "SELECT * FROM book";
                Statement statement = con.createStatement();

                // 4. Execute the query and get the result set
                ResultSet resultSet = statement.executeQuery(selectQuery);
                System.out.println("The Available Data\n");

                // 5. Iterate through the result set and print the data
                while (resultSet.next()) {
                    int id = resultSet.getInt("id");
                    String author_name = resultSet.getString("author");
                    String book_name = resultSet.getString("name");
                    String book_price = resultSet.getString("price");
                    // print the retrieved data
                    System.out.println(
                        "ID: " + id +
                        ", Author_Name: " + author_name +
                        ", Book_Name: " + book_name +
                        ", Book_Price " + book_price
                    );
                }
            } else {
                System.out.println("Not Connected...");
            }
        } catch (Exception e) {
            System.out.println("Exception is " + e.getMessage());
        }
    }
}
```

***

## **Expected Output (Assuming Book Table Data is Present):**
```
The Available Data

ID: 1, Author_Name: John Doe, Book_Name: Java Basics, Book_Price 400
ID: 2, Author_Name: Mary Smith, Book_Name: NetworkX, Book_Price 350
...
```

Output will display every row present in the `book` table, formatted as above.

***

## **Summary Table**

| Step             | Code/Command                                                                | Output If Success                    |
|------------------|----------------------------------------------------------------------------|--------------------------------------|
| Register Driver  | `Class.forName(...)`                                                       | (No output, or ClassNotFoundException) |
| Create Conn      | `DriverManager.getConnection(...)`                                         | (No output, or SQLException)         |
| Create Statement | `con.createStatement()`                                                    | (No output)                          |
| Execute Query    | `statement.executeQuery("SELECT ...")`                                     | Rows printed by loop                 |
| Close Conn       | `con.close()`                                                              | (No output)                          |

---
