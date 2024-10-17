# Examples for Lesson 3: Data Structures

1. **Lists Example**
   ```python
   numbers = [1, 2, 3, 4, 5]
   numbers.append(6)
   print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
   ```

2. **Dictionaries Example**
   ```python
   people_ages = {
       "Alice": 30,
       "Bob": 25,
       "Charlie": 35
   }
   print(people_ages)  # Output: {'Alice': 30, 'Bob': 25, 'Charlie': 35}
   ```

3. **Sets Example**
   ```python
   set1 = {1, 2, 3, 4, 5}
   set2 = {4, 5, 6, 7, 8}
   print(set1.union(set2))       # Output: {1, 2, 3, 4, 5, 6, 7, 8}
   print(set1.intersection(set2)) # Output: {4, 5}
   print(set1.difference(set2))   # Output: {1, 2, 3}
   ```

4. **Tuples Example**
   ```python
   words = ("apple", "banana", "cherry")
   for word in words:
       print(word[::-1])  # Output: elppa,ananab,yrrehc
