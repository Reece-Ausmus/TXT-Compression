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
    
class Heap:
    """A class used to store a heap of TreeNode objects"""

    def __init__(self, nodes):
        self.nodes = nodes

    def heapify(self):
        """This method sorts the array into min-heap order based on frequency in place"""
        for i in range((len(self) // 2) - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        small = i
        left = 2*i + 1
        right = 2*i + 2
        if (left < len(self) and self.nodes[left].frequency < self.nodes[small].frequency):
            small = left
        if (right < len(self) and self.nodes[right].frequency < self.nodes[small].frequency):
            small = right
        if (small != i):
            self.swap(i, small)
            self.sink(small)

    def swim(self, i):
        if (self.nodes[i].frequency < self.nodes[(i-1) // 2].frequency):
            self.swap(i, (i-1) // 2)
            self.swim((i-1) // 2)

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def pop(self):
        minNode = self.nodes[0]
        self.swap(0, len(self)-1)
        self.pop(len(self)-1)
        self.sink(0)
        return minNode

    def push(self, newNode):
        self.append(newNode)
        self.swim(len(self)-1)
    
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
    min_heap = Heap([TreeNode(char, frequency) for char, frequency in frequency_table.items()])
    min_heap.heapify()
