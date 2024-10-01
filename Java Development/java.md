# Java interview

To prepare for a Java interview, it's essential to understand both **core concepts** and **advanced topics**. Below is a structured approach to help you master Java for interview preparation, covering key concepts and providing examples.

### 1. **Java Basics**

#### a. Data Types and Variables

- Understand primitive data types (`int`, `char`, `float`, `double`, `boolean`, etc.).
- Difference between primitive types and reference types.

   ```java
   int age = 25;
   double salary = 5000.50;
   char grade = 'A';
   boolean isValid = true;
   ```

#### b. Operators

- Know the different types of operators: arithmetic, relational, logical, bitwise, and assignment.

   ```java
   int a = 10, b = 20;
   int sum = a + b;  // Arithmetic
   boolean result = (a == b);  // Relational
   boolean logical = (a > b) && (a != 0);  // Logical
   ```

#### c. Control Flow (Loops, Conditionals)

- **Conditionals**: `if-else`, `switch`.
- **Loops**: `for`, `while`, `do-while`.

   ```java
   if (age > 18) {
       System.out.println("Adult");
   } else {
       System.out.println("Minor");
   }

   for (int i = 0; i < 5; i++) {
       System.out.println("Count: " + i);
   }
   ```

### 2. **Object-Oriented Programming (OOP)**

#### a. Classes and Objects

- Understand how to define classes, create objects, and work with fields and methods.

   ```java
   class Person {
       String name;
       int age;

       void greet() {
           System.out.println("Hello, my name is " + name);
       }
   }

   public class Main {
       public static void main(String[] args) {
           Person p1 = new Person();
           p1.name = "John";
           p1.age = 30;
           p1.greet();
       }
   }
   ```

#### b. Encapsulation

- Encapsulation is about bundling data and methods that operate on the data into a single unit (class), and restricting access using access modifiers (`private`, `public`, `protected`).

   ```java
   class Account {
       private double balance;

       public void deposit(double amount) {
           if (amount > 0) {
               balance += amount;
           }
       }

       public double getBalance() {
           return balance;
       }
   }
   ```

#### c. Inheritance

- **Inheritance** allows a class to inherit properties and methods from another class.

   ```java
   class Animal {
       void makeSound() {
           System.out.println("Animal makes sound");
       }
   }

   class Dog extends Animal {
       void makeSound() {
           System.out.println("Dog barks");
       }
   }

   public class Main {
       public static void main(String[] args) {
           Dog d = new Dog();
           d.makeSound();  // Output: Dog barks
       }
   }
   ```

#### d. Polymorphism

- **Method Overloading**: Same method name, different parameters.
- **Method Overriding**: Subclass provides its own implementation of a method defined in the superclass.

   ```java
   // Overloading
   class MathOperation {
       int add(int a, int b) {
           return a + b;
       }

       double add(double a, double b) {
           return a + b;
       }
   }

   // Overriding
   class Parent {
       void display() {
           System.out.println("Parent Display");
       }
   }

   class Child extends Parent {
       @Override
       void display() {
           System.out.println("Child Display");
       }
   }

   public class Main {
       public static void main(String[] args) {
           Parent p = new Child();  // Polymorphism
           p.display();  // Output: Child Display
       }
   }
   ```

#### e. Abstraction

- **Abstract Classes**: Classes that cannot be instantiated, used to provide a base for subclasses.
- **Interfaces**: Define methods that a class must implement without providing the implementation itself.

   ```java
   // Abstract class
   abstract class Shape {
       abstract void draw();  // Abstract method
   }

   class Circle extends Shape {
       @Override
       void draw() {
           System.out.println("Drawing Circle");
       }
   }

   // Interface
   interface Drawable {
       void draw();  // Abstract method in interface
   }

   class Square implements Drawable {
       @Override
       public void draw() {
           System.out.println("Drawing Square");
       }
   }
   ```

### 3. [**Java Collections Framework**](#java-collections-framework)

- **Lists**: `ArrayList`, `LinkedList`.
- **Sets**: `HashSet`, `TreeSet`.
- **Maps**: `HashMap`, `TreeMap`.
- **Queues**: `PriorityQueue`.

   ```java
   import java.util.*;

   public class Main {
       public static void main(String[] args) {
           // List Example
           List<String> list = new ArrayList<>();
           list.add("Apple");
           list.add("Banana");

           // HashMap Example
           Map<Integer, String> map = new HashMap<>();
           map.put(1, "One");
           map.put(2, "Two");

           System.out.println(map.get(1));  // Output: One
       }
   }
   ```

### 4. **Exception Handling**

- Learn how to handle errors using `try`, `catch`, `finally`, and `throw`.

   ```java
   public class Main {
       public static void main(String[] args) {
           try {
               int division = 10 / 0;
           } catch (ArithmeticException e) {
               System.out.println("Cannot divide by zero");
           } finally {
               System.out.println("Always execute");
           }
       }
   }
   ```

### 5. [**Multithreading and Concurrency**](#multithreading-and-concurrency)

- Understand how to create threads using `Thread` and `Runnable`.
- Learn about `synchronized`, `wait()`, `notify()`, and `notifyAll()` for thread communication.

   ```java
   class MyThread extends Thread {
       public void run() {
           System.out.println("Thread running");
       }
   }

   public class Main {
       public static void main(String[] args) {
           MyThread t1 = new MyThread();
           t1.start();  // Starting the thread
       }
   }
   ```

### 6. **Java 8 Features**

- **Lambda Expressions**: Introduced in Java 8 to allow functional programming.

   ```java
   interface Operation {
       int add(int a, int b);
   }

   public class Main {
       public static void main(String[] args) {
           Operation addition = (a, b) -> a + b;
           System.out.println(addition.add(5, 3));  // Output: 8
       }
   }
   ```

- **Streams**: For working with collections in a functional style.

   ```java
   import java.util.Arrays;
   import java.util.List;

   public class Main {
       public static void main(String[] args) {
           List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

           numbers.stream()
               .filter(n -> n % 2 == 0)
               .forEach(System.out::println);  // Output: 2 4
       }
   }
   ```

### 7. **Common Interview Topics**

#### a. **Immutable Objects**

- Understanding how to create immutable classes like `String` in Java.

   ```java
   final class ImmutableClass {
       private final String name;

       public ImmutableClass(String name) {
           this.name = name;
       }

       public String getName() {
           return name;
       }
   }
   ```

#### b. **Singleton Pattern**

- How to create a class with only one instance in the application.

   ```java
   class Singleton {
       private static Singleton instance = null;

       private Singleton() {}  // Private constructor

       public static Singleton getInstance() {
           if (instance == null) {
               instance = new Singleton();
           }
           return instance;
       }
   }
   ```

#### c. **Equals and HashCode**

- Understand how to properly override `equals()` and `hashCode()` for objects.

   ```java
   class Person {
       private String name;
       private int id;

       @Override
       public boolean equals(Object o) {
           if (this == o) return true;
           if (o == null || getClass() != o.getClass()) return false;
           Person person = (Person) o;
           return id == person.id && name.equals(person.name);
       }

       @Override
       public int hashCode() {
           return Objects.hash(name, id);
       }
   }
   ```

### Interview Tips

- **Be ready for coding questions**: You might be asked to solve problems using arrays, strings, linked lists, or trees.
- **Explain OOP concepts clearly**: Be prepared to give real-world examples.
- **Understand Java memory management**: Explain how the heap, stack, and garbage collection work.
- **Be familiar with Java’s concurrency**: Know the difference between threads and processes, and how synchronization works.

---

# Important Topics

Here’s a list of the **most important Java interview topics** that you should be well-versed in, broken down into categories:

### 1. **Core Java Concepts**

- **Data Types, Variables, and Operators**: Primitive types, reference types, and various operators (arithmetic, relational, logical, bitwise).
- **Control Flow**: If-else, switch, loops (`for`, `while`, `do-while`).
- **Arrays and Strings**:
  - Multi-dimensional arrays.
  - String manipulation and String immutability.
- **Object-Oriented Programming (OOP)**:
  - **Encapsulation**: Access modifiers and getter/setter methods.
  - **Inheritance**: `extends` keyword, method overriding.
  - **Polymorphism**:
    - **Overloading**: Same method name, different parameters.
    - **Overriding**: Subclass redefines superclass methods.
  - **Abstraction**: Difference between abstract classes and interfaces.
  - **Interfaces vs Abstract Classes**: When to use which.
- **Constructors**: Types of constructors, constructor chaining, use of `this()` and `super()`.
- **Static and Final Keywords**: How and when to use them.

### 2. **Java Memory Management**

- **Heap vs Stack**: Understanding the memory areas where objects and variables are stored.
- **Garbage Collection**: How Java manages memory and how to handle memory leaks.
- **Final, Finally, and Finalize**:
  - `final` keyword (in variables, methods, and classes).
  - `finally` block in exception handling.
  - `finalize()` method and its use in garbage collection.

### 3. **Exception Handling**

- **Checked vs Unchecked Exceptions**.
- **Try-catch-finally**: Exception propagation, rethrowing exceptions.
- **Custom Exceptions**: How to define your own exception class.

   ```java
   public class CustomException extends Exception {
       public CustomException(String message) {
           super(message);
       }
   }
   ```

### 4. **Java Collections Framework**

- **List, Set, Map** Interfaces:
  - `ArrayList` vs `LinkedList`.
  - `HashSet` vs `TreeSet`.
  - `HashMap`, `TreeMap`, `LinkedHashMap`.
- **Queue and Deque**: `PriorityQueue`, `ArrayDeque`.
- **Comparable vs Comparator**: Sorting custom objects.
- **Iterators**: Usage of `Iterator` and `ListIterator`.

   ```java
   class Person implements Comparable<Person> {
       private String name;
       private int age;

       @Override
       public int compareTo(Person other) {
           return this.age - other.age;  // Compare by age
       }
   }
   ```

### 5. **Multithreading and Concurrency**

- **Thread Lifecycle**: States of a thread (New, Runnable, Blocked, Waiting, Timed Waiting, Terminated).
- **Creating Threads**: Using `Thread` class and `Runnable` interface.
- **Synchronization**: `synchronized` keyword, `wait()`, `notify()`, and `notifyAll()`.
- **Concurrency Utilities**: `ExecutorService`, `Future`, `Callable`, `CountDownLatch`.

   ```java
   class MyThread extends Thread {
       public void run() {
           System.out.println("Thread running");
       }
   }

   public class Main {
       public static void main(String[] args) {
           MyThread t1 = new MyThread();
           t1.start();  // Starts the thread
       }
   }
   ```

### 6. **Java 8 Features**

- **Lambda Expressions**: Syntax and usage.
- **Streams API**: Working with collections in a functional style (`filter()`, `map()`, `reduce()`).
- **Optional**: Avoiding `NullPointerException`.
- **Functional Interfaces**: `Predicate`, `Function`, `Supplier`, `Consumer`.
- **Default and Static Methods in Interfaces**: How Java 8 changed interfaces.

   ```java
   List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
   names.stream()
       .filter(name -> name.startsWith("A"))
       .forEach(System.out::println);
   ```

### 7. **Design Patterns**

- **Singleton**: Ensuring only one instance of a class exists.
- **Factory Pattern**: Creating objects without exposing the creation logic.
- **Builder Pattern**: Handling complex constructors and immutability.
- **Observer Pattern**: When an object needs to notify multiple observers.
- **Decorator Pattern**: Dynamically adding behavior to objects.
- **Strategy Pattern**: Encapsulating algorithms for dynamic selection.

   ```java
   class Singleton {
       private static Singleton instance;

       private Singleton() {}  // Private constructor

       public static Singleton getInstance() {
           if (instance == null) {
               instance = new Singleton();
           }
           return instance;
       }
   }
   ```

### 8. **JVM, JRE, JDK**

- **JVM (Java Virtual Machine)**: How it works and why it matters.
- **JRE (Java Runtime Environment)**: What it includes.
- **JDK (Java Development Kit)**: Compiler, libraries, etc.
- **Class Loaders**: Boot, extension, and application class loaders.

### 9. **Input and Output (I/O)**

- **File I/O**: Reading and writing files using `FileInputStream`, `FileOutputStream`, `BufferedReader`, and `BufferedWriter`.
- **Serialization**: Converting an object into a byte stream and vice versa (`Serializable` interface).
- **NIO (New I/O)**: Using `Path`, `Files`, and `ByteBuffer`.

   ```java
   try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
       String line;
       while ((line = reader.readLine()) != null) {
           System.out.println(line);
       }
   } catch (IOException e) {
       e.printStackTrace();
   }
   ```

### 10. **Java Memory Model (JMM)**

- **Volatile Keyword**: Ensures visibility of changes to variables across threads.
- **Happens-Before Relationship**: Ensures memory visibility between threads.
- **Locks and Monitors**: How intrinsic locks work in Java.

### 11. **Java Annotations**

- Custom annotations.
- Commonly used annotations like `@Override`, `@Deprecated`, `@FunctionalInterface`, and `@SuppressWarnings`.

   ```java
   @Override
   public String toString() {
       return "Overriding toString method";
   }
   ```

### 12. **Immutable Classes**

- How to create classes that cannot be changed after instantiation (`String` class as an example).

   ```java
   final class ImmutablePerson {
       private final String name;
       private final int age;

       public ImmutablePerson(String name, int age) {
           this.name = name;
           this.age = age;
       }

       public String getName() {
           return name;
       }

       public int getAge() {
           return age;
       }
   }
   ```

### 13. **Database Connectivity (JDBC)**

- How to connect to a database using Java.
- Steps involved in creating a connection, executing queries, and closing resources.

   ```java
   Connection conn = DriverManager.getConnection(url, user, password);
   Statement stmt = conn.createStatement();
   ResultSet rs = stmt.executeQuery("SELECT * FROM users");

   while (rs.next()) {
       System.out.println(rs.getString("username"));
   }
   ```

### 14. **Unit Testing with JUnit**

- Writing unit tests using **JUnit**.
- Understanding annotations like `@Test`, `@Before`, `@After`, `@BeforeClass`, and `@AfterClass`.
- **Mockito** for mocking objects in unit tests.

   ```java
   import static org.junit.Assert.*;
   import org.junit.Test;

   public class CalculatorTest {
       @Test
       public void testAdd() {
           Calculator calc = new Calculator();
           assertEquals(10, calc.add(5, 5));
       }
   }
   ```

---

### **General Interview Tips**

- **Know the Basics Well**: Interviewers often focus on core Java concepts like OOP, data structures, and algorithms.
- **Practice Coding Problems**: Be comfortable solving problems involving arrays, strings, linked lists, and recursion.
- **Understand Real-World Usage**: Be able to explain how the concepts apply in real-world scenarios.
- **Design Patterns**: Be prepared to discuss and implement design patterns based on problem descriptions.
- **Multithreading and Concurrency**: Most companies value knowledge about threads, synchronization, and concurrency, especially for high-performance applications.
- **Prepare for Behavioral Questions**: Apart from technical skills, companies often evaluate how you approach problem-solving and work in a team environment.

---

# Multithreading and Concurrency

Multithreading and concurrency are essential topics in Java, especially for building high-performance applications. Understanding how to create and manage threads, synchronize access to shared resources, and handle concurrent operations is crucial for writing efficient and scalable Java programs.

### Multithreading and Concurrency in Java

Multithreading and concurrency are crucial topics in Java, especially for building high-performance applications. Here's a comprehensive guide to understanding these concepts:

---

### 1. **What is Multithreading?**

Multithreading refers to the concurrent execution of multiple threads within a single program. A **thread** is a lightweight sub-process, the smallest unit of processing. Java supports multithreading by providing built-in classes and methods to manage threads.

Key terms:

- **Thread**: A small unit of process.
- **Multithreading**: Running multiple threads concurrently.
- **Concurrency**: Multiple tasks being processed at the same time.

---

### 2. **Thread Life Cycle**

A thread can be in one of several states:

1. **New**: The thread is created but hasn’t started.
2. **Runnable**: The thread is ready to run but waiting for CPU time.
3. **Blocked**: The thread is waiting for a monitor lock or some condition.
4. **Waiting**: The thread is waiting indefinitely for another thread to perform a specific action.
5. **Timed Waiting**: The thread is waiting for a specific period of time.
6. **Terminated**: The thread has finished execution.

---

### 3. **Creating Threads in Java**

Java provides two main ways to create a thread:

#### (a) **Extending the `Thread` class**

You can create a new thread by extending the `Thread` class and overriding its `run()` method.

```java
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread is running");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start();  // Start the thread
    }
}
```

#### (b) **Implementing the `Runnable` interface**

This is the preferred approach, as it allows the class to extend other classes as well.

```java
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Thread is running");
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();  // Start the thread
    }
}
```

#### Thread Creation Key Points

- **`start()`**: Creates a new thread and starts executing the `run()` method.
- **`run()`**: Contains the code that will be executed by the thread.

---

### 4. **Thread Synchronization**

When multiple threads access shared resources concurrently, it can lead to **data inconsistency**. Java provides mechanisms to handle this through **synchronization**.

#### (a) **Synchronized Methods**

When a method is declared `synchronized`, only one thread can execute it at a time for a given object.

```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Thread t1 = new Thread(() -> { for(int i=0; i<1000; i++) counter.increment(); });
        Thread t2 = new Thread(() -> { for(int i=0; i<1000; i++) counter.increment(); });

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println(counter.getCount());  // Output will be 2000
    }
}
```

#### (b) **Synchronized Blocks**

Instead of synchronizing the entire method, you can synchronize a block of code to reduce overhead.

```java
class Counter {
    private int count = 0;

    public void increment() {
        synchronized (this) {
            count++;
        }
    }
}
```

#### (c) **Static Synchronization**

If you want to synchronize a class-level method, you can synchronize it using the `static` keyword.

```java
class Counter {
    private static int count = 0;

    public static synchronized void increment() {
        count++;
    }
}
```

---

### 5. **Inter-Thread Communication**

Java provides methods like `wait()`, `notify()`, and `notifyAll()` for thread communication when threads need to wait for a condition or signal other threads.

- **`wait()`**: The thread releasing the monitor goes into waiting mode until another thread invokes `notify()` or `notifyAll()`.
- **`notify()`**: Wakes up one waiting thread.
- **`notifyAll()`**: Wakes up all waiting threads.

Example:

```java
class Data {
    private int number;
    private boolean available = false;

    public synchronized void produce(int number) throws InterruptedException {
        while (available) {
            wait();  // Wait if data is already available
        }
        this.number = number;
        available = true;
        notify();  // Notify the consumer
    }

    public synchronized int consume() throws InterruptedException {
        while (!available) {
            wait();  // Wait if data is not available
        }
        available = false;
        notify();  // Notify the producer
        return number;
    }
}
```

---

### 6. **Concurrency Utilities (Java `java.util.concurrent` Package)**

The `java.util.concurrent` package provides advanced concurrency utilities to manage multithreading more efficiently.

#### (a) **Executor Framework**

Instead of manually creating and managing threads, Java provides an **ExecutorService** interface for managing a pool of threads.

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        Runnable task1 = () -> System.out.println("Task 1");
        Runnable task2 = () -> System.out.println("Task 2");

        executor.submit(task1);
        executor.submit(task2);

        executor.shutdown();
    }
}
```

#### (b) **Callable and Future**

`Callable` is similar to `Runnable`, but it can return a result or throw an exception. You can use `Future` to get the result of a `Callable`.

```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        Callable<Integer> task = () -> {
            TimeUnit.SECONDS.sleep(1);
            return 42;
        };

        Future<Integer> result = executor.submit(task);

        System.out.println("Result: " + result.get());  // Blocks until the result is available

        executor.shutdown();
    }
}
```

#### (c) **CountDownLatch**

Used to make one thread wait for multiple other threads to complete their tasks.

```java
import java.util.concurrent.CountDownLatch;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch latch = new CountDownLatch(2);

        Runnable task = () -> {
            System.out.println("Task started");
            latch.countDown();  // Decrement the count of the latch
        };

        new Thread(task).start();
        new Thread(task).start();

        latch.await();  // Wait for the latch count to reach zero
        System.out.println("All tasks completed");
    }
}
```

#### (d) **CyclicBarrier**

It allows multiple threads to wait for each other at a common barrier point before continuing execution.

```java
import java.util.concurrent.CyclicBarrier;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        CyclicBarrier barrier = new CyclicBarrier(3);

        Runnable task = () -> {
            try {
                System.out.println("Waiting at barrier");
                barrier.await();  // Wait for all threads to reach the barrier
                System.out.println("Barrier crossed");
            } catch (Exception e) {
                e.printStackTrace();
            }
        };

        new Thread(task).start();
        new Thread(task).start();
        new Thread(task).start();
    }
}
```

---

### 7. **Locks and Synchronizers**

#### (a) **ReentrantLock**

Provides more control than `synchronized` blocks. You can lock and unlock manually, try to lock without waiting, and interrupt lock attempts.

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Main {
    private final Lock lock = new ReentrantLock();

    public void accessResource() {
        lock.lock();
        try {
            System.out.println("Resource accessed");
        } finally {
            lock.unlock();
        }
    }
}
```

#### (b) **ReadWriteLock**

Allows multiple threads to read simultaneously while allowing only one thread to write at a time.

---

### 8. **Volatile Keyword**

The `volatile` keyword ensures that changes made to a variable by one thread are visible to other threads. This is essential for variables that are accessed and modified by multiple threads.

```java
public class Main {
    private volatile boolean flag = false;

    public void setFlagTrue() {
        flag = true;
    }

    public void checkFlag() {
        while (!flag) {
            // Do something until flag becomes true
        }
    }
}
```

---

# **Java Collections Framework**

The **Java Collections Framework (JCF)** is a fundamental part of the Java programming language, providing data structures and algorithms to store, retrieve, and manipulate collections of objects. It offers a set of interfaces, classes, and algorithms for working with groups of objects. This framework is widely used in real-world applications for tasks such as sorting, searching, and maintaining a dynamic collection of elements.

### Key Components of the Java Collections Framework

1. **Interfaces**: Define common methods for collections.
2. **Implementations**: Concrete classes (like `ArrayList`, `HashSet`, `HashMap`) that implement these interfaces.
3. **Algorithms**: Utility methods for common operations like sorting and searching.

---

### 1. **Core Interfaces**

The JCF is built around several core interfaces:

- **Collection**: The root interface for most of the JCF.
  - **List**: Ordered collection (can contain duplicates). Implements `Collection`.
  - **Set**: Unordered collection (no duplicates). Implements `Collection`.
  - **Queue**: A collection used for holding elements prior to processing.
  - **Map**: A collection that maps keys to values (key-value pairs, no duplicate keys).

#### Example of Core Interfaces and Hierarchy

```
Collection
  ├── List
  │   ├── ArrayList
  │   └── LinkedList
  ├── Set
  │   ├── HashSet
  │   └── TreeSet
  └── Queue
      ├── PriorityQueue
      └── LinkedList
Map
  ├── HashMap
  └── TreeMap
```

---

### 2. **List Interface**

The **List** interface represents an ordered collection (sequence) of elements. It can contain duplicate elements. Lists allow random access to elements and can be easily iterated.

#### Common Implementations

- **ArrayList**: Resizable array implementation.
- **LinkedList**: Doubly linked list implementation.

#### Example: Using `ArrayList`

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Orange");
        list.add("Banana");  // Duplicates allowed in List

        System.out.println(list);  // [Apple, Banana, Orange, Banana]

        // Accessing elements
        System.out.println(list.get(1));  // Banana
        
        // Iterating through the list
        for (String fruit : list) {
            System.out.println(fruit);
        }
    }
}
```

#### Example: Using `LinkedList`

```java
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.add("Apple");
        linkedList.add("Banana");
        linkedList.add("Orange");

        // Adding elements at specific positions
        linkedList.addFirst("Mango");
        linkedList.addLast("Grapes");

        System.out.println(linkedList);  // [Mango, Apple, Banana, Orange, Grapes]

        // Removing elements
        linkedList.removeFirst();
        linkedList.removeLast();

        System.out.println(linkedList);  // [Apple, Banana, Orange]
    }
}
```

---

### 3. **Set Interface**

A **Set** is a collection that contains no duplicate elements. It models the mathematical set abstraction. Common implementations of Set are `HashSet`, `LinkedHashSet`, and `TreeSet`.

#### Common Implementations

- **HashSet**: Unordered, backed by a hash table.
- **LinkedHashSet**: Ordered version of `HashSet` (maintains insertion order).
- **TreeSet**: Sorted set implementation using a red-black tree.

#### Example: Using `HashSet`

```java
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Orange");
        set.add("Banana");  // Duplicate, won't be added

        System.out.println(set);  // [Apple, Orange, Banana] (order may vary)

        // Checking existence of an element
        System.out.println(set.contains("Banana"));  // true
    }
}
```

#### Example: Using `TreeSet` (Sorted Set)

```java
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>();
        set.add(30);
        set.add(10);
        set.add(20);

        System.out.println(set);  // [10, 20, 30] (sorted order)
        
        // Navigating elements
        System.out.println(set.first());  // 10
        System.out.println(set.last());   // 30
    }
}
```

---

### 4. **Map Interface**

A **Map** is an object that maps keys to values. Each key can map to at most one value. `Map` is not a subtype of `Collection`.

#### Common Implementations

- **HashMap**: Unordered map backed by a hash table.
- **LinkedHashMap**: Ordered version of `HashMap` (maintains insertion order).
- **TreeMap**: Sorted map implementation.

#### Example: Using `HashMap`

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("Apple", 1);
        map.put("Banana", 2);
        map.put("Orange", 3);
        
        System.out.println(map);  // {Apple=1, Banana=2, Orange=3}

        // Accessing values using keys
        System.out.println(map.get("Banana"));  // 2

        // Iterating over keys and values
        for (String key : map.keySet()) {
            System.out.println(key + ": " + map.get(key));
        }
    }
}
```

#### Example: Using `TreeMap` (Sorted Map)

```java
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) {
        TreeMap<String, Integer> map = new TreeMap<>();
        map.put("Orange", 3);
        map.put("Banana", 2);
        map.put("Apple", 1);

        System.out.println(map);  // {Apple=1, Banana=2, Orange=3} (sorted by key)
    }
}
```

---

### 5. **Queue Interface**

A **Queue** is used to hold elements before processing. Queues typically follow a FIFO (First In, First Out) order. Common implementations are `PriorityQueue` and `LinkedList`.

#### Common Implementations

- **PriorityQueue**: Elements are ordered according to their natural ordering or by a comparator provided at queue construction.
- **LinkedList**: Can act as a queue as well as a list.

#### Example: Using `PriorityQueue`

```java
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        queue.add(30);
        queue.add(10);
        queue.add(20);

        // Polling elements in priority order
        System.out.println(queue.poll());  // 10 (lowest element)
        System.out.println(queue.poll());  // 20
        System.out.println(queue.poll());  // 30
    }
}
```

---

### 6. **Iterators**

The `Iterator` interface allows you to traverse collections like `List`, `Set`, and `Map`.

#### Example: Using `Iterator`

```java
import java.util.ArrayList;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Orange");

        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
```

---

### 7. **Collections Utility Class**

The `Collections` class provides static methods for manipulating collections, like sorting and searching.

#### Example: Sorting a List

```java
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(30);
        list.add(10);
        list.add(20);

        // Sorting the list
        Collections.sort(list);

        System.out.println(list);  // [10, 20, 30]
    }
}
```

---

### Summary of the Java Collections Framework

- **List**: Ordered, allows duplicates (`ArrayList`, `LinkedList`).
- **Set**: Unordered, no duplicates (`HashSet`, `TreeSet`).
- **Map**: Key-value pairs, no duplicate keys (`HashMap`, `TreeMap`).
- **Queue**: FIFO order, used to hold elements temporarily (`PriorityQueue`, `LinkedList`).

The Java Collections Framework offers great flexibility and performance in managing groups of objects, making it an essential part of Java programming.

---
# Java Regex

Regular expressions (regex) are a powerful tool for pattern matching and string manipulation. In Java, regex is supported through the `java.util.regex` package, which provides classes like `Pattern` and `Matcher` for working with regular expressions.

Java Regular Expressions (regex) provide a powerful way to perform pattern matching and text manipulation. The `java.util.regex` package contains classes that allow you to work with regular expressions in Java.

### Key Components

1. **Pattern**: A compiled representation of a regex.
2. **Matcher**: An engine that performs matching operations on a character sequence.
3. **Flags**: Modifiers that change how the regex is interpreted (e.g., case sensitivity).

### Basic Syntax

Here are some basic regex symbols:

- `.`: Matches any character except a newline.
- `*`: Matches 0 or more occurrences of the preceding element.
- `+`: Matches 1 or more occurrences of the preceding element.
- `?`: Matches 0 or 1 occurrence of the preceding element.
- `[]`: Matches any one of the characters inside the brackets.
- `^`: Matches the beginning of a line.
- `$`: Matches the end of a line.
- `\\`: Escapes special characters.
- `|`: Logical OR (matches the expression before or after the operator).
- `{n}`: Matches exactly `n` occurrences.
- `{n,}`: Matches `n` or more occurrences.
- `{n,m}`: Matches between `n` and `m` occurrences.

### Example: Basic Usage

Here's how to use regex in Java:

```java
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        String text = "The quick brown fox jumps over the lazy dog.";
        String pattern = "quick";

        // Compile the regex pattern
        Pattern compiledPattern = Pattern.compile(pattern);
        // Create a matcher
        Matcher matcher = compiledPattern.matcher(text);

        // Check if the pattern matches
        if (matcher.find()) {
            System.out.println("Found: " + matcher.group());
        } else {
            System.out.println("Not found");
        }
    }
}
```

### Example: Using Special Characters

Here's an example of using special regex characters:

```java
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        String text = "abc123 xyz456";
        String pattern = "\\d+"; // Matches one or more digits

        // Compile the regex pattern
        Pattern compiledPattern = Pattern.compile(pattern);
        Matcher matcher = compiledPattern.matcher(text);

        while (matcher.find()) {
            System.out.println("Found number: " + matcher.group());
        }
    }
}
```

### Example: Using Flags

You can use flags to change how the regex behaves. For example, `Pattern.CASE_INSENSITIVE` makes the match case-insensitive:

```java
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        String text = "Hello World";
        String pattern = "hello";

        // Compile the regex pattern with case-insensitive flag
        Pattern compiledPattern = Pattern.compile(pattern, Pattern.CASE_INSENSITIVE);
        Matcher matcher = compiledPattern.matcher(text);

        if (matcher.find()) {
            System.out.println("Found: " + matcher.group());
        }
    }
}
```

### Example: Replacing Text

You can also use regex to replace parts of a string:

```java
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        String text = "I have a cat and a bat.";
        String pattern = "cat|bat"; // Matches 'cat' or 'bat'

        // Compile the regex pattern
        Pattern compiledPattern = Pattern.compile(pattern);
        Matcher matcher = compiledPattern.matcher(text);

        // Replace matched text with 'dog'
        String newText = matcher.replaceAll("dog");
        System.out.println(newText);  // Output: I have a dog and a dog.
    }
}
```

### Example: Splitting Strings

You can also use regex to split strings:

```java
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        String text = "apple,orange;banana grape";
        String pattern = "[,; ]"; // Split by comma, semicolon, or space

        // Split the text using the regex pattern
        String[] fruits = text.split(pattern);

        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
```

### Summary

- **Pattern**: Use `Pattern.compile()` to compile a regex.
- **Matcher**: Use `matcher()` to create a matcher from a text.
- **Find Matches**: Use `find()` to search for occurrences.
- **Replace**: Use `replaceAll()` to replace matched text.
- **Split**: Use `split()` to break a string based on a regex pattern.

Regular expressions are a powerful tool for string manipulation and pattern matching in Java. With practice, you can master regex to handle complex text processing tasks efficiently!

---
