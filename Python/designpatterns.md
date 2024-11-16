Python, being a versatile and multi-paradigm language, supports various design patterns, which are typical solutions to common problems in software design. These patterns are broadly classified into **Creational**, **Structural**, and **Behavioral** patterns. Here’s an overview of some common design patterns in Python, along with brief examples:

### 1. **Creational Design Patterns**

These patterns deal with object creation mechanisms, trying to create objects in a way that suits the situation.

#### **1.1 Singleton**
Ensures a class has only one instance and provides a global point of access to it.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True
```

#### **1.2 Factory Method**
Defines an interface for creating an object but lets subclasses decide which class to instantiate.

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()

# Usage
animal = AnimalFactory.create_animal('dog')
print(animal.speak())  # Woof
```

#### **1.3 Builder**
Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

```python
class House:
    def __init__(self, windows, doors):
        self.windows = windows
        self.doors = doors

class HouseBuilder:
    def __init__(self):
        self.windows = 0
        self.doors = 0
    
    def add_windows(self, number):
        self.windows = number
        return self
    
    def add_doors(self, number):
        self.doors = number
        return self
    
    def build(self):
        return House(self.windows, self.doors)

# Usage
builder = HouseBuilder()
house = builder.add_windows(4).add_doors(2).build()
print(house.windows, house.doors)  # 4 2
```

### 2. **Structural Design Patterns**

These patterns deal with object composition and typically help ensure that if one part of a system changes, the entire system doesn’t need to change.

#### **2.1 Adapter**
Allows incompatible interfaces to work together.

```python
class EuropeanSocket:
    def voltage(self):
        return 230

class AmericanSocket:
    def voltage(self):
        return 120

class Adapter:
    def __init__(self, european_socket):
        self.european_socket = european_socket
    
    def voltage(self):
        return self.european_socket.voltage() * 0.52  # Converts to a lower voltage

# Usage
european_socket = EuropeanSocket()
adapter = Adapter(european_socket)
print(adapter.voltage())  # Output: 119.6
```

#### **2.2 Decorator**
Allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class.

```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"

print(text())  # Output: <b><i>Hello</i></b>
```

### 3. **Behavioral Design Patterns**

These patterns are about object interaction and responsibility. They describe patterns of communication between objects.

#### **3.1 Observer**
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def update(self):
        print("Observer has been notified!")

# Usage
subject = Subject()
observer = ConcreteObserver()

subject.add_observer(observer)
subject.notify_observers()  # Output: Observer has been notified!
```

#### **3.2 Strategy**
Defines a family of algorithms, encapsulates each one, and makes them interchangeable. The strategy pattern lets the algorithm vary independently from clients that use it.

```python
class Strategy:
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
    
    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)

# Usage
context = Context(AddStrategy())
print(context.execute_strategy(5, 3))  # Output: 8

context = Context(SubtractStrategy())
print(context.execute_strategy(5, 3))  # Output: 2
```

#### **3.3 Command**
Encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, and queuing of requests.

```python
class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class Light:
    def turn_on(self):
        print("The light is on.")

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Usage
light = Light()
light_on_command = LightOnCommand(light)

remote = RemoteControl()
remote.set_command(light_on_command)
remote.press_button()  # Output: The light is on.
```

### Summary of Popular Python Design Patterns:

- **Creational**: Singleton, Factory, Builder
- **Structural**: Adapter, Decorator, Proxy, Facade
- **Behavioral**: Observer, Strategy, Command, Chain of Responsibility

These patterns help you organize your code efficiently, handle scalability, and improve maintainability of complex software systems.