# Write here the code challenge solution
class HashTable:
    def __init__(self, size=100):
        """
        Initializes a new instance of the HashTable class.
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize with empty lists

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return False  # Key already exists
        self.table[index].append((key, True))
        return True

    def exists(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

def first_repeated_word(s):
    """
    Finds the first repeated word in a given string.
    """
    words = s.split()  
    hash_table = HashTable()  
    
    for word in words:
        
        if hash_table.exists(word):
            return word  
        hash_table.insert(word)
    
    return "No Repetition"  

# Examples
print(first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC."))  # Output: ASAC
print(first_repeated_word("I am learning programming at ASAC.")) # Output: No Repetition
