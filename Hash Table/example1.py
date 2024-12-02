# Creating a hash table (dictionary)
hash_table = {}

# Adding key-value pairs
hash_table["name"] = "Abdiel"
hash_table["age"] = "37"
hash_table["city"] = "Santiago"

# Accessing values using keys
print("Name: ", hash_table["name"])
print("Age: ", hash_table["age"])
print("City: ", hash_table["city"])

# Modifying values
hash_table["name"] = "Baruk"
hash_table["age"] = "26"
hash_table["city"] = "Málaga"

# Deleting a key-value pair
del hash_table["age"]

# Checking if a key exists
if "name" in hash_table:
    print("Key 'name' exists")

# Iterating through the hash table
for key, value in hash_table.items():
    print(f"{key}: {value}")