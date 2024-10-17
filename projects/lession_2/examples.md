# Examples for Lesson 2: Control Flow

1. **Conditional Statements Example**
   ```python
   number = int(input("Enter a number: "))
   if number > 0:
       print(f"{number} is positive.")
   elif number < 0:
       print(f"{number} is negative.")
   else:
       print("The number is zero.")
   ```

2. **Loops Example**
   ```python
   for i in range(1, 21):
       if i % 2 == 0:
           print(i)
   ```

3. **Break and Continue Example**
   ```python
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   for num in numbers:
       if num % 2 != 0:
           print(num)
       elif num % 5 == 0:
           continue
