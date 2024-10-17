# Examples for Lesson 5: List Comprehension

1. **List Comprehensions Example**
   ```python
   squares = [x**2 for x in range(1, 11)]
   print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   ```

2. **Filtering with List Comprehension Example**
   ```python
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   even_numbers = [num for num in numbers if num % 2 == 0]
   print(even_numbers)  # Output: [2, 4, 6, 8, 10]
   ```
