# Socket Programming in Java - Detailed Explanation

## 1) What is Socket Programming?

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

**Everything above summarizes all instructive content from the PDF about these classes, including their real use, differences between IP versions, constructor variations, caching, and typical usage with Java code and output examples.**

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/68867823/9a9975f6-a6f4-4ffa-a8cc-c422f541ca51/4.pdf)
