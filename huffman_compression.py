import sys
import TreeNode
import Heap

def main():
    print()

if __name__ == "__main__":
    main()
    
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
    print(min_heap)