import math

class HeapNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return i // 2

    def left_child(self, i):
        return i * 2

    def right_child(self, i):
        return i * 2 + 1

    def heapify(self, idx):
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)

        if left_idx <= self.size and self.heap[left_idx].key < self.heap[idx].key:
            smallest_idx = left_idx
        else:
            smallest_idx = idx
            
        if right_idx <= self.size and self.heap[right_idx].key < self.heap[smallest_idx].key: # PARA EL MIN HEAP CAMBIA EL SEGUNDO A < 
            smallest_idx = right_idx

        if smallest_idx != idx:
            aux = self.heap[idx]
            self.heap[idx] = self.heap[smallest_idx]
            self.heap[smallest_idx] = aux
            self.heapify(smallest_idx)            
    
       
    def build_heap(self, elements):
        self.heao=elements
        self.heap = elements
        self.size = len(elements)
        self.heap.insert(0, HeapNode(math.inf))  

        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

    def peek(self):
        if self.size == 0:
            return None
        return self.heap[1].key

    def pop(self):
        if self.size == 0:
            return None
        if self.size>=1:
            raiz = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.size -= 1
            self.heap.pop()
            self.heapify(1)
            
            return raiz

    def increase_key(self, idx, key):
        if key >= self.heap[idx].key:
            return "La nueva llave es mayor o igual que la actual"

        else:
            self.heap[idx].key = key
            self.heap[idx].value = key
            self.heap[idx].key = key
            
        while idx > 1 and self.heap[idx].key < self.heap[self.parent(idx)].key:
            self.heap[idx], self.heap[self.parent(idx)] = self.heap[self.parent(idx)], self.heap[idx]
            idx = self.parent(idx)

    def insert(self, node):
        self.size += 1

        if self.size >= len(self.heap) - 1:
            self.heap.append(node)
        else:
            self.heap[self.size] = node

        self.increase_key(self.size, node.key)

    def get_size(self):
        return self.size
