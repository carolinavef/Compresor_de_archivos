
import zipfile
import os
from bitarray import bitarray
import MinHeap

class HuffmanNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

class HuffmanCoding:
    def __init__(self):
        self.original_text = ""
        self.freq_table = {}
        self.heap = MinHeap.Heap()
        self.huffman_tree = None
        self.table_conversion = {}

    def set_original_text(self, text):

        with open(text, 'r') as file:
            self.original_text = file.read()
        
        #self.original_text = text

    def calculate_frequency_table(self):
        for c in self.original_text:
            if c in self.freq_table:
                self.freq_table[c] += 1
            else:
                self.freq_table[c] = 1

    def create_huffman_tree(self):
        elements = []

        for letter, freq in self.freq_table.items():
            elements.append(HuffmanNode(key=freq, value=letter))

        self.heap.build_heap(elements)

        while self.heap.get_size() > 1:
            left_node = self.heap.pop()
            right_node = self.heap.pop()

            nuevo_nodo = HuffmanNode(key=left_node.key + right_node.key)
            nuevo_nodo.left_child = left_node
            nuevo_nodo.right_child = right_node
            
            self.heap.insert(nuevo_nodo)
            
        self.huffman_tree = self.heap.pop()

    def calculate_table_conversion(self):
        self.table_conversion = {}
        self.__dfs(self.huffman_tree, "")

    def __dfs(self, curr_node, current_code):
        if not curr_node.left_child and not curr_node.right_child:
            self.table_conversion[curr_node.value] = current_code
        else:
            if curr_node.left_child:
                self.__dfs(curr_node.left_child, current_code + "0")

            if curr_node.right_child:
                self.__dfs(curr_node.right_child, current_code + "1")

    def get_compressed_text(self):
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
            
        file_compressed=bitarray()#en vez de regresar, ya usar bitarray  #donde se guarda los caracteres
        file_compressed.encode({char: bitarray(code) for char, code in self.table_conversion.items()},self.original_text)
        with open("C:/Users/crisa/Downloads/salida_file.txt", 'wb') as file:
            file_compressed.tofile(file)

    def decompress_text(self, compressed_text):
        decoded_text = ""
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text += current_node.value
                current_node = self.huffman_tree

        return decoded_text
    
    #class bitarray(self):#de simbolos a textos
        '''encode for cada symbolo lo pasa a bitsarray 
        abres el archivo y le metes lo que te regresa la clase'''

#para hacer simbolo usas la tabla de frecuencia y el texto comprimido
# Ejemplo de uso
original_text_path = 'H:/My Drive/programacion/Python/ESDI/ESDI3/archivo.txt'
compressed_text_path = 'compressed_file.txt'
decompressed_text_path = 'decompressed_file.txt'
zip_file_path = 'compressed_file.zip'

# Comprimir el archivo
HC = HuffmanCoding()
HC.set_original_text(original_text_path)
HC.calculate_frequency_table()
HC.create_huffman_tree()
HC.calculate_table_conversion()
compressed_text = HC.get_compressed_text()

# Imprimir resultados
print("\nTexto original:", HC.original_text)
print("Texto comprimido:", compressed_text)

# Decodificar el texto comprimido
decoded_text = HC.decompress_text(compressed_text)
print("Texto reconstruido: ", decoded_text, "\n")

# Guardar el archivo comprimido como texto
with open(compressed_text_path, 'w') as file:
    
    
    file.write(compressed_text)
