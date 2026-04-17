# Hash Table Implementation

This project is part of the freeCodeCamp Python Certification.

## 📌 Description

A Python implementation of a hash table from scratch. The hash function is based on the sum of Unicode values of the characters in a key.

## ⚙️ Features

- Custom hash function
- Add key-value pairs
- Handle hash collisions
- Remove elements
- Lookup values by key

## 🧠 Concepts Used

- Data structures (hash tables)
- Dictionaries
- Hashing
- Collision handling
- Object-oriented programming

## 🧪 Example

```python
table = HashTable()

table.add("name", "Matias")
table.add("age", 20)

print(table.lookup("name"))  # Matias

table.remove("name")
print(table.lookup("name"))  # None