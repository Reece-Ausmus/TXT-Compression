class TreeNode:
    """A class used to create a binary tree, also storing a char and a frequency"""
    
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Performs less than comparison based on frequency"""
        return (self.frequency < other.frequency)
    
def build_frequency_table(text):
    """This method creates a frequency table for the text"""
    frequency_table = {}
    for char in text:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    return frequency_table

def build_huffman_tree(frequency_table):
    """This method builds a tree out of TreeNode objects based on the frequency_table"""
    min_heap = [TreeNode(char, frequency) for char, frequency in frequency_table.items()]
    heapify(min_heap)


def heapify(heap):
    """This method sorts the array into min-heap order based on frequency in place"""
    for i in range((len(heap) // 2) - 1, -1, -1):
        sink(heap, i)

def sink(heap, i):
    small = i
    left = 2*i + 1
    right = 2*i + 2
    if (left < len(heap) and heap[left].frequency < heap[small].frequency):
        small = left
    if (right < len(heap) and heap[right].frequency < heap[small].frequency):
        small = right
    if (small != i):
        swap(heap, i, small)
        sink(small)

def swim(heap, i):
    if (heap[i].frequency < heap[(i-1) // 2].frequency):
        swap(heap, i, (i-1) // 2)
        swim((i-1) // 2)

def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]

def pop(heap):
    minNode = heap[0]
    swap(heap, 0, len(heap)-1)
    heap.pop(len(heap)-1)
    sink(heap, 0)
    return minNode

def push(heap, newNode):
    heap.append(newNode)
    swim(heap, len(heap)-1)
