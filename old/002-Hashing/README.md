# Hashing

### Advantages
In terms of time complexity, hash maps blow arrays out of the water. The following operations are all O(1) for a hash map:

- Add an element and associate it with a value
- Delete an element if it exists
- Check if an element exists

A hash map also has many of the same useful properties as an array with the same time complexity:

- Find length/number of elements
- Updating values
- Iterate over elements

> An ordered data structure is one where the insertion order is "remembered". An unordered data structure is one where the insertion order is not relevant.

## Disadvantages

- Can take up more space when you do not know how much input you will recieve.
- Resizing is very hard.

> Note: remember that time complexity functions only involve the variables you define. When we say that hash map operations are O(1), the variable we are concerned with is usually n, which is the size of the hash map. However, this may be misleading. For example, hashing a string requires O(m) time, where m is the length of the string. The constant time operations are only constant relative to the size of the map.

### Python Hash Map Cheatsheet
```python
# Declaration: a hash map is declared like any other variable. The syntax is {}
hash_map = {}

# If you want to initialize it with some key value pairs, use the following syntax:
hash_map = {1: 2, 5: 3, 7: 2}

# Checking if a key exists: simply use the `in` keyword
1 in hash_map # True
9 in hash_map # False

# Accessing a value given a key: use square brackets, similar to an array.
hash_map[5] # 3

# Adding or updating a key: use square brackets, similar to an array.
# If the key already exists, the value will be updated
hash_map[5] = 6

# If the key doesn't exist yet, the key value pair will be inserted
hash_map[9] = 15

# Deleting a key: use the del keyword. Key must exist or you will get an error.
del hash_map[9]

# Get size
len(hash_map) # 3

# Get keys: use .keys(). You can iterate over this using a for loop.
keys = hash_map.keys()
for key in keys:
    print(key)

# Get values: use .values(). You can iterate over this using a for loop.
values = hash_map.values()
for val in values:
    print(val)
```

## Tips:
- Use hashmap when you need to store a value with a key. If you are just checking if an element is in the data structure then its better to use set.