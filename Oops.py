''' 1. Multilevel inheritance: Vehicle → Car → Electric Car. '''

# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

# Child class of Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Child class of Car
class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

my_car = ElectricCar() # object creation

my_car.start()
my_car.drive()
my_car.charge()

# ==================================================================================

''' 2. Multiple inheritance: Teacher + Researcher → Professor. '''

# First parent class
class Teacher:
    def teach(self):
        print("Professor teaches students")

# Second parent class
class Researcher:
    def research(self):
        print("Professor conducts research")

# Child class
class Professor(Teacher, Researcher):
    def guide(self):
        print("Professor guides students")


p = Professor()

p.teach()
p.research()
p.guide()

# ==================================================================================

''' 3. Hierarchical inheritance: Shape → Circle, Rectangle, Triangle. '''

# Parent class
class Shape:
    def display(self):
        print("This is a shape")

# First child class
class Circle(Shape):
    def circle_area(self, radius):
        print("Circle Area:", 3.14 * radius * radius)

# Second child class
class Rectangle(Shape):
    def rectangle_area(self, length, breadth):
        print("Rectangle Area:", length * breadth)

# Third child class
class Triangle(Shape):
    def triangle_area(self, base, height):
        print("Triangle Area:", 0.5 * base * height)


c = Circle()
r = Rectangle()
t = Triangle()

c.display()
c.circle_area(5)

r.display()
r.rectangle_area(10, 5)

t.display()
t.triangle_area(6, 4)

# ==================================================================================

''' 4. Method overriding: Animal → Dog/Cat sound example. '''

# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

# ==================================================================================

''' 5. Operator overloading: Add two complex numbers. '''

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overloading the + operator
    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary

        return Complex(real, imaginary)

    def display(self):
        print(f"{self.real} + {self.imaginary}i")

# Creating two complex number objects
c1 = Complex(3, 4)
c2 = Complex(2, 5)

# Adding two objects
c3 = c1 + c2

print("First complex number:")
c1.display()

print("Second complex number:")
c2.display()

print("Sum:")
c3.display()

# ==================================================================================

''' 6. Create class with: Private variable (__salary) '''

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def display_salary(self):
        print("Salary:", self.__salary)


emp = Employee(50000)

emp.display_salary()

# ==================================================================================

''' 7. ATM system using encapsulation: Hide PIN and balance. '''

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print("Available Balance:", self.__balance)
        else:
            print("Incorrect PIN!")

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin:
            if amount <= 0:
                print("Enter a valid amount!")
            elif amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", self.__balance)
            else:
                print("Insufficient Balance!")
        else:
            print("Incorrect PIN!")


my_atm = ATM(1234, 10000)

my_atm.check_balance(1234)

my_atm.withdraw(1234, 2000)

# ==================================================================================

''' 8. Game Character Design: Base character class with specialized subclasses. '''

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Name:", self.name)
        print("Health:", self.health)

class Warrior(Character):
    def attack(self):
        print(self.name, "attacks using a sword!")

class Mage(Character):
    def attack(self):
        print(self.name, "casts a magic spell!")

class Archer(Character):
    def attack(self):
        print(self.name, "shoots an arrow!")


w = Warrior("Thor", 100)
m = Mage("Merlin", 80)
a = Archer("Robin", 90)

# Warrior
w.display()
w.attack()

# Mage
m.display()
m.attack()

# Archer
a.display()
a.attack()

# ==================================================================================