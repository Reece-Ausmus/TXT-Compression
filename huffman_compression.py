import sys
import os
from TreeNode import TreeNode
from Heap import Heap

def is_min_heap(arr):
    n = len(arr)
    # Check each non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        # Compare with left child
        left_child = 2 * i + 1
        if left_child < n and arr[i] > arr[left_child]:
            return False
        # Compare with right child
        right_child = 2 * i + 2
        if right_child < n and arr[i] > arr[right_child]:
            return False
    return True
 
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
    print(min_heap)
    min_heap.heapify()
    print(min_heap)
    print(is_min_heap(min_heap.nodes))
    return min_heap.nodes[0]

def compress(input_file, compressed_file):
    with open(input_file, "r") as file:
        text = file.read()
    
    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".txt"):
        print("Usage: python huffman_compression.py <file_name>.txt")
    else:
        input_file = sys.argv[1]
        compressed_file = input_file.replace(".txt", "_compressed.bin")
        compress(input_file, compressed_file)