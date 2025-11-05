class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)
    
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, i):
        max_idx = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_idx]:
            max_idx = left
        if right < len(self.heap) and self.heap[right] > self.heap[max_idx]:
            max_idx = right
        
        if max_idx != i:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self._heapify_down(max_idx)
    
    def get_max(self):
        return self.heap[0] if self.heap else None
