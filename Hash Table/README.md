# Hash Table Implementations in Python

This repository contains examples of hash table implementations in Python, showcasing different techniques for handling collisions and basic operations such as insertions, lookups, and deletions.

## Table of Contents
- [Description](#description)
- [Examples](#examples)
  - [1. Hash Table Using Python Dictionary](#1-hash-table-using-python-dictionary)
  - [2. Custom Hash Table with Collision Handling (Chaining)](#2-custom-hash-table-with-collision-handling-chaining)
- [How to Run the Code](#how-to-run-the-code)
- [License](#license)

## Description

A hash table is a data structure that stores key-value pairs and allows for efficient lookups, insertions, and deletions. These examples demonstrate two different ways to implement hash tables in Python:

1. Using Python's built-in `dict`, which is a highly optimized hash table implementation.
2. Creating a custom hash table class with a hash function and collision handling using chaining.

---

## Examples

### 1. Hash Table Using Python Dictionary

This example leverages Python's built-in `dict`, which is already implemented as a hash table. It demonstrates basic operations like:

- Adding key-value pairs
- Accessing values by key
- Modifying values
- Deleting key-value pairs
- Checking for the existence of keys
- Iterating through the table

#### Code:

```python
# Creating a hash table (dictionary)
hash_table = {}

# Adding key-value pairs
hash_table["name"] = "Alice"
hash_table["age"] = 25
hash_table["city"] = "New York"

# Accessing values using keys
print("Name:", hash_table["name"])  # Output: Name: Alice
print("Age:", hash_table["age"])    # Output: Age: 25

# Modifying values
hash_table["age"] = 26
print("Updated Age:", hash_table["age"])  # Output: Updated Age: 26

# Deleting a key-value pair
del hash_table["city"]
print("City after deletion:", hash_table.get("city", "Not Found"))  # Output: Not Found
```

---

### 2. Custom Hash Table with Collision Handling (Chaining)

This example implements a custom hash table class from scratch, including:

- A simple hash function (`hash(key) % size`)
- Collision handling using **chaining** (storing multiple key-value pairs in the same bucket as a list)
- Methods for insertion, retrieval, and deletion

#### Code:

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update value if key exists
                return
        self.table[index].append([key, value])  # Insert new key-value pair

    def get(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = [item for item in self.table[index] if item[0] != key]

# Example usage
ht = HashTable(10)
ht.insert("name", "Alice")
ht.insert("age", 30)

print(ht.get("name"))  # Output: Alice
print(ht.get("age"))   # Output: 30

ht.delete("name")
print(ht.get("name"))  # Output: None
```

---

## How to Run the Code

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/abdiel-moyano/hash-table-examples.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hash-table-examples
   ```
3. Run the Python scripts:
   ```bash
   python hash_table_dict.py  # For the first example
   python custom_hash_table.py  # For the second example
   ```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Feel free to fork the repository and submit pull requests with improvements, new features, or bug fixes.

---

## Contact

For questions or suggestions, please contact me at `<your-email-address>`.
