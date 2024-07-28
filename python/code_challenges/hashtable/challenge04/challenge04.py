class Node:
    def __init__(self, key, value):
        """Initialize a Node with a key, value, and next reference."""
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty LinkedList."""
        self.head = None

    def insert(self, key, value):
        """Insert a new node with the given key and value at the beginning of the LinkedList."""
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        """Find the value associated with the given key in the LinkedList."""
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        """Delete the node with the given key from the LinkedList."""
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

class HashTable:
    def __init__(self, size):
        """Initialize a HashTable with the given size."""
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        """Compute the hash value of the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the HashTable."""
        index = self.hash_function(key)
        self.table[index].insert(key, value)

    def find(self, key):
        """Find the value associated with the given key in the HashTable."""
        index = self.hash_function(key)
        return self.table[index].find(key)

    def delete(self, key):
        """Delete the key-value pair with the given key from the HashTable."""
        index = self.hash_function(key)
        return self.table[index].delete(key)

def reorder_people_by_heights(people, heights):
    """Reorder people by their heights in descending order."""
    size = len(people)
    hash_table = HashTable(size)
    for i in range(size):
        hash_table.insert(heights[i], people[i])
    sorted_heights = sorted(heights, reverse=True)
    sorted_people = [hash_table.find(height) for height in sorted_heights]
    return sorted_people

# Example usage:
people = ["Alice", "Bob", "Charlie"]
heights = [165, 180, 175]
print(reorder_people_by_heights(people, heights))  # Output: ['Bob', 'Charlie', 'Alice']
