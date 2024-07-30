class ListNode:
    """Node in a linked list."""
    def __init__(self, key=None):
        self.key = key
        self.next = None

class HashTable:
    """HashTable with separate chaining using linked lists to handle collisions."""
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """Compute hash index for a given key."""
        return key % self.size

    def insert(self, key):
        """Insert a key into the hash table."""
        hash_index = self._hash(key)
        if not self.table[hash_index]:
            self.table[hash_index] = ListNode(key)
        else:
            current = self.table[hash_index]
            while current:
                if current.key == key:  # Avoid inserting duplicates
                    return
                if not current.next:
                    current.next = ListNode(key)
                    return
                current = current.next

    def contains(self, key):
        """Check if a key is present in the hash table."""
        hash_index = self._hash(key)
        current = self.table[hash_index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

def intersection(arr1, arr2):
    """Find the intersection of two arrays, returning unique elements."""
    hash_table = HashTable()
    result = []

    # Insert elements of arr1 into the hash table
    for num in arr1:
        hash_table.insert(num)

    # Check for intersection with elements of arr2
    for num in arr2:
        if hash_table.contains(num):
            if num not in result:
                result.append(num)

    return result

# Example usage:
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersection(arr1, arr2))  # Output: [2]
