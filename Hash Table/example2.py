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

# Using the custom hash table
ht = HashTable(10)
ht.insert("name", "Bob")
ht.insert("age", 30)
ht.insert("city", "Paris")

print("Name:", ht.get("name"))  # Output: Name: Bob
ht.insert("name", "Charlie")
print("Updated Name:", ht.get("name"))  # Output: Updated Name: Charlie

ht.delete("city")
print("City:", ht.get("city"))  # Output: City: None