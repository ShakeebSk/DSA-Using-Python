import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, FancyArrowPatch
import random
import hashlib

# ============== HASH FUNCTIONS ==============

class HashFunctions:
    """Collection of common hash functions"""
    
    @staticmethod
    def division_method(key, size):
        """Simple modulo hash function"""
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        return key % size
    
    @staticmethod
    def multiplication_method(key, size):
        """Multiplication method: h(k) = floor(size * (k*A mod 1))"""
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        A = 0.6180339887  # (sqrt(5) - 1) / 2
        return int(size * ((key * A) % 1))
    
    @staticmethod
    def mid_square_method(key, size):
        """Mid-square method"""
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        squared = key * key
        mid = int(str(squared)[len(str(squared))//4:len(str(squared))//4*3])
        return mid % size if mid > 0 else 0
    
    @staticmethod
    def folding_method(key, size):
        """Folding method for strings"""
        if isinstance(key, str):
            total = 0
            for i in range(0, len(key), 2):
                chunk = key[i:i+2]
                total += sum(ord(c) for c in chunk)
            return total % size
        return key % size
    
    @staticmethod
    def polynomial_rolling_hash(key, size):
        """Polynomial rolling hash (good for strings)"""
        if not isinstance(key, str):
            key = str(key)
        hash_val = 0
        prime = 31
        for char in key:
            hash_val = (hash_val * prime + ord(char)) % size
        return hash_val


# ============== HASH TABLE WITH CHAINING ==============

class HashNode:
    """Node for chaining in hash table"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    """Hash Table with Separate Chaining for collision handling"""
    
    def __init__(self, size=10, hash_func='division'):
        self.size = size
        self.table = [None] * size
        self.count = 0
        self.collisions = 0
        self.hash_func_name = hash_func
        
        # Select hash function
        hash_funcs = {
            'division': HashFunctions.division_method,
            'multiplication': HashFunctions.multiplication_method,
            'mid_square': HashFunctions.mid_square_method,
            'folding': HashFunctions.folding_method,
            'polynomial': HashFunctions.polynomial_rolling_hash
        }
        self.hash_function = hash_funcs.get(hash_func, HashFunctions.division_method)
    
    def _hash(self, key):
        """Compute hash value for key"""
        return self.hash_function(key, self.size)
    
    def insert(self, key, value):
        """Insert key-value pair"""
        index = self._hash(key)
        
        # Check if key already exists and update
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        
        # Insert new node at beginning of chain
        new_node = HashNode(key, value)
        if self.table[index] is not None:
            self.collisions += 1
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.count += 1
        
        # Rehash if load factor > 0.75
        if self.load_factor() > 0.75:
            self._rehash()
    
    def get(self, key):
        """Retrieve value by key"""
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair"""
        index = self._hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.count -= 1
                return current.value
            prev = current
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """Check if key exists"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def load_factor(self):
        """Calculate load factor"""
        return self.count / self.size
    
    def _rehash(self):
        """Resize and rehash all elements"""
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        self.collisions = 0
        
        for head in old_table:
            current = head
            while current:
                self.insert(current.key, current.value)
                current = current.next
    
    def get_chain_lengths(self):
        """Get length of each chain for analysis"""
        lengths = []
        for i in range(self.size):
            length = 0
            current = self.table[i]
            while current:
                length += 1
                current = current.next
            lengths.append(length)
        return lengths
    
    def display(self):
        """Display hash table contents"""
        print(f"\nHash Table (Size: {self.size}, Count: {self.count}, Load Factor: {self.load_factor():.2f})")
        print(f"Collisions: {self.collisions}")
        print("-" * 60)
        
        for i in range(self.size):
            items = []
            current = self.table[i]
            while current:
                items.append(f"({current.key}: {current.value})")
                current = current.next
            
            if items:
                print(f"[{i}] -> " + " -> ".join(items))
            else:
                print(f"[{i}] -> None")
