# Examples for Lesson 7: Advanced Topics

1. **Decorator Example**
   ```python
   def log_arguments(func):
       def wrapper(*args, **kwargs):
           print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
           return func(*args, **kwargs)
       return wrapper

   @log_arguments
   def add(a, b):
       return a + b

   result = add(3, 5)  # Output: Arguments: (3, 5), Keyword Arguments: {}
   ```

2. **Context Manager Example**
   ```python
   class FileHandler:
       def __init__(self, filename, mode):
           self.filename = filename
           self.mode = mode
           self.file = None

       def __enter__(self):
           self.file = open(self.filename, self.mode)
           return self.file

       def __exit__(self, exc_type, exc_val, exc_tb):
           if self.file:
               self.file.close()

   with FileHandler('example.txt', 'w') as file:
       file.write("Hello, world!")
   ```

3. **Asyncio Example**
   ```python
   import asyncio

   async def fetch_data():
       print("Fetching data...")
       await asyncio.sleep(2)
       return "Data fetched"

   async def main():
       result = await fetch_data()
       print(result)

   asyncio.run(main())  # Output: Fetching data... Data fetched
   ```

4. **File Handling Example**
   ```python
   with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
       content = input_file.read()
       reversed_content = content[::-1]
       output_file.write(reversed_content)
   ```

5. **Exception Handling Example**
   ```python
   def divide(a, b):
       try:
           return a / b
       except ZeroDivisionError:
           print("Cannot divide by zero")
           return None

   result = divide(10, 0)  # Output: Cannot divide by zero
