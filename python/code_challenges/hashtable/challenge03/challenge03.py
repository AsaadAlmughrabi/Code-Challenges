class ListNode:
    def __init__(self, value=0, next=None):
        """Initialize a ListNode with a value and optional next node."""
        self.value = value
        self.next = next

class HashTable:
    def __init__(self, size=100):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """Compute the hash index for a key."""
        return key % self.size

    def add(self, key):
        """Add a key to the hash table, handling collisions with linked lists."""
        hash_index = self._hash(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = key
        else:
            if isinstance(self.table[hash_index], ListNode):
                current = self.table[hash_index]
                while current:
                    if current.value == key:
                        return  # Key already exists
                    if current.next is None:
                        current.next = ListNode(key)
                        return
                    current = current.next
            else:
                # Collision detected, create linked list
                if self.table[hash_index] != key:
                    old_value = self.table[hash_index]
                    self.table[hash_index] = ListNode(old_value, ListNode(key))

    def contains(self, key):
        """Check if a key exists in the hash table."""
        hash_index = self._hash(key)
        if self.table[hash_index] is None:
            return False
        if isinstance(self.table[hash_index], ListNode):
            current = self.table[hash_index]
            while current:
                if current.value == key:
                    return True
                current = current.next
            return False
        else:
            return self.table[hash_index] == key

    def count(self, key):
        """Count occurrences of a key in the hash table."""
        hash_index = self._hash(key)
        if self.table[hash_index] is None:
            return 0
        if isinstance(self.table[hash_index], ListNode):
            count = 0
            current = self.table[hash_index]
            while current:
                if current.value == key:
                    count += 1
                current = current.next
            return count
        else:
            return 1 if self.table[hash_index] == key else 0

def sum_of_unique_elements(arr):
    """Compute the sum of unique elements in the array."""
    hash_table = HashTable()
    frequency = {}  # To store frequency of each element

    # Count frequencies of each element
    for num in arr:
        hash_table.add(num)
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Sum only elements that occur exactly once
    unique_sum = sum(num for num in frequency if frequency[num] == 1)

    return unique_sum

# Test Example 1:
nums1 = [1, 2, 3, 2]
result1 = sum_of_unique_elements(nums1)
print("Sum of unique elements (Example 1):", result1)  # Expected Output: 4 (1 + 3)

# Test Example 2:
nums2 = [1, 2, 3, 4, 5]
result2 = sum_of_unique_elements(nums2)
print("Sum of unique elements (Example 2):", result2)  # Expected Output: 15 (1 + 2 + 3 + 4 + 5)
