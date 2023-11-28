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
        
    def set_original_img(self, img):
        with open(img, 'rb') as file:
            self.original_text = file.read()

    def set_original_aud(self, audio):
        with open(audio, 'rb') as file:
            self.original_text = file.read()
    
    def set_original_vid(self, vid):
        with open(vid, 'rb') as file:
            self.original_text = file.read()

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
                


                                                    #COMPRIMIR Y DESCOMPRIMIR ARCHIVO DE TEXTO

    def get_compressed_text(self):
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
            
        file_compressed=bitarray()#en vez de regresar, ya usar bitarray  #donde se guarda los caracteres
        file_compressed.encode({char: bitarray(code) for char, code in self.table_conversion.items()},self.original_text)
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compreso_txt.txt', 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text

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
        with open(r"C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\descompress_txt.txt", 'w') as file:
            file.write(decoded_text)

        return decoded_text
   
                                                 #COMPRIMIR Y DESCOMPRIMIR IMAGENES

    
    
    def get_compressed_img(self):          
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
            
        file_compressed=bitarray()
        file_compressed.encode({char: bitarray(code) for char, code in self.table_conversion.items()},self.original_text)
        with open(r"C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compressso_img.zip", 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text

    def decompress_img(self, compressed_text):
        decoded_text = bytearray()
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text.append( current_node.value)
                current_node = self.huffman_tree
        with open(r"C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\descompressoo_img.png", 'wb') as file:
            file.write(decoded_text)

        return decoded_text
    
    
                                     
                                              #COMPRIMIR Y DESCOMPRIMIR AUDIOS

    def get_compressed_aud(self):          
        compressed_text = ""
        for byte in self.original_text:
            compressed_text += self.table_conversion[byte]
            
        file_compressed=bitarray()
        file_compressed.encode({byte: bitarray(code) for byte, code in self.table_conversion.items()},self.original_text)
        with open(r"C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compreso_aud.zip", 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text

    def decompress_aud(self, compressed_text):
        decoded_text = bytearray()
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text.append( current_node.value)
                current_node = self.huffman_tree
        with open(r"C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\descompress.mp3", 'wb') as file:
            file.write(decoded_text)

        return decoded_text
    
    #                               COMPRESS Y DESCOMPRESS VIDEOS 
    def get_compressed_vid(self):          
        compressed_text = ""
        for byte in self.original_text:
            compressed_text += self.table_conversion[byte]
            
        file_compressed=bitarray()
        file_compressed.encode({byte: bitarray(code) for byte, code in self.table_conversion.items()},self.original_text)
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compreso_vid.zip', 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text

    def decompress_vid(self, compressed_text):
        decoded_text = bytearray()
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text.append( current_node.value)
                current_node = self.huffman_tree
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\decompreso_vid.mp4', 'wb') as file:
            file.write(decoded_text)

        return decoded_text
        

original_text_path= r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\Prueba.mp4'
# Comprimir VIDEO
HC_img = HuffmanCoding()
HC_img.set_original_img(original_text_path)  # Cambiado a set_original_img
HC_img.calculate_frequency_table()
HC_img.create_huffman_tree()
HC_img.calculate_table_conversion()
compressed_text_img = HC_img.get_compressed_vid()  # Cambiado a get_compressed_img

# Imprimir resultados para la imagen
print("\nImagen original:", HC_img.original_text)
print("Imagen comprimida:", compressed_text_img)

# Decodificar la imagen comprimida
decoded_text_img = HC_img.decompress_vid(compressed_text_img)
print("Imagen reconstruida: ", decoded_text_img, "\n")

# Guardar el archivo comprimido de imagen
with open(compressed_text_img, 'w') as file:
    file.write(compressed_text_img)


HC_aud = HuffmanCoding()
HC_aud.set_original_aud(original_text_path)  # Cambiado a set_original_img
HC_aud.calculate_frequency_table()
HC_aud.create_huffman_tree()
HC_aud.calculate_table_conversion()
compressed_text_vid = HC_aud.get_compressed_vid()  # Cambiado a get_compressed_img

# Imprimir resultados para la imagen
print("\nImagen original:", HC_aud.original_text)
print("Imagen comprimida:", compressed_text_vid)

# Decodificar la imagen comprimida
decoded_text_aud = HC_aud.decompress_aud(compressed_text_vid)
print("Imagen reconstruida: ", decoded_text_aud, "\n")

# Guardar el archivo comprimido de imagen
with open(compressed_text_vid, 'w') as file:
    file.write(compressed_text_vid)

