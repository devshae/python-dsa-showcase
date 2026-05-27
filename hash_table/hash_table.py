# Create a HashTable class with a fixed size array of empty lists
# Write a _hash(key) method that converts a key into an index
# Write an insert(key, value) method
# Write a search(key) method — returns the value if found
# Write a delete(key) method
# Add a test block at the bottom

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # update existing value
                return
        # If key doesn't exist, add new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # return the value
        return None  # key not found

    def delete(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair [0] == key:
                self.table[index].remove(pair) # remove the key-value pair
                return True
        return False  # key not found
    
# Test block
if __name__ == "__main__":
    hash_table = HashTable()
    
    # Insert key-value pairs
    hash_table.insert("name", "Devon")
    hash_table.insert("age", 27)
    hash_table.insert("city", "Ridgecrest")

    # Search for values
    print(hash_table.search("name"))  # Output: Devon
    print(hash_table.search("age"))   # Output: 27
    print(hash_table.search("city"))  # Output: Ridgecrest
    print(hash_table.search("country"))  # Output: None (not found)

    # Delete a key-value pair
    hash_table.delete("age")
    print(hash_table.search("age"))   # Output: None (deleted)
