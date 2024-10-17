# Examples for Lesson 4: Functions and Classes

1. **Functions Example**
   ```python
   def add_numbers(a, b):
       return a + b

   result = add_numbers(3, 5)
   print(result)  # Output: 8
   ```

2. **Classes Example**
   ```python
   class Car:
       def __init__(self, make, model, year):
           self.make = make
           self.model = model
           self.year = year

       def display_info(self):
           print(f"{self.year} {self.make} {self.model}")

   my_car = Car("Toyota", "Corolla", 2021)
   my_car.display_info()  # Output: 2021 Toyota Corolla
   ```

3. **Inheritance Example**
   ```python
   class Animal:
       def speak(self):
           pass

   class Dog(Animal):
       def speak(self):
           return "Woof!"

   class Cat(Animal):
       def speak(self):
           return "Meow!"

   my_dog = Dog()
   print(my_dog.speak())  # Output: Woof!

   my_cat = Cat()
   print(my_cat.speak())  # Output: Meow!
   ```

4. **Polymorphism Example**
   ```python
   def animal_sound(animal):
       return animal.speak()

   dog = Dog()
   cat = Cat()

   print(animal_sound(dog))  # Output: Woof!
   print(animal_sound(cat))  # Output: Meow!
