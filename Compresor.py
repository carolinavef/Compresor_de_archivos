import math
from MinHeap import Heap, HeapNode
import bitarray

class HuffmanNode(HeapNode):
    def __init__(self, key, value=None):
        super().__init__(key, value)
        self.left_child = None
        self.right_child = None

class HuffmanCoding:
    def __init__(self):
        self.original_text = ""
        self.freq_table = {}
        self.heap = Heap()
        self.huffman_tree = None
        self.table_conversion = {}

    def set_original_text(self, text):
        with open(text, 'r') as file:#para imagen y video y audio es rb 
            #para video y lo demas es bytes en vez de char
            self.original_text = file.read()

    def calculate_frequency_table(self):
        for c in self.original_text:
            if c in self.freq_table:
                self.freq_table[c] += 1
            else:
                self.freq_table[c] = 1

    def create_huffman_tree(self):
        elements = [HuffmanNode(key=freq, value=letter) for letter, freq in self.freq_table.items()]

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
        self.__dfs(self.huffman_tree, bitarray())

    def __dfs(self, curr_node, current_code):
        if not curr_node.left_child and not curr_node.right_child:
            self.table_conversion[curr_node.value] = current_code.copy()
        else:
            if curr_node.left_child:
                current_code.append(False)  # 0
                self.__dfs(curr_node.left_child, current_code)
                current_code.pop()

            if curr_node.right_child:
                current_code.append(True)  # 1
                self.__dfs(curr_node.right_child, current_code)
                current_code.pop()

    def get_compressed_text(self):
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
            
        #imagen abrir con rb y en vez de char byte
        file_compressed=bitarray()#en vez de regresar, ya usar bitarray  #donde se guarda los caracteres
        file_compressed.encode({char: bitarray(code) for char, code in self.table_conversion.items()},self.original_text)
        with open("C:\\Users\\caro_\\OneDrive\\Documents\\GitHub\\Compresor_de_archivos\\salida_file.txt", 'wb') as file:
            file_compressed.tofile(file)

    def decompress_text(self, file_compressed):#archivo que ya sacaste
        decoded_text = ""
        current_node = self.huffman_tree

        for bit in compressed_text:
            if  bit:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
            
            if not current_node.left_child and not current_node.right_child:
                decoded_text += current_node.value
                current_node = self.huffman_tree
                
        with open("C:\\Users\\caro_\\OneDrive\\Documents\\GitHub\\Compresor_de_archivos\\descomprimido_file.txt", 'w') as file:
            decoded_text.write(file)

         # retornas a la funcion de descompresion 

# Crear una instancia de HuffmanCoding
HC = HuffmanCoding()
original_text = 'C:\\Users\\caro_\\OneDrive\\Documents\\GitHub\\Compresor_de_archivos\\prueba1.txt'
HC.set_original_text(original_text)
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



'''
# Crear una instancia de HuffmanCoding
HC = HuffmanCoding()
original_text_path = "C:\\Users\\caro_\\OneDrive\\Documents\\GitHub\Compresor_de_archivos\\prueba1.txt"
compressed_text_path = 'compressed_file.txt'
decompressed_text_path = 'decompressed_file.txt'

HC.set_original_text(original_text_path)
HC.calculate_frequency_table()
HC.create_huffman_tree()
HC.calculate_table_conversion()

# Comprimir el archivo
HC.get_compressed_text(compressed_text_path)
print("Archivo comprimido y guardado como:", compressed_text_path)
#aqui se guarda como binario y .txt

# Descomprimir el archivo
decoded_text = HC.decompress_text(compressed_text_path, decompressed_text_path)
print("Archivo descomprimido y guardado como:", decompressed_text_path)
'''