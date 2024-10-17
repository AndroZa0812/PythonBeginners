# Examples for Lesson 6: Generator Functions

1. **Generator Function Example**
   ```python
   def fibonacci(n):
       a, b = 0, 1
       for _ in range(n):
           yield a
           a, b = b, a + b

   fib_numbers = list(fibonacci(10))
   print(fib_numbers)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
