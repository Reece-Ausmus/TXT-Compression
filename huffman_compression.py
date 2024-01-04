import sys
import pickle
from TreeNode import TreeNode
from Heap import Heap

def is_min_heap(arr):
    """This method checks whether or not the passed arr is sorted in min-heap order"""
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
    min_heap.heapify()

    while len(min_heap) > 1:
        left = min_heap.pop()
        right = min_heap.pop()
        merged = TreeNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        min_heap.push(merged)

    return min_heap.nodes[0]

def build_huffman_codes(node, current_code="", huffman_codes=None):
    """This method creates a dictionary of huffman_codes based on the Huffman Tree"""
    if huffman_codes is None:
        huffman_codes = {}

    if node:
        if node.char is not None:
            huffman_codes[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", huffman_codes)
        build_huffman_codes(node.right, current_code + "1", huffman_codes)
    
    return huffman_codes

def encode_text(text, huffman_codes):
    """This method encodes the text according to the huffman_codes and returns the result as an integer"""
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text

def compress(input_file, output_file):
    with open(input_file, "r") as file:
        text = file.read()
    
    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_codes = build_huffman_codes(huffman_tree)

    encoded_text = encode_text(text, huffman_codes)

    with open(output_file, "wb") as file:
        pickle.dump(huffman_tree, file)

        file.write(b"\0")
        
        file.write(len(encoded_text).to_bytes(4, byteorder='big'))

        file.write(int(encoded_text, 2).to_bytes((len(encoded_text) + 7) // 8, byteorder='big'))

def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree
        
    return decoded_text

def decompress(input_file, output_file):
    with open(input_file, "rb") as file:
        huffman_tree = pickle.load(file)

        separator = file.read(1)
        if separator != b"\0":
            raise ValueError("Invalid compressed file format")
        
        encoded_text_length = int.from_bytes(file.read(4), byteorder='big')
        
        encoded_data = bin(int.from_bytes(file.read((encoded_text_length + 7) // 8), byteorder='big'))[2:]

    encoded_text = encoded_data.zfill(encoded_text_length)

    decoded_text = decode_text(encoded_text, huffman_tree)

    with open(output_file, 'w') as file:
        file.write(decoded_text)

if __name__ == "__main__":
    if (len(sys.argv) != 3) or not \
        ((sys.argv[1].endswith(".txt") or sys.argv[1].endswith(".bin"))) or \
            (sys.argv[2] != "c" and sys.argv[2] != "d"):
        print("Usage: python huffman_compression.py <file_name> <c/d>")
    elif sys.argv[2] == "c":
        input_file = sys.argv[1]
        compressed_file = input_file.replace(".txt", "_compressed.bin")
        compress(input_file, compressed_file)
    elif sys.argv[2] == "d":
        input_file = sys.argv[1]
        decompressed_file = input_file.replace(".bin", "_decompressed.txt")
        decompress(input_file, decompressed_file)