class HashTableOpenAddressing:
    """Hash Table with Open Addressing (Linear Probing, Quadratic Probing, Double Hashing)"""
    
    def __init__(self, size=10, probing='linear', hash_func='division'):
        self.size = size
        self.table = [None] * size
        self.count = 0
        self.collisions = 0
        self.probing_method = probing
        self.hash_func_name = hash_func
        
        # Select hash function
        hash_funcs = {
            'division': HashFunctions.division_method,
            'multiplication': HashFunctions.multiplication_method,
            'polynomial': HashFunctions.polynomial_rolling_hash
        }
        self.hash_function = hash_funcs.get(hash_func, HashFunctions.division_method)
        
        # Deleted marker
        self.DELETED = object()
    
    def _hash(self, key):
        """Primary hash function"""
        return self.hash_function(key, self.size)
    
    def _hash2(self, key):
        """Secondary hash function for double hashing"""
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        return 7 - (key % 7)  # Common practice: prime - (key % prime)
    
    def _probe(self, index, i, key):
        """Calculate probe sequence based on method"""
        if self.probing_method == 'linear':
            return (index + i) % self.size
        elif self.probing_method == 'quadratic':
            return (index + i * i) % self.size
        elif self.probing_method == 'double':
            return (index + i * self._hash2(key)) % self.size
        return index
    
    def insert(self, key, value):
        """Insert key-value pair"""
        if self.load_factor() >= 0.7:
            self._rehash()
        
        index = self._hash(key)
        i = 0
        
        while i < self.size:
            probe_index = self._probe(index, i, key)
            
            # Empty slot or deleted slot
            if self.table[probe_index] is None or self.table[probe_index] is self.DELETED:
                self.table[probe_index] = (key, value)
                self.count += 1
                if i > 0:
                    self.collisions += 1
                return
            
            # Update existing key
            if self.table[probe_index][0] == key:
                self.table[probe_index] = (key, value)
                return
            
            i += 1
        
        raise Exception("Hash table is full")
    
    def get(self, key):
        """Retrieve value by key"""
        index = self._hash(key)
        i = 0
        
        while i < self.size:
            probe_index = self._probe(index, i, key)
            
            if self.table[probe_index] is None:
                raise KeyError(f"Key '{key}' not found")
            
            if self.table[probe_index] is not self.DELETED:
                if self.table[probe_index][0] == key:
                    return self.table[probe_index][1]
            
            i += 1
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair (lazy deletion)"""
        index = self._hash(key)
        i = 0
        
        while i < self.size:
            probe_index = self._probe(index, i, key)
            
            if self.table[probe_index] is None:
                raise KeyError(f"Key '{key}' not found")
            
            if self.table[probe_index] is not self.DELETED:
                if self.table[probe_index][0] == key:
                    value = self.table[probe_index][1]
                    self.table[probe_index] = self.DELETED
                    self.count -= 1
                    return value
            
            i += 1
        
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
        
        for item in old_table:
            if item is not None and item is not self.DELETED:
                self.insert(item[0], item[1])
    
    def display(self):
        """Display hash table contents"""
        print(f"\nHash Table - {self.probing_method.capitalize()} Probing")
        print(f"(Size: {self.size}, Count: {self.count}, Load Factor: {self.load_factor():.2f})")
        print(f"Collisions: {self.collisions}")
        print("-" * 60)
        
        for i in range(self.size):
            if self.table[i] is None:
                print(f"[{i}] -> None")
            elif self.table[i] is self.DELETED:
                print(f"[{i}] -> DELETED")
            else:
                key, value = self.table[i]
                print(f"[{i}] -> ({key}: {value})")


# ============== HASH SET ==============

class HashSet:
    """Hash Set implementation (stores unique values only)"""
    
    def __init__(self, size=10):
        self.hash_table = HashTableChaining(size)
    
    def add(self, value):
        """Add value to set"""
        self.hash_table.insert(value, True)
    
    def remove(self, value):
        """Remove value from set"""
        try:
            self.hash_table.delete(value)
        except KeyError:
            pass
    
    def contains(self, value):
        """Check if value exists in set"""
        return self.hash_table.contains(value)
    
    def size(self):
        """Get number of elements"""
        return self.hash_table.count
    
    def clear(self):
        """Clear all elements"""
        self.hash_table = HashTableChaining(self.hash_table.size)
    
    def to_list(self):
        """Convert set to list"""
        result = []
        for head in self.hash_table.table:
            current = head
            while current:
                result.append(current.key)
                current = current.next
        return result
    
    def union(self, other_set):
        """Return union of two sets"""
        result = HashSet(self.hash_table.size)
        for val in self.to_list():
            result.add(val)
        for val in other_set.to_list():
            result.add(val)
        return result
    
    def intersection(self, other_set):
        """Return intersection of two sets"""
        result = HashSet(self.hash_table.size)
        for val in self.to_list():
            if other_set.contains(val):
                result.add(val)
        return result
    
    def difference(self, other_set):
        """Return difference of two sets"""
        result = HashSet(self.hash_table.size)
        for val in self.to_list():
            if not other_set.contains(val):
                result.add(val)
        return result
    
    def display(self):
        """Display set contents"""
        print(f"\nHashSet (Size: {self.size()})")
        print(f"Elements: {{{', '.join(map(str, sorted(self.to_list())))}}}")
