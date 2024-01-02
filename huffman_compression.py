import sys
import os
import TreeNode
import Heap
 
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

def compress(input_file, compressed_file):
    with open(input_file, "r") as file:
        text = file.read()
    
    
        

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".txt"):
        print("Usage: python huffman_compression.py <file_name>.txt")
    else:
        input_file = sys.argv[1]
        compressed_file = input_file.replace(".txt", "_compressed.bin")
        compress(input_file, compressed_file)